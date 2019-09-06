cats = '/Users/marctheshark/Documents/GitHub/Leopard-Shark-Code-Repo/Python_Crash_Course_Coding_Tutorial/cats.txt'
dogs = '/Users/marctheshark/Documents/GitHub/Leopard-Shark-Code-Repo/Python_Crash_Course_Coding_Tutorial/dogs.txt'
missing_file = '/Documents/GitHub/Leopard-Shark-Code-Repo/Python_Crash_Course_Coding_Tutorial/dogs.txt'

both = [cats,dogs]
def get_my_items(file):
    try:
        with open(file) as file_object:
            lines = file_object.readline()
    except FileNotFoundError:
        #fail silently
        pass
        #print('The file is missing friend!')
    else:

        print(lines)


get_my_items(missing_file)
