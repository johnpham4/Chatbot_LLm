# 📚 PDF Chat Assistant

An AI-powered chatbot that lets you chat with the content of any PDF file.  
Built with **LangChain**, **Cohere Embeddings**, and **Fireworks LLaMA-v3**, all wrapped in a sleek **Gradio UI**.

---

## 🚀 Quickstart

> ⚙️ Works on **Git Bash**, **Windows CMD**, or **macOS/Linux Terminal**.  
> ❌ Not tested on Anaconda Prompt.

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/pdf-chat-assistant.git
cd pdf-chat-assistant

# 2️⃣ Create a virtual environment and install dependencies
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

# 3️⃣ Create a .env file and add your API keys
echo FIREWORKS_API_KEY=your_fireworks_key >> .env
echo COHERE_API_KEY=your_cohere_key >> .env

# 4️⃣ Start the application
python app.py
