fact_dict={}
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
a="yes"
while(a!="no"):
    num=int(input("Enter a number "))
    ans=factorial(num)
    fact_dict[num]=ans
    a=input("Do you wish to continue-yes or no : ")


print(fact_dict)
