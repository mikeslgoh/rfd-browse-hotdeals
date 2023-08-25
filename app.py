from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import json
import re

app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_page():
    url = 'https://forums.redflagdeals.com'
    resp = requests.get(f'{url}/hot-deals-f9/')
    soup = BeautifulSoup(resp.content, 'html.parser')
    json_strs = {}
    # print(soup)

    last_page = soup.find("a", class_="pagination_last pagination_button")
    # To get the last page: int(last_page['href'].strip('/'))
    for n in range(2, 3):
        dealers_html = soup.find_all("h3", class_="topictitle")
        post_link_html = soup.find_all("a", class_="topic_title_link")

        dealers = [re.search(r"(\[*)([a-zA-Z]+([ |.|-](])*)*[a-zA-Z]+)", d.text) for d in dealers_html]
        for i in range(len(dealers)):
            p = post_link_html[i]
            dealer = dealers[i].groups()[1]
            post = {
                'post_title': p.text.strip(),
                'post_link': f'{url}/{p["href"]}'
            }
            if dealer not in json_strs:
                json_strs[dealer] = []
            json_strs[dealer].append(post)
        resp = requests.get(f'{url}/hot-deals-f9/{n}')
        soup = BeautifulSoup(resp.content, 'html.parser')
    print(json_strs)

    return render_template("index.html", posts=json_strs)
