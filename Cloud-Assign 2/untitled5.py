from collections import Counter
import nltk
from nltk.corpus import stopwords

def read_text_file(file_path):
    """Read the contents of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def remove_stopwords_nltk(text):
    """Remove stopwords from the text using NLTK."""
    words = text.split()
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.isalpha()]
    return filtered_words

def count_word_frequency(words):
    """Count the frequency of each word in the text."""
    return Counter(words)

def display_word_frequency(word_freq):
    """Display word frequency count to the console."""
    for word, freq in word_freq.items():
        print(f'{word}: {freq}')

def main():
    # Read the contents of the text file
    file_path = "C:/Users/PCM/Downloads/paragraphs.txt"
    text = read_text_file(file_path)
    
    # Remove stopwords using NLTK
    filtered_words = remove_stopwords_nltk(text)
    
    # Count word frequency
    word_freq = count_word_frequency(filtered_words)
    
    # Display word frequency count
    display_word_frequency(word_freq)

if __name__ == "__main__":
    main()
