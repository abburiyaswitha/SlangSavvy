import requests
API_KEY = "AIzaSyA4NLwbVVLb-vEKsT9k8OAgDJh--4KQqX4"

def slang_chatbot(user_message):
    """Send a message to Google Gemini AI for slang interpretation."""
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
    
    payload = {
        "contents": [
            {"parts": [{"text": user_message}]}
        ]
    }
    
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            return response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "I couldn't understand that slang.")
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Chatbot Error: {str(e)}"
if __name__ == "__main__":
    user_input = input("Enter slang: ")
    response = slang_chatbot(user_input)
    print("AI Response:", response)
