import os
import requests
import re
import sys
from bs4 import BeautifulSoup

def get_page():
    global url
    url = input("Enter url of a medium article")
    if not re.match(r'https?://medium.com/',url):
        print('Please enter a valid website, or make sure it is a medium article')
        os.sys.exit(1)
# Code here - Call get method in requests object, pass url and collect it in res

    res = requests.get(url)

    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')

    return soup

# function to remove all the html tags and replace some with specific strings
def clean(tex):
    rep = {"<br>": "\n", "<br/>": "\n", "<li>":  "\n"}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    tex_ = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
    tex= re.sub('\<(.*?)\>', '', text)
    return text

def collect_text(sou):
    tex= f'url: {url}\n\n'
    para_text = sou.find_all('p')
    print(f"paragraphs text = \n {para_text}")
    for para in para_text:
        tex = f"{para.text}\n\n"
        return tex
# function to save file in the current directory
def save_file(tex):
    if not os.path.exists('./scraped_articles'):
        os.mkdir('./scraped_articles')
    name = url.split("/")[-1]
    print(name)
    f_name=f'scraped_articles/{name}.txt'
	# Code here - write a file using with (2 lines)
    with open(f_name,'w') as f:
         f.write(tex)

# Code ends here

    print(f'File saved in directory {f_name}')
if __name__ == '__main__':
    text = collect_text(get_page())
    save_file(text)