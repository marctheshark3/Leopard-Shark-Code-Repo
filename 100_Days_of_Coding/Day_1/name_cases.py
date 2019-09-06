name = 'Eric'
message = f"hello {name}, How do you like learning python so far? "
print(message)

print(name.upper())
print(name.lower())
print(f"Hello,{name.title()}!")

quote = 'Albert Einstein once said: "A Person who never made a mistake never tried anything new" '
print(quote)

new_quote = ' "Be who you are and say what you feel, because those who mind don’t matter and those who matter don’t mind." '
famous_persons = 'Dr. Suess'
message = f"{famous_persons} once said:{new_quote}"
print(message)

some_name = ' \t Peter \n '
print(some_name)
#left strip
print(some_name.lstrip())
#right strip
print(some_name.rstrip())
#both strip
print(some_name.strip())
