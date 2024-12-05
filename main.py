def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Analysiere das Buch {book_path} ---")
    print(f"Das genannte Buch enthält {num_words} Worte")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"Das Zeichen '{item['char']}' wurde {item['num']} mal gefunden")

    print("--- Analyse beendet ---")

    
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list 

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_characters(text):
    alphabet = {}
    for c in text:
        lowered = c.lower()
        if lowered in alphabet:
            alphabet[lowered] += 1
        else:
            alphabet[lowered] = 1
    return alphabet



main()
