"""
כתבו תוכנית המקבלת 10 מספרים מהמשתמש ומדפיסה את הגדול ביותר.
"""
def age_in_month(user_age):
    while True:
        age = user_age * 12
        print(f"your AGE in month is {age}")
        break


while True:
    try:
        age_in_month(int(input("Hello user,Please enter your AGE\n")))
    except ValueError:
        print("The AGE Must Have to be a Number")
        age_in_month(int(input("Hello user,Please enter your AGE\n")))