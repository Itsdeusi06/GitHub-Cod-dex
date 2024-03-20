import math


print("==================")
print("Area Calculator 📐")
print("==================\n")
    

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit\n")


choice = input("Which shape: ")


if choice == '1':
    height = int(input("Height: "))
    base = int(input("Base: "))
    area = (height * base)/2
    print(f"The area is,", area)
elif choice == '2':
    height = int(input("Height: "))
    width = int(input("Width: "))
    area = height * width
    print("The area is,", area)
elif choice == '3':
    side = int(input("Side: "))
    area = side ** 2
    print("The area is, ", area)
elif choice == '4':
    radius = int(input("Radius: "))
    area = math.pi * radius ** 2
    print("The area is, ", area)
elif choice == '5':
    print("Exiting...")
else:
    print("Invalid choice. Please choose a number from 1 to 5.")

