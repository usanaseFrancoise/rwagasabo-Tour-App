import urllib.request,json
from .models import Location

# Getting api key
api_key = None
# Getting the location base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['LOCATION_API_KEY']
    base_url = app.config['LOCATION_API_BASE_URL']


def search_location(location_address):
    search_location_url = ''
    with urllib.request.urlopen(search_location_url) as url:
        search_location_data = url.read()
        search_location_response = json.loads(search_location_data)

        search_location_results = None

        if search_location_response['results']:
            search_location_list = search_location_response['results']
            search_location_results = process_results(search_location_list)


    return search_location_results