def fun(n,name):
    if n>5:
        return 
    else:
        print(name)
        n+=1
    fun(n,name)

fun(0,"Venkat")