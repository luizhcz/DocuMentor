import pdfkit
import markdown2

class GeneratorService:
    def __init__(self):
        pass

    def generate_pdf_from_markdown(self, markdown_text, output_file):
        # Converter Markdown para HTML
        html_content = markdown2.markdown(markdown_text)
        
        # Gerar PDF a partir do HTML
        pdfkit.from_string(html_content, output_file, options={'encoding': 'UTF-8'})
        
        print(f"PDF gerado e salvo em: {output_file}")