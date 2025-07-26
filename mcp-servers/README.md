# MCP Servers

Model Context Protocol (MCP) servers for various utilities and services.

## Servers

### 🔧 Text Processing Server (`text-processing-server/`)

A comprehensive MCP server providing text analysis, password generation, hashing, and utility functions.

**Files:**

- `simple_mcp_server.py` - Main MCP server (vanilla Python)
- `flask_version.py` - Flask-based version for production
- `test_mcp_client.py` - Test client for server functionality
- `requirements.txt` - Python dependencies

**Features:**

- Text analysis (word count, character count, statistics)
- Password generation with strength assessment
- Text hashing (MD5, SHA1, SHA256, SHA512)
- Base64 encoding/decoding
- UUID generation
- Date calculations

**Usage:**

```bash
cd text-processing-server
pip install -r requirements.txt

# Run vanilla server
python3 simple_mcp_server.py

# Run Flask version
python3 flask_version.py

# Test the server
python3 test_mcp_client.py
```

### ☁️ Azure Functions Server (`azure-functions-server/`)

Serverless Azure Functions implementation of the MCP server for cost-effective cloud deployment.

**Files:**

- `function_app.py` - Azure Functions implementation
- `host.json` - Azure Functions configuration

**Deployment:**

```bash
cd azure-functions-server
func start  # Local testing
func azure functionapp publish your-function-app-name
```

## API Endpoints

All servers provide the following tools via POST requests:

- `textAnalysis` - Analyze text statistics
- `generatePassword` - Generate secure passwords
- `hashText` - Hash text with various algorithms
- `encodeBase64` / `decodeBase64` - Base64 operations
- `generateUUID` - Generate unique identifiers
- `dateCalculator` - Date arithmetic

## Testing

Use the provided test client or curl:

```bash
curl -X POST http://localhost:3000 \
  -H "Content-Type: application/json" \
  -d '{"name": "textAnalysis", "parameters": {"text": "Hello World"}}'
```
