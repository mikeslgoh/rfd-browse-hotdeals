from flask import Flask, render_template
import aiohttp

app = Flask(__name__)


@app.route("/")
async def get_page():
    async with aiohttp.ClientSession() as session:
        url = 'https://forums.redflagdeals.com/hot-deals-f9/'
        async with session.get(url) as resp:
            page = await resp.text()
            render_template('index.html', output=page)
