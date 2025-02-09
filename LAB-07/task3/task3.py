input_file=open("input3_3.txt","r")
output_file=open("output3_3.txt","w")
red=int(input_file.readline())
def dynamical_programming(n):
  if n<=1:
    return 1
  arr=[0]*(n+1)
  arr[1]=1
  arr[2]=2
  for x in range(3,n+1):
    arr[x]=arr[x-1]+arr[x-2]
  return arr[n]
call=dynamical_programming(red)
output_file.write(str(call))
input_file.close()
output_file.close()