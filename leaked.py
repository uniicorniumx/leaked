# Import requests library to send HTTP requests
import requests

# Import BeautifulSoup library to parse HTML content
from bs4 import BeautifulSoup

# Define the web app URL
web_app_url = "https://example.com"

# Define a list of common data leakage paths
data_leakage_paths = ["/.git", "/.env", "/.htaccess", "/.htpasswd", "/.DS_Store", "/.svn", "/.well-known", "/robots.txt", "/sitemap.xml", "/backup", "/log", "/tmp"]

# Define a set of visited URLs to avoid duplicates
visited_urls = set()

# Define a recursive function to crawl the web app and check for data leakage
def crawl_and_check(url):
    # Check if the URL is already visited
    if url in visited_urls:
        # Return from the function
        return
    # Add the URL to the visited set
    visited_urls.add(url)
    # Send a GET request to the URL and store the response object
    response = requests.get(url)
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Print a warning message with the URL
        print(f"Warning: Potential data leakage at {url}")
        # Parse the response content as HTML using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        # Find all the anchor tags (<a>) in the HTML content
        links = soup.find_all("a")
        # Loop through each link
        for link in links:
            # Get the href attribute of the link
            href = link.get("href")
            # Check if the href is not None and starts with a slash (/)
            if href and href.startswith("/"):
                # Construct the full URL by appending the href to the web app URL
                full_url = web_app_url + href
                # Recursively call the function with the full URL
                crawl_and_check(full_url)
    # Otherwise, print a normal message with the URL and the status code
    else:
        print(f"Normal: No data leakage at {url} (status code: {response.status_code})")

# Loop through each path and call the function with the full URL
for path in data_leakage_paths:
    # Construct the full URL by appending the path to the web app URL
    full_url = web_app_url + path
    # Call the function with the full URL
    crawl_and_check(full_url)
