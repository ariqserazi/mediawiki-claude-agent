import asyncio
from mcp_server import run_agent

if __name__ == "__main__":
    prompt = input("Enter your research prompt: ")
    result = asyncio.run(run_agent(prompt))
    print("\n\n--- RESULT ---\n")
    print(result)
