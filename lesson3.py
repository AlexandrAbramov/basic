side_a = int(input("please input a: "))
side_b = int(input("please input b: "))
side_c = int(input("please input c: "))

perimeter = side_a + side_b + side_c

if perimeter > 20:
    print(max(side_a, side_b, side_c))
elif side_a == 0:
    print("there are no such triangles")
elif side_b == 0:
    print("there are no such triangles")
elif side_c == 0:
    print("there are no such triangles")
if perimeter < 10:
    print(min(side_a, side_b, side_c))
