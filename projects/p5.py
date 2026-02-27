print ()
print ()
print ("PART 1 - CLEANING PHONE NUMBERS")
print ()
print ()

phones = [
    "(260) 555-1234",
    "260.555.9876",
    "260-555-0000",
    "260  555 4321",
    "  260)555  2468 ",
    "  (260) 555-9999",
    "2605551111",
    "260-55-1234",
    "CALL: 260-555-1212 ext 9",
    "N/A"
]

for phone in phones:
    
    phone = phone.strip ()

    # Step 1: keep only digits
    digits = ""

    for character in phone:

        if character.isdigit():
        
         digits += character


 # Step 2: validate length (must be 10 digits, else pring Invalid)
    
    if len(digits) != 10:
        print("Invalid")
    else:
        formatted = digits [:3] + "-" + digits[3:6] + "-" + digits[6:10]
        print(formatted)
 
print ()
print ()
print ("PART 2 - CLEANING NAMES")
print ()
print ()

names = [
    "  moSes   ",
    "DAVID shepherd",
    "  maRy   magDalene  ",
    "pEter  fIsherman",
    "paUL apostle   ",
    "  estHER queen",
    "joSePh  ",
    "   saMUel prophet",
    "rUTH  gleaner ",
    "  soLoMon   king"
]

for name in names:

    name = name.strip ()
    cleaned = ""
    previous_letter = ""
    started = False 

# remove leading spaces 

    for character in name:
        
        if not started and character == " ":
            continue

        started = True 

# reduce multiple spaces to single space

        if character != " ": 
            cleaned += character
        elif previous_letter != " ":
            cleaned += character 

        previous_letter = character

#capitalization 

    cleaned = cleaned.lower ().title ()

    print (cleaned)
        
print ()
print ()
print ("PART 3 - CLEANING TITLES")
print ()
print ()

import re

courses = [
    "CS111",
    "MATH101",
    "BIO202",
    "cs111",
    "CS-111",
    "CS11",
    "COMPSCI101",
    "ENGR10A",
    "HIST300"
]

pattern = r"^[A-Z]{2,4}\d{3}$"   

for course in courses:

    if re.fullmatch(pattern, course):
        print(f"{course} - Valid")
    else:   
        print(f"{course} - Invalid")

    # *** use re.fullmatch() to validate ***
    
    print(course)