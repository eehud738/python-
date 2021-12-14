"""
כתבו תוכנית המבקשת מהמשתמש לבחור מספר ומדפיסה את המילה Boom אם המספר מתחלק ב-7 או מכיל את הסיפרה 7.
"""
while True:
    print(" Hello User, please put a number ")
    number = int(input())
    if number % 7 == 0 or '7' in str(number) :
        print("BOOM")
    else :
        print("The number if not not divided by 7 and not contains the number 7")