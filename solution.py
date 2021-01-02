"""62136"""

l = float(input("Enter value for lambda: "))

if l == -6:
    print("Impossible lambda value.")
    exit(1)

if -2 <= l <= 3:
    limit = 3 if l == -2 or l == 3 else 2
    print(f"The sequence converges with a limit of {limit}")
else:
    sign = "plus" if l > -6 else "minus"
    print(f"The sequence diverges and goes to {sign} infinity")
