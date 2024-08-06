import streamlit as st
import random
import time

# Streamed response emulator
def response_generator():
    response = random.choice(
        [   
            "Hey there! Need help? Check out my LinkedIn profile: https://linkedin.com/in/shreyash-somvanshi",
            "Hi! What's up? Don't forget to connect with me on LinkedIn: https://linkedin.com/in/shreyash-somvanshi !",
            "Hey! Got a question? Also, connect with me on LinkedIn for awesome tips: https://linkedin.com/in/shreyash-somvanshi",
            "Hi there! How can I help?",
            "Hey! Need assistance? Contact me at: https://shreyash.rbind.io/contact/",
            "Hi! Got any questions? Please email me at: shreyashsomvanshi03@gmail.com",
            "Hello! Need help? Feel free to reach out via email: shreyashsomvanshi03@gmail.com !",
            "Hey there! Any questions? You can contact me at: https://shreyash.rbind.io/contact/",
            "Hi, I hope you find the resources here useful, and please let me know if there's something you think I can improve upon.",
            "Hi, I hope you find the resources here useful, and please let me know if there's something you think I can improve upon. Linkedin: https://linkedin.com/in/shreyash-somvanshi | Email: shreyashsomvanshi03@gmail.com | Website: https://shreyash.rbind.io/contact/ "
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# st.toast("Note: This chatbot is currently under development and may not operate as intended.",icon="⚠️")

# st.warning("Note: This chatbot is currently under development and may not operate as intended. \n If important, please use the contact form at https://shreyash.rbind.io/contact to convey your message.",icon="⚠️")

st.title("🤖 | CHATBOT ")

st.warning("Note: This chatbot is currently under development and may not operate as intended.",icon="⚠️")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    time.sleep(0.6)
    with st.chat_message("assistant"):
        time.sleep(0.7)
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    

