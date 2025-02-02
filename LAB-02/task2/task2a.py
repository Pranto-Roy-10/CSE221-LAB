input_file=open("input2a.txt", "r")
output_file=open("output2a.txt", "w")
red=int(input_file.readline())
arr1=input_file.readline().split()
red2=int(input_file.readline())
arr2=input_file.readline().split()
lst=[]
for x in range(red):
  lst.append(int(arr1[x]))
for y in range(red2):
  lst.append(int(arr2[y]))
lst.sort()
for x in lst:
  output_file.write(str(x) + " ")
input_file.close()
output_file.close()
