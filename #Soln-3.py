#Soln-3.11
#initialise variables
total_miles_driven = 0
total_gallons_used= 0
total_miles_per_gallons= 0
gallons= 0
miles= 0
miles_per_gallons = miles/gallons
total_miles_per_gallons = total_miles_driven/total_gallons_used
#sentinel
while gallons != -1:
    gallons = float (input('Enter the gallons used (-1 to end):'))
    if gallons == -1: 
     miles = float (input('Enter the miles driven:'))
    print('The miles_per_gallons for this tank was',f'{round(miles_per_gallons, 6):}') 
    total_gallons_used += gallons
    total_miles_driven += miles
    print('The overall average miles/gallon was',f"{round(total_miles_per_gallons,6):}")
