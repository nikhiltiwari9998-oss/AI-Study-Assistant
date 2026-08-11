import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Ye resources sirf pehli baar download honge
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def preprocess_text(text):
    # Sab text ko lowercase mein convert karo
    text = text.lower()

    # Words mein tod do
    words = word_tokenize(text)

    # Stopwords load karo
    stop_words = set(stopwords.words('english'))

    # Punctuation aur stopwords hatao
    filtered_words = []

    for word in words:
        if word not in stop_words and word not in string.punctuation:
            filtered_words.append(word)

    return filtered_words 

if __name__ == "__main__":
    text = "This is my AI Study Assistant project. It helps students."
    print(preprocess_text(text))