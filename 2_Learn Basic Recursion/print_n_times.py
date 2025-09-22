def fun(n):
    if n>10: # Base conditon
        return  # Terminate the function
    else:
        print(n)
        n+=1
        fun(n)     # Function call itself

fun(1)