n = int(input())
align = [0] * (n+1)
align[0] = 1
align[1] = 1

if n!=1:
	for i in range(2, n+1):
	    align[i] = (align[i-1] + align[i-2]) % 10007
print(align[n])