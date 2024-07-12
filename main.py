# Hello! Welcome to my tag creator.
# Please add a title and message content, and then run the application.
# Have fun with it and give me some comments
# The stop word is from https://countwordsfree.com/stopwords#google_vignette, although I added some to customize it for me




import pandas as pd
from processing import process_error_title  # Assuming this imports your function correctly
error_message="this is the error message"
title="this is the title"
ranked_words = process_error_title(error_message, title)
print (ranked_words)
