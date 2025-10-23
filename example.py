"""
Example script showing how to use environment variables in your Python project.
"""

from env_loader import setup_environment, get_env_var


def main():
    """Example main function using environment variables."""
    
    # Set up environment variables from .env file
    setup_environment()
    
    # Get API keys (these will be loaded from .env file)
    try:
        openai_key = get_env_var("OPENAI_API_KEY", required=True)
        print(f"✅ OpenAI API Key loaded successfully")
        
        anthropic_key = get_env_var("ANTHROPIC_API_KEY", required=True)
        print(f"✅ Anthropic API Key loaded successfully")
        
    except ValueError as e:
        print(f"❌ Error loading required API keys: {e}")
        print("Make sure to create a .env file with your API keys")
        return
    
    # Get optional configuration
    debug_mode = get_env_var("DEBUG", default="False").lower() == "true"
    port = int(get_env_var("PORT", default="8000"))
    environment = get_env_var("ENVIRONMENT", default="development")
    
    print(f"🔧 Configuration:")
    print(f"   Debug mode: {debug_mode}")
    print(f"   Port: {port}")
    print(f"   Environment: {environment}")
    
    # Example: Use the API keys (replace with actual API calls)
    print(f"\n🚀 Ready to make API calls!")
    print(f"   OpenAI key: {openai_key[:10]}...")
    print(f"   Anthropic key: {anthropic_key[:10]}...")


if __name__ == "__main__":
    main()
