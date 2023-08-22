# rfd-browse-hotdeals
Filters post from RedFlagDeals Hot Deals page using keywords provided by you

# For local development (on Windows)
## Start up virtual environment
- Open Powershell or Command prompt and navigate to this project folder
- Enter "python -m venv venv"
- Start virtual environment (venv) environment by running .\venv\Scripts\activate
- Run .\venv_install_requirements.bat
- To stop virtual environment, type deactivate

## Start up local webserver
- Run python -m http.server

## Resources
- Setup static Flask website: https://pythonhosted.org/Frozen-Flask/
- Flask: https://flask.palletsprojects.com/en/2.3.x/quickstart/#deploying-to-a-web-server
- Async Flask: https://flask.palletsprojects.com/en/2.3.x/async-await/
- Async requests: https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp