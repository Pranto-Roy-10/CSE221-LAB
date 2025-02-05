def quickSort(arr,p,r):
  if p<r:
    q=partition(arr,p,r)
    quickSort(arr,p,q-1)
    quickSort(arr,q+1,r)

def partition(arr,p,r):
  x=arr[r]
  i=p-1
  for j in range(p,r):
    if arr[j]<=x:
      i=i+1
      arr[i],arr[j]=arr[j],arr[i]
  arr[i+1],arr[r]=arr[r],arr[i+1]
  return i+1
input_file=open("input5.txt","r")
output_file=open( "output5.txt", "w")
red=int(input_file.readline())
fake_arr=input_file.readline().split()
arr=[]
for i in range(red):
  arr.append(int(fake_arr[i]))
quickSort(arr,0,red-1)
for i in arr:
  output_file.write(f"{i} ")
input_file.close()
output_file.close()