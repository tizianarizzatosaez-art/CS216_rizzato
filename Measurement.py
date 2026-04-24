# Tiziana Rizzato
# 04/23/26
# This program defines a Measurement class. 
# Measurement  


class Measurement:
    
    def __init__(self, label="undefined",feet=0,inches=0):
        self.label = label
        self.feet = feet
        self.inches = inches
        
# getters        

    def get_label(self):
        return self.label
    
    def get_feet(self):
        return self.feet
    
    def get_inches(self):
        return self.inches
    
# setters
     
    def set_label(self, label):
        self.label = label
        
    def set_feet(self, feet):
        self.feet = feet
        
    def set_inches(self, inches):
        self.inches = inches
    
# get measurement string

    def getMeasurementString(self):
        return f'{self.feet}\' {self.inches}\"'
    

# override the __str__ method

    def __str__(self):
        return f'{self.label}: {self.feet}\' {self.inches}\"'

# add an addInches() method 

    def addInches(self, amount):
        total_inches = int(self.feet * 12 + self.inches + amount)
        self.feet = total_inches // 12
        self.inches = total_inches % 12

# add a getTotalInches() Method 

    def getTotalInches(self):
        return self.feet * 12 + self.inches
    
# add getCentimeters() method
    def getCentimeters(self):
        total_inches = self.getTotalInches()
        return total_inches * 2.54
            
# add a getMetricString() method 

    def getMetricString(self):
        centimeters = self.getCentimeters()
        return f'{centimeters:.2f} cm'
    

if __name__ == "__main__":
    
    office = Measurement()
    
    print(office.label)
    print(office.feet)
    print(office.inches)
    print()
    
# modify the office measurement

    office.set_label("SH 186")
    office.set_feet(15)
    office.set_inches(3)
    
    print(office.label)
    print(office.feet)
    print(office.inches)
    print()
    
# create and print another measurement

    alice = Measurement ("Center Alice #16", 5, 9)

    print(alice.label)
    print(alice.feet)
    print(alice.inches)
    print()

    print (alice.getMeasurementString())
    print ()
    
    print(alice)
    print ()


    alice.addInches(3)
    print(alice.getMeasurementString())
    print()


    print(alice.getTotalInches())
    print()

    print(alice.getCentimeters())
    print()

    print(alice.getMetricString())
    print()




