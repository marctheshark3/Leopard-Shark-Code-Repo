p1 = {'First Name': 'bob', 'Last Name' : 'Belcher','age': '45', 'city':'Somewhere in NJ'}
print(p1['First Name'])

fav_num = {'Bob' : 3 ,
           'Louise' : 43,
           'Linda': 23,
           'Jean': 9,
           'Tina':54,
           'teddy':13,
           'Mr. Fishoeder':50,
           'Mort': 33,
           'Mashmellow' : 70}

for names in (fav_num):
    print(f"{names}'s favorite number is {fav_num[names]}")


rivers = {'nile' : 'egypt',
          'Manatee' : 'florida',
          'colorado' : 'colorado'
            }
for river in rivers:
    print(f"The river {river} is in {rivers[river]}")

for name in rivers:
    print(f"the rivers name is {name}")
for region in rivers.values():
    print(f"the region is in {region.title()} ")
for name, region in rivers.items():
    print(f"The name of the river is: {name.title()} and in the region of {region.title()}")
