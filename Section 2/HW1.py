"""
כתבו תוכנית המקבלת 10 מספרים מהמשתמש ומדפיסה את הגדול ביותר.
"""
list = []
for _ in range(10):
    number = int(input("hello please enter some number\n"))
    list.append(number)
print(max(list))
print(list)