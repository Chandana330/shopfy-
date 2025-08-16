import requests
from bs4 import BeautifulSoup
from models import Product

def fetch_products_json(store_url):
    try:
        response = requests.get(f"{store_url}/products.json")
        if response.status_code != 200:
            return []
        data = response.json()
        products = []
        for p in data.get('products', []):
            products.append(Product(
                id=str(p.get('id')),
                title=p.get('title'),
                description=p.get('body_html'),
                price=p.get('variants')[0].get('price') if p.get('variants') else None,
                url=f"{store_url}/products/{p.get('handle')}"
            ))
        return products
    except:
        return []

def fetch_page_text(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text(separator="\n").strip()
    except:
        return None
