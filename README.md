# 🖼️ Art2Story

Art2Story is a Streamlit web app that takes an image (artwork or photo), extracts a caption using BLIP (a HuggingFace image captioning model), and then generates a creative story using Google's Gemini API.

## 🚀 How It Works

1. Upload an image.
2. The app uses BLIP to describe the image.
3. The description is sent to Gemini to write a creative short story.
4. The story is displayed on the screen.

## 🛠️ Technologies

- Python 🐍
- Hugging Face Transformers (BLIP)
- Google Gemini API
- Streamlit
- dotenv

## 🧪 Running Locally

Make sure you have Python 3.9+ installed.

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/art2story.git
cd art2story

# Set up virtual environment
python -m venv artenv
.\artenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file
echo GEMINI_API_KEY=your-api-key-here > .env

# Run the app
streamlit run app.py
