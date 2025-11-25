import sys

if len(sys.argv) < 2:
 print("Usage: python3 main.py <path_to_book>")
 sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

from stats import counting

from stats import character_count

from stats import sort_list

def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = counting(text)
    num_character = character_count(text)
    dic_sorted = sort_list(num_character)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in dic_sorted:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")

main()