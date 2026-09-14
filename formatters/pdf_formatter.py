import os
from io import BytesIO
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
import config

class PDFFormatter:
    """Formata livro em PDF"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Configura estilos personalizados"""
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=28,
            textColor=colors.HexColor('#1a1a1a'),
            spaceAfter=30,
            alignment=1  # Center
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomHeading',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=12,
            spaceBefore=12
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['BodyText'],
            fontSize=11,
            alignment=4,  # Justified
            spaceAfter=12
        ))
    
    def format_book(self, book_data: dict) -> str:
        """Converte dados do livro para PDF"""
        
        filename = os.path.join(
            config.OUTPUT_DIR,
            f"{book_data['title'].replace(' ', '_')}.pdf"
        )
        
        doc = SimpleDocTemplate(
            filename,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        story = []
        
        # Capa
        story.append(Paragraph(book_data['title'], self.styles['CustomTitle']))
        story.append(Spacer(1, 0.3*inch))
        story.append(Paragraph(f"Tema: {book_data['topic']}", self.styles['Heading2']))
        story.append(Paragraph(f"Autor: {book_data['author']}", self.styles['Normal']))
        story.append(Paragraph(f"Data: {datetime.now().strftime('%d/%m/%Y')}", self.styles['Normal']))
        story.append(PageBreak())
        
        # Introdução
        story.append(Paragraph("Introdução", self.styles['CustomHeading']))
        story.append(Paragraph(book_data['introduction'], self.styles['CustomBody']))
        story.append(PageBreak())
        
        # Capítulos
        for chapter in book_data['chapters']:
            story.append(Paragraph(f"{chapter['title']}", self.styles['CustomHeading']))
            story.append(Paragraph(chapter['content'], self.styles['CustomBody']))
            story.append(PageBreak())
        
        # Conclusão
        story.append(Paragraph("Conclusão", self.styles['CustomHeading']))
        story.append(Paragraph(book_data['conclusion'], self.styles['CustomBody']))
        
        # Gerar PDF
        doc.build(story)
        
        print(f"📄 PDF formatado: {filename}")
        return filename
