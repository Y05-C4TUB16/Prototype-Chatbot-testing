# import streamlit as st
# import requests
#
# RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"
#
#
# def get_rasa_response(message):
#     response = requests.post(RASA_API_URL, json={"message": message})
#     return response.json()
#
#
# st.title("HEDCEN's Chatbot")
#
# # Store the frequently asked questions in the session state (so they persist across reruns)
# if 'frequently_asked_questions' not in st.session_state:
#     st.session_state.frequently_asked_questions = []
#
# user_input = st.text_input("Your Message:")
# if user_input:
#     response = get_rasa_response(user_input)
#
#     # Display the Rasa bot's response
#     for msg in response:
#         st.write("---")
#         st.write(msg.get('text'))
#
#     # Add to FAQ list and display it
#     st.session_state.frequently_asked_questions.append(user_input)
#     st.write("---")
#     st.subheader("History:")
#     st.write(st.session_state.frequently_asked_questions)

import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Constants
RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"

# Initialize session state variables
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'faqs' not in st.session_state:
    st.session_state.faqs = []
if 'user_feedback' not in st.session_state:
    st.session_state.user_feedback = []


def get_rasa_response(message):
    response = requests.post(RASA_API_URL, json={"message": message})
    return response.json()


def save_chat(user_message, bot_response):
    st.session_state.chat_history.append({
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'user_message': user_message,
        'bot_response': bot_response
    })


# Sidebar navigation
st.sidebar.title("Admin Panel")
page = st.sidebar.radio("Navigate to", ["Chat Interface", "Chat History", "FAQ Management", "Analytics"])

if page == "Chat Interface":
    st.title("HEDCEN's Chatbot")

    user_input = st.text_input("Your Message:")
    if user_input:
        response = get_rasa_response(user_input)
        bot_response = response[0].get('text') if response else "No response"

        st.write("User:", user_input)
        st.write("Bot:", bot_response)

        # Save the conversation
        save_chat(user_input, bot_response)

        # Feedback buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👍 Helpful"):
                st.session_state.user_feedback.append({"message": user_input, "feedback": "positive"})
                st.success("Thank you for your feedback!")
        with col2:
            if st.button("👎 Not Helpful"):
                st.session_state.user_feedback.append({"message": user_input, "feedback": "negative"})
                st.error("Thank you for your feedback!")

elif page == "Chat History":
    st.title("Chat History")

    if st.session_state.chat_history:
        df = pd.DataFrame(st.session_state.chat_history)
        st.dataframe(df)

        if st.button("Export Chat History"):
            df.to_csv("chat_history.csv", index=False)
            st.success("Chat history exported successfully!")
    else:
        st.info("No chat history available")

elif page == "FAQ Management":
    st.title("FAQ Management")

    # Add new FAQ
    with st.form("add_faq"):
        question = st.text_input("Question:")
        answer = st.text_area("Answer:")
        if st.form_submit_button("Add FAQ"):
            st.session_state.faqs.append({"question": question, "answer": answer})
            st.success("FAQ added successfully!")

    # Display existing FAQs
    if st.session_state.faqs:
        st.subheader("Existing FAQs")
        for i, faq in enumerate(st.session_state.faqs):
            with st.expander(f"FAQ #{i + 1}: {faq['question']}"):
                st.write("Answer:", faq['answer'])
                if st.button(f"Delete FAQ #{i + 1}"):
                    st.session_state.faqs.pop(i)
                    st.experimental_rerun()

elif page == "Analytics":
    st.title("Chatbot Analytics")

    # Basic analytics
    total_conversations = len(st.session_state.chat_history)
    total_feedback = len(st.session_state.user_feedback)
    positive_feedback = sum(1 for f in st.session_state.user_feedback if f['feedback'] == 'positive')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Conversations", total_conversations)
    with col2:
        st.metric("Total Feedback", total_feedback)
    with col3:
        satisfaction_rate = (positive_feedback / total_feedback * 100) if total_feedback > 0 else 0
        st.metric("Satisfaction Rate", f"{satisfaction_rate:.1f}%")

    # Display feedback history
    if st.session_state.user_feedback:
        st.subheader("User Feedback History")
        feedback_df = pd.DataFrame(st.session_state.user_feedback)
        st.dataframe(feedback_df)

# Footer
st.sidebar.markdown("---")
st.sidebar.info("HEDCEN Chatbot Admin Panel v1.0")
