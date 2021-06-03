def solution(n):
	X=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']

	# convert n to binary string
	for k in range (0,31):
		mask = 2**k
		if (n & mask) != 0:
			X[31-k] = '1'

	s = ''.join(X)
	
	# check for max binary gap using string match
	for j in range (30):
		gap = "1" + '0'*(30-j) + "1"
		if gap in s:
			return len(gap)-2
	else:
		return 0
		
for m in range (2,20):
	print("bingap 0x%2x = %d" % (m, solution(m)))

