from flask import Flask, render_template, request, jsonify, send_file
import os
import config
from generators.book_generator import BookGenerator
from formatters.pdf_formatter import PDFFormatter
from formatters.epub_formatter import EPUBFormatter

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    title = data.get('title', 'Meu Livro')
    topic = data.get('topic', 'Python')
    chapters = min(max(int(data.get('chapters', 3)), 1), 10)
    author = data.get('author', 'Gerador IA')
    fmt = data.get('format', 'pdf')
    use_local = data.get('local', False)

    try:
        generator = BookGenerator(
            use_local=use_local,
            model='mistral' if use_local else config.DEFAULT_MODEL
        )

        book_data = generator.generate_book(
            title=title,
            topic=topic,
            chapters=chapters,
            author=author
        )

        files = []
        if fmt in ['pdf', 'both']:
            pdf_formatter = PDFFormatter()
            pdf_file = pdf_formatter.format_book(book_data)
            files.append({'name': os.path.basename(pdf_file), 'format': 'PDF'})

        if fmt in ['epub', 'both']:
            epub_formatter = EPUBFormatter()
            epub_file = epub_formatter.format_book(book_data)
            files.append({'name': os.path.basename(epub_file), 'format': 'EPUB'})

        return jsonify({'success': True, 'files': files})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/download/<path:filename>')
def download(filename):
    filename = os.path.basename(filename)
    filepath = os.path.join(config.OUTPUT_DIR, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404
    return send_file(filepath, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
