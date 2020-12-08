from classes.circle import *
from classes.square import *
from classes.rectangle import *

shape1 = Shapes()
shape2 = Shapes("silver")
shape3 = Shapes("gold", False)
circle1 = Circle()
circle2 = Circle(2.5)
circle3 = Circle(2.9, "purple")
circle4 = Circle(3.9, "grey", False)
square1 = Square()
square2 = Square(3.5)
square3 = Square(3.5, "red")
square4 = Square(4.5, "yellow", True)
rectangle1 = Rectangle()
rectangle2 = Rectangle(4.7, 4.9)
rectangle3 = Rectangle(3.5, 5.7, "black")
rectangle4 = Rectangle(2.7, 9.3, "brown", False)

print(shape1.to_string())
print(shape1.get_color(), shape1.is_filled(), '\n')
print(shape2.to_string())
print(shape2.get_color(), shape2.is_filled(), '\n')
print(shape3.to_string())
print(shape3.get_color(), shape3.is_filled(), '\n\n')

print(circle1.to_string())
print(circle1.get_radius(), circle1.get_area(), circle1.get_color(), circle1.is_filled(), '\n')
print(circle2.to_string())
print(circle2.get_radius(), circle2.get_area(), circle2.get_color(), circle2.is_filled(), '\n')
print(circle3.to_string())
print(circle3.get_radius(), circle3.get_area(), circle3.get_color(), circle3.is_filled(), '\n')
print(circle4.to_string())
print(circle4.get_radius(), circle4.get_area(), circle4.get_color(), circle4.is_filled(), '\n\n')

print(rectangle1.to_string())
print(rectangle1.get_width(), rectangle1.get_length(), rectangle1.get_area(),
	  rectangle1.get_perimeter(), rectangle1.get_color(), rectangle1.is_filled(), '\n')
print(rectangle2.to_string())
print(rectangle2.get_width(), rectangle2.get_length(), rectangle2.get_area(),
	  rectangle2.get_perimeter(), rectangle2.get_color(), rectangle2.is_filled(), '\n')
print(rectangle3.to_string())
print(rectangle3.get_width(), rectangle3.get_length(), rectangle3.get_area(),
	  rectangle3.get_perimeter(), rectangle3.get_color(), rectangle3.is_filled(), '\n')
print(rectangle4.to_string())
print(rectangle4.get_width(), rectangle4.get_length(), rectangle4.get_area(),
	  rectangle4.get_perimeter(), rectangle4.get_color(), rectangle4.is_filled(), '\n\n')

print(square1.to_string())
print(square1.get_side(), square1.get_length(), square1.get_width(), square1.get_area(),
	  square1.get_perimeter(), square1.get_color(), square1.is_filled(), '\n')
print(square2.to_string())
print(square2.get_side(), square2.get_length(), square2.get_width(), square2.get_area(),
	  square2.get_perimeter(), square2.get_color(), square2.is_filled(), '\n')
print(square3.to_string())
print(square3.get_side(), square3.get_length(), square3.get_width(), square3.get_area(),
	  square3.get_perimeter(), square3.get_color(), square3.is_filled(), '\n')
print(square4.to_string())
print(square4.get_side(), square4.get_length(), square4.get_width(), square4.get_area(),
	  square4.get_perimeter(), square3.get_color(), square3.is_filled(), '\n')
