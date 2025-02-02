input_file = open("input4.txt","r")
output_file = open("output4.txt","w")
red=list(map(int,input_file.readline().split(" ")))
var=red[0]
arr=[[0]*2]*red[1]
arr1=[]
for x in range(var):
    red1=list(map(int,input_file.readline().split(" ")))
    arr1.append(red1)
def mergesort(A):
    if len(A)==1:
        return A
    else:
        mid=len(A)//2
        a=mergesort(A[:mid])
        b=mergesort(A[mid:])
        return merge(a,b)
def merge(a,b):
    i=0
    j=0 
    new_arr=[]
    while i<len(a) and j<len(b):
        if a[i][1]<=b[j][1]:
            new_arr.append(a[i])
            i+=1
        else:
            new_arr.append(b[j])
            j+=1
    if i==len(a):
        for item in range(j,len(b)):
            new_arr.append(b[item])
    else:
        for item in range(i,len(a)):
            new_arr.append(a[item])
    return new_arr
srt_time=mergesort(arr1)
count = 0
for y in range(var):
    checker=False
    diff=[-1]*len(arr)

    for j in range(len(arr)):
        if arr[j][1]<=srt_time[y][0]:
            diff[j]=srt_time[y][0]-arr[j][1]
            checker=True
    if checker:
        count+=1
        min=float('inf')
        k=0
        idx=0
        for z in diff:
            if z<min and z!=-1:
                min=z
                idx=k
            k+=1
        arr[idx]=srt_time[y]    
output_file.write(f'{count}')
input_file.close()
output_file.close()