import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np
from gemini_api import get_extracted_details  # Importing the function from gemini_api.py

# Set the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as per your installation

# Streamlit app title
st.title("🖼️ OCR with Tesseract and Streamlit")

# Customize the sidebar
st.sidebar.header("Settings")
st.sidebar.markdown("""
    This application uses Tesseract OCR to extract text from images.
    Upload a JPG image and click the button to extract text.
""")

# Upload images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])

if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Convert image to grayscale
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Perform OCR
    extracted_text = pytesseract.image_to_string(thresh)

    # Display extracted text
    st.subheader("📜 Extracted Text")
    st.text_area("Text Output", extracted_text, height=250)

    # Provide a prompt for extracting specific details
    prompt = st.text_input("Enter a prompt for extracting specific details from the text")

    if st.button("Extract Details"):
        if prompt:
            # Use the Gemini API function to extract details
            result = get_extracted_details(extracted_text, prompt)
            st.subheader("🔍 Extracted Details")
            st.write(result)
        else:
            st.warning("Please provide a prompt for extraction!")

    # Provide download option for the extracted text
    st.download_button(
        label="Download Extracted Text",
        data=extracted_text,
        file_name='extracted_text.txt',
        mime='text/plain'
    )

# Add footer
st.markdown("---")
st.markdown("Made with ❤️ our Team")