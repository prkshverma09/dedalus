"""
Dedalus Tool Call Visibility - Based on Official Documentation
https://docs.dedaluslabs.ai/llms.txt

This example demonstrates the best ways to see tool calls as shown in the Dedalus documentation.
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

async def streaming_example():
    """Based on: https://docs.dedaluslabs.ai/examples/03-streaming.md"""
    print("\n" + "="*60)
    print("📡 STREAMING EXAMPLE (from Dedalus docs)")
    print("="*60)
    
    client = AsyncDedalus()
    runner = DedalusRunner(client)
    
    result = runner.run(
        input="Calculate (15 + 27) * 2, then subtract 10",
        model="openai/gpt-5",
        tools=[add, multiply, subtract],
        stream=True
    )
    
    await stream_async(result)

async def tool_chaining_example():
    """Based on: https://docs.dedaluslabs.ai/examples/07-tool-chaining.md"""
    print("\n" + "="*60)
    print("🔗 TOOL CHAINING EXAMPLE (from Dedalus docs)")
    print("="*60)
    
    client = AsyncDedalus()
    runner = DedalusRunner(client)
    
    result = await runner.run(
        input="Calculate (15 + 27) * 2, then subtract 10",
        model="openai/gpt-5",
        tools=[add, multiply, subtract]
    )
    
    print(f"Final Output: {result.final_output}")
    
    # Inspect the result object for tool information
    if hasattr(result, 'tools_called'):
        print(f"Tools called: {result.tools_called}")
    
    if hasattr(result, 'tool_results'):
        print(f"Tool results: {result.tool_results}")
    
    if hasattr(result, 'steps_used'):
        print(f"Steps used: {result.steps_used}")

async def basic_tools_example():
    """Based on: https://docs.dedaluslabs.ai/examples/02-basic-tools.md"""
    print("\n" + "="*60)
    print("🛠️ BASIC TOOLS EXAMPLE (from Dedalus docs)")
    print("="*60)
    
    client = AsyncDedalus()
    runner = DedalusRunner(client)
    
    result = await runner.run(
        input="Calculate (15 + 27) * 2",
        model="openai/gpt-5",
        tools=[add, multiply]
    )
    
    print(f"Result: {result.final_output}")

async def debug_mode_example():
    """Use debug mode to see detailed execution"""
    print("\n" + "="*60)
    print("🐛 DEBUG MODE EXAMPLE")
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
    """Run all examples from the Dedalus documentation"""
    print("📚 DEDALUS TOOL CALL VISIBILITY")
    print("Based on: https://docs.dedaluslabs.ai/llms.txt")
    
    # Run examples from the documentation
    await streaming_example()
    # await tool_chaining_example()
    # await basic_tools_example()
    # await debug_mode_example()
    
    print("\n" + "="*60)
    print("📋 SUMMARY FROM DEDALUS DOCUMENTATION")
    print("="*60)
    print("✅ Streaming: Use stream=True + stream_async() for real-time tool execution")
    print("✅ Tool Chaining: Advanced workflows with automatic tool chaining")
    print("✅ Basic Tools: Simple tool execution with DedalusRunner")
    print("✅ Debug Mode: Use debug=True for detailed execution information")
    print("✅ Result Inspection: Access result.tools_called, result.tool_results")

if __name__ == "__main__":
    asyncio.run(main())
