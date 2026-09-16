import streamlit as st
from groq import Groq

st.title("🤖 My First AI Chatbot")
st.write("Ask me anything and I'll try to help!")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

question = st.text_input("Your question:")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please type a question first.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[{"role": "user", "content": question}],
            )
        st.write(response.choices[0].message.content)
