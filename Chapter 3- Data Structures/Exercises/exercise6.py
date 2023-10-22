#A guests list that stores three people that I would like to invite to dinner

guests = ["Bert", "Rudolfo", "Robner"]

#Print statements on inviting each person of the guests list to a dinner
print(f'Good day! {guests[0]} I would like to invite you to dinner.')
print(f'Good day! {guests[1]} I would like to invite you to dinner.')
print(f'Good day! {guests[2]} I would like to invite you to dinner.')

#A print statement that states the name of the guest who can not make it to dinner
print(f'{guests[2]} can not make it to dinner.')

#Modifying the guests list with replacing the name of the guest who can’t make it with the name of the new person invited to dinner
#Using positive indexing of 2 which is the 3rd element and assigning a new value/name to it
guests[2] = "Robner"

#A second set of invitation messages for each person who is still in the guests list
print(f'Good day! {guests[0]} I would like to invite you to dinner.')
print(f'Good day! {guests[1]} I would like to invite you to dinner.')
print(f'Good day! {guests[2]} I would like to invite you to dinner.')

#A print statement saying that only two people can be invited for dinner
print(f'Sorry for the inconvenience but I can invite only two people for dinner.')

#Using the pop() to remove guests from the list leaving two names in the list
#A print statement letting them know that they can not be invited to dinner
print(f'I am very sorry to inform you {guests.pop(1)} but I can not invite you to dinner.')

#Print statements to each of the two people still in the list letting them know they are still invited
print(f'Good day! {guests[0]} you are still invited to dinner.')
print(f'Good day! {guests[1]} you are still invited to dinner.')

#Using the del() with list slicing in positive indexing to remove the last two names from the list
del guests[0:2]

#A print statement showing that the guests list is empty
print(guests)