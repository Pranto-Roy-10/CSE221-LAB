def max(a,b):
  if a>b:
    return a
  else:
    return b
def find_max(arr):
  if len(arr) <= 1:
      return arr[0]
  else:
      mid = len(arr)//2
      a1 = find_max(arr[:mid])   
      a2 = find_max(arr[mid:])  
      return max(a1, a2)
input_file=open("input2.txt","r")
output_file=open( "output2.txt", "w")
red=int(input_file.readline())
fake_arr=input_file.readline().split()
arr=[]
for i in range(red):
  arr.append(int(fake_arr[i]))
var=find_max(arr)
output_file.write(f"{var} ")
input_file.close()
output_file.close()  
