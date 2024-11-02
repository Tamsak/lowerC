def lowerC(a):
    newS = ""
    i = 0
    for i in range(len(a)): 
            if i == 0 or a[i-1] == " ":
               newS += a[i].upper()
            else :
               newS += a[i].lower()
        
    print(newS)

lowerC("LET CHANGE THIS TO LOWER CASE WITH THE FIRST LETTER AS UPPER CASE")