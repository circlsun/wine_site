from http.server import HTTPServer, SimpleHTTPRequestHandler
from get_age import get_age
from jinja2 import Environment, FileSystemLoader, select_autoescape

year_foundation = 1920 

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    age_winery=get_age(year_foundation)
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
