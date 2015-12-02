from markdown import markdown
import pdfkit

input_filename = 'README.md'
output_filename = 'README.pdf'

with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format='html4')

print(html_text)
pdfkit.from_string('<h3>Deerlet</h3>h3>', output_filename)
