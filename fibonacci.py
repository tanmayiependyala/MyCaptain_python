n1,n2=0,1
count=0
n=int(input("enter the number of terms in series:"))
while count<n:
  print(n1)
  nth=n1+n2
  n1=n2
  n2=nth
  count=count+1
