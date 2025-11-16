import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Comet ML Configuration
    COMET_API_KEY = os.getenv("COMET_API_KEY")
    COMET_PROJECT_NAME = os.getenv("COMET_PROJECT_NAME", "ai-executive-agent")
    AGENT_NAME = os.getenv("AGENT_NAME", "ExecutiveAssistant")
    
    # LLM Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    
    # Apidog Configuration
    APIDOG_API_KEY = os.getenv("APIDOG_API_KEY")
    APIDOG_PROJECT_ID = os.getenv("APIDOG_PROJECT_ID")
    
    # Browser Configuration
    BROWSER_TIMEOUT = int(os.getenv("BROWSER_TIMEOUT", "30"))
    HEADLESS_MODE = os.getenv("HEADLESS_MODE", "true").lower() == "true"
    
    # Database & Storage
    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./data/vectordb")
    KNOWLEDGE_BASE_PATH = os.getenv("KNOWLEDGE_BASE_PATH", "./data/knowledge")
    
    # LLM Settings
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

settings = Settings()
