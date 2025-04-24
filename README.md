# 📚 Chatbot LLM - PDF Assistant

A lightweight AI chatbot that can interact with users and summarize PDF content.

---

## 🚀 Quick Start

### ✅ Prerequisites

- Python 3.10  
- Git  
- Anaconda/Miniconda (recommended)

---

## 🎥 Demo Video

👉 [Watch the Demo Video](https://drive.google.com/file/d/1-Hm7230_Om8QmtIP3AQzlya8-fQO9dht/view?usp=sharing)

---
## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/johnpham4/Chatbot_llm.git
cd Chatbot_llm
```

---

### 2. Create and activate environment

#### 🅰️ Option A: Using Anaconda (Recommended)

```bash
conda create -n chatbot python=3.10 -y
conda activate chatbot
pip install -r requirements.txt
```

#### 🅱️ Option B: Using Virtual Environment

##### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

##### For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3. (Optional) Set up your API keys

To use the chatbot with your own API keys:

1. Open the project folder.  
2. Visit [Cohere](https://dashboard.cohere.com/api-keys?_gl=1*bflam*_gcl_au*MTY5Mzk4NjUxNy4xNzQ0NTU4MDQw*_ga*NDUxOTMxMDQ2LjE3NDQxMTY2Mjk.*_ga_CRGS116RZS*MTc0NTQ3NTI4MC4xMS4xLjE3NDU0NzUzMTUuMjUuMC4w) and [Fireworks AI](https://fireworks.ai/account/api-keys) to generate your API keys.  
3. Create a `.env` file in the root of the project with the following content:

```env
COHERE_API_KEY=your_cohere_api_key
FIREWORKS_API_KEY=your_fireworks_api_key
```

Replace the placeholders with your actual keys.

---

### 4. Run the application

```bash
python app.py
```

---

✅ You're all set! Start chatting with your PDFs effortlessly.
