import streamlit as st
import requests

RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"


def get_rasa_response(message):
    response = requests.post(RASA_API_URL, json={"message": message})
    return response.json()


st.title("HEDCEN's Chatbot")

# Store the frequently asked questions in the session state (so they persist across reruns)
if 'frequently_asked_questions' not in st.session_state:
    st.session_state.frequently_asked_questions = []

user_input = st.text_input("Your Message:")
if user_input:
    response = get_rasa_response(user_input)

    # Display the Rasa bot's response
    for msg in response:
        st.write("---")
        st.write(msg.get('text'))

    # Add to FAQ list and display it
    st.session_state.frequently_asked_questions.append(user_input)
    st.write("---")
    st.subheader("History:")
    st.write(st.session_state.frequently_asked_questions)
