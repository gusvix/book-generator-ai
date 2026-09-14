# 📚 Gerador Automático de Livros com IA

Um gerador de livros técnicos e educativos usando Python e modelos de IA.

## 🚀 Características

- ✅ Gera capítulos automaticamente com IA
- ✅ Formata em PDF e EPUB
- ✅ Suporta modelos locais ou APIs
- ✅ Personalizável (títulos, temas, quantidade de capítulos)
- ✅ Fácil de usar para iniciantes

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/gusvix/book-generator-ai.git
cd book-generator-ai
```

### 2. Crie um ambiente virtual (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

## 📖 Como Usar

### Opção 1: Usando API (OpenAI - Recomendado para iniciantes)
```bash
python main.py --title "Meu Livro" --chapters 5 --topic "Python para Iniciantes"
```

### Opção 2: Usando Modelo Local (Ollama)
```bash
python main.py --title "Meu Livro" --chapters 5 --topic "Python" --local
```

## 📁 Estrutura do Projeto

```
book-generator-ai/
├── main.py                 # Arquivo principal
├── requirements.txt        # Dependências
├── config.py              # Configurações
├── generators/
│   ├── book_generator.py  # Gerador de livros
│   ├── openai_handler.py  # Integração OpenAI
│   └── local_handler.py   # Modelos locais (Ollama)
├── formatters/
│   ├── pdf_formatter.py   # Exportar para PDF
│   └── epub_formatter.py  # Exportar para EPUB
├── output/                # Livros gerados
└── examples/              # Exemplos de uso
```

## 🎯 Exemplos

### Gerar um livro sobre Python
```bash
python main.py --title "Guia Completo Python" --chapters 10 --topic "Python Avançado"
```

### Gerar um livro educativo
```bash
python main.py --title "Fundamentos de IA" --chapters 8 --topic "Machine Learning" --format pdf
```

## 🔑 Configurar API Key (OpenAI)

1. Vá para: https://platform.openai.com/api-keys
2. Crie uma chave API
3. Adicione ao seu sistema:

```bash
# Windows (PowerShell)
$env:OPENAI_API_KEY = "sua-chave-aqui"

# Linux/Mac
export OPENAI_API_KEY="sua-chave-aqui"
```

## 📦 Dependências Principais

- `openai` - API da OpenAI
- `reportlab` - Gerar PDF
- `ebooklib` - Gerar EPUB
- `requests` - Requisições HTTP

## 🛠️ Requisitos de Sistema

- **RAM mínima**: 4GB
- **Espaço em disco**: 2GB (para modelos locais)
- **Conexão**: Necessária para APIs online

## 📝 Licença

MIT

## 💬 Dúvidas?

Abra uma issue no repositório!

---

**Desenvolvido com ❤️ para iniciantes**