#v, X=10, XV=15, L=50, C=100, D=500, M=1000
def f1(n):
    R={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    I=0
    if len(n)==1:
        return R[n]
    else:
        for i in range(len(n)-1):
            if R[n[i]]<R[n[i+1]]:
                I-=R[n[i]]
            else:
                I+=R[n[i]]
        return I+R[n[-1]]
x=input("Enter Roman numeral: ")
print("Equivalent Integer value :",f1(x))