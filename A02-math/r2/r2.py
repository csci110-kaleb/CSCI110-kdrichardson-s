#putting r1 and s into a single line so they are read together
r1, s = map(int, input().split())
#to find the missing variable r2 we have to use this equation which will give us the missing variable
r2 = (2 * s) - r1
#lastly we have to print out our answer for r2
print(r2)
#I used google to help me find the beginning code but came up with the eqaution on my own