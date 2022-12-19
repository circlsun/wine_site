from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
import pandas
import argparse
from jinja2 import Environment, FileSystemLoader, select_autoescape
from get_age import get_age


def main():
    foundation_year = 1920

    parser = argparse.ArgumentParser(
        description='This script run web-market of wine')
    parser.add_argument(
        '-d', '--dir', default='product_line.xlsx',
        help='Input the path to the folder with the excel-file')
    args = parser.parse_args()

    wines = pandas.read_excel(
        args.dir,
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
        winery_age=get_age(foundation_year),
        products=product_line,
        )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
