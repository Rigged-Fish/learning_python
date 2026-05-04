# My second ever python learning Project!
# This one is a simple Bill-Splitter, absolutely nothing too fancy or complicated
# Just documenting my journey and progress
# I am absolutely aware that this code is noobish and due to extreme improvements, however it is the code I came up with with the knowledge I had until that point
# There is nothing to be ashamed of! I am learning and want to share my journey!
# If you have advice for me, I am absolute more than open for every bit I can learn!

# Code Start: Bill Splitter for nights out with friends

# Set of Variables and their definition Values for calculation

running_total = 0
num_of_friends = 4

# Set of Variables 'Food Items' with variable definition Values for calculation

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Now we're getting to the actual math!

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill, 2)

print(f"Each person pays: {each_pays}")

# second project done! There is a lot to improve on, aswell as documenting '#' in a proper sense, not like I am doing so far - but this will improve aswell.