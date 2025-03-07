import sys
from stats import get_word_length, get_character_lengths, print_character_lengths

def get_book_text(path):
  with open(path) as f:
    print("============ BOOKBOT ============")

    print("Analyzing book found at books/frankenstein.txt...")
    file_contents = f.read()

    print("----------- Word Count ----------")
    num_words = get_word_length(file_contents)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_lengths = get_character_lengths(file_contents)
    print_character_lengths(char_lengths)

    print("============= END ===============")
  
def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  get_book_text(sys.argv[1])

main()