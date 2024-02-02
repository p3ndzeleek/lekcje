a = input()
b = input()
X, Y = list(a), list(b)
X.sort()
Y.sort()
a ="".join(X)
b ="".join(Y)
print(a,b)
if a == b:
    print("tak")
else:
    print("nie")