import requests
import bs4
import re
import functools
import timeit

macron_url = 'https://fr.wikipedia.org/wiki/Emmanuel_Macron'

@functools.lru_cache(maxsize = None, typed = True)  #decorator to cache the result of the function
def get_first_paragraph(url):
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    # print(soup.prettify)
    for p in soup.find_all('p'):
        if p.find_all('b'):
            
            pattern = r"(\(.*\))|(\[.*\])"  # remove parentheses or [] from text
            sanitized_text = re.sub(pattern, "", p.text)
            return sanitized_text

print(timeit.timeit('get_first_paragraph(macron_url)', 'from __main__ import get_first_paragraph, macron_url', number = 1))



print(get_first_paragraph.cache_info())