#trying N3+1
#number = int(input("enter a number: "))
#if (({number} % 2)==0):
   # ans = {number} /2
    #print (f"(odp jest {ans})")

number = int(input("enter a number: "))
if (number % 2) == 0:
    ans = number / 2
    print(f"odp jest {ans}")
elif (number % 2) != 0:
    ans2 = number + 1
    print (f"odp jest {ans2}")