import requests
def get_slang_meaning(word):
    """Fetch slang meaning from Urban Dictionary API."""
    api_url = f"https://api.urbandictionary.com/v0/define?term={word}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            meanings = response.json().get("list", [])
            return meanings[0]["definition"] if meanings else "No meaning found."
        return "Error fetching slang."
    except Exception as e:
        return f"Error: {str(e)}"
