import os
from dotenv import load_dotenv

load_dotenv()

# Configurações da API
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'mistral')

# Configurações de Geração
DEFAULT_CHAPTERS = 5
DEFAULT_WORDS_PER_CHAPTER = 800
DEFAULT_MODEL = 'gpt-3.5-turbo'  # ou 'gpt-4' para melhor qualidade

# Diretórios
OUTPUT_DIR = 'output'
TEMPLATES_DIR = 'templates'

# Criar diretórios se não existirem
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)
