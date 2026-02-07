# Original guest list
guest_list =["jesus", "marcus aurelius", "adolf hitler", "franky knuckles", "sun tzu"]

# Variable assigned to a string for reusability
dinner_reservation = "Game Amongst Masters"

# 5 print() statements to welcome original 5 guests
print(f"\nShalom, {guest_list[0].title()} of Nazareth. You are invited as a special guest to my {dinner_reservation} formal dinner.")
print(f"\nGreetings, {guest_list[1].title()}. Please accept my invitation to the {dinner_reservation} formal dinner.")
print(f"\nGuten Tag {guest_list[2].title()}! I welcome you to my {dinner_reservation} formal dinner.")
print(f"\nYo {guest_list[3].title()}, I implore you to join me and several other historic figures to the {dinner_reservation} formal dinner.")
print(f"\nNi hao Master {guest_list[-1].title()}. Your presence is welcome to the {dinner_reservation} formal dinner with several other prominent men.")

# print() function used to announce Sun Tzu is unable to attend the dinner
print(f"\nUnfortunately, {guest_list[-1].title()} is unable to attend the {dinner_reservation} formal dinner.\n")

# Use the .remove() method to remove Sun Tzu from the original list
guest_list.remove("sun tzu")
# Use the .append() method to add a new guest to the end of the "guest_list" Python list
guest_list.append("ichigo kurasaki")

# Re-print greetings to guests, but now you will see a new invite for "Ichigo"
print(f"\nShalom, {guest_list[0].title()} of Nazareth. You are invited as a special guest to my {dinner_reservation} formal dinner.")
print(f"\nGreetings, {guest_list[1].title()}. Please accept my invitation to the {dinner_reservation} formal dinner.")
print(f"\nGuten Tag {guest_list[2].title()}! I welcome you to my {dinner_reservation} formal dinner.")
print(f"\nYo {guest_list[3].title()}, I implore you to join me and several other historic figures to the {dinner_reservation} formal dinner.")
print(f"\nNi hao Master {guest_list[-1].title()}. Your presence is welcome to the {dinner_reservation} formal dinner with several other prominent men.")
print(f"\nKonnichiwa {guest_list[-1].title()}. I am thrilled to announce you have been invited for food & drink at the {dinner_reservation} formal dinner event.\n")

# Using the print() function to announce there is a larger dinner table, so more guests are invited
print(f"\nThank you to all that accepted my invite to the {dinner_reservation} formal dinner. I have just been informed, we found a larger table for more guest seating.\n")

# Adding 3 more invitees using the .insert() method for accuracy, along with the .append() method
guest_list.insert(0, "malcom x")
guest_list.insert(2, "george washington")
guest_list.append("mr. locario")

# Print the new welcome messages, but the only difference is there are more guests to invite AND their index numbers have shifted due to additional guests being added into the beginning, middle, and end of the Python List entitled "guest_list"
print(f"\nHello, {guest_list[0].title()}, you are invited to the {dinner_reservation} formal dinner.")
print(f"\nShalom, {guest_list[1].title()} of Nazareth. You are invited as a special guest to my {dinner_reservation} formal dinner.")
print(f"\nGreetings, {guest_list[3].title()}. Please accept my invitation to the {dinner_reservation} formal dinner.")
print(f"\nGuten Tag {guest_list[4].title()}! I welcome you to my {dinner_reservation} formal dinner.")
print(f"\nYo {guest_list[5].title()}, I implore you to join me and several other historic figures to the {dinner_reservation} formal dinner.")
print(f"\nKonnichiwa {guest_list[6].title()}. I am thrilled to announce you have been invited for food & drink at the {dinner_reservation} formal dinner event.")
print(f"\nHello, {guest_list[2].title()}, you are invited to the {dinner_reservation} formal dinner.")
print(f"\nHello, {guest_list[-1].title()}, you are invited to the {dinner_reservation} formal dinner.")

print(f"\nSorry all for the inconvenience. I have just received word that I can only invite to guests for dinner due to dinner tables not being delivered in time for the {dinner_reservation} formal dinner.\n")

# Only Jesus & Hitler are invited to the dinner now. Use the .pop() method to remove the guests from the 'guest_list', but this method allows the data to still be saved within the program in order to reference it in my print() statements below
# I assigned each .pop() to a variable and referencing each guests names' since their names have been popped from the 'guest_list' in order to send an apology announcement
mr_locario = guest_list.pop(-1)
print(f"Hello {mr_locario.title()}, I apologize for not being able to invite you to the {dinner_reservation} formal dinner gathering.")

ichigo_kurasaki = guest_list.pop(6)
print(f"Hello {ichigo_kurasaki.title()}, I apologize for not being able to invite you to the {dinner_reservation} formal dinner gathering.")

franky_knuckles = guest_list.pop(5)
print(f"Hello {franky_knuckles.title()}, I apologize for not being able to invite you to the {dinner_reservation} formal dinner gathering.")

hitler = guest_list.pop(4)
print(f"Hello {hitler.title()}, I apologize for not being able to invite you to the {dinner_reservation} formal dinner gathering.")

george_washington = guest_list.pop(2)
print(f"Hello {george_washington.title()}, I apologize for not being able to invite you to the {dinner_reservation} formal dinner gathering.")

malcom_x = guest_list.pop(0)
print(f"Hello {malcom_x.title()}, I apologize for not being able to invite you to the {dinner_reservation} formal dinner gathering.\n")

"""
# The indices shifting confused the fuck out of me, so I used the following print statement to help me locate their specific index:
print(guest_list.index("jesus"))
print(guest_list.index("marcus aurelius"))
"""

# 2 print() statements to re-state that Jesus & Marcus Aurelius are still invited to the Game Among Master's formal dinner gathering
print(f"\nShalom, {guest_list[0].title()} of Nazareth. You are still invited as a special guest to my {dinner_reservation} formal dinner.")
print(f"\nGreetings, {guest_list[1].title()}. Please still accept my invitation to the {dinner_reservation} formal dinner.")

# Use the delete statement to delete the final two guests from the list
# Just like .pop() method, deleting an element from a list starting at the bottom of the 'deck of cards' will cause the indices to shift, as opposed to starting at the top of the 'deck of cards'
del guest_list[1]
del guest_list[0]

print(f"\n{guest_list}")

# Use len() function to print a message indicating the number of people I am inviting to dinner
print(f"\nI am inviting {len(guest_list)} guests to the {dinner_reservation} formal dinner.")









