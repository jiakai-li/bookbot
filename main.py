import sys

from stats import format_char_dict, get_num_chars, get_num_words


def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as f:
        content = f.read()
    return content


def main(book_file: str) -> None:
    content = get_book_text(book_file)
    num_words = get_num_words(content)
    num_chars = get_num_chars(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in format_char_dict(num_chars):
        print("{char}: {count}".format(char=item["char"], count=item["num"]))
    print("============= END ===============")


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(book_file=sys.argv[1])
