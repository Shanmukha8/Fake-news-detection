import streamlit as st
from transformers import pipeline
import time

# Page configuration
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        text-align: center;
    }
    .real-news {
        background-color: #d4edda;
        border: 2px solid #28a745;
        color: #155724;
    }
    .fake-news {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
        color: #721c24;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for caching the model
@st.cache_resource
def load_model():
    """Load the pre-trained fake news detection model"""
    try:
        # Using a lightweight text classification model
        # You can replace this with a specific fake news detection model
        classifier = pipeline(
            "text-classification",
            model="hamzab/roberta-fake-news-classification",
            tokenizer="hamzab/roberta-fake-news-classification"
        )
        return classifier
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def predict_news(text, classifier):
    """Predict if the news is real or fake"""
    try:
        if not text or len(text.strip()) < 10:
            return None, None, "Please enter at least 10 characters."
        
        # Get prediction
        result = classifier(text[:512])[0]  # Limit to 512 tokens
        label = result['label']
        confidence = result['score'] * 100
        
        # Map labels to user-friendly format
        if label.upper() in ['FAKE', 'LABEL_0']:
            prediction = "FAKE"
        else:
            prediction = "REAL"
        
        return prediction, confidence, None
    except Exception as e:
        return None, None, f"Error during prediction: {str(e)}"

# Main App
def main():
    # Header
    st.title("📰 Fake News Detection System")
    st.markdown("### Classify news articles as **Real** or **Fake** using AI")
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ About")
        st.info(
            """
            This application uses a pre-trained NLP model from HuggingFace 
            to detect fake news articles.
            
            **How to use:**
            1. Enter or paste a news article
            2. Click 'Analyze Article'
            3. View the prediction and confidence score
            """
        )
        
        st.header("📊 Model Info")
        st.write("**Model:** RoBERTa-based classifier")
        st.write("**Task:** Binary Text Classification")
        st.write("**Source:** HuggingFace Transformers")
        
        st.header("⚠️ Disclaimer")
        st.warning(
            "This is an AI-based prediction system and may not be 100% accurate. "
            "Always verify information from multiple reliable sources."
        )
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Enter News Article")
        
        # Text input area
        news_text = st.text_area(
            "Paste your news article here:",
            height=300,
            placeholder="Enter the news article text you want to verify...",
            help="Enter at least 10 characters for analysis"
        )
        
        # Sample texts for quick testing
        with st.expander("📝 Try Sample Articles"):
            if st.button("Sample Real News"):
                news_text = st.text_area(
                    "Sample Real News:",
                    value="Scientists at MIT have developed a new breakthrough in renewable energy technology. "
                          "The research team published their findings in Nature journal, demonstrating a 40% "
                          "improvement in solar panel efficiency through innovative materials. The peer-reviewed "
                          "study involved extensive testing over three years and has been independently verified.",
                    height=150,
                    key="real_sample"
                )
            
            if st.button("Sample Fake News"):
                news_text = st.text_area(
                    "Sample Fake News:",
                    value="BREAKING: Aliens have officially made contact with world leaders in secret meeting! "
                          "Anonymous sources claim that extraterrestrial beings landed yesterday. The government "
                          "is hiding the truth from citizens. Share this before it gets deleted! "
                          "This is what they don't want you to know!",
                    height=150,
                    key="fake_sample"
                )
        
        # Analyze button
        analyze_button = st.button("🔍 Analyze Article", type="primary", use_container_width=True)
    
    with col2:
        st.subheader("Analysis Tips")
        st.markdown("""
        **Look for these signs:**
        - ✅ Credible sources cited
        - ✅ Balanced reporting
        - ✅ Clear author/date
        - ❌ Sensational headlines
        - ❌ Poor grammar
        - ❌ Unverified claims
        """)
    
    # Prediction section
    if analyze_button:
        if not news_text or len(news_text.strip()) < 10:
            st.error("⚠️ Please enter at least 10 characters to analyze.")
        else:
            with st.spinner("🔄 Analyzing article..."):
                # Load model
                classifier = load_model()
                
                if classifier is None:
                    st.error("Failed to load the model. Please try again later.")
                    return
                
                # Simulate processing time for better UX
                time.sleep(1)
                
                # Get prediction
                prediction, confidence, error = predict_news(news_text, classifier)
                
                if error:
                    st.error(f"⚠️ {error}")
                else:
                    # Display results
                    st.markdown("---")
                    st.subheader("📊 Analysis Results")
                    
                    # Create result container
                    if prediction == "REAL":
                        st.markdown(
                            f"""
                            <div class="prediction-box real-news">
                                <h2>✅ REAL NEWS</h2>
                                <p style="font-size: 24px; font-weight: bold;">
                                    Confidence: {confidence:.2f}%
                                </p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        st.success("This article appears to be legitimate news based on the AI analysis.")
                    else:
                        st.markdown(
                            f"""
                            <div class="prediction-box fake-news">
                                <h2>⚠️ FAKE NEWS</h2>
                                <p style="font-size: 24px; font-weight: bold;">
                                    Confidence: {confidence:.2f}%
                                </p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        st.error("This article may contain misinformation. Please verify from reliable sources.")
                    
                    # Additional metrics
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Word Count", len(news_text.split()))
                    with col2:
                        st.metric("Character Count", len(news_text))
                    with col3:
                        st.metric("Confidence Level", f"{confidence:.1f}%")
                    
                    # Recommendation
                    st.info(
                        "💡 **Recommendation:** Always cross-check news from multiple trusted sources "
                        "before sharing or believing it."
                    )

if __name__ == "__main__":
    main()