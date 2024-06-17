import main as model
import streamlit as st

st.set_page_config(page_title="Rohmat-GPT")
st.title("Rohmat-GPT")
st.write("Powered by GPT-4o")
    
with st.sidebar:
  st.header("Rohmat-GPT")
  st.markdown("Asisten Ngoding Serbaguna")
  st.caption("Note by admint: Memory akan tereset setelah percakapan ketiga.")
  st.divider()
  st.caption("Made by Dave")

# Initialize session state and show historical messages
if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Start Chating"):
  st.session_state.messages.append({"role": "user", "content": prompt})

  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    answer = model.LangChain_generate(prompt)
    response = st.write(answer)
  
  st.session_state.messages.append({"role": "assistant", "content": answer})