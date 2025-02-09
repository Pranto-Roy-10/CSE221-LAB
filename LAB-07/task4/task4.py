input_file=open("input4_2.txt","r")
output_file=open("output4_2.txt","w")
n,m=map(int,input_file.readline().split())
coins=list(map(int,input_file.readline().split()))
def coin_change(coins,m):
  arr=[float('inf')]*(m+1)
  arr[0]=0
  for x in coins:
    for y in range(x,m+1):
      arr[y]=min(arr[y],arr[y-x]+1)
  if arr[m]==float('inf'):
    return -1
  else:
    return arr[m]
call = coin_change(coins,m)
output_file.write(str(call))
input_file.close()
output_file.close()
