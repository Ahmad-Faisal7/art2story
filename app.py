import streamlit as st
from PIL import Image
from blip_utils import extract_caption
from gemini_utils import generate_story_from_caption

st.set_page_config(page_title="Art2Story", layout="centered")

st.title("🎨 Art2Story")
st.write("Upload an image of art and get a beautiful story generated from it.")

uploaded_file = st.file_uploader("Upload an art image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Art", use_column_width=True)

    with st.spinner("🔍 Generating caption..."):
        caption = extract_caption(image)
    st.subheader("🖼️ Caption:")
    st.write(caption)

    with st.spinner("✍️ Creating story..."):
        story = generate_story_from_caption(caption)
    st.subheader("📖 Story:")
    st.write(story)
