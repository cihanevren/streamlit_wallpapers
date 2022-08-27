import requests


def subreddit_query(key, params=None):
    
    url = "https://www.reddit.com/r/" + key 
    url_json = "https://www.reddit.com/r/" + key + "/.json"
    
    try : 
        r = requests.get(url, params=params, headers={'User-Agent': 'Wallscraper Script by @psarin'})
        r.raise_for_status()
        r.ok
        
    except requests.exceptions.HTTPError as e:
        print("Aaaa Page not found! Try another subreddit")
        print(str(e))
        return r

    try:
        response = requests.get(url_json, params=params, headers={'User-Agent': 'Wallscraper Script by @psarin'})
        response.raise_for_status()
        
    except requests.exceptions.ConnectionError as e:
        print("There is a Connection Error happening around. Just Letting you know")
        print(str(e))

    except requests.exceptions.Timeout as e:
        print("There is a Timeout Error happening around. Just Letting you know")
        print(str(e))

    except requests.exceptions.RequestException as e:
        print("There is a RequestException Error happening around. Just Letting you know")
        print(str(e))

    except KeyboardInterrupt as e:
        print("Well apparently someone intervened the program ")
        print(str(e))
    
    
    return response.json()