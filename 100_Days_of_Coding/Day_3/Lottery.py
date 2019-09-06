from random import choice


ticket = [1, 4, 3, 6, 3,
           5, 8, 9, 7, 0,
           'a', 'x', 'r', 'y', 'p']


def get_numbers(jackpot):
    
    first = choice(jackpot)
    second = choice(jackpot)
    third = choice(jackpot)
    fourth = choice(jackpot)



    print(f"If you number or letters are: {first} ,{second}, {third}, or {fourth} you won!")
get_numbers(ticket)

