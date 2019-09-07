

def myhome(city_name,country_name,population=''):
    ''' Function that grabs county and city name'''
    #print(f"{city_name.title()},{country_name.title()}")
    if population:
        full_string = f"{city_name}, {country_name}, {population}"
    else:
        full_string = f"{city_name}, {country_name}"
    return full_string.title()

print(myhome("Rome", 'Italy', 1_000_000_000))

