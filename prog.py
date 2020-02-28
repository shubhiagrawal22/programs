
l1 = list(input().split(","))
l2 = list(input().split(","))
l3 = list(input().split(","))
l4=[]
for i in l1:
    if i not in l2 and i not in l3:
        l4.append(i)
print(l4)
        
