import argparse
import sys
from generators.book_generator import BookGenerator
from formatters.pdf_formatter import PDFFormatter
from formatters.epub_formatter import EPUBFormatter
import config

def main():
    parser = argparse.ArgumentParser(description='Gerar livros com IA')
    parser.add_argument('--title', type=str, default='Meu Livro', help='Título do livro')
    parser.add_argument('--chapters', type=int, default=5, help='Número de capítulos')
    parser.add_argument('--topic', type=str, default='Python', help='Tema do livro')
    parser.add_argument('--format', type=str, default='pdf', choices=['pdf', 'epub', 'both'], help='Formato de saída')
    parser.add_argument('--local', action='store_true', help='Usar modelo local (Ollama) ao invés de API')
    parser.add_argument('--author', type=str, default='Gerador IA', help='Autor do livro')
    
    args = parser.parse_args()
    
    print(f"\n📚 Gerando livro: {args.title}")
    print(f"📖 Capítulos: {args.chapters}")
    print(f"🔖 Tema: {args.topic}")
    print(f"💾 Formato: {args.format}")
    print("-" * 50)
    
    # Gerar conteúdo
    generator = BookGenerator(
        use_local=args.local,
        model='mistral' if args.local else config.DEFAULT_MODEL
    )
    
    book_data = generator.generate_book(
        title=args.title,
        topic=args.topic,
        chapters=args.chapters,
        author=args.author
    )
    
    # Formatar e salvar
    if args.format in ['pdf', 'both']:
        print("\n📄 Gerando PDF...")
        pdf_formatter = PDFFormatter()
        pdf_file = pdf_formatter.format_book(book_data)
        print(f"✅ PDF salvo: {pdf_file}")
    
    if args.format in ['epub', 'both']:
        print("\n📖 Gerando EPUB...")
        epub_formatter = EPUBFormatter()
        epub_file = epub_formatter.format_book(book_data)
        print(f"✅ EPUB salvo: {epub_file}")
    
    print("\n🎉 Livro gerado com sucesso!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Operação cancelada pelo usuário")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        sys.exit(1)
