def maxi(x):
	incl=0
	excl=0
	for i in x:
		n_excl=excl if excl>incl else incl
		incl=excl+i
		excl=n_excl
	return max(excl,incl)
n=int(input())
l=list(map(int,input().split()))
h=maxi(l)
print(h)
