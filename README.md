📚 AI Study Assistant

An AI-powered study assistant built using Python, NLP, Streamlit, and Google Gemini API.

🚀 Features

- 📄 Upload and read PDF files
- 📝 Extract text from PDF documents
- 🧹 Text preprocessing using NLP
- 📌 Generate AI-powered summaries
- 💬 Ask questions from uploaded PDF
- 🤖 Google Gemini AI integration
- 🗂️ Chat history during the session
- 🖥️ Simple and user-friendly Streamlit interface

🛠️ Technologies Used

- Python
- Streamlit
- Natural Language Processing (NLP)
- NLTK
- Google Gemini API
- PyPDF2

📁 Project Structure

AI_Study_Assistant/
│
├── assets/
│
├── data/
│   ├── Basic-Computer-Hardware-Notes-in-PDF-1.pdf
│   ├── Ch.01_Introduction_to_computers.pdf
│   └── sample.pdf
│
├── modules/
│   ├── gemini_helper.py
│   ├── main_processor.py
│   ├── pdf_reader.py
│   ├── summarizer.py
│   └── text_preprocessing.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation

1. Clone the Repository

git clone https://github.com/nikhiltiwari9998-oss/AI-Study-Assistant.git

2. Open the Project Folder

cd AI-Study-Assistant

3. Create a Virtual Environment

python -m venv venv

4. Activate the Virtual Environment

For Windows:

venv\Scripts\activate

5. Install Required Libraries

pip install -r requirements.txt

🔑 Gemini API Setup

Create a ".env" file in the project folder and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

⚠️ Never upload your ".env" file or API key to GitHub.

▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

🎯 Project Objective

The main objective of this project is to help students understand and study PDF-based learning material using Artificial Intelligence and Natural Language Processing.

The application can process educational PDFs, generate summaries, and answer questions related to the uploaded study material.

👨‍💻 Developer

Nikhil Tiwari

BCA Student

Interested in Python, Web Development, Artificial Intelligence, and Natural Language Processing.