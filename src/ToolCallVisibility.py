"""
Dedalus Tool Call Visibility - Best Practices
Based on Dedalus documentation: https://docs.dedaluslabs.ai/llms-full.txt

This example shows the most effective ways to see tool calls in Dedalus.
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

def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    print(f"🔧 TOOL CALLED: subtract({a}, {b})")
    result = a - b
    print(f"🔧 TOOL RESULT: {result}")
    return result

async def best_method_streaming():
    """BEST METHOD: Streaming with tool call logging"""
    print("\n" + "="*60)
    print("🎯 BEST METHOD: STREAMING + TOOL LOGGING")
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

async def inspect_result_object():
    """Inspect the result object for detailed tool information"""
    print("\n" + "="*60)
    print("🔍 INSPECT RESULT OBJECT")
    print("="*60)
    
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    result = await runner.run(
        input="Calculate (15 + 27) * 2, then subtract 10 from the result",
        model="openai/gpt-5",
        tools=[add, multiply, subtract]
    )
    
    print(f"Final Output: {result.final_output}")
    
    # Access tool call information from result object
    if hasattr(result, 'tools_called'):
        print(f"\nTools called: {result.tools_called}")
    
    if hasattr(result, 'tool_results'):
        print(f"Tool results: {result.tool_results}")
    
    if hasattr(result, 'steps_used'):
        print(f"Steps used: {result.steps_used}")
    
    if hasattr(result, 'intents'):
        print(f"Intents: {result.intents}")

async def debug_mode_example():
    """Use debug mode for detailed execution information"""
    print("\n" + "="*60)
    print("🐛 DEBUG MODE")
    print("="*60)
    
    client = AsyncDedalus()
    runner = DedalusRunner(client)

    result = await runner.run(
        input="Calculate (15 + 27) * 2",
        model="openai/gpt-5",
        tools=[add, multiply],
        debug=True
    )
    
    print(f"Final Output: {result.final_output}")

async def main():
    """Demonstrate the best ways to see tool calls in Dedalus"""
    print("🚀 DEDALUS TOOL CALL VISIBILITY - BEST PRACTICES")
    print("Based on: https://docs.dedaluslabs.ai/llms-full.txt")
    
    # Show the most effective methods
    await best_method_streaming()
    await inspect_result_object()
    await debug_mode_example()
    
    print("\n" + "="*60)
    print("📋 SUMMARY - HOW TO SEE TOOL CALLS")
    print("="*60)
    print("1. 🎯 STREAMING + TOOL LOGGING:")
    print("   - Use stream=True in runner.run()")
    print("   - Add print statements in your tool functions")
    print("   - Use stream_async() to see real-time execution")
    print()
    print("2. 🔍 INSPECT RESULT OBJECT:")
    print("   - Access result.tools_called")
    print("   - Access result.tool_results")
    print("   - Access result.steps_used")
    print()
    print("3. 🐛 DEBUG MODE:")
    print("   - Use debug=True in runner.run()")
    print("   - Shows detailed execution steps")
    print()
    print("4. 📊 CUSTOM LOGGING:")
    print("   - Add logging to your tool functions")
    print("   - Use wrapper functions for enhanced logging")

if __name__ == "__main__":
    asyncio.run(main())
