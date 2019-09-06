num_list = []
for counting in (range(1,1_000_001)):
    #print(counting)
    num_list.append(counting)

print(min(num_list))
print(max(num_list))
print(sum(num_list))

for odds in range(1,20,2):
    print(odds)

three_multiples =[]
for threes in range(3,31,3):
    three_multiples.append(threes)
    print(threes)

mycube = [num**3 for num in range(1,10)]
print(mycube)

