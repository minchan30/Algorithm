import sys

A , B , C = map(int , sys.stdin.readline().split())

if A == B == C:
    print(10000 + A * 1000)
elif A == B: 
    print(1000 + A * 100)
elif B == C:
     print(1000 + B * 100)
elif A == C:
     print(1000 + C * 100)
else:
    if A > B and A > C:
        print(A * 100)
    elif B > A and B > C:
        print(B * 100)
    elif C > A and C > B:
        print(C * 100)