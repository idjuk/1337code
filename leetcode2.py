#Two non-empty linked lists represnting 2 numbers (non negative)
#Digits are stored in reverse order
#Each node is a single digit

def reverselist(list):
    i = len(list) - 1
    rlist = []
    while i >= 0:
        rlist.append(list[i])
        i-=1
    return(rlist)

def makelist(input):
    i = 0
    rlist = []
    while i < len(input):
        rlist.append(input[i])
        i+=1
    return(rlist)

def makestring(list):
    i = 0
    rstring = ""
    while i < len(list):
        rstring = rstring + str(list[i])
        i+=1
    return(rstring)  

input1 = [9,9,9,9,9,9,9]
input2 = [9,9,9,9]

input1b = reverselist(input1)
input2b = reverselist(input2)

#concat numbers
input1c = int(makestring(input1b))
input2c = int(makestring(input2b))

outputr = input1c + input2c
output = reverselist(makelist(str(outputr)))
print(output)