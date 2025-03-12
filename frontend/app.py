import streamlit as st
import sys
import os
import requests

# Add backend folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))

# Import other backend functions
from slang_api import get_slang_meaning
from trending_api import get_trending_slang

# Function to call Chatbot API
def slang_chatbot(user_input):
    url = f"http://127.0.0.1:8000/chat/{user_input}"  # Backend API URL
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("response", "No response available.")
        else:
            return "Error: Unable to fetch response from chatbot."
    except requests.exceptions.ConnectionError:
        return "Error: Chatbot API is not running. Please start the backend server."

# Streamlit App Title
st.title("SlangSavvy - AI Slang Decoder")

# Navigation Sidebar
menu = ["Home", "Slang Decoder", "Chatbot", "Trending Slang"]
choice = st.sidebar.selectbox("Menu", menu)

# Home Page
if choice == "Home":
    st.write("Welcome to SlangSavvy! Decode, chat, and explore trending slang.")

# Slang Decoder Page
elif choice == "Slang Decoder":
    st.subheader("Decode Slang Words")
    slang_input = st.text_input("Enter a slang word:")
    if st.button("Get Meaning"):
        if slang_input:
            meaning = get_slang_meaning(slang_input)
            st.write(f"{slang_input}:** {meaning}")
        else:
            st.warning("Please enter a slang word.")

# Chatbot Page
elif choice == "Chatbot":
    st.subheader("AI Slang Chatbot")
    user_input = st.text_input("Chat with AI:")
    if st.button("Send"):
        if user_input:
            response = slang_chatbot(user_input)
            st.write("🤖 AI:", response)
        else:
            st.warning("Please enter a message.")

# Trending Slang Page
elif choice == "Trending Slang":
    st.subheader("Trending Slang Words")
    trending = get_trending_slang()
    if trending:
        st.write("🔥 Trending Slang Words:")
        for word in trending:
            st.write(f"- {word}")
    else:
        st.write("No trending slang found.")
