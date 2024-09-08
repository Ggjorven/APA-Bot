import requests
from bs4 import BeautifulSoup

# TODO: Needs a lot of work
class SourceGen:
    def __init__(self, url: str):
        self.datePublished: str | None = None
        self.authorName: str | None = None

        try:
            # Fetch the page
            response: requests.Response = requests.get(url)
            response.raise_for_status()  # Check for request errors

            # Parse the page content
            soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')

            # Extract the date of publishing and author (example selectors)
            date: requests.Tag | requests.NavigableString | None = soup.find('meta', {'property': 'article:published_time'})    # Example for meta tags
            author: requests.Tag | requests.NavigableString | None = soup.find('meta', {'name': 'author'})                      # Example for meta tags

            # Extract text or default to 'N/A' if not found
            self.datePublished = date['content'] if date else 'N/A'
            self.authorName = author['content'] if author else 'N/A'

        except requests.RequestException as e:
            print(f"Error fetching the page: {e}")
            return None
    
    def GetDatePublished(self) -> str:
        return self.datePublished
    
    def GetAuthor(self) -> str:
        return self.authorName