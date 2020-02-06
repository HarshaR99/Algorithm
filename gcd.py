def gcdEuclidAlgo(m,n) :
	if n==0 :
		return m;
	else :
		return gcdEuclidAlgo(n,m%n);

print("Enter two numbers for G.C.D calculation");
m = int(input("Enter first number : "));
n = int(input("Enter second number : "));
if m > n :
	res = gcdEuclidAlgo(m,n)
else :
	res = gcdEuclidAlgo(n,m)
print("G.C.D of "+str(m)+" and "+str(n)+" is "+str(res));
	
