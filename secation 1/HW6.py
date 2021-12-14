"""
ולאחר מכן כתבו תוכנית המבקשת מהמשתמש לבחור את האיבר הראשון, ההפרש ומספר האיברים בסידרה חשבונית ומדפיסה את סכום הסידרה.
"""
"""
The Program Calculate The SUM of Arithmetic sequence.
You Need To Provide a Few Parameters of the Arithmetic sequence:
1. First value of the Sequence [A1]
2. Constant Differential {D]
3. The Number Of Syntax at The Sequence [N]
"""
a1 = int(input(" ENTER THE VALUE OF THE FIRST SEGMENT AT THE ARITHMETIC SEQUENCE "))
d = int(input(" ENTER THE VALUE OF THE DIFFERENTIAL OF THE ARITHMETIC SEQUENCE "))
n = int(input(" ENTER THE NUMBER OF THE SEGMENTS AT THE ARITHMETIC SEQUENCE "))
s = ((((n-1)*d)+2*a1)*n)/2
print(f"THE SUM OF THE ARITHMETIC SEQUENS IS: ", {s})