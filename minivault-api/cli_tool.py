import argparse
import requests

def health_check(base_url):
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("Health Check: OK")
        else:
            print(f"Health Check Failed: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error: {e}")

def generate_response(base_url):
    try:
        response = requests.post(f"{base_url}/generate-response")
        if response.status_code == 200:
            print("Response Generated Successfully")
            print("Response:", response.json())
        else:
            print(f"Failed to Generate Response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="CLI tool to interact with the MiniVault API")
    parser.add_argument("--base-url", type=str, default="http://localhost:8000", help="Base URL of the API")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Health check command
    subparsers.add_parser("health", help="Check the health of the API")
    # Generate response command
    subparser_generate = subparsers.add_parser("generate-response", help="Generate a response from the API")

    args = parser.parse_args()

    if args.command == "health":
        health_check(args.base_url)
    elif args.command == "generate-response":
        generate_response(args.base_url)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
