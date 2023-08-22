from pyodide.http import pyfetch
import asyncio

async def get_page():
	print('Getting page ...')
	url = 'https://forums.redflagdeals.com/hot-deals-f9/'

	response = await pyfetch(url, method="GET")
	data_dict = await response.json()
	print(data_dict)