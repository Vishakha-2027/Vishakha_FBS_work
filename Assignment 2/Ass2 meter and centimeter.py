# convert feet and inches into meter and centimeters

feet = int (input(" Enter distance in feet:"))
inches = int (input(" Enter remaining distance in inches:"))

#Conversion factors
#1 foot = 0.3048 meters
#1 inches = 0.0254 meters

# Convert to tal meters
total_meters = (feet * 0.3048)+ (inches * 0.0254)

# Separate meter and centimeters
meter = int(total_meters)
centimeter = (total_meters -meter)*100

print("Meters:",meter)
print ("Centimeters:",centimeter)

 