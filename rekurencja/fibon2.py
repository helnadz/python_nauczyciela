def f(n, fn_2=0,fn_1=1):
    if n==0:
        return fn_2
    elif n==1:
        return fn_1
    else:
        return f(n-1,fn_1,fn_2+fn_1)
if __name__ == '__main__':
        print(f(10))

