#Soln-3.11

total_miles_driven = 0.0
total_gallons_used= 0.0
total_miles_per_gallons= 0.0
gallons= 0.0
miles= 0.0
miles_per_gallons = 0
gallons = float (input('Enter the gallons used (-1 to end):'))
if gallons!= -1: 
           miles = float (input('Enter the miles driven: '))
while gallons!= -1:
        miles_per_gallons =miles/gallons
        print('The miles/gallon for this tank was:',+miles_per_gallons) 
        total_gallons_used += gallons
        total_miles_driven += miles
        gallons = float (input('Enter the gallons used (-1 to end):'))
if gallons!= -1: 
        miles = float (input('Enter the miles driven: '))
else:
        total_miles_per_gallons=total_miles_driven/total_gallons_used
        print('The overall average miles/gallon was',f"{round(total_miles_per_gallons,6):}")