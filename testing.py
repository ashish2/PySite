# from tagging.fields import *

# Enter your code here. Read input from STDIN. Print output to STDOUT

# from collections import Counter, defaultdict
# N = int( raw_input() )
# if N >= 3 and N <= 2500:
#     li = raw_input().split()
#     li = map(int, li)
#     diff = []
#     for i in li:
#         try:
#             nmbr = li[li.index(i)+1] - li[li.index(i)]
#             diff.append(nmbr)
#         except Exception, e:
#             pass

#     d = defaultdict(int)
#     for i in diff:
#         d[i] += 1
#     mx = max(d.iteritems(), key = lambda x: x[1] )
#     mn = min(d.iteritems(), key = lambda x: x[1] )
#     print li[diff.index(mn[0])] + mx[0]



# ==============================================

# 5 4 4 2 2 8

# N = input()
# num = map(int, raw_input().split())

# N = 6
# num = [1,1,1,5,4,4,2,2,8,8]

# val = [0]*11
# for i in num:
#     val[i] += 1

# print val
# counter = 0
# val = val[::-1]
# print val

# ans = []
# for i in val:
#     if i > 0:
#         counter += i
#         ans.append(counter)
#         # print ans

# print ans
# ans = ans[::-1]
# print ans


# ==============================================


# N = int(raw_input() )
# s = ''
# s = [ raw_input() for i in range(0, int(raw_input() )) ]
# s = ['abcdde', 'baccd', 'eeabg']
# se = set(s[0])
# for i in s: se = se.intersection(i)
# print se.__len__()
# f = lambda x: x in s[0]
# print map(se.intersection, s)
# print filter(se.intersection, s)
# print map(f, s)
# print filter( lambda x: x in s[1] , s)


# s = ['abcdde', 'baccd', 'eeabg']
# f = lambda x: x in s[0]
# print f(s, s)
# print map(f, s)


# s = [ raw_input() for i in range(0, int(raw_input() )) ]
# se = set(s[0])
# for i in s: se = se.intersection(i)
# print len(se)
# abcdde
# baccd
# eeabg

# ==============================================

# s = "The quick brown fox jumps over the lazy dog"
# print 'a' and 'z' and 'c' in s




# s = str(raw_input())
# s = "We promptly judged antique ivory buckles for the prize"
# s = "We promptly judged antique ivory buckles for the next prize"

# if len(s) <= pow(10, 3):

#     if "a" in s and "b" in s and "c" in s and "d" in s and "e" in s and "f" in s and "g" in s and "h" in s and "i" in s and "j" in s and "k" in s and "l" in s and "m" in s and "n" in s and "o" in s and "p" in s and "q" in s and "r" in s and "s" in s and "t" in s and "u" in s and "v" in s and "w" in s and "x" in s and "y" in s and "z" in s:
#         print "pangram"
#     else:
#         print "not pangram"



# ==============================================

s="aaab"

N = int( raw_input() )
for i in xrange(N):
	s = raw_input()
	if s != s[::-1]:
		d = {}
		for i in s: 
			d.update({i: int( d.get(i) or 0)+1})
		for i in d:
			if d[i] == 1:
				vr = i
		ss = s.replace(vr, '')
		if ss == ss[::-1]:
			print s.index(vr)
	else:
		print -1



