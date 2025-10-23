"""
Enhanced Dedalus Tools Example - Multiple Ways to See Tool Calls
Based on Dedalus documentation: https://docs.dedaluslabs.ai/llms-full.txt
"""

import asyncio
from dedalus_labs import AsyncDedalus, DedalusRunner
from dotenv import load_dotenv
from dedalus_labs.utils.streaming import stream_async
import json

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

def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    print(f"🔧 TOOL CALLED: subtract({a}, {b})")
    result = a - b
    print(f"🔧 TOOL RESULT: {result}")
    return result

async def method_1_streaming():
    """Method 1: Use streaming to see tool calls in real-time"""
    print("\n" + "="*60)
    print("METHOD 1: STREAMING OUTPUT")
    print("="*60)
    
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    result = runner.run(
        input="Calculate (15 + 27) * 2, then subtract 10 from the result",
        model="openai/gpt-5",
        tools=[add, multiply, subtract],
        stream=True
    )
    
    await stream_async(result)

async def method_2_inspect_result():
    """Method 2: Inspect the result object for tool call details"""
    print("\n" + "="*60)
    print("METHOD 2: INSPECT RESULT OBJECT")
    print("="*60)
    
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    result = await runner.run(
        input="Calculate (15 + 27) * 2, then subtract 10 from the result",
        model="openai/gpt-5",
        tools=[add, multiply, subtract]
    )
    
    print(f"Final Output: {result.final_output}")
    
    # Inspect the result object for tool call information
    if hasattr(result, 'messages'):
        print(f"\nTotal messages: {len(result.messages)}")
        for i, message in enumerate(result.messages):
            print(f"Message {i+1}: {message}")
    
    if hasattr(result, 'tool_calls'):
        print(f"\nTool calls made: {len(result.tool_calls)}")
        for i, tool_call in enumerate(result.tool_calls):
            print(f"Tool call {i+1}: {tool_call}")
    
    # Try to access other attributes that might contain tool information
    print(f"\nResult attributes: {dir(result)}")

async def method_3_debug_mode():
    """Method 3: Use debug/verbose mode if available"""
    print("\n" + "="*60)
    print("METHOD 3: DEBUG MODE")
    print("="*60)
    
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    # Try with debug/verbose parameters
    result = await runner.run(
        input="Calculate (15 + 27) * 2",
        model="openai/gpt-5",
        tools=[add, multiply],
        debug=True,  # Try debug mode
        verbose=True  # Try verbose mode
    )
    
    print(f"Final Output: {result.final_output}")

async def method_4_custom_logging():
    """Method 4: Custom logging with wrapper functions"""
    print("\n" + "="*60)
    print("METHOD 4: CUSTOM LOGGING")
    print("="*60)
    
    # Create wrapper functions that log tool calls
    def logged_add(a: int, b: int) -> int:
        print(f"📊 LOGGED TOOL CALL: add({a}, {b})")
        result = add(a, b)
        print(f"📊 LOGGED TOOL RESULT: {result}")
        return result
    
    def logged_multiply(a: int, b: int) -> int:
        print(f"📊 LOGGED TOOL CALL: multiply({a}, {b})")
        result = multiply(a, b)
        print(f"📊 LOGGED TOOL RESULT: {result}")
        return result
    
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    result = await runner.run(
        input="Calculate (15 + 27) * 2",
        model="openai/gpt-5",
        tools=[logged_add, logged_multiply]
    )
    
    print(f"Final Output: {result.final_output}")

async def main():
    """Run all methods to demonstrate different ways to see tool calls"""
    print("🔍 DEDALUS TOOL CALL VISIBILITY DEMONSTRATION")
    print("Based on: https://docs.dedaluslabs.ai/llms-full.txt")
    
    # Run all methods
    await method_1_streaming()
    await method_2_inspect_result()
    await method_3_debug_mode()
    await method_4_custom_logging()
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print("✅ Method 1: Streaming shows real-time tool execution")
    print("✅ Method 2: Inspect result object for tool call details")
    print("✅ Method 3: Debug mode (if supported)")
    print("✅ Method 4: Custom logging with wrapper functions")

if __name__ == "__main__":
    asyncio.run(main())
