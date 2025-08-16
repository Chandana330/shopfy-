# Shopify Insights Fetcher

A Python FastAPI project to fetch Shopify store insights (products, policies, contact info, etc.) without using the official Shopify API.

## Features

- Fetch full product catalog of a Shopify store
- Identify hero products (featured on homepage)
- Extract Privacy Policy, Return/Refund Policy, and About text
- Get FAQs, social media handles, contact details, and important links
- Returns data as structured JSON via a REST API

## Tech Stack

- **Language:** Python  
- **Framework:** FastAPI  
- **Parsing:** BeautifulSoup4  
- **HTTP Requests:** Requests library  
- **Optional DB:** MySQL  

## Setup Instructions

1. **Clone the repo:**
```bash
git clone <your-repo-url>
cd shopify_insights_fetcher
Create & activate virtual environment:

bash
Copy
Edit
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Linux/Mac
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the FastAPI server:

bash
Copy
Edit
uvicorn main:app --reload
Access API Documentation:
Open http://127.0.0.1:8000/docs in your browser and test /fetch_insights/?website_url=<shopify-url>

Example API Call
bash
Copy
Edit
GET /fetch_insights/?website_url=https://memy.co.in
Response:

json
Copy
Edit
{
  "website_url": "https://memy.co.in",
  "hero_products": [...],
  "product_catalog": [...],
  "privacy_policy": "...",
  "return_policy": "...",
  "faqs": {},
  "social_handles": {},
  "contact_details": {},
  "about_text": "...",
  "important_links": {}
}
Future Improvements (Bonus)
Competitor analysis with same insights

Persist data into MySQL

Extract more structured FAQs and social media links

yaml
Copy
Edit
Access API Documentation:
Open http://127.0.0.1:8000/docs in your browser and test /fetch_insights/?website_url=<shopify-url>
