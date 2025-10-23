import asyncio
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv
from dedalus_labs.utils.streaming import stream_async

load_dotenv()

def add(a: int, b: int) -> int:
    """Add two numbers."""
    print(f"🔧 TOOL CALLED: add({a}, {b})")
    result = a + b
    print(f"🔧 TOOL RESULT: {result}")
    return result

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    print(f"🔧 TOOL CALLED: multiply({a}, {b})")
    result = a * b
    print(f"🔧 TOOL RESULT: {result}")
    return result

async def main():
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    # Method 1: Use streaming to see tool calls in real-time
    print("=== Using Streaming to See Tool Calls ===")
    result = runner.run(
        input="Calculate (15 + 27) * 2",
        model="openai/gpt-5",
        tools=[add, multiply],
        stream=True  # Enable streaming
    )
    
    # Stream the output to see tool calls as they happen
    await stream_async(result)

if __name__ == "__main__":
    asyncio.run(main())