from googlesearch import search
from urllib.parse import quote_plus
import yaml
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Load e-commerce sites from YAML
def load_ecommerce_sites(filename="options.yml"):
    with open(filename, "r") as file:
        options = yaml.safe_load(file)
        return options["ecommerce_sites"]

ecommerce_sites = load_ecommerce_sites()

# Keywords to detect e-commerce and filter out blogs/reviews
ecom_keywords = ["buy", "shop", "store", "gifts", "personalized", "custom", "order", "cart", "checkout", "free shipping", "delivery", "sale"]
exclude_keywords = ["blog", "guide", "review", "article", "gift ideas", "recommendations", "top 10", "best gifts", "pinterest", "nyt", "quora"]

def is_valid_ecommerce_link(url, description):
    """Check if a link is an e-commerce site using both the URL and description."""
    url_lower = url.lower()
    description_lower = description.lower()

    # Ensure it's from a known e-commerce site OR contains e-commerce signals
    is_ecom = any(site in url for site in ecommerce_sites) or any(keyword in url_lower for keyword in ecom_keywords)

    # Check description for e-commerce signals
    has_ecom_description = any(keyword in description_lower for keyword in ecom_keywords)

    # Exclude blogs/reviews/guides
    is_not_blog = not any(keyword in url_lower for keyword in exclude_keywords) and not any(keyword in description_lower for keyword in exclude_keywords)

    return (is_ecom or has_ecom_description) and is_not_blog

def analyze_sentiment(text):
    """Perform sentiment analysis on product reviews or descriptions."""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Returns a score between -1 and 1

def fetch_product_reviews(url):
    """Scrape product page to extract reviews for sentiment analysis."""
    try:
        response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Attempt to find review elements (this will vary by site)
        reviews = soup.find_all("p", class_=lambda x: x and "review" in x.lower())
        review_texts = [review.get_text() for review in reviews]
        
        if review_texts:
            avg_sentiment = sum(analyze_sentiment(text) for text in review_texts) / len(review_texts)
            return avg_sentiment
        return 0  # Default sentiment if no reviews found
    except Exception:
        return 0

import time

def fetch_gift_recommendations(query, num_results=5):
    """Fetch valid gift recommendation links using Google Search, ensuring they belong to valid e-commerce sites."""
    try:
        safe_query = quote_plus(query)  # Ensure query is URL-safe
        valid_results = []
        
        search_results = search(safe_query, num_results=num_results * 5)

        for i, result in enumerate(search_results):
            if isinstance(result, tuple):
                url, description = result  # Extract both URL and description
            else:
                url, description = result, ""

            if not url.startswith("http"):
                continue

            if is_valid_ecommerce_link(url, description):
                sentiment_score = fetch_product_reviews(url)
                valid_results.append((url, sentiment_score))

            # Stop once we have enough valid results
            if len(valid_results) >= num_results:
                break

            time.sleep(2)  # 🔴 Add a delay between requests

        valid_results.sort(key=lambda x: x[1], reverse=True)
        return [url for url, _ in valid_results]

    except Exception as e:
        return [f"Error fetching results: {e}"]