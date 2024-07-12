import json
from collections import Counter
from nltk.stem import WordNetLemmatizer
import string

# Initialize WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

# Load the list of words to remove from JSON file
with open('stop_words_english.json', 'r', encoding='utf-8') as f:
    words_to_remove = json.load(f)

# List of words to prioritize (rank higher if found)
custom_words = ["filter", "token", "api", "miniapp", "shortcode", "h5", "password", "username"]

# Function to filter out stop words, remove punctuation, lemmatize words in a single sentence
def filter_words_in_sentence(sentence, words_to_remove, lemmatizer):
       # Convert sentence to string if it's not already (handles case for float or other types)
    sentence = str(sentence)
    # Remove punctuations
    translator = str.maketrans('', '', string.punctuation)
    sentence = sentence.translate(translator)
    
    # Split sentence into words
    words = sentence.lower().split()
    
    # Filter out stop words and ignore numbers
    filtered_words = []
    for word in words:
        if word.isalpha():  # Check if word contains only alphabetic characters
            if word.lower() not in words_to_remove:
                filtered_words.append(word)
    
    # Lemmatize words
    lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in filtered_words]
    
    return lemmatized_words

# Function to process error message and title, and return ranked words
def process_error_title(error_message, title):
    # Initialize an empty Counter to hold the combined word counts
    combined_word_counts = Counter()

    # Process error message
    lemmatized_words_error = filter_words_in_sentence(error_message, words_to_remove, lemmatizer)
    word_counts_error = Counter(lemmatized_words_error)
    combined_word_counts.update(word_counts_error)

    # Convert title to string if it's a JSON object
    if isinstance(title, dict):
        title = json.dumps(title)

    # Process title
    lemmatized_words_title = filter_words_in_sentence(title, words_to_remove, lemmatizer)
    word_counts_title = Counter(lemmatized_words_title)
    combined_word_counts.update(word_counts_title)

    # Adjust word counts based on custom list
    for word in custom_words:
        if word in combined_word_counts:
            combined_word_counts[word] += 100  # Increase the count significantly

    # Rank all words based on their occurrence across both sentences
    ranked_words = combined_word_counts.most_common()

    return ranked_words
