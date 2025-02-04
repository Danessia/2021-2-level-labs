"""
Language detection starter
"""

import os

from main import tokenize
from main import remove_stop_words
from main import calculate_frequencies
from main import get_top_n_words
from main import create_language_profile
from main import compare_profiles
from main import detect_language

PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))
PATH_TO_TEXTS_FOLDER = os.path.join(PATH_TO_LAB_FOLDER, 'texts')

if __name__ == '__main__':
    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'en.txt'), 'r', encoding='utf-8') as file_to_read_en:
        en_text = file_to_read_en.read()

    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'de.txt'), 'r', encoding='utf-8') as file_to_read_de:
        de_text = file_to_read_de.read()

    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'unknown.txt'), 'r', encoding='utf-8') as \
            file_to_read_unk:
        unknown_text = file_to_read_unk.read()

    with open(os.path.join(PATH_TO_TEXTS_FOLDER, 'la.txt'), 'r', encoding='utf-8') as \
            file_to_read:
        la_text = file_to_read.read()

en_tokens = tokenize(en_text)
print('tokenization:', tokenize(en_text))
en_stop_words = ['the', 'a', 'an']
de_stop_words = ['der', 'die', 'das']
la_stop_words = ['et', 'cum', 'hic', 'hoc', 'latin']
print('tokens_with_removed_stop_words:', remove_stop_words(en_tokens, en_stop_words))
frequencies = remove_stop_words(en_tokens, en_stop_words)
print('freq_dictionary: ', calculate_frequencies(frequencies))
freq_dict = calculate_frequencies(frequencies)
top_n = 3
print('top_n_words:', get_top_n_words(freq_dict, top_n))
en_profile = create_language_profile('en', en_text, en_stop_words)
print('en_profile: ', en_profile)
de_profile = create_language_profile('de', de_text, de_stop_words)
la_profile = create_language_profile('la', la_text, la_stop_words)
unknown_profile = create_language_profile('unknown', unknown_text, [])
print('compare_profiles: ', compare_profiles(unknown_profile, en_profile, top_n))
print('detect_language: ', detect_language(unknown_profile, en_profile, de_profile, top_n))

EXPECTED = 'en'
RESULT = 'en'

# DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
# assert RESULT, 'Detection not working'
assert RESULT, 'Detection not working'