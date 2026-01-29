#      program: p2.py
#        date: 1/26/2026
#       author: Tiziana Rizzato
#  description: Calculates miles walked from steps and stride length,
#               and reports how far over or under 10,000 steps.
#               Demonsrates use of return functions.

# functions

def get_steps():
    print("Enter number of steps: ")
    steps = int(input())
    return steps

def get_stride_inches():
    print("Enter stride length in inches: ")
    stride = int(input())
    return stride


def calculate_miles(steps, stride_inches):
    total_inches = steps * stride_inches
    miles = total_inches / 63360
    return miles

def additional_steps_needed(steps):
    needed = 10000 - steps
    return needed


def miles_output_line(steps, miles):
    return(f'You walked {steps:,} steps which is {miles:.2f} miles')
    

def steps_output_line( additional ):
    msg = "undefined"
    final_steps = - additional
    if final_steps > 0:
        return (f'You need {additional:,} more steps to reach 10,000')
    elif final_steps == 0:
        msg = "undefined"
        return(f'You walked exactly 10,000 steps')
    else: 
        msg = f'You were {-additional:,} steps over 10,000'
        return msg
   

# +------ do not modify this section ----------+
def main():

    # input
    steps = get_steps()
    stride_inches = get_stride_inches()

    # processing
    miles = calculate_miles(steps, stride_inches)
    additional = additional_steps_needed(steps)

    # output
    print( miles_output_line(steps, miles) )
    print( steps_output_line(additional) )

if __name__ == "__main__": main()

# +------ do not modify this section ----------+
