i=int(input("enter the Num: "))

rev_str = str(i)[::-1]

rev_i = int(rev_str)

if (i == rev_i):
    print("Palindrome")
else:
    print("not palindrome")
