import azure.functions as func
import json
import hashlib
import base64
import random
import string
import uuid
from datetime import datetime, timedelta

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


class MCPProcessor:
    def analyze_text(self, text):
        if not text:
            return {"error": "Text parameter is required"}

        words = text.split()
        sentences = text.split(".")

        return {
            "characterCount": len(text),
            "wordCount": len(words),
            "sentenceCount": len([s for s in sentences if s.strip()]),
            "longestWord": max(words, key=len) if words else "",
        }

    def generate_password(self, length, include_symbols):
        try:
            length = int(length)
            if length < 4 or length > 128:
                return {"error": "Password length must be between 4 and 128 characters"}

            chars = string.ascii_letters + string.digits
            if include_symbols:
                chars += "!@#$%^&*()_+-="

            password = "".join(random.choice(chars) for _ in range(length))
            return {"password": password, "length": len(password)}
        except ValueError:
            return {"error": "Invalid length parameter"}

    def hash_text(self, text, algorithm):
        if not text:
            return {"error": "Text parameter is required"}

        try:
            if algorithm.lower() == "sha256":
                hash_obj = hashlib.sha256(text.encode())
            elif algorithm.lower() == "md5":
                hash_obj = hashlib.md5(text.encode())
            else:
                return {"error": "Unsupported algorithm"}

            return {
                "originalText": text,
                "algorithm": algorithm.upper(),
                "hash": hash_obj.hexdigest(),
            }
        except Exception as e:
            return {"error": str(e)}


processor = MCPProcessor()


@app.route(route="mcp", methods=["POST"])
def mcp_handler(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        tool_name = req_body.get("name")
        parameters = req_body.get("parameters", {})

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
        else:
            result = {"error": "Unknown tool"}

        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            headers={"Content-Type": "application/json"},
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            headers={"Content-Type": "application/json"},
        )
