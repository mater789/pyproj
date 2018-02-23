print("hello world")
x = 1
y = 2
z = x + y
print(z)
print(z, type(z))
a = True
print(a)
a = "sss"#可以不同类型赋值
print(a)



s1 = (2, 1.3, 'love', 5.6, 9, 12, False)# tuple元组不可变
print(s1,type(s1))
s2 = [True, 5, 'smile']#list可以变
print(s2,type(s2))
s3 = [1,[3,4,5]]
s4 = []
print(s1[0])
print(s2[2])
print(s3[1][2])
s2[1] = 3.0
s2[0] = "ss"#可以不同类型赋值
print(s2)

print(s1[:5])# 从开始到下标4 （下标5的元素 不包括在内）
print(s1[2:])# 从下标2到最后
print(s1[0:5:2])# 从下标0到下标4 (下标5不包括在内)，每隔2取一个元素 （下标为0，2，4的元素）
print(s1[2:0:-1])# 从下标2到下标1
print(s1[-1])# 序列最后一个元素
print(s1[-3])# 序列倒数第三个元素
print(s1[0:-1])#那么最后一个元素不会被引用

str = 'abcdef'#字符串是元组
print(str[2:4])

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(1+9)
print(1.3 - 4)
print(10%3)
print(3/2)#和c不一样这个地方是返回真实值
print(3**2)#pow

print(5==6)
print(5!=8)
print(4<5, 6>4)
print(5 in [1, 4, 5])#in
print(5 is 5)
print(5 is not 5)

#逻辑运算
print(True and True)
print(True or False)
print(not (True or False))

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#语句
i = 1
x = 1
if i > 0:
    x = x + 1
print(x)

i = -1
if i > 0:
    print("pos i")
    i = i + 1
elif i == 0:
    print("zero i")
    i = i*10;
else:
    print("neg i")
    i = i - 1
print("new i", i)

i = 5
if i > 1:
    print("bg 1")
    print("good")
    if i > 2:
        print("bg 2")

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

for a in [3, 4, "lei"]:
    print(a)

idx = list(range(5))#生成0-5的一个list
print(idx)

while i < 10:
    print(i)
    i = i + 1

for i in range(10):#range是一种数据类型不是list
    if i == 2:
        continue
    print(i)

for i in range(10):
    if i == 2:
        break
    print(i)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#函数
def square_sum(a, b):
    c = a**2 + b**2
    return c #Python的函数允许不返回值，也就是不用return,函数将自动返回None。None是Python中的一个特别的数据类型
    #return c,a #return可以返回多个值，以逗号分隔。相当于返回一个tuple(定值表)

print(square_sum(3,4))

#基本类型传值
a = 1
def change_integer(a):
    a = a + 1
    return a
print(change_integer(a))
print(a)
#list传地址
b = [1,2,3]
def change_list(b):
    b[0] = b[0] + 1
    return b
print(change_list(b))
print(b)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#oop
class Bird(object):
    have_feather = True
    way_of_reproduction = "egg"
    def move(self, dx, dy):#方法的第一个参数必须是self，无论是否用到(成员函数)
        position = [1, 1]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

summer = Bird()
print(summer.way_of_reproduction)
print('after move:',summer.move(5,8))#我们只传递了dx和dy两个参数，不需要传递self参数（因为self只是为了内部使用）

class Chicken(Bird):#继承
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

summer = Chicken()
print(summer.have_feather)
print(summer.move(5,8))


class Human(object):
    laugh = 'hahahaha'
    def show_laugh(self):
        print(self.laugh)
    def laugh_5th(self):
        for i in range(5):
            self.show_laugh()

li_lei = Human()
li_lei.laugh_5th()

class happyBird(Bird):
    def __init__(self,more_words):#相当于构造函数
        print('We are happy birds.',more_words)

summer = happyBird('Happy,Happy!')

class Human(object):
    def __init__(self, input_gender):
        #return None
        self.gender = input_gender #会自动创建这个成员
    def printGender(self):
        print(self.gender)

li_lei = Human('male')
print(li_lei.gender)
li_lei.printGender()

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(dir(list))
print(help(list))
nl = [1,2,5,3,5]
print(nl.count(5))#5的个数
print(nl.index(2))#第一个2的index
nl.append(6)
nl.sort()
print(nl.pop())
nl.remove(2)#去除第一个2
print(nl)
nl.insert(0,9)# 在下标为0的位置插入9
print(nl)

print([1,2,3] + [5,6,9])#123569

class superList(list):
    def __sub__(self, b):
        a = self[:]     # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象。
        #b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a
print(superList([1,2,3]) - [3,4])


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#词典
dic = {'tom':11, 'sam':57,'lily':100}
print(type(dic))
print(dic['tom'])
dic['tom'] = 30
print(dic['tom'])

print(dic)
dic = {}
print(dic)
dic['lilei'] = 99
print(dic)
dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
for key in dic:
    print(dic[key])

print(dic.keys())
print(dic.values())
print(dic.items())
hh = dic.items()
for hf in hh:
    print(hf)
print(hh)

del dic['tom']
print(dic)
print(len(dic))

dic = {12:11, 'sam':57,'lily':100}
for key in dic:
    print(type(key))


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#文本
f = open("test.txt","w")
f.write('I like apple\n')
f.write('I like apple萨达萨达')
f.close()

f = open("test.txt", "r")
line = f.readline()
print(type(line))
line = f.readline()
print(line)
f.seek(0)
line = f.readlines()
print(line)
f.close()


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#模块

print(__name__)
print(__package__)

from pack1.subpack1 import *
Forth.laugh4()
from pack2 import *
Third.laugh3()
import pack2.Third
pack2.Third.laugh3()
import pack1.subpack1.Forth
pack1.subpack1.Forth.laugh4()


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#传参 先位置，再关键字，再包裹位置，再包裹关键字
def f(a,b,c):
    return a+b+c
print(f(1,2,3))
print(f(c=3,b=2,a=1))#关键字a和函数形参a保持一致
print(f(1,c=3,b=2))#关键字传递可以和位置传递混用。但位置参数要出现在关键字参数之前：

def f(a,b,c=10):#默认参数
    return a+b+c
print(f(3,2))
print(f(3,2,1))

def func(*name):#name是包裹位置传递所用的元组名，在定义func时，在name前加*号
    print(type(name))
    print(name)
func(1,4,6)
func(5,6,7,1,2,3)

def func(**dict):#参数dict是包裹关键字传递所用的字典，在dict前加**。
    print(type(dict))
    print(dict)
func(a=1,b=9)
func(m=2,n=1,c=11)

def func(a,b,c):
    print(a,b,c)
args = [1,3,4]
func(*args)#解包裹成不同参数
dict = {'a':5,'c':2,'b':3}#关键字a和函数形参a保持一致
func(**dict)#解包裹成不同参数,dic以值为准


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#循环设计
S = 'abcdefghijk'
for i in range(0,len(S),2):#2是每次循环的步长,C语言中的for循环相类似了
    print(S[i])

S = 'abcdefghijk'
for (a,b) in enumerate(S):#可以在每次循环中同时得到下标和元素
    print(a)
    print(b)

ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):#如果你多个等长的序列，然后想要每次循环时从各个序列分别取出一个元素，可以利用zip()方便地实现
    print(a,b,c)

ta = [1,2,3]
tb = [9,8,7]
zipped = zip(ta,tb)# cluster压缩成zipobj
print(zipped)
na, nb = zip(*zipped)# decompose解压成tuple
print(na, nb)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#循环对象
for line in open('test1.txt'):
    print(line)

def gen():#只是在return的地方改为yield。生成器中可以有多个yield。当生成器遇到一个yield时，会暂停运行生成器，返回yield后面的值。当再次调用生成器的时候，会从刚才暂停的地方继续运行，直到下一个yield
    a = 100
    yield a
    a = a*8
    yield a
    yield 1000
for i in gen():
    print(i)

def gen():#生成器的编写方法和函数定义类似
    for i in range(4):
        yield i
for i in gen():
    print(i)

G = (x for x in range(4))#成生成器表达式(Generator Expression),可查阅相关资料
for i in G:
    print(i)

L = []
for x in range(10):
    L.append(x**2)
#表推导(list comprehension) 处理
L = [x**2 for x in range(10)]#这与生成器表达式类似，只不过用的是中括号。

xl = [1,3,5]
yl = [9,12,13]
L  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]
print(L)
#同
L = []
for (x,y) in zip(xl,yl):
    if y > 10:
        L.append(x**2)
print(L)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#函数对象
func = lambda x,y: x + y
print(func(3,4))
print(type(func))
#同
def func(x, y):
    return x + y

def test(f, a, b):#函数可以作为一个对象，进行参数传递
    print('test')
    print(f(a, b))
test(func, 3, 5)
test((lambda x,y: x**2 + y), 6, 9)

re = map((lambda x: x+3),[1,3,5,6])#map()的功能是将函数对象依次作用于表的每一个元素
print(type(re))
re = map((lambda x,y: x+y),[1,2,3],[6,7,9])
for e in re:
    print(e)

def func(a):
    if a > 100:
        return True
    else:
        return False
fr = filter(func,[10,56,101,500])#如果函数对象返回的是True，则该次的元素被储存于返回的表中,用于过滤
print(fr)
for e in fr:
    print(e)

import functools
re = functools.reduce((lambda x,y: x+y),[1,2,5,7,9])#相当于(((1+2)+5)+7)+9
print(re)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#异常
re = iter(range(5))
print(type(re))
#for i in range(100):
#    print(re.__next__())#异常
print("HaHaHaHa")

re = iter(range(5))
try:
    for i in range(100):
        print(re.__next__())
except StopIteration:
    print('here is end ',i)
print('HaHaHaHa')

try:
    print(a*2)
except TypeError:
    print("TypeError")
except:#如果except后面没有任何参数，那么表示所有的exception都交给这段程序处理
    print("Not Type Error & Error noted")

def test_func():
    try:
        m = 1/0
    except NameError:
        print("Catch NameError in the sub-function")
try:
    test_func()
except ZeroDivisionError:
    print("Catch error in the main program")
finally:#是无论是否有异常，最后都要做的一些事情
    print("ssss")

try:
    print('Lalala')
    raise StopIteration#抛出异常
    print('Hahaha')
except:
    print("ex")


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#动态类型
#对象不再有引用指向它。Python会自动将没有引用指向的对象销毁(destruct)，释放相应内存
#(对于小的整数和短字符串，Python会缓存这些对象，而不是频繁的建立和销毁。)
a = 5
b = a
a = a + 2#指向了新对象
L1 = [1,2,3]
L2 = L1
L1 = 1#指向了新对象

L1 = [1,2,3]
L2 = L1
L1[0] = 10#L1[0] = 10这一赋值操作，并不是改变L1的指向，而是对L1[0]
print(L2)
#列表词典可以通过引用其元素，改变对象自身(in-place change)。这种对象类型，称为可变数据对象(mutable object)
#数字和字符串，不能改变对象本身，只能改变引用的指向，称为不可变数据对象(immutable object)

#函数的参数传递，本质上传递的是引用
def f(x):
    x = 100#对参数x的操作不会影响引用,类似于C语言中的值传递
    print(x)
a = 1
f(a)
print(a)

def f(x):
    x[0] = 100#没有改变x和x[0]的关联,所以这个可以看作传引用
    print(x)
a = [1,2,3]
f(a)
print(a)

