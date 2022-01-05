"""

"""
from bs4 import BeautifulSoup
import requests


def searchWollplatz(brand, product_name):
    brand_edited = brand.lower()
    name_edited = product_name.replace(' ', '-').lower()
    link = requests.get(f"https://www.wollplatz.de/wolle/{brand_edited}/{brand_edited}-{name_edited}")
    soup = BeautifulSoup(link.content, 'lxml')
    if not soup.find('h1', id="pageheadertitle"):
        name = "Not Found"
    else:
        name = soup.find('h1', id="pageheadertitle").text

    if not soup.find('span', class_="product-price", itemprop="price"):
        price = "-"
    else:
        price = soup.find('span', class_="product-price", itemprop="price").text

    if not soup.find('span', class_="stock-green"):
        delivery = "-"
    else:
        delivery = soup.find('span', class_="stock-green").text

    if not soup.find("div", {"id": "pdetailTableSpecs"}):
        needle_size = "-"
        composition = "-"
    else:
        table = soup.find("div", {"id": "pdetailTableSpecs"}).text

        start_needle_size = table.find("Nadelstärke") + len("Nadelstärke")
        end_needle_size = table.find("Garnstärke")
        needle_size = table[start_needle_size:end_needle_size].strip()

        start_composition = table.find("Zusammenstellung") + len("Zusammenstellung")
        end_composition = table.find("Nadelstärke")
        composition = table[start_composition:end_composition].strip()

    product = {'website': 'https://www.wollplatz.de/',
               'name': name,
               'price': price,
               'delivery': delivery,
               'needle_size': needle_size,
               'composition': composition}
    return product

