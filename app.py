
import streamlit as st
from poem_generator import generate_poem

st.set_page_config(page_title="Silent Poem Generator")

st.title("🕊️ Silent Poem Generator")
st.markdown("生成ボタンを押すと、非命題的な詩的断片が出力されます。")

if st.button("詩を生成する"):
    poem = generate_poem()
    st.markdown(f"---\n\n{poem}\n\n---")
