import os
import json
from datetime import datetime
from typing import Dict, List
import config

class BookGenerator:
    """Gerador de livros usando IA"""
    
    def __init__(self, use_local: bool = False, model: str = None):
        self.use_local = use_local
        self.model = model or config.DEFAULT_MODEL
        
        if use_local:
            from .local_handler import LocalAIHandler
            self.ai = LocalAIHandler(self.model)
        else:
            from .openai_handler import OpenAIHandler
            self.ai = OpenAIHandler(self.model)
    
    def generate_book(self, title: str, topic: str, chapters: int, author: str) -> Dict:
        """Gera um livro completo com capítulos"""
        
        print(f"\n🤖 Gerando conteúdo com {self.model}...")
        
        # Gerar introdução
        intro = self._generate_introduction(title, topic)
        
        # Gerar capítulos
        book_chapters = []
        for i in range(1, chapters + 1):
            print(f"   ⏳ Gerando capítulo {i}/{chapters}...")
            chapter = self._generate_chapter(topic, i, chapters)
            book_chapters.append(chapter)
        
        # Gerar conclusão
        conclusion = self._generate_conclusion(title, topic)
        
        # Estrutura do livro
        book_data = {
            'title': title,
            'author': author,
            'topic': topic,
            'generated_at': datetime.now().isoformat(),
            'introduction': intro,
            'chapters': book_chapters,
            'conclusion': conclusion,
            'total_chapters': chapters
        }
        
        return book_data
    
    def _generate_introduction(self, title: str, topic: str) -> str:
        """Gera a introdução do livro"""
        prompt = f"""
        Escreva uma introdução profissional e envolvente para um livro chamado "{title}" 
        sobre o tema "{topic}". A introdução deve ter entre 300-400 palavras.
        """
        return self.ai.generate(prompt)
    
    def _generate_chapter(self, topic: str, chapter_num: int, total_chapters: int) -> Dict:
        """Gera um capítulo individual"""
        prompt = f"""
        Escreva o capítulo {chapter_num} de um livro educativo sobre "{topic}".
        Este é o capítulo {chapter_num} de {total_chapters} capítulos no total.
        O capítulo deve ter entre 800-1000 palavras.
        Inclua um título descritivo para o capítulo.
        """
        
        content = self.ai.generate(prompt)
        
        return {
            'number': chapter_num,
            'title': f'Capítulo {chapter_num}',
            'content': content
        }
    
    def _generate_conclusion(self, title: str, topic: str) -> str:
        """Gera a conclusão do livro"""
        prompt = f"""
        Escreva uma conclusão inspiradora e impactante para um livro chamado "{title}" 
        sobre o tema "{topic}". A conclusão deve ter entre 300-400 palavras.
        """
        return self.ai.generate(prompt)
