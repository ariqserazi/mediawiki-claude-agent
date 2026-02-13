import asyncio
from claude_agent import run_agent

if __name__ == "__main__":
    prompt = input("Enter your research prompt: ")
    result = asyncio.run(run_agent(prompt))
    print("\n\n--- RESULT ---\n")
    print(result)
