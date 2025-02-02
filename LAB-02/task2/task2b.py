input_file=open("input2b.txt","r")
output_file=open("output2b.txt","w")
red=int(input_file.readline())
arr1=input_file.readline().split()
red2=int(input_file.readline())
arr2=input_file.readline().split()
lst1=[]
pointer1=0
pointer2=0
while int(pointer1)<red and int(pointer2)<red2:
  if int(arr1[pointer1])<int(arr2[pointer2]):
    lst1.append(int(arr1[pointer1]))
    pointer1+=1
  else:
    lst1.append(int(arr2[pointer2]))
    pointer2+=1
lst1=lst1+arr1[pointer1:]+arr2[pointer2:]
for x in lst1:
  output_file.write(str(x)+" ")
input_file.close()
output_file.close()