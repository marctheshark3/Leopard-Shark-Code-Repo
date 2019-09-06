mybook = '/Users/marctheshark/Documents/GitHub/Leopard-Shark-Code-Repo/Python_Crash_Course_Coding_Tutorial/Project_Gutenberg_harriet_comstock.txt'

def get_my_items(file):
    book = []
    try:
        with open(file) as file_object:
            for line in file_object:
                book.append(line)


    except FileNotFoundError:
        print('The file is missing friend!')

    else:
        return (book)

corpus = get_my_items(mybook)
print(len(corpus))

for line in corpus:
    words = line.split()
    
    #print(len(words))

print(corpus[99])
