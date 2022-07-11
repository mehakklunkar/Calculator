from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

print("Select Any operation.")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(a/b/c/d): ")

    # Check if choice is one of the four options
    if choice in ('a', 'b', 'c', 'd'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'a':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'b':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'c':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'd':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Please Input correctly.")