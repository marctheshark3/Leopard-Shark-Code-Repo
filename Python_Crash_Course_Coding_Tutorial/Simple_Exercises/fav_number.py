import json

def fav_num():
    user_fav_num = input("Whats your favorite number?")
    filename = 'user_fav_num.json'

    try:
        with open(filename, 'w') as f:
            json.dump = (user_fav_num,f)
            print(f" Your favorite number {user_fav_num} was stored")
    except ValueError:
        print("please choose a number")
fav_num()