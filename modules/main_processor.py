from pdf_reader import extract_text_from_pdf
from text_preprocessing import preprocess_text
from summarizer import summarize_text


pdf_path = "../data/sample.pdf"


text = extract_text_from_pdf(pdf_path)

print("\nOriginal Text:\n")
print(text)


clean_text = " ".join(preprocess_text(text))

print("\n\nProcessed Text:\n")
print(clean_text)


summary = summarize_text(text)

print("\n\nSummary:\n")
print(summary)