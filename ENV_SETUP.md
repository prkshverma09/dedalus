# Environment Variables Setup Guide

## 🔐 Secure API Key Management

This project uses environment variables to securely store API keys and configuration. Your API keys will **never** be committed to git.

## 📁 Files Created

- `.env` - Your actual API keys (NOT committed to git)
- `env_template.txt` - Template showing what variables to set
- `env_loader.py` - Python script to load environment variables
- `example.py` - Example showing how to use the environment variables
- `requirements.txt` - Python dependencies

## 🚀 Quick Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Add Your API Keys
Edit the `.env` file and replace the placeholder values with your actual API keys:

```bash
# Edit .env file
nano .env
```

Replace the placeholder values:
```
OPENAI_API_KEY=sk-your-actual-openai-key-here
ANTHROPIC_API_KEY=sk-ant-your-actual-anthropic-key-here
GOOGLE_API_KEY=your-actual-google-key-here
DATABASE_URL=your-actual-database-url-here
```

### 3. Test the Setup
```bash
python example.py
```

## 🔧 How to Use in Your Code

### Method 1: Using the env_loader module
```python
from env_loader import setup_environment, get_env_var

# Set up environment (call this once at startup)
setup_environment()

# Get API keys
openai_key = get_env_var("OPENAI_API_KEY", required=True)
anthropic_key = get_env_var("ANTHROPIC_API_KEY", required=True)

# Get optional config
debug_mode = get_env_var("DEBUG", default="False").lower() == "true"
port = int(get_env_var("PORT", default="8000"))
```

### Method 2: Using python-dotenv directly
```python
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access environment variables
openai_key = os.getenv("OPENAI_API_KEY")
anthropic_key = os.getenv("ANTHROPIC_API_KEY")
```

## 🛡️ Security Features

- ✅ `.env` file is in `.gitignore` - never committed
- ✅ Template file shows what variables are needed
- ✅ Environment variables override .env file values
- ✅ Required variables throw errors if missing
- ✅ Sensitive data never appears in logs

## 📝 Adding New Environment Variables

1. Add to `.env` file:
   ```
   NEW_API_KEY=your_new_api_key_here
   ```

2. Use in your code:
   ```python
   new_key = get_env_var("NEW_API_KEY", required=True)
   ```

3. Update `env_template.txt` to document the new variable

## 🔍 Troubleshooting

- **"Required environment variable not found"**: Check your `.env` file exists and has the correct variable name
- **"Warning: .env file not found"**: Make sure you copied `env_template.txt` to `.env`
- **API calls failing**: Verify your API keys are correct and active
