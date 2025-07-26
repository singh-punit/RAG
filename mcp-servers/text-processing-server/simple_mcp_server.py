#!/usr/bin/env python3
"""
Simple MCP Server Example - Text Processing & Utilities
No API keys or external services required!
"""
import json
import sys
import hashlib
import base64
import random
import string
from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler


class MCPHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        request = json.loads(post_data.decode("utf-8"))

        print(f"Received request: {request}", file=sys.stderr)

        # Process the request based on the tool name
        tool_name = request.get("name")
        parameters = request.get("parameters", {})

        response = {"error": "Unknown tool"}

        if tool_name == "textAnalysis":
            response = self.analyze_text(parameters.get("text", ""))
        elif tool_name == "generatePassword":
            length = parameters.get("length", 12)
            include_symbols = parameters.get("includeSymbols", True)
            response = self.generate_password(length, include_symbols)
        elif tool_name == "hashText":
            text = parameters.get("text", "")
            algorithm = parameters.get("algorithm", "sha256")
            response = self.hash_text(text, algorithm)
        elif tool_name == "encodeBase64":
            text = parameters.get("text", "")
            response = self.encode_base64(text)
        elif tool_name == "decodeBase64":
            encoded = parameters.get("encoded", "")
            response = self.decode_base64(encoded)
        elif tool_name == "generateUUID":
            response = self.generate_uuid()
        elif tool_name == "dateCalculator":
            date_str = parameters.get("date", "")
            days_to_add = parameters.get("daysToAdd", 0)
            response = self.calculate_date(date_str, days_to_add)

        self._set_headers()
        self.wfile.write(json.dumps(response).encode())

    def analyze_text(self, text):
        """Analyze text and return various statistics"""
        if not text:
            return {"error": "Text parameter is required"}

        words = text.split()
        sentences = text.split(".")
        paragraphs = text.split("\n\n")

        return {
            "characterCount": len(text),
            "characterCountNoSpaces": len(text.replace(" ", "")),
            "wordCount": len(words),
            "sentenceCount": len([s for s in sentences if s.strip()]),
            "paragraphCount": len([p for p in paragraphs if p.strip()]),
            "averageWordsPerSentence": round(
                len(words) / max(len([s for s in sentences if s.strip()]), 1), 2
            ),
            "longestWord": max(words, key=len) if words else "",
            "mostCommonWords": self.get_most_common_words(words),
        }

    def get_most_common_words(self, words):
        """Get the 5 most common words"""
        word_count = {}
        for word in words:
            clean_word = word.lower().strip('.,!?";')
            if len(clean_word) > 2:  # Ignore short words
                word_count[clean_word] = word_count.get(clean_word, 0) + 1

        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_words[:5])

    def generate_password(self, length, include_symbols):
        """Generate a random password"""
        try:
            length = int(length)
            if length < 4 or length > 128:
                return {"error": "Password length must be between 4 and 128 characters"}

            chars = string.ascii_letters + string.digits
            if include_symbols:
                chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

            password = "".join(random.choice(chars) for _ in range(length))

            return {
                "password": password,
                "length": len(password),
                "strength": self.assess_password_strength(password),
            }
        except ValueError:
            return {"error": "Invalid length parameter"}

    def assess_password_strength(self, password):
        """Simple password strength assessment"""
        score = 0
        if len(password) >= 8:
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            score += 1

        strength_levels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]
        return strength_levels[min(score, 4)]

    def hash_text(self, text, algorithm):
        """Hash text using specified algorithm"""
        if not text:
            return {"error": "Text parameter is required"}

        try:
            if algorithm.lower() == "md5":
                hash_obj = hashlib.md5(text.encode())
            elif algorithm.lower() == "sha1":
                hash_obj = hashlib.sha1(text.encode())
            elif algorithm.lower() == "sha256":
                hash_obj = hashlib.sha256(text.encode())
            elif algorithm.lower() == "sha512":
                hash_obj = hashlib.sha512(text.encode())
            else:
                return {
                    "error": "Unsupported algorithm. Use: md5, sha1, sha256, sha512"
                }

            return {
                "originalText": text,
                "algorithm": algorithm.upper(),
                "hash": hash_obj.hexdigest(),
            }
        except Exception as e:
            return {"error": str(e)}

    def encode_base64(self, text):
        """Encode text to base64"""
        if not text:
            return {"error": "Text parameter is required"}

        try:
            encoded = base64.b64encode(text.encode()).decode()
            return {"originalText": text, "encoded": encoded}
        except Exception as e:
            return {"error": str(e)}

    def decode_base64(self, encoded):
        """Decode base64 text"""
        if not encoded:
            return {"error": "Encoded parameter is required"}

        try:
            decoded = base64.b64decode(encoded).decode()
            return {"encoded": encoded, "decoded": decoded}
        except Exception as e:
            return {"error": "Invalid base64 string"}

    def generate_uuid(self):
        """Generate a UUID-like string"""
        import uuid

        return {"uuid": str(uuid.uuid4()), "timestamp": datetime.now().isoformat()}

    def calculate_date(self, date_str, days_to_add):
        """Calculate date by adding/subtracting days"""
        try:
            if not date_str:
                base_date = datetime.now()
            else:
                base_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))

            new_date = base_date + timedelta(days=int(days_to_add))

            return {
                "originalDate": base_date.isoformat(),
                "daysAdded": days_to_add,
                "resultDate": new_date.isoformat(),
                "dayOfWeek": new_date.strftime("%A"),
                "formattedDate": new_date.strftime("%B %d, %Y"),
            }
        except Exception as e:
            return {"error": f"Invalid date format: {str(e)}"}


def run_server(port=3000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, MCPHandler)
    print(f"Starting MCP Text Processing Server on port {port}...", file=sys.stderr)
    print("Available tools:", file=sys.stderr)
    print("- textAnalysis: Analyze text statistics", file=sys.stderr)
    print("- generatePassword: Generate secure passwords", file=sys.stderr)
    print("- hashText: Hash text with various algorithms", file=sys.stderr)
    print("- encodeBase64/decodeBase64: Base64 encoding/decoding", file=sys.stderr)
    print("- generateUUID: Generate unique identifiers", file=sys.stderr)
    print("- dateCalculator: Calculate dates", file=sys.stderr)
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
