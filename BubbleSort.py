import random
def CreateArray(n): 
	array = []
	for count in range(0, n):
		array.append(int(round(random.random()*10000)))
	return array

def BubbleSort(n):
	for count1 in range(0, len(n)):
		for count2 in range(0, (len(n)-count1)-1):
			if n[count2+1]<n[count2]:
				temp = n[count2+1]
				n[count2+1] = n[count2]
				n[count2] = temp
	return n

arr = CreateArray(100)
print arr
print '\n\n********************************************************************************\n\n'
arr2 = BubbleSort(arr)
print arr2