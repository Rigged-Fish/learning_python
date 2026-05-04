# My third ever python Project!
# Documenting my learning journey along the way!
# Of course there is a lot!! that can and should be improved on that code!
# However this is a documentation of my knowledge up until that point and is vital for me learning the fundamentals and logic behind it.
# If you have advice for me, I am absolute more than open for every bit I can learn!

# Setting the parameters, variable definition values

base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

# My first Set of conditional operators!

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)
    final_price = base_price + extra_charges + service_charges - discount
    print("Final price of ticket:", final_price)
    
else:
    print('Ticket booking failed due to restrictions')


# Finished!
# There was a lot to learn in this project, in regards to the conditional operators.
# I have also to improve on my documentation '#' comments, aswell as of course, the code itself, I am fully aware of those two construction sites I am working at.
