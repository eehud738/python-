from random import randint
"""
כתבו תוכנית המגרילה בלולאה מספרים שלמים בין 1 ל 1,000,000
עד שמוצאת מספר המתחלק גם ב-7, גם ב-13 וגם ב-15.
"""
while True:
    Number = (randint(1, 1000000))
    if Number % 7 == 0 and Number % 13 == 0 and Number % 15 == 0:
        print(f"The number {Number} is divided by 7 and 13 and 15")
        print(f"Divided by 7 : {Number / 7}")
        print(f"Divided by 13 : {Number / 13}")
        print(f"Divided by 15 : {Number / 15}")
        break
    else:
        print(f"The number {Number} is not divided by 7 and 13 and 15 ")
        continue