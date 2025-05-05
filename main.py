from stats import word_count, char_counter,sort_text
import sys

def get_book_text(book):
    file_contents = book.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(sys.argv[1],'r') as book:
        text = get_book_text(book)
        count = word_count(text)
        counter= char_counter(text)
        sorted_counter=sort_text(counter)
        print(f"Found {count} total words")
        pure_list=[]
        for item in sorted_counter:
            print(f"{item["name"]}: {item["num"]}")
        
        

        
main()