s=str(input("enter any string"))
lst1=[]
lst2=[]
i=0
for j in s:
  count=0
  for k in s[i+1:]:
    if j==k:
      count=count+1
  if j not in lst1:
    lst1.append(j)
    lst2.append(count)
for q in range(len(lst1)):
  print(lst1[q],lst2[q])
