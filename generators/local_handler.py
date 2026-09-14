import requests
from typing import Optional
import config

class LocalAIHandler:
    """Handler para modelos IA locais (Ollama)"""
    
    def __init__(self, model: str = 'mistral'):
        self.model = model
        self.base_url = config.OLLAMA_URL
        self._check_connection()
    
    def _check_connection(self):
        """Verifica se Ollama está disponível"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                print(f"✅ Ollama conectado em {self.base_url}")
            else:
                raise ConnectionError("Ollama não respondeu corretamente")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(
                f"❌ Não foi possível conectar ao Ollama em {self.base_url}\n"
                "Certifique-se de que Ollama está rodando: ollama serve"
            )
    
    def generate(self, prompt: str, temperature: float = 0.7) -> str:
        """Gera texto usando modelo local"""
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "temperature": temperature,
                    "stream": False
                },
                timeout=300
            )
            
            if response.status_code == 200:
                return response.json()['response'].strip()
            else:
                raise Exception(f"Erro Ollama: {response.text}")
        
        except requests.exceptions.Timeout:
            raise TimeoutError("⏱️ Timeout ao gerar conteúdo. Tente novamente.")
        except Exception as e:
            raise Exception(f"❌ Erro ao usar modelo local: {str(e)}")
