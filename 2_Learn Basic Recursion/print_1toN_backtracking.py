def fun_1_n(n):
    if n<1:
        return 
    else:
        fun_1_n(n-1)
        print(n)
    
fun_1_n(5)
def fun_n_1(i,n):
    if i>n:
        return
    else:
        fun_n_1(i+1,n)
        print(i)

# fun_n_1(1,5)