"""
Simple Dedalus Tool Call Visibility
Based on Dedalus documentation: https://docs.dedaluslabs.ai/llms.txt

This shows the BEST way to see tool calls in Dedalus.
"""

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
    """The BEST way to see tool calls in Dedalus"""
    print("🎯 BEST METHOD: STREAMING + TOOL LOGGING")
    print("Based on: https://docs.dedaluslabs.ai/llms.txt")
    print()
    
    client = AsyncDedalus()
    runner = DedalusRunner(client)
    
    # Use streaming to see tool calls in real-time
    result = runner.run(
        input="Calculate (15 + 27) * 2",
        model="openai/gpt-5",
        tools=[add, multiply],
        stream=True  # This is the key!
    )
    
    # Stream the output to see tool calls as they happen
    await stream_async(result)
    
    print("\n" + "="*50)
    print("✅ SUCCESS! You can see tool calls with:")

if __name__ == "__main__":
    asyncio.run(main())
