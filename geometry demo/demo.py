from geometry import Rectangle, Triangle, Shape, area_stats

# 1. Construct shapes
r1 = Rectangle(3, 4)
r2 = Rectangle(5, 6)
t1 = Triangle(3, 4, 5)

shapes = [r1, r2, t1]

# 2. Print their areas
for i, shape in enumerate(shapes, start=1):
    print(f"Shape {i} ({type(shape).__name__}) area: {shape.area()}")

# 3. Print the summary dict from area_stats
stats = area_stats(*shapes)
print("\nArea statistics summary:")
for key, value in stats.items():
    print(f"{key}: {value}")
