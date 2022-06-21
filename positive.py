n=int(input("enter size")
lst=[]
for i in range(n):
      el=int(input())
      lst.append(el)
print("given list by user",lst)
print("list of positive nos")
for j in lst:
      if j>0:
         print(j)
