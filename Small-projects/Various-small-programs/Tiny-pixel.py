# Task: replace 0 with " " and 1 with "*"
# print the picture
picture=[
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,1,1,1,1],
    [0,0,1,0,0]
]

for row in picture:
    for char in row:
        if char==0:
            print(" ",end="")
        else:
            print("*",end="")
    print("") # needed a new line after each row

