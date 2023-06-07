import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

def count_pos(phrase):
    # Tokenize the phrase into words
    words = word_tokenize(phrase)

    # Perform part-of-speech tagging on the words
    tagged_words = pos_tag(words)

    # Initialize counts for verbs, nouns, pronouns, and adjectives
    verb_count = 0
    noun_count = 0
    pronoun_count = 0
    adjective_count = 0

    # Count the number of each part of speech
    for word, tag in tagged_words:
        if tag.startswith('VB'):  # Verb
            verb_count += 1
        elif tag.startswith('NN'):  # Noun
            noun_count += 1
        elif tag.startswith('PRP'):  # Pronoun
            pronoun_count += 1
        elif tag.startswith('JJ'):  # Adjective
            adjective_count += 1

    # Create a dictionary with the counts
    pos_counts = {
        'Verbs': verb_count,
        'Nouns': noun_count,
        'Pronouns': pronoun_count,
        'Adjectives': adjective_count
    }

    return pos_counts

# Test case
phrase1 = "Write code comments wherever required for code."

# Count the parts of speech in the test case
counts1 = count_pos(phrase1)

# Test case 2
phrase2 = "The greatest glory in living lies not in never falling, but in rising every time we fall."

counts2 = count_pos(phrase2)

# Test case 3
phrase3 = "Write a program to count the number of verbs, nouns, pronouns, and adjectives in a given particular phrase or paragraph, and return their respective count as a dictionary"

counts3 = count_pos(phrase3)

# Print the results
print(f"TC1:\n {phrase1}\n{counts1}")
print(f"TC2:\n {phrase2}\n{counts2}")
print(f"TC3:\n {phrase3}\n{counts3}")
