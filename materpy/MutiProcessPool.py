import multiprocessing as mul

def f(x):
    return x**2

if __name__ == '__main__':
    pool = mul.Pool(5)
    rel  = pool.map(f,[1,2,3,4,5,6,7,8,9,10])
    print(rel)

#apply_async(func,args)  从进程池中取出一个进程执行func，args为func的参数。它将返回一个AsyncResult的对象，你可以对该对象调用get()方法以获得结果。
#close()  进程池不再创建新的进程
#join()   wait进程池中的全部进程。必须对Pool先调用close()方法才能join。