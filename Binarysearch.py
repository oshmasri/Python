
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]>n:
                u=mid-1
            else:
                l=mid+1
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j+1]
                list[j+1]=list[j]
                list[j]=temp

list=[34,45,8,24,424,445,1]
sort(list)
print(list)
n=1
pos=-1
if search(list,n):
    print('Number found at  ', pos+1)
else:
    print('Number not found ')
