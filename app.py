import streamlit as st
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)
from modules.pdf_reader import extract_text_from_pdf
from modules.text_preprocessing import preprocess_text
from modules.summarizer import summarize_text
from modules.gemini_helper import ask_pdf_question


st.title("📚 AI Study Assistant")
st.caption(
    "An AI-powered application that summarizes PDFs and answers questions using NLP and Gemini AI."
)
st.sidebar.title("📚 AI Study Assistant")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""
st.markdown("### 🤖 Smart PDF Summarizer & Question Answering System")

summary_status = "Ready" if st.session_state.get("pdf_text") else "Waiting"
ai_status = "Ready" if st.session_state.get("pdf_text") else "Waiting"

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📄 PDF",
        "Uploaded" if st.session_state.get("pdf_text") else "Not Uploaded"
    )

with col2:
    st.metric("📝 Summary", summary_status)

with col3:
    st.metric("🤖 AI", ai_status)

st.sidebar.write(
    "Upload your PDF and ask questions with AI."
)

st.sidebar.info(
    "Powered by Python, NLP & Gemini AI"
)
st.sidebar.divider()

st.sidebar.subheader("✨ Features")
st.sidebar.write("✅ PDF Upload")
st.sidebar.write("✅ AI Summary")
st.sidebar.write("✅ PDF Question Answering")
st.sidebar.write("✅ Chat History")

st.sidebar.divider()
st.sidebar.caption("👨‍💻 Developed by Nikhil")
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.session_state.pdf_text = ""


uploaded_file = st.file_uploader(
    "Upload your PDF",
    type="pdf"
)


if uploaded_file:
    st.success("✅ PDF Uploaded Successfully")
    st.write(f"**📄 File Name:** {uploaded_file.name}")
    st.write(f"**📦 File Size:** {uploaded_file.size / 1024:.2f} KB")
    pdf_path = f"data/{uploaded_file.name}"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())


    text = extract_text_from_pdf(pdf_path)

    if not text:
        st.error("PDF se text nahi mil paya. Dusri PDF try karo.")
        st.stop()


    st.session_state.pdf_text = text


    with st.expander("📄 View Extracted Text"):
     st.write(text)


    clean_text = " ".join(preprocess_text(text))

    with st.expander("🧹 View Processed Text"):
     st.write(clean_text)

    with st.spinner("📝 Generating Summary..."):
     summary = summarize_text(text)
    st.success("Summary Generated")

    st.subheader("✨ PDF Summary")
    st.write(summary)



if st.session_state.pdf_text:
    st.divider()

    st.subheader("💬 Ask AI About Your PDF")

    question = st.text_input("Ask your question")

    if question:

        with st.spinner("🤖 AI is thinking..."):
         answer = ask_pdf_question(
        st.session_state.pdf_text,
        question
    )
         


        st.session_state.chat_history.append(
            ("You", question)
        )

        st.session_state.chat_history.append(
            ("AI", answer)
        )


st.subheader("💬 Chat History")

for role, message in st.session_state.chat_history:

    if role == "You":
        with st.chat_message("user"):
            st.write(message)

    else:
        with st.chat_message("assistant"):
            st.write(message)