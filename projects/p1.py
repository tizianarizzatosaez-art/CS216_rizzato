#      program: assignment.py
#         date: 1/15/2026
#       author: Tiziana Rizzato 
#  description: Calculate the quantity of steps in a day depending on the recommended number of 10000

# input
print ("Enter number of steps")

steps_number = int( input() )
print("Enter stride distance in inches")

inches = int(input())

# processing

total_distance_in = steps_number * inches

total_distance_miles = total_distance_in / 63360  # Convert total inches to miles

 
# output
print(f"You walked {steps_number:,} steps which is { total_distance_miles:.2f} miles")

if steps_number < 10000:
    
    print(f"You need {10000 - steps_number:,} more steps to reach 10,000 ")
    
elif steps_number > 10000:
    
    print(f"You were {steps_number - 10000:,} steps over 10,000 ") 
    
else:
    
    print("You walked exactly 10,000 steps")

