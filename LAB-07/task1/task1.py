input_file = open("input1_1.txt", "r")
output_file = open("output1_1.txt", "w")
n,m= map(int, input_file.readline().split())
adjlst=[]
for x in range(m):
    red=tuple(map(int,input_file.readline().split()))
    adjlst.append(red)
def friendship(arr1,cnt_arr,a,b):
  var1=find_frnd(arr1,a+1)
  var2=find_frnd(arr1,b+1)
  if var1==var2:
    return cnt_arr[var1]
  if cnt_arr[var1]<cnt_arr[var2]:
    cnt_arr[var1]=var2
    cnt_arr[var2]+=cnt_arr[var1]
    return cnt_arr[var2]
  else:
    arr1[var2]=var1
    cnt_arr[var1]+=cnt_arr[var2]
    return cnt_arr[var1]
def find_frnd(arr,x):
  if arr[x]==x:
    return x
  arr[x]=find_frnd(arr,arr[x])
  return arr[x]
arr1=[]
for x in range(n+1):
  arr1.append(x)
size_arr=[1]*(n+1)
results=[]
for x in adjlst:
    results.append(friendship(arr1,size_arr,x[0],x[1]))
for result in results:
    output_file.write(str(result) +"\n")
input_file.close()
output_file.close()