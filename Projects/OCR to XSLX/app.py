import streamlit as st
from gemini import GeminiProcessor

st.title("OCR to Excel Converter")

image_file = st.file_uploader("Upload an image file", type=["png","jpeg","jpg"])

if image_file:
    constructor_image = GeminiProcessor(image_file)
    extracted_data = constructor_image.generate_table()
    generated_excel = constructor_image.save_to_excel(extracted_data)
    st.download_button(
        label="Download File",
        data=generated_excel,
        file_name="output.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")