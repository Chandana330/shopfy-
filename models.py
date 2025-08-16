from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    id: str
    title: str
    description: Optional[str]
    price: Optional[str]
    url: Optional[str]

class BrandInsights(BaseModel):
    website_url: str
    brand_name: Optional[str]
    hero_products: List[Product] = []
    product_catalog: List[Product] = []
    privacy_policy: Optional[str]
    return_policy: Optional[str]
    faqs: Optional[dict] = {}
    social_handles: Optional[dict] = {}
    contact_details: Optional[dict] = {}
    about_text: Optional[str]
    important_links: Optional[dict] = {}
