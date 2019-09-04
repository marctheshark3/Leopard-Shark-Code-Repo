guest_ls = ['Albert Einstein', 'Elon Musk', 'Malcolm Gladwell','Tich Naht Hanh', 'Black Beard','Moses']

guest = guest_ls[0]

invite = f"{guest} , you are formally invited to dinner this Friday at 3pm"

canceled_guest = guest_ls[3]
print(canceled_guest)

new_guest = 'Dr. Seuss'
guest_ls[3] =new_guest

print('we found a new table for three more guest')

#adding more to the list
guest_ls.insert(0,'Joe Rogan')
guest_ls.insert(4,'Rick Sanchez')
guest_ls.append('Anthony Bourdan')
#print(guest_ls)

#function that loops through the list for indiviual invite messages
def invites(guest_list):
    for i in range(len(guest_ls)):
        myguest = guest_ls[i]
        message = f"{myguest} , you are formally invited to dinner this Friday at 3pm"
        print(message)


#invites(guest_ls)

print('Attention: we can now only invite two people, sorry for any inconvience')
def two_people_only(guest_list):
    for i in range(len(guest_list)):
        if len(guest_list) == 2:
            break
        guest_list.pop()
    for i in range(len(guest_list)):
        myguest = guest_list[i]
        new_message = f"{myguest} , you are still formally invited to dinner this Friday at 3pm"
        print(new_message)

two_people_only(guest_ls)

guest_ls.pop()
guest_ls.pop()
print(guest_ls)