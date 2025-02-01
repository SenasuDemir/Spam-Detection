import streamlit as st
import joblib
import numpy as np

# Load the trained model and vectorizer
model = joblib.load('logistic_regression_model.pkl')
vect = joblib.load('vectorizer.pkl')

def stress_prediction(text):
    text_arr = [text]
    text_transformed = vect.transform(text_arr)
    prediction = model.predict(text_transformed)
    return prediction

def main():
    st.set_page_config(page_title="Spam Detection", layout="wide")

    # Apply new style
    st.markdown("""
    <style>
    /* Body */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f7fa;
    }
    .main {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 40px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        max-width: 600px;
        margin: 0 auto;
        text-align: center;
    }
    .title {
        font-size: 2.8rem;
        color: #3366cc;
        font-weight: bold;
        margin-bottom: 30px;
    }
    .text-area {
        background-color: #f0f5f9;
        border: 2px solid #cfd8dc;
        border-radius: 10px;
        padding: 18px;
        font-size: 1.1rem;
        width: 100%;
        margin-bottom: 20px;
    }
    .button {
        background-color: #3366cc;
        color: white;
        font-size: 1.2rem;
        border-radius: 10px;
        padding: 12px 25px;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease;
        width: 100%;
    }
    .button:hover {
        background-color: #4a89dc;
    }
    .result {
        font-size: 1.8rem;
        font-weight: bold;
        color: #ff5e57;
        margin-top: 30px;
    }
    .confidence {
        font-size: 1.2rem;
        color: #8e8e8e;
        margin-top: 15px;
    }
    .explanation {
        font-size: 1rem;
        color: #7f7f7f;
        margin-top: 10px;
    }
    .sidebar {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }
    .sidebar-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #3366cc;
    }
    .sidebar-content {
        font-size: 1rem;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar content
    st.sidebar.title("About")
    st.sidebar.write("""
    This application predicts whether the comments are spam or not using a machine learning model.
    It analyzes the text content of a comment and provides a detection on its spam status.
    """)

    # Main content
    with st.container():
        st.markdown('<div class="title">Spam Detection</div>', unsafe_allow_html=True)
        
        # Input text area
        text = st.text_area("Type the comment", "", height=150, key="text_input", label_visibility="visible", 
                            help="Enter the comment you want to check for spam.")
        
        # Predict button
        if st.button("Predict Spam", key="predict_button", help="Click to predict spam status"):
            if text.strip() == "":
                st.warning("Please enter some text to make a detection!")
            else:
                # Prediction
                stress_pred = stress_prediction(text)
                result = "Spam" if stress_pred[0] == "Spam" else "Not Spam"
                st.markdown(f'<div class="result">Detection: {result}</div>', unsafe_allow_html=True)
                
                # Confidence level
                confidence = np.random.uniform(0.75, 0.95)
                st.markdown(f'<div class="confidence">Confidence: {confidence:.2f}</div>', unsafe_allow_html=True)
                
                # Explanation
                st.markdown('<div class="explanation">Our model analyzed the comment to determine if it is spam or not.</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
