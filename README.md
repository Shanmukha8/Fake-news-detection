# Fake News Detection Web App 📰

An AI-powered web application that classifies news articles as Real or Fake using state-of-the-art Natural Language Processing (NLP) models from HuggingFace Transformers.

## Features

- **AI-Powered Detection**: Uses pre-trained RoBERTa-based model for accurate classification
- **Interactive UI**: Clean and user-friendly interface built with Streamlit
- **Real-time Analysis**: Instant predictions with confidence scores
- **Confidence Scoring**: Shows percentage confidence for each prediction
- **Sample Articles**: Pre-loaded examples for quick testing
- **Input Validation**: Graceful error handling and informative feedback
- **Responsive Design**: Works seamlessly on different screen sizes
- **Analysis Metrics**: Displays word count, character count, and confidence levels

## Technologies Used

- **Python 3.8+**: Core programming language
- **Streamlit**: Frontend framework for interactive web applications
- **HuggingFace Transformers**: Pre-trained NLP models
- **PyTorch**: Deep learning framework
- **RoBERTa Model**: Robust optimized BERT approach for text classification

## Project Structure

```
Fake-news-detection/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shanmukha8/Fake-news-detection.git
   cd Fake-news-detection
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to the URL shown in the terminal

3. **Analyze news articles**
   - Paste or type a news article in the text area
   - Click "Analyze Article" button
   - View the prediction (Real/Fake) with confidence score
   - Check additional metrics and recommendations

## How It Works

1. **Text Input**: User enters or pastes a news article
2. **Preprocessing**: Text is prepared for the model (tokenization, truncation)
3. **Model Inference**: Pre-trained RoBERTa model analyzes the text
4. **Classification**: Model outputs prediction (Real/Fake) with confidence score
5. **Display Results**: User-friendly visualization of results with metrics

## Model Information

- **Model**: `hamzab/roberta-fake-news-classification`
- **Base Architecture**: RoBERTa (Robustly Optimized BERT Pretraining Approach)
- **Task**: Binary Text Classification
- **Input**: Text (max 512 tokens)
- **Output**: Label (Real/Fake) + Confidence Score

## Key Skills Demonstrated

- Natural Language Processing (NLP)
- Text Classification using Transformers
- HuggingFace Transformers library
- Streamlit web application development
- Python programming
- AI/ML model integration
- User interface design
- Error handling and input validation
- Full-stack web development

## Screenshots

*Add screenshots of your application here*

### Example Usage:
1. **Real News Detection**
   - Input: Legitimate news article
   - Output: "REAL NEWS" with confidence score

2. **Fake News Detection**
   - Input: Suspicious or fabricated article
   - Output: "FAKE NEWS" with confidence score

## Limitations & Disclaimer

- Model accuracy depends on training data quality
- May not detect all types of misinformation
- Should be used as a supplementary tool, not the sole source of verification
- Always cross-check information from multiple reliable sources
- The model is trained on specific datasets and may have biases

## Future Enhancements

- [ ] Add support for multiple languages
- [ ] Implement source credibility checking
- [ ] Add fact-checking API integration
- [ ] Include historical analysis of articles
- [ ] Deploy to cloud platform (Heroku/AWS)
- [ ] Add batch processing for multiple articles
- [ ] Implement user feedback mechanism
- [ ] Add visual analytics dashboard

## Deployment

### Deploy on Streamlit Cloud (Free)

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Sign in with GitHub
4. Click "New app" and select your repository
5. Set main file path as `app.py`
6. Click "Deploy"

### Local Deployment

```bash
streamlit run app.py --server.port 8501
```

## Dependencies

- `streamlit`: Web application framework
- `transformers`: HuggingFace Transformers library
- `torch`: PyTorch deep learning framework
- `sentencepiece`: Text tokenization
- `protobuf`: Protocol buffers support

## Troubleshooting

### Model Download Issues
If the model fails to download:
```bash
# Manually download the model
python -c "from transformers import pipeline; pipeline('text-classification', model='hamzab/roberta-fake-news-classification')"
```

### Memory Issues
If you encounter memory errors:
- Reduce the input text length
- Use a smaller model
- Increase system RAM allocation

### Port Already in Use
```bash
streamlit run app.py --server.port 8502
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Shanmukha**
- GitHub: [@Shanmukha8](https://github.com/Shanmukha8)

## Acknowledgments

- HuggingFace for providing pre-trained models
- Streamlit for the amazing web framework
- The open-source community for various libraries and tools

## References

- [HuggingFace Transformers Documentation](https://huggingface.co/docs/transformers/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [RoBERTa Paper](https://arxiv.org/abs/1907.11692)

---

**Note**: This project demonstrates the integration of AI/ML models with web applications, showcasing skills in NLP, Python programming, and full-stack development. It serves as a practical example of deploying machine learning models for real-world applications.