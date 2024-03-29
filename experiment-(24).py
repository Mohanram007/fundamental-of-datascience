

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

df = pd.read_csv(r"C:\Users\alext\Desktop\mohan 1\FOD\feedback_data.csv")

def preprocess_text(text):
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

df['tokens'] = df['feedback'].apply(preprocess_text)

all_words = [word for tokens in df['tokens'] for word in tokens]
word_freq = Counter(all_words)

N = int(input("Enter the number of top frequent words to display: "))
top_words = word_freq.most_common(N)
for word, freq in top_words:
    print(f"{word}: {freq}")

top_words_df = pd.DataFrame(top_words, columns=['Word', 'Frequency'])
plt.figure(figsize=(10, 6))
plt.bar(top_words_df['Word'], top_words_df['Frequency'], color='skyblue')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Top {} Most Frequent Words'.format(N))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
