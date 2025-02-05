def mod_mergesort(arr):
  if len(arr)==2:
    return arr[0]+arr[-1]**2
  elif len(arr)<2:
    return 0
  mid_val=len(arr)//2
  left_arr=mod_mergesort(arr[:mid_val])
  right_arr=mod_mergesort(arr[mid_val:])
  result=calculations(arr[:mid_val],arr[mid_val:])
  return max(left_arr,right_arr,result)
def calculations(left_arr,right_arr):
  left_max=max(left_arr)
  right_list=[]
  for x in right_arr:
    if x<0:
      right_list.append(abs(x))
    else:
      right_list.append(x)
  right_max=max(right_list)
  return int(left_max+right_max**2)
input_file=open("input4.txt","r")
output_file=open("output4.txt","w")
red=int(input_file.readline())
fake_arr=input_file.readline().split()
arr=[]
for i in range(red):
  arr.append(int(fake_arr[i]))
var=mod_mergesort(arr)
output_file.write(f"{var}")
input_file.close()
output_file.close()