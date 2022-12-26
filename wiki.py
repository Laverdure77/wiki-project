import requests
import bs4

macron_url = 'https://fr.wikipedia.org/wiki/Emmanuel_Macron'

def get_first_paragraph(url):
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    # print(soup.prettify)
    for p in soup.find_all('p'):
        if p.find_all('b'): 
            return p.text

print(get_first_paragraph(url = macron_url))
