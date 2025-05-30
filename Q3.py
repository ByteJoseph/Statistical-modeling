# write a program to find surface area and volume of a cylinder using functions
# A=2πrh+2πr^2 
# V= pi r^2 h
def area(r,h):
    return (2*3.14*r*h)+(2*3.14*(r*r))
def volume(r,h):
    return (3.14*(r*r)*h)

a = float(input("Enter the radius of Cylinder: "))
b = float(input("Enter the height of Cylinder: "))

_area = area(a,b)
_volume = volume(a,b)

print("Area = ",_area,"\nVolume = ",_volume)