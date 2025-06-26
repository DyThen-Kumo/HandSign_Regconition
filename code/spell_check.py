import re
from spellchecker import SpellChecker

spell = SpellChecker(language='en')  # hoặc 'vi'

def remove_repeated_chars(s):
    # Giữ tối đa 2 ký tự liên tiếp giống nhau
    return re.sub(r'(.)\1{2,}', r'\1\1', s)

def process_sentence(raw_sentence):
    result = ""
    tokens = raw_sentence.strip().split()

    for token in tokens:
        if token == "space":
            result += " "
        elif token == "del":
            result = result[:-1]
        elif re.fullmatch(r"[A-Z]", token):
            result += token
        else:
            pass  # Bỏ qua ký tự không hợp lệ

    # Loại bỏ lặp quá 2 ký tự
    result = remove_repeated_chars(result)
    return result

def check_spell(result):
    # Chính tả
    corrected_words = []
    for word in result.strip().split():
        corrected = spell.correction(word)
        corrected_words.append(corrected if corrected else word)

    corrected_sentence = " ".join(corrected_words)
    return corrected_sentence.upper()

# raw = "H S S del del S S S S S S S S del del del del del del del E L L O"
# print(process_sentence(raw))  # → "hello world"
# print(check_spell(process_sentence(raw)))
