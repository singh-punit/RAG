#!/usr/bin/env python3
"""
Production-ready MCP Server using Flask for Azure deployment
"""
import json
import hashlib
import base64
import random
import string
import uuid
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


class MCPProcessor:
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
            if len(clean_word) > 2:
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
        """Generate a UUID"""
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


processor = MCPProcessor()


@app.route("/", methods=["POST"])
def handle_mcp_request():
    """Handle MCP tool requests"""
    try:
        request_data = request.get_json()
        tool_name = request_data.get("name")
        parameters = request_data.get("parameters", {})

        if tool_name == "textAnalysis":
            result = processor.analyze_text(parameters.get("text", ""))
        elif tool_name == "generatePassword":
            length = parameters.get("length", 12)
            include_symbols = parameters.get("includeSymbols", True)
            result = processor.generate_password(length, include_symbols)
        elif tool_name == "hashText":
            text = parameters.get("text", "")
            algorithm = parameters.get("algorithm", "sha256")
            result = processor.hash_text(text, algorithm)
        elif tool_name == "encodeBase64":
            text = parameters.get("text", "")
            result = processor.encode_base64(text)
        elif tool_name == "decodeBase64":
            encoded = parameters.get("encoded", "")
            result = processor.decode_base64(encoded)
        elif tool_name == "generateUUID":
            result = processor.generate_uuid()
        elif tool_name == "dateCalculator":
            date_str = parameters.get("date", "")
            days_to_add = parameters.get("daysToAdd", 0)
            result = processor.calculate_date(date_str, days_to_add)
        else:
            result = {"error": "Unknown tool"}

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint for Azure"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})


@app.route("/tools", methods=["GET"])
def list_tools():
    """List available tools"""
    tools = [
        {"name": "textAnalysis", "description": "Analyze text statistics"},
        {"name": "generatePassword", "description": "Generate secure passwords"},
        {"name": "hashText", "description": "Hash text with various algorithms"},
        {"name": "encodeBase64", "description": "Encode text to base64"},
        {"name": "decodeBase64", "description": "Decode base64 text"},
        {"name": "generateUUID", "description": "Generate unique identifiers"},
        {"name": "dateCalculator", "description": "Calculate dates"},
    ]
    return jsonify({"tools": tools})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
