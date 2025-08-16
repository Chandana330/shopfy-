from fastapi import FastAPI, HTTPException
from models import BrandInsights
from fetcher import fetch_products_json, fetch_page_text

app = FastAPI(title="Shopify Insights Fetcher")

@app.get("/fetch_insights/", response_model=BrandInsights)
def fetch_insights(website_url: str):
    try:
        product_catalog = fetch_products_json(website_url)
        hero_products = product_catalog[:3]  # simple example: first 3 as hero
        
        privacy_policy = fetch_page_text(f"{website_url}/pages/privacy-policy")
        return_policy = fetch_page_text(f"{website_url}/pages/return-policy")
        
        # Example structure
        brand_insights = BrandInsights(
            website_url=website_url,
            hero_products=hero_products,
            product_catalog=product_catalog,
            privacy_policy=privacy_policy,
            return_policy=return_policy,
            faqs={},
            social_handles={},
            contact_details={},
            about_text=fetch_page_text(f"{website_url}/pages/about-us"),
            important_links={}
        )
        return brand_insights

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=401, detail="Website not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Error: {e}")
