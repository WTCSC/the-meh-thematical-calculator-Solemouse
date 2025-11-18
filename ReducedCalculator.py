def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return False
    else:
        return x / y
def exponent(x, y):
    return x ** y
if __name__ == "__main__":
    print("Ugh math, why do you want to do that? Why would you need to do math? Fine, have a calculator")
    print("1. Are you sure you want to add? \n2. You want to subtract? Really?\n3. Multiply? Ehh, that's fine\n4. No, why would you need division?\n5. Exponents? Make it simple.")
    while True:
        choice = input("Alright, what do you want to do? (1, 2, 3, 4, 5): ")
        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Hmph, fine. What is your first number, oh mighty user? "))
                num2 = float(input("If it were me, I would have done something other than choose a second number: "))
            except ValueError:
                print("Naughty Naughty, you better choose a right option!")
                continue
            if choice == '1':
                print(f"Alright fine, heres your answer {add(num1, num2)}")
            elif choice == '2':
                print(f"You sure you want these numbers subtracted? Yes? Fine but I dont want to hear any whining {subtract(num1, num2)}")
            elif choice == '3':
                print(f"At least it's better than division {multiply(num1, num2)}")
            elif choice == '4':
                if num2 == 0:
                    print("Nuh uh, no division by 0. Rethink your actions.")
                else:
                    print(f"Hmph, here's your divided number {divide(num1, num2)}")
            elif choice == '5':
                print(f"Is it simple? It better be simple, {exponent(num1, num2)}")
            continue_choice = input("Do you want to calculate more? Because I dont (yes/no): ").lower()
            if continue_choice == "no":
                print("Get out of here")
                break
        else:
            print("Can't do that, bud.")
