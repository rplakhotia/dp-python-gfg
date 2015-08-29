
# Python Implementation for Longest Common Subsequence problem from geeksforgeeks.org
seq_one = "ABCDGHHH"
seq_two = "AEDFHRHH"

def get_longest_common_subsequence(seq_one, seq_two):
   len_seq_one = len(seq_one)
   len_seq_two = len(seq_two)
   LCS = [[0 for x in range(len_seq_one+1)] for y in range(len_seq_two+1)]

   for i in range(0, len_seq_one+1):
      for j in range(0,len_seq_two+1):
         if i ==0 or j ==0:
            LCS[i][j] = 0
         elif seq_one[i-1] == seq_two[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
         else:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])

   return LCS[len_seq_one][len_seq_two]

print (get_log_common_subseq(seq_one,seq_two)) 
