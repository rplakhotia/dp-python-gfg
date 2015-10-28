
#from enum import Enum
# edit distance function calculates the minimum number of operations
# required for changing one string to another 

def edit_distance(texta, textb, lena, lenb):
	
	D = [[0 for x in range(lenb+1)] for x in range(lena+1)]
	bt = [["" for x in range(lenb+1)] for x in range(lena+1)]

	# right - insert
	# down - delete
	# diagonal down - substitute

	for i in range(0, lena+1):
		for j in range(0, lenb+1):

			if j == 0:
				D[i][j]= i
				#bt[i][j] = "INSERT"

			elif i == 0:
				D[i][j]= j
				#bt[i][j] = "DELETE"

			elif texta[i-1] == textb[j-1]:
				D[i][j] = D[i-1][j-1]
				#bt[i][j] = "NO-OP"

			else:
				m = min( D[i][j-1], D[i-1][j], D[i-1][j-1] )
				D[i][j] = 1 + m
	
				#if m == D[i][j-1]:
				#	bt[i][j] =  "INSERT"
				#elif m == D[i-1][j-1]:
				#	bt[i][j] = "SUBSTITUTE"
				#elif m == D[i-1][j]:
				#	bt[i][j] = "DELETE"

	for i in range(0, lena+1):
		print D[i]
	
	#for j in range(0,lena+1):
	#	print bt[j]

	return D[lena][lenb]

texta = "happy"
textb = "polla"
D = edit_distance(texta, textb, len(texta), len(textb))
#backtrace(D)			
