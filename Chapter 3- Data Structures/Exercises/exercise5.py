#A guests list that stores three people that I would like to invite to dinner

guests = ["Bert", "Rudolfo", "Pele"]

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