n = input("Enter a number")
if int(n)%2 == 0:
    #we must type cast as by default n has str version of number
    print("Number is even")
else:
    print("Number is odd")