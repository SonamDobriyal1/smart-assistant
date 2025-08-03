import streamlit as st
from app.document_parser import extract_text
from app.summarizer import generate_summary
from app.ask_anything import answer_question
from app.challenge_me import generate_questions, evaluate_answer

st.set_page_config(page_title="Smart Research Assistant", layout="wide")

st.title("Smart Assistant for Research Summarization")

uploaded_file = st.file_uploader(" Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    text = extract_text(uploaded_file)
    st.success(" Document uploaded successfully!")

    st.subheader(" Auto Summary")
    summary = generate_summary(text)
    st.info(summary)

    st.markdown(" Choose Interaction Mode")
    mode = st.radio("Select Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        user_question = st.text_input(" Ask a question from the document")
        if user_question:
            answer, confidence = answer_question(user_question, text)
            st.success(f"**Answer:** {answer}")
            st.caption(f"Confidence: {confidence:.2f}")

    elif mode == "Challenge Me":
        st.markdown(" Attempt the following logic-based questions:")
        questions = generate_questions(text)
        for i, q in enumerate(questions):
            user_answer = st.text_input(f"Q{i+1}: {q}", key=f"q_{i}")
            if user_answer:
                feedback, justification = evaluate_answer(user_answer, text)
                st.write(feedback)
                st.caption(f"Justification: {justification}")
