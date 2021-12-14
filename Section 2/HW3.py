"""
כתבו תוכנית הקוראת שורות מהמשתמש עד שהמשתמש מכניס שורה ריקה.
לאחר הכנסת שורה ריקה יש להדפיס חזרה למשתמש את כל השורות שכתב מהסוף להתחלה.
"""
while True:
    try :
        print("Hello User, Please Write something\n")
        user_input = input()
        print(f"You have written : {user_input[::-1]}")
    except ValueError:
        print("You have to write somethings")