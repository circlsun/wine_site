from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape
from get_age import get_age


def main():
    year_foundation = 1920

    wines = pandas.read_excel(
        'wine3.xlsx',
        usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'],
        na_values='None',
        keep_default_na=False
        ).to_dict('records')

    product_line = defaultdict(list)
    for wine in wines:
        product_line[wine.get('Категория')].append(wine)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        age_winery=get_age(year_foundation),
        wines=product_line,
        )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
