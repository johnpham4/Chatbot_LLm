# 📚 PDF Chat Assistant

A lightweight AI chatbot to interact with the content of uploaded PDF files. Powered by Fireworks LLaMA, Cohere embeddings, and LangChain-based retrieval.

---

## 🚀 Quickstart

bash
# 1. Clone the repo
git clone https://github.com/your-username/pdf-chat-assistant.git
cd pdf-chat-assistant

# 2. Create environment and install dependencies
conda create -n pdfchat python=3.10 -y && \
conda activate pdfchat && \
pip install -r requirements.txt

# 3. Create a .env file with your API keys
echo "FIREWORKS_API_KEY=your_fireworks_key" >> .env
echo "COHERE_API_KEY=your_cohere_key" >> .env

# 4. Run the app
python app.py
