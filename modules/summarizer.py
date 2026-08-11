from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
import nltk

nltk.download('punkt')
nltk.download('stopwords')


def summarize_text(text, sentence_count=3):

    sentences = sent_tokenize(text)

    stop_words = set(stopwords.words('english'))

    words = text.lower().split()

    freq = {}

    for word in words:
        if word not in stop_words:
            freq[word] = freq.get(word, 0) + 1


    sentence_scores = {}

    for sentence in sentences:
        for word in sentence.lower().split():
            if word in freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]


    summary_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:sentence_count]


    return " ".join(summary_sentences)