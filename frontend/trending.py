import requests
def get_trending_slang():
    """
    Fetches trending slang words from Urban Dictionary API.
    """
    api_url = "https://api.urbandictionary.com/v0/trending"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            slang_list = [item['word'] for item in response.json().get('list', [])[:5]]
            return slang_list
        return ["No trending slang found."]
    except Exception as e:
        return [f"Error fetching trending slang: {str(e)}"]
