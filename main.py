from stats import get_num_words
from stats import count_characters
from stats import sort_characters
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def main(book_path):
    with open(book_path) as f:
        book_text = f.read()

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    print("----------- Word Count ----------")
    # Count words
    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    # Count characters
    character_counts = count_characters(book_text)
    # Sort characters
    char_list = sort_characters(character_counts)
    # Print character list by line
    for pair in char_list:
        for char, count in pair.items():
            print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":
    main(book_path)