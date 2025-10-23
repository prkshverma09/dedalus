"""
Environment variable loader for the Dedalus project.
This script loads API keys and other environment variables from a .env file.
"""

import os
from pathlib import Path
from typing import Optional


def load_env_file(env_file_path: str = ".env") -> dict:
    """
    Load environment variables from a .env file.
    
    Args:
        env_file_path: Path to the .env file (default: ".env")
    
    Returns:
        Dictionary of environment variables
    """
    env_vars = {}
    
    # Get the project root directory
    project_root = Path(__file__).parent
    env_file = project_root / env_file_path
    
    if not env_file.exists():
        print(f"Warning: {env_file_path} file not found. Using system environment variables only.")
        return env_vars
    
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
            
            # Parse KEY=VALUE format
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # Remove quotes if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                
                env_vars[key] = value
    
    return env_vars


def get_env_var(key: str, default: Optional[str] = None, required: bool = False) -> str:
    """
    Get an environment variable, checking .env file first, then system environment.
    
    Args:
        key: Environment variable name
        default: Default value if not found
        required: Whether the variable is required (raises error if missing)
    
    Returns:
        Environment variable value
    
    Raises:
        ValueError: If required variable is not found
    """
    # Load .env file variables
    env_vars = load_env_file()
    
    # Check .env file first, then system environment
    value = env_vars.get(key) or os.getenv(key)
    
    if value is None:
        if required:
            raise ValueError(f"Required environment variable '{key}' not found")
        return default or ""
    
    return value


def setup_environment():
    """
    Set up environment variables from .env file.
    Call this function at the start of your application.
    """
    env_vars = load_env_file()
    
    # Set environment variables in os.environ
    for key, value in env_vars.items():
        if key not in os.environ:  # Don't override existing system env vars
            os.environ[key] = value
    
    print(f"Loaded {len(env_vars)} environment variables from .env file")


# Example usage
if __name__ == "__main__":
    # Set up environment
    setup_environment()
    
    # Example: Get API keys
    try:
        openai_key = get_env_var("OPENAI_API_KEY", required=True)
        print(f"OpenAI API Key loaded: {openai_key[:10]}...")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Example: Get optional variables
    debug_mode = get_env_var("DEBUG", default="False")
    port = get_env_var("PORT", default="8000")
    
    print(f"Debug mode: {debug_mode}")
    print(f"Port: {port}")
