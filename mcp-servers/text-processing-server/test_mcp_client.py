#!/usr/bin/env python3
"""
Simple test client for the MCP server
"""
import requests
import json


def test_mcp_tool(tool_name, parameters, server_url="http://localhost:3000"):
    """Test a specific MCP tool"""
    payload = {"name": tool_name, "parameters": parameters}

    try:
        response = requests.post(server_url, json=payload)
        result = response.json()
        print(f"\n=== Testing {tool_name} ===")
        print(f"Request: {json.dumps(payload, indent=2)}")
        print(f"Response: {json.dumps(result, indent=2)}")
        return result
    except Exception as e:
        print(f"Error testing {tool_name}: {e}")
        return None


def run_all_tests():
    """Run tests for all available tools"""

    # Test text analysis
    test_mcp_tool(
        "textAnalysis",
        {
            "text": "Hello world! This is a comprehensive test of the text analysis tool. It should count words, characters, and sentences properly."
        },
    )

    # Test password generation
    test_mcp_tool("generatePassword", {"length": 12, "includeSymbols": True})

    # Test hashing
    test_mcp_tool("hashText", {"text": "Hello World", "algorithm": "sha256"})

    # Test base64 encoding
    test_mcp_tool("encodeBase64", {"text": "Hello World"})

    # Test base64 decoding
    test_mcp_tool("decodeBase64", {"encoded": "SGVsbG8gV29ybGQ="})

    # Test UUID generation
    test_mcp_tool("generateUUID", {})

    # Test date calculation
    test_mcp_tool("dateCalculator", {"date": "2025-01-01", "daysToAdd": 30})


if __name__ == "__main__":
    print("Testing MCP Server...")
    print("Make sure the server is running with: python3 simple_mcp_server.py")

    run_all_tests()

    print("\n=== Interactive Testing ===")
    while True:
        print("\nAvailable tools:")
        print("1. textAnalysis")
        print("2. generatePassword")
        print("3. hashText")
        print("4. encodeBase64")
        print("5. decodeBase64")
        print("6. generateUUID")
        print("7. dateCalculator")
        print("8. Exit")

        choice = input("\nEnter choice (1-8): ").strip()

        if choice == "1":
            text = input("Enter text to analyze: ")
            test_mcp_tool("textAnalysis", {"text": text})
        elif choice == "2":
            length = int(input("Password length (default 12): ") or "12")
            symbols = input("Include symbols? (y/n, default y): ").lower() != "n"
            test_mcp_tool(
                "generatePassword", {"length": length, "includeSymbols": symbols}
            )
        elif choice == "3":
            text = input("Enter text to hash: ")
            algorithm = (
                input("Algorithm (md5/sha1/sha256/sha512, default sha256): ")
                or "sha256"
            )
            test_mcp_tool("hashText", {"text": text, "algorithm": algorithm})
        elif choice == "4":
            text = input("Enter text to encode: ")
            test_mcp_tool("encodeBase64", {"text": text})
        elif choice == "5":
            encoded = input("Enter base64 to decode: ")
            test_mcp_tool("decodeBase64", {"encoded": encoded})
        elif choice == "6":
            test_mcp_tool("generateUUID", {})
        elif choice == "7":
            date = input("Enter date (YYYY-MM-DD, or leave empty for today): ")
            days = int(input("Days to add/subtract: ") or "0")
            test_mcp_tool("dateCalculator", {"date": date, "daysToAdd": days})
        elif choice == "8":
            break
        else:
            print("Invalid choice!")
