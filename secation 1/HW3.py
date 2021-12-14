"""
כתבו תוכנית המבקשת מהמשתמש לבחור מספר ומדפיסה את המילה Boom אם המספר מתחלק ב-7
"""
num = int( input (" CHOOSE A NUMBER "));
if (num % 7) == 0  or (num == 7):
    print ("BOOM")
else: print("Not Boom")