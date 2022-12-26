import requests

# Query variables
root = "https://country-leaders.onrender.com"
endpoint_status = "status"                 
endpoint_countries = "countries"                  
endpoint_cookie = "cookie"                
endpoint_leaders = "leaders"                


def get_url(root : str, endpoint : str, params = None ):
    url = f"{root}/{endpoint}"
    req = s.get(url, params = params)
    print(req.url)

    status_code = req.status_code
    data = req.json()

    if type(data) == dict:
        message = data.get("message")

    if type(data) == list:
        message = data

    if status_code == 200:
        print ( f" API connexion succeeded, data received")
    else:
        print(f"API connexion failed, status code : {status_code} {message}")

    return message

def get_leaders(_country_list):
    _leaders_per_country = dict()
    for country in _country_list:
        _leaders_per_country[country] = list()
        params_leaders = {'country' : country}
        # Gets the list of leaders, by country defined in the params    
        leaders_list = get_url(root, endpoint_leaders, params = params_leaders)
        for leader in leaders_list:
            _leaders_per_country[country].append(leader)
    return _leaders_per_country


with requests.Session() as s:
    # Gets the cookie to open a session
    get_url(root, endpoint_cookie)
    # cookie = s.cookies
    # print(cookie)

    # Gets the list of Countries
    country_list = get_url(root, endpoint_countries)

    # Build a dictionary { "country" : [{leaders}]}
    leaders_per_country = get_leaders(country_list)

    # print(leaders_per_country.keys())
    for k in leaders_per_country.keys():
        print(f"{k}: total leaders = {len(leaders_per_country[k])}")




### WIKI

