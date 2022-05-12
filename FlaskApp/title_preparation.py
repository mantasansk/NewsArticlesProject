import pandas as pd
import re


def clean_title(title):
    """Remove special symbols from title and accents from letters"""
    clean_words = []
    lt_to_en = {"ą": "a", "č": "c", "ę": "e", "ė": "e", "į": "i", "š": "s", "ų": "u", "ū": "u", "ž": "z"}
    lt_letters = [*lt_to_en.keys()]
    title = title.lower()

    for word in title.split():
        # Removing special symbols
        word_only_letters = re.sub(r"\W", "", word)

        if word_only_letters:  # If word is not an empty string
            # Removing accents from letters
            clean_letters = [lt_to_en.get(l) if l in lt_letters else l for l in word_only_letters]
            clean_word = "".join(clean_letters)
            clean_words.append("".join(clean_letters))

    return " ".join(clean_words)


def title_to_data(title):
    """Convert title to data suitable for model"""
    # Cleaning title
    title = clean_title(title)

    # Calculating title length and word count
    title_length = len(title)
    word_count = len(title.split())

    # Convert data to dataframe
    data = pd.DataFrame({"title": [title], "title_length": [title_length], "word_count": [word_count]})

    return data


def return_title_column(x):
    return x["title"]


def return_numeric_columns(x):
    return x[["title_length", "word_count"]]
