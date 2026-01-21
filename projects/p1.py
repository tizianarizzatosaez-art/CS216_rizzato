
#      program: assignment.py
#         date: 1/15/2026
#       author: Tiziana Rizzato 
#  description: Calculate quantity of steps in a day depending on the recommended number of 10000

# input


                   
print ("Enter number of steps: ")

steps_number = int( input() )
                   
# need to change this to two-line approach
steps_length_in = float(input("Enter the average length of your steps in inches: "))

# processing

steps_length_in = steps_length_in * 0.0254 # Convert

total_distance_in = steps_number * steps_length_in

total_distance_miles = total_distance_in / 63360  # Convert total inches to miles

 
# output

print(f"Total distance walked: {total_distance_miles:.2f} miles")

if steps_number > 10000:
    
    print(f"You took {steps_number - 10000} steps over the recommended 10,000 steps.")
    
elif steps_number < 10000:
    
    print(f"You took {10000 - steps_number} steps under the recommended 10,000 steps.")
    
else:
    
    print("You met the recommended number of steps.")
