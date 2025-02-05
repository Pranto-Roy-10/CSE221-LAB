def mod_quick(arr,n,q):
  if n==-1:
      return
  else:
      count=partition(arr,n)
      if count==query:
          output_file.write(f"{arr[n]}\n")
      else:
          mod_quick(arr,n-1,q)

def partition(arr,n):
  pivot=arr[n]
  cnt=0
  for num in range(len(arr)):
      if arr[num]<=pivot:
          cnt+=1
  return cnt
input_file=open("input6.txt","r")
output_file=open("output6.txt", "w")
red=int(input_file.readline())
fake_arr=input_file.readline().split()
arr=[]
for i in range(red):
  arr.append(int(fake_arr[i]))
queries=int(input_file.readline())
for i in range(queries):
  query=int(input_file.readline())
  mod_quick(arr,red-1,query)  
input_file.close()
output_file.close()