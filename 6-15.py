class llstring(str):
	def levenstein_distance(self, s2):
		s1 = self.__str__()
		l = [[0] * (len(s2)+1) for i in range(len(s1)+1)]
		for i in range(len(s1)+1):
			l[i][0] = i
		for i in range(len(s2)+1):
			l[0][i] = i
		for i in range(1,len(s1)+1):
			for j in range(1,len(s2)+1):
				if s1[i-1] == s2[j-1]:
					repl = 0
				else:
					repl = 1
				l[i][j] = min(l[i-1][j-1]+repl,l[i-1][j]+1,l[i][j-1]+1)
		return l[len(s1)][len(s2)]
s = llstring("LUCK")
print(s.levenstein_distance("BUCK"))
