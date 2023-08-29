from flask import Flask, render_template
from flask_frozen import Freezer

import requests
from bs4 import BeautifulSoup
import re
import webbrowser

app = Flask(__name__)
freezer = Freezer(app)


def get_page(filter : str) -> {}:
    limit = 5
    posts = 0
    url = 'https://forums.redflagdeals.com'
    resp = requests.get(f'{url}/hot-deals-f9/')
    soup = BeautifulSoup(resp.content, 'html.parser')
    json_strs = {}
    # print(soup)

    last_page_html = soup.find("a", class_="pagination_last pagination_button")
    last_page = int(last_page_html['href'].strip('/'))
    for n in range(2, last_page+1):
        dealers_html = soup.find_all("h3", class_="topictitle")
        post_link_html = soup.find_all("a", class_="topic_title_link")

        dealers = [re.search(r"(\[*)([a-zA-Z]+([ |.|-](])*)*[a-zA-Z]+)", d.text) for d in dealers_html]
        for i in range(len(dealers)):
            p = post_link_html[i]
            dealer = dealers[i].groups()[1]
            if filter in dealer:
                post = {
                    'post_title': p.text.strip(),
                    'post_link': f'{url}/{p["href"]}'
                }
                if dealer not in json_strs:
                    json_strs[dealer] = []
                
                if posts >= limit:
                    break
                json_strs[dealer].append(post)
                posts+=1
        resp = requests.get(f'{url}/hot-deals-f9/{n}')
        soup = BeautifulSoup(resp.content, 'html.parser')
    return json_strs

@app.route("/")
def home():
    json_strs = get_page(filter='')
    return render_template("index.html", posts=json_strs)


if __name__ == "__main__":
    app.run(debug=True)
    webbrowser.open_new_tab('http://localhost:5000')
    # freezer.freeze() - generate static pages
