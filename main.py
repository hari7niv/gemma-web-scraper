import requests
import sys
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) < 2:
        print("Error: Please provide a URL.")
        sys.exit(1)
    url = sys.argv[1]
    try:
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'} 
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        for element in soup.find_all(["script", "style", "nav", "footer", "header", "aside"]):
            element.decompose()
        cleaned_text = soup.get_text(separator=' ', strip=True)
        lines = (line.strip() for line in cleaned_text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        final_text = '\n'.join(chunk for chunk in chunks if chunk)

        print("-----------------Start---------------------")
        print(final_text)
        print("------------------End---------------------")

    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")

if __name__ == "__main__":
    main()