
def main():
    import sys
    from stats import get_num_words, get_num_chars, sort_dict
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
   

    book_path = (f"{sys.argv[1]}")
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    
    num_chars = get_num_chars(text)
    #print(num_chars)
    sorted_list = sort_dict(num_chars)
    print("--------- Character Count -------")
    for i in range(0,len(sorted_list)):
        print(f"{sorted_list[i][0]}: {sorted_list[i][1]}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()







main()
