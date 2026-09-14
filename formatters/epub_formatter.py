import os
from datetime import datetime
from ebooklib import epub
import config

class EPUBFormatter:
    """Formata livro em EPUB"""
    
    def format_book(self, book_data: dict) -> str:
        """Converte dados do livro para EPUB"""
        
        filename = os.path.join(
            config.OUTPUT_DIR,
            f"{book_data['title'].replace(' ', '_')}.epub"
        )
        
        # Criar livro EPUB
        book = epub.EpubBook()
        book.set_identifier(book_data['title'].lower().replace(' ', '_'))
        book.set_title(book_data['title'])
        book.set_language('pt')
        book.add_author(book_data['author'])
        
        # Capítulo de introdução
        intro_chapter = epub.EpubHtml(
            title='Introdução',
            file_name='intro.xhtml',
            lang='pt'
        )
        intro_chapter.content = f"<h1>Introdução</h1><p>{book_data['introduction']}</p>"
        book.add_item(intro_chapter)
        
        chapters = [intro_chapter]
        
        # Capítulos
        for chapter_data in book_data['chapters']:
            chapter = epub.EpubHtml(
                title=chapter_data['title'],
                file_name=f"chap_{chapter_data['number']}.xhtml",
                lang='pt'
            )
            chapter.content = f"<h1>{chapter_data['title']}</h1><p>{chapter_data['content']}</p>"
            book.add_item(chapter)
            chapters.append(chapter)
        
        # Capítulo de conclusão
        conclusion_chapter = epub.EpubHtml(
            title='Conclusão',
            file_name='conclusion.xhtml',
            lang='pt'
        )
        conclusion_chapter.content = f"<h1>Conclusão</h1><p>{book_data['conclusion']}</p>"
        book.add_item(conclusion_chapter)
        chapters.append(conclusion_chapter)
        
        # Definir índice e spine
        book.toc = tuple(chapters)
        book.spine = ['nav'] + chapters
        
        # Adicionar items de navegação
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        
        # Salvar
        epub.write_epub(filename, book, {})
        
        print(f"📖 EPUB formatado: {filename}")
        return filename
