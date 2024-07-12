import json

# Load the list of words from JSON file
with open('stop_words_english.json', 'r',encoding='utf-8') as f:
    words_to_remove = json.load(f)
sentences = [
    "This is a sample sentence with some words to remove.",
    "Another sentence that contains words we want to filter out.",
    "Here's a third sentence for testing purposes."
]

# Function to filter out words from sentences
def filter_words_from_sentences(sentences, words_to_remove):
    filtered_sentences = []
    for sentence in sentences:
        words = sentence.split()  # Split sentence into words
        filtered_words = [word for word in words if word.lower() not in words_to_remove]
        print('$' ,filtered_words)
        filtered_sentence = ' '.join(filtered_words)  # Join words back into sentence
        filtered_sentences.append(filtered_sentence)
    return filtered_sentences

# Remove words from sentences
filtered_sentences = filter_words_from_sentences(sentences, words_to_remove)

# Print or use the modified sentences
for sentence in filtered_sentences:
    print(sentence)
