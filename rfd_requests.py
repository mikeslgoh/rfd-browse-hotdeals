import requests


def get_page():
	url = 'https://forums.redflagdeals.com/hot-deals-f9/'
	page = requests.get(url)

	print(page.text)