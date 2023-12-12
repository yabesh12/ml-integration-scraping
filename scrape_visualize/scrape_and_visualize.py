import requests
from bs4 import BeautifulSoup
from collections import Counter
from jinja2 import Template
import matplotlib.pyplot as plt

def scrape_quotes(url):
    """
    Fetches quotes from a specified URL.

    Parameters:
    - url (str): The URL of the website containing quotes.

    Returns:
    - soup (BeautifulSoup): Parsed HTML content of the website.
    - quotes (list): List of quotes extracted from the website.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = [quote.text for quote in soup.select('.text')]
    return soup, quotes

def visualize_top_authors(soup, quotes):
    """
    Extracts top authors and their quote counts from the parsed HTML content.

    Parameters:
    - soup (BeautifulSoup): Parsed HTML content of the website.
    - quotes (list): List of quotes extracted from the website.

    Returns:
    - top_authors (list): List of top authors.
    - counts (list): Corresponding counts of quotes for each top author.
    """
    authors = [quote.find('small', class_='author').text for quote in soup.select('.quote')]
    author_counts = Counter(authors)

    top_authors = [author[0] for author in author_counts.most_common(5)]
    counts = [author_counts[author] for author in top_authors]

    return top_authors, counts

def generate_html(authors, counts):
    """
    Generates an HTML file with a bar chart visualization of top authors and their quote counts.

    Parameters:
    - authors (list): List of top authors.
    - counts (list): Corresponding counts of quotes for each top author.
    """
    with open('visualization_template.html', 'r') as file:
        template_content = file.read()

    template = Template(template_content)
    rendered_html = template.render(authors=authors, counts=counts)

    with open('output_visualization.html', 'w') as output_file:
        output_file.write(rendered_html)

def main():
    """
    Main function to execute the entire process:
    1. Scrapes quotes from a specified website.
    2. Visualizes and prints the top authors and their quote counts.
    3. Generates an HTML file with a bar chart visualization.
    """
    url = "http://quotes.toscrape.com"
    soup, quotes = scrape_quotes(url)
    authors, counts = visualize_top_authors(soup, quotes)
    generate_html(authors, counts)

if __name__ == "__main__":
    main()
