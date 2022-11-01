def convertNumber(n, B):
	result = ''
	while n > 0:
		result = result + str(n%B)  
		n = n//B
   
	return result[::-1]

def convertWithoutTurn(n,B):
	result=''
	temLsit = []
	while n > 0:
		temLsit.insert(0,str(n%B))
		n = n//B
	result = result.join(temLsit)
	return result


print(convertNumber(128, 2))
print(convertNumber(24, 8))

print(convertWithoutTurn(128, 2))
print(convertWithoutTurn(24, 8))