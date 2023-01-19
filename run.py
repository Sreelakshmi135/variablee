import graphics.circle as b
import graphics.rect as c
import graphics.threeDgraphics.cuboid as dt
import graphics.threeDgraphics.sphere as dm
print("!! Circle !!")
a=int(input("Enter the radius :"))
print("Area of circle is",b.area(a))
print("Peri of circle is",b.perimeter(a))
print("\n!! Rectangle!!")
l=int(input("Enter the length of rect :"))
b=int(input("Enter the breadth of rect :"))
print("area of rectangle",c.area(l,b))
print("perimeter of rectangle",c.perimeter(l,b))

print("\n!!Cuboid!!")
l1=int(input("Enter the length :"))
b2=int(input("Enter the breadth :"))
h=int(input("Enter the height :"))
print("area of cuboid",dt.area(l,b,h))
print("perimeter of cuboid",dt.perimeter(l,b,h))

print("\n!! Sphere !!")
r1=int(input("Enter the radius"))
print("area of cuboid",dm.area(r1))
print("perimeter of cuboid",dm.perimeter(r1))

