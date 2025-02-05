def merge(a,b,pos):
  x=0
  y=0
  arr1=[]
  while x<len(a) and y<len(b):
      if a[x]<=b[y]:
          arr1.append(a[x])
          x+=1
      else:
          arr1.append(b[y])
          pos+=(len(a)-x)
          y+=1
  if x==len(a):
      arr1+=b[y:]
  else:
      arr1+=a[x:]  
  return arr1,pos

def mergesort(arr,a):
  if len(arr)==1:
      return arr,a
  mid_val=len(arr)//2
  left=arr[:mid_val]
  right=arr[mid_val:]
  left_arr,left_count=mergesort(left,a)
  right_arr,right_count=mergesort(right,a)
  a=left_count+right_count
  return merge(left_arr,right_arr,a)
input_file=open("input3.txt","r")
output_file=open("output3.txt", "w")
red=int(input_file.readline())
fake_arr=input_file.readline().split()
arr=[]
for i in range(red):
  arr.append(int(fake_arr[i]))
var,total=mergesort(arr,0)
output_file.write(f"{total} ")
input_file.close()
output_file.close()