from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def generate_pdf(data, output_filename="report.pdf"):
    env = Environment(loader=FileSystemLoader('app/templates'))
    template = env.get_template('report.html')
    html_out = template.render(repos=data)

    HTML(string=html_out).write_pdf(output_filename)
    