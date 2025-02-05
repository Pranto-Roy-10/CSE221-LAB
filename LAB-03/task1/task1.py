def merge(a, b):
  lst=[]
  left=0
  right=0
  while left<len(a) and right<len(b):
    if a[left]<b[right]:
      lst.append(a[left])
      left+=1
    else:
      lst.append(b[right])
      right+=1
  while left<len(a):
    lst.append(a[left])
    left+=1
  while right<len(b):
    lst.append(b[right])
    right+=1
  return lst   
def mergeSort(arr):
  if len(arr) <= 1:
      return arr
  else:
      mid = len(arr)//2
      a1 = mergeSort(arr[:mid])   
      a2 = mergeSort(arr[mid:])  
      return merge(a1, a2)     
input_file=open("input1.txt","r")
output_file=open( "output1.txt", "w")
red=int(input_file.readline())
fake_arr=input_file.readline().split()
arr=[]
for i in range(red):
  arr.append(int(fake_arr[i]))
lst=mergeSort(arr)
for i in lst:
  output_file.write(f"{i} ")

input_file.close()
output_file.close()  