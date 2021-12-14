from random import randint
"""
כתבו תוכנית המגרילה שני מספרים בין 1 ל-10 ומחשבת את המכפלה המשותפת הקטנה ביותר שלהם,
 כלומר המספר הקטן ביותר שמתחלק בשני המספרים.
 אם לדוגמא הגרלתם את המספרים 4 ו-6 יש להדפיס חזרה את המספר 12.
"""
num1 = randint(1, 10)
num2 = randint(1, 10)
y = max(num1, num2)

while not (y % num1 == 0) & (y % num2 == 0):
    y += 1
print(f"The smallest multiplier of {num1} and {num2} is  {y}")