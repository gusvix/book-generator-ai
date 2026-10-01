import os
import json
import requests
from typing import Optional
import config

class OpenAIHandler:
    """Handler para integração com API OpenAI"""
    
    def __init__(self, model: str = 'gpt-3.5-turbo'):
        self.model = model
        self.api_key = config.OPENAI_API_KEY
        
        if not self.api_key:
            raise ValueError(
                "❌ OPENAI_API_KEY não configurada. "
                "Configure a variável de ambiente ou edite o arquivo .env"
            )
    
    def generate(self, prompt: str, temperature: float = 0.7, max_tokens: int = 1500) -> str:
        """Gera texto usando API OpenAI"""
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key)
            
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Você é um escritor profissional de livros educativos e técnicos."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return response.choices[0].message.content.strip()
        
        except ImportError:
            raise ImportError("❌ Instale a biblioteca: pip install openai")
        except Exception as e:
            raise Exception(f"❌ Erro ao chamar API OpenAI: {str(e)}")
