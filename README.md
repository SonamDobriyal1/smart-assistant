# Smart Assistant for Research Summarization

An AI-powered offline assistant that reads user-uploaded PDF/TXT documents, summarizes content, answers questions contextually, and challenges users with logic-based questions — all **without using any external API** like OpenAI.

Built using `Streamlit`, `Transformers`, and `Hugging Face` models.

---

## Features

* Upload PDF or TXT files
*  Generate an auto-summary (≤150 words)
*  Ask Anything mode (context-aware QA)
*  Challenge Me mode (3 logic-based questions with feedback)
*  Document-aware answers with reference-based evaluation
*  100% API-free using local models (no cost!)

---

## Folder Structure

```
smart-assistant/
├── main.py                       # Streamlit app entry point
├── requirements.txt              # Project dependencies
├── .gitignore
│
└── app/
    ├── __init__.py
    ├── document_parser.py        # File handling + text extraction
    ├── summarizer.py             # Summarization (local model)
    ├── ask_anything.py           # QA system (local)
    └── challenge_me.py           # Question generation + evaluation
```

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SonamDobriyal1/smart-assistant.git
cd smart-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

* **Activate (Windows):**

  ```bash
  venv\Scripts\activate
  ```
* **Activate (Linux/macOS):**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Run the App

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Usage Instructions

1. Upload a `.pdf` or `.txt` document.
2. Choose a mode:

   * **Ask Anything**: Ask context-based questions.
   * **Challenge Me**: Try answering generated logical questions.
3. View all responses with explanations sourced from the document.

---

##  Tech Stack

* Python 
* Streamlit
* Transformers (Hugging Face)
* sentence-transformers
* PDFPlumber

---

## Dependencies (`requirements.txt`)

```txt
streamlit
pdfplumber
transformers
sentence-transformers
torch
```

Install all with:

```bash
pip install -r requirements.txt
```


---

## Acknowledgements

* [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
* [Streamlit](https://streamlit.io/)
* [PDFPlumber](https://github.com/jsvine/pdfplumber)

---
