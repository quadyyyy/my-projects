n = int(input()) 
h = str(n % 86400 // 3600) 

m1 = str(n % 3600 // 60 // 10) 

m2 = str(n % 3600 // 60 % 10)

s1 = str(n % 60 // 10) 

s2 = str(n % 10) 

print(h + ':' + m1 + m2 + ':' + s1 + s2)