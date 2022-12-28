'''
Test RegEx
'''

import re

text = "Emmanuel Macron (/ɛmanɥɛl makʁɔ̃/[e] Écouter), né le 21 décembre 1977 à Amiens est un haut fonctionnaire et homme d'État français. Il est président de la République française depuis 2017."

# Removing text in brackets or parenthesis
pattern = r"(\(.*\))|(\[.*\])"

cleaned_text = re.sub(pattern, "", text)
print(cleaned_text)