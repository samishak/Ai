#numerous network requests to fetch web pages 

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://docs.langchain.com/oss/python/langchain/overview",
    "https://docs.langchain.com/oss/python/langchain/philosophy",
    "https://docs.langchain.com/oss/python/langchain/messages",
]

def fetch_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        print(f"Fetched {len(soup.get_text())} characters from {url}")
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")

threads = []

# Create and start threads
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All web pages fetched")
