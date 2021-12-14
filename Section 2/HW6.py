from random import randint
"""
כתבו תוכנית הבוחרת באקראי מספר בין 1 ל-100. על המשתמש לנחש את המספר שנבחר ואחרי כל ניחוש יש להדפיס ״גדול מדי״ או ״קטן מדי״ לפי היחס בין המספר שנבחר לניחוש.
בונוס: כדי שיהיה מעניין דאגו שמדי פעם התוכנית תדפיס את ההודעה הלא נכונה.
"""
def check_user_input(user_number):
    number = randint(1, 100)

    if user_number > number:
        print(f"The number is you choose is higher than the number which is being raffled{number}")
    elif user_number < number:
        print("The number is you choose is Lower than the number which is being raffled")
    else:
        print("YOU GUESSED THE NUMBER --> WELL DONE ")


while True:
    try:
        print("Hello User, Which number is being raffled?")
        check_user_input(int(input()))
    except ValueError:
        print("Please enter a number")