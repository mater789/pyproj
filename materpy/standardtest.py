#len(s)         返回： 序列中包含元素的个数
#min(s)         返回： 序列中最小的元素
#max(s)         返回： 序列中最大的元素
#all(s)         返回： True, 如果所有元素都为True的话
#any(s)         返回： True, 如果任一元素为True的话
#sum(s)         返回：序列中所有元素的和
#s.count(x)     返回： x在s中出现的次数
#s.index(x)     返回： x在s中第一次出现的下标

#l.extend(l2)        在表l的末尾添加表l2的所有元素
#l.append(x)         在l的末尾附加x元素
#l.sort()            对l中的元素排序
#l.reverse()         将l中的元素逆序
#l.pop()             返回：表l的最后一个元素，并在表l中删除该元素
#del l[i]            删除该元素

#str.count(sub)       返回：sub在str中出现的次数
#str.find(sub)        返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
#str.index(sub)       返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误
#str.rfind(sub)       返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
#str.rindex(sub)      返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误
#str.isalnum()        返回：True， 如果所有的字符都是字母或数字
#str.isalpha()        返回：True，如果所有的字符都是字母
#str.isdigit()        返回：True，如果所有的字符都是数字
#str.istitle()        返回：True，如果所有的词的首字母都是大写
#str.isspace()        返回：True，如果所有的字符都是空格
#str.islower()        返回：True，如果所有的字符都是小写字母
#str.isupper()        返回：True，如果所有的字符都是大写字母
#str.split([sep, [max]])    返回：从左开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.split(',')的方式使用逗号或者其它分割符
#str.rsplit([sep, [max]])   返回：从右开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.rsplit(',')的方式使用逗号或者其它分割符
#str.join(s)                返回：将s中的元素，以str为分割符，合并成为一个字符串。 ":".join("hello") -> h:e:l:l:o
#str.strip([sub])           返回：去掉字符串开头和结尾的空格。也可以提供参数sub，去掉位于字符串开头和结尾的sub
#str.replace(sub, new_sub)  返回：用一个新的字符串new_sub替换str中的sub
#str.capitalize()           返回：将str第一个字母大写
#str.lower()                返回：将str全部字母改为小写
#str.upper()                返回：将str全部字母改为大写
#str.swapcase()             返回：将str大写字母改为小写，小写改为大写
#str.title()                返回：将str的每个词(以空格分隔)的首字母大写
#str.center(width)          返回：长度为width的字符串，将原字符串放入该字符串中心，其它空余位置为空格。 'runoob'.center(20, '*')->'*******runoob*******'
#str.ljust(width)           返回：长度为width的字符串，将原字符串左对齐放入该字符串，其它空余位置为空格。'runoob'.ljust(20, '*')->'runoob**************'
#str.rjust(width)           返回：长度为width的字符串，将原字符串右对齐放入该字符串，其它空余位置为空格。'runoob'.ljust(20, '*')->'**************runoob'


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
#正则表达式
import re
m = re.search('[0-9]','a3bcd4ef')
print(m.group(0))
print(type(m))

m = re.search('[0-9]','a3bcd4ef')  # 搜索整个字符串，直到发现符合的子字符串。
print(m)
m = re.match('[0-9]','a3bcd4ef')   # 从头开始检查字符串是否符合正则表达式。必须从字符串的第一个字符开始就相符。
print(m)

str = re.sub('[0-9]', "v", 'a3bcd4ef')# 替换 在string中利用正则变换pattern进行搜索，对于搜索到的字符串，用另一字符串replacement替换。返回替换后的字符串。
print(str)

#re.split()    # 根据正则表达式分割字符串， 将分割后的所有子字符串放在一个表(list)中返回
#re.findall()  # 根据正则表达式搜索字符串，将所有符合的子字符串放在一给表(list)中返回

#单个字符:
#.          任意的一个字符
#a|b        字符a或字符b
#[afg]      a或者f或者g的一个字符
#[0-4]      0-4范围内的一个字符
#[a-f]      a-f范围内的一个字符
#[^m]       不是m的一个字符
#\s         一个空格
#\S         一个非空格
#\d         [0-9]
#\D         [^0-9]
#\w         [0-9a-zA-Z]
#\W         [^0-9a-zA-Z]

#重复 紧跟在单个字符之后，表示多个这样类似的字符
#*         重复 >=0 次
#+         重复 >=1 次
#?         重复 0或者1 次
#{m}       重复m次。比如说 a{4}相当于aaaa，再比如说[1-3]{2}相当于[1-3][1-3]
#{m, n}    重复m到n次。比如说a{2, 5}表示a重复2到5次。小于m次的重复，或者大于n次的重复都不符合条件。
#举例
#[0-9]{3,5}       9678
#a?b              b
#a+b              aaaaab

# 位置
#^         字符串的起始位置
#$         字符串的结尾位置
#例子
#^ab.*c$   相符abeec   不符cabeec (如果用re.search(), 将无法找到。)

#返回控制 群
m = re.search("output_(\d{4})", "output_1986.txt")#(\d{4})用括号()包围了一个小的正则表达式，\d{4}
print(m.group(0))
print(m.group(1))#group(0)是整个正则表达的搜索结果，group(1)是第一个群
#将群命名
m = re.search("output_(?P<year>\d{4})", "output_1986.txt")   #(?P<name>...) 为group命名
print(m.group("year"))


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
#日期和时间
import time
print(time.time())   # wall clock time, unit: second
print(time.clock())  # processor clock time, unit: second

print('start')
time.sleep(0.1)     # sleep for 0.1 seconds
print('wake up')

st = time.gmtime()      # 返回struct_time格式的UTC时间
print(st)
st = time.localtime()   # 返回struct_time格式的当地时间, 当地时区根据系统环境决定。
print(st)
s  = time.mktime(st)    # 将struct_time格式转换成wall clock time
print(s)

import datetime
t = datetime.datetime(2012,9,6,21,30)
print(t)
print(t.weekday())

t = datetime.datetime(2012,9,3,21,30)
t_next = datetime.datetime(2012,9,5,23,30)
delta1 = datetime.timedelta(seconds = 600)
delta2 = datetime.timedelta(weeks = 3)
print(t + delta1)
print(t + delta2)
print(t_next - t)
print(t > t_next)

format = "%Y-%m-%d-%H%M%S"
str = "1997-12-23-030000"
t = datetime.datetime.strptime(str, format)
print(t)

print(t_next.strftime(format))


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
#路径与文件
import os.path

path = 'D:\\PyProj\\materpy\\test1.txt'
print(os.path.basename(path))    # 查询路径中包含的文件名
print(os.path.dirname(path))     # 查询路径中包含的目录
info = os.path.split(path)       # 将路径分割成文件名和目录两个部分，放在一个表中返回
path2 = os.path.join('/', 'D:\\','PyProj', 'materpy', 'test2.txt')  # 使用目录名和文件名构成一个路径字符串
print(path2)
p_list = [path, path2]
print(os.path.commonprefix(p_list))    # 查询多个路径的共同部分'D:\\PyProj\\materpy\\test'
print(os.path.normpath('D:\\PyProj\\materpy\\..')) #去除冗余D:\\PyProj\\

print(os.path.exists(path))    # 查询文件是否存在
print(os.path.getsize(path))   # 查询文件大小
print(os.path.getatime(path))  # 查询文件上一次读取的时间
print(os.path.getmtime(path))  # 查询文件上一次修改的时间
print(os.path.isfile(path))    # 路径是否指向常规文件
print(os.path.isdir(path))     # 路径是否指向目录文件

import glob
print(glob.glob('D:\\PyProj\\materpy\\*'))#列出所有文件(函dir)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
os.makedirs('D:\\PyProj\\materpy\\testdir', 0o777, True)#exist_ok true
os.removedirs('D:\\PyProj\\materpy\\testdir')
print(os.listdir('D:\\PyProj\\materpy'))

path = 'D:\\PyProj\\materpy\\test1.txt'
#os.remove(path)txt', 'D:\\PyProj\\materpy\\test.txt')
#os.rename('D:\\PyProj\\materpy\\test2.
import stat
os.chmod(path, stat.S_IREAD)
os.chmod(path, stat.S_IWRITE)
print(os.stat(path))
print(os.getcwd()) #查询当前工作路径

import shutil
shutil.copy('test1.txt', 'test2.txt')
shutil.move('test2.txt', 'test3.txt')


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
#serial
import pickle

class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'
summer = Bird()   # construct an object
picklestring = pickle.dumps(summer)   # serialize object
print(picklestring)
print(type(picklestring))

fn  = 'a.pkl'
with open(fn, 'wb') as f:  # open file with write-mode
    picklestring = pickle.dump(summer, f)   # serialize and save object

with open(fn, 'rb') as f:
    summer = pickle.load(f)
    print(summer.way_of_reproduction)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
#subprocess 执行外部的命令和程序
import subprocess
out = subprocess.call("dir", shell=True)#sys de
print("sssssssss")

child = subprocess.Popen(["ping","-c","5","www.163.com"])#asys
print("parent process")

child = subprocess.Popen(["ping","-c","5","www.google.com"])
child.wait()#sys
print("parent process")
print(child.pid)
#child.poll()           # 检查子进程状态
#child.kill()           # 终止子进程
#child.send_signal()    # 向子进程发送信号
#child.terminate()      # 终止子进程

child1 = subprocess.Popen(["ping","-c","5","www.163.com"], stdout=subprocess.PIPE)#subprocess.PIPE实际上为文本流提供一个缓存区。child1的stdout将文本输出到缓存区
child2 = subprocess.Popen(["ping","-c","5","www.126.com"], stdin=child1.stdout,stdout=subprocess.PIPE)#child2的stdin从该PIPE中将文本读取走。child2的输出文本也被存放在PIPE中
out = child2.communicate()#直到communicate()方法从PIPE中读取出PIPE中的文本。该方法会阻塞父进程，直到子进程完成
print(out)

#child = subprocess.Popen(["python","matertest.py"], stdin=subprocess.PIPE)
#child.communicate("vamei") #我们启动子进程之后，cat会等待输入，直到我们用communicate()输入"vamei"。
#child.wait()


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
#signal linux专用 windows功能低
import signal
print(signal.SIGABRT)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
#thread
#threading.Semaphore对象: semaphore，也就是计数锁(semaphore传统意义上是一种进程间同步工具，见Linux进程间通信)。创建对象的时候，可以传递一个整数作为计数上限 (sema = threading.Semaphore(5))。它与Lock类似，也有Lock的两个方法。
#threading.Event对象: 与threading.Condition相类似，相当于没有潜在的Lock保护的condition variable。对象有True和False两个状态。可以多个线程使用wait()等待，直到某个线程调用该对象的set()方法，将对象设置为True。线程可以调用对象的clear()方法来重置对象为False状态。


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
#当前进程信息
import platform
print(platform.uname())#os包变成platform包
#umask() 设置该进程创建文件时的权限mask。
print(os.getpid())


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
#math

#math.e   # 自然常数e
#math.pi  # 圆周率pi
#math.ceil(x)       # 对x向上取整，比如x=1.2，返回2
#math.floor(x)      # 对x向下取整，比如x=1.2，返回1
#math.pow(x,y)      # 指数运算，得到x的y次方
#math.log(x)        # 对数，默认基底为e。可以使用base参数，来改变对数的基地。比如math.log(100,base=10)
#math.sqrt(x)       # 平方根
#三角函数: math.sin(x), math.cos(x), math.tan(x), math.asin(x), math.acos(x), math.atan(x)这些函数都接收一个弧度(radian)为单位的x作为参数。
#角度和弧度互换: math.degrees(x), math.radians(x)
#双曲函数: math.sinh(x), math.cosh(x), math.tanh(x), math.asinh(x), math.acosh(x), math.atanh(x)
#特殊函数： math.erf(x), math.gamma(x)

#random.seed(x) 来改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
#random.choice(seq)   # 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
#random.sample(seq,k) # 从序列中随机挑选k个元素
#random.shuffle(seq)  # 将序列的所有元素随机排序
#random.random()          # 随机生成下一个实数，它在[0,1)范围内。
#random.uniform(a,b)      # 随机生成下一个实数，它在[a,b]范围内。
#random.gauss(mu,sigma)    # 随机生成符合高斯分布的随机数，mu,sigma为高斯分布的两个参数。
#random.expovariate(lambd) # 随机生成符合指数分布的随机数，lambd为指数分布的参数。

import random
all_people = ['Tom', 'Vivian', 'Paul', 'Liya', 'Manu', 'Daniel', 'Shawn']
random.shuffle(all_people)
for i,name in enumerate(all_people):
    print(i,':'+name)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
#循环器 (itertools)
for i in iter([2, 4, 5, 6]):
    print(i)

import itertools
#count(5, 2)     #从5开始的整数循环器，每次增加2，即5, 7, 9, 11, 13, 15 ...
#cycle('abc')    #重复序列的元素，既a, b, c, a, b, c ...
#repeat(1.2)     #重复1.2，构成无穷循环器，即1.2, 1.2, 1.2, ...
#repeat(10, 5)   #重复10，共重复5次

rlt = itertools.starmap(pow, [(1, 1), (2, 2), (3, 3)])#1.4.27
for num in rlt:
    print(num)

rlt = itertools.filterfalse(lambda x: x > 5, [2, 3, 5, 6, 7])
for num in rlt:
    print(num)

rlt = itertools.takewhile(lambda x: x < 5, [1, 3, 6, 7, 1])#当函数返回True时，收集元素到循环器。一旦函数返回False，则停止。1, 3
for num in rlt:
    print(num)

rlt = itertools.dropwhile(lambda x: x < 5, [1, 3, 6, 7, 1])#当函数返回False时，跳过元素。一旦函数返回True，则开始收集剩下的所有元素到循环器。6, 7, 1
for num in rlt:
    print(num)

rlt = itertools.chain([1, 2, 3], [4, 5, 7])      # 连接两个循环器成为一个。1, 2, 3, 4, 5, 7
for num in rlt:
    print(num)

rlt = itertools.product('abc', [1, 2])   # 多个循环器集合的笛卡尔积。相当于嵌套循环
for m, n in rlt:
    print(m, n)

rlt = itertools.permutations('abc', 2)   # 从'abcd'中挑选两个元素，比如ab, bc, ... 将所有结果排序，返回为新的循环器。排列组合(有顺序的结果)
for num in rlt:
    print(num)

print("combinations")
rlt = itertools.combinations('abc', 2)    # 从'abcd'中挑选两个元素，比如ab, bc, ... 将所有结果排序，返回为新的循环器。排列组合(无顺序的结果)
for num in rlt:
    print(num)

print("combinations_with_replacement")
rlt = itertools.combinations_with_replacement('abc', 2)#排列组合(无顺序但可以相同即多了aa, bb, cc)
for num in rlt:
    print(num)

print("groupby")
def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"
friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
friends = sorted(friends, key = height_class)
for m, n in itertools.groupby(friends, key = height_class):
    print(m)
    print(list(n))

rlt = itertools.compress('ABCD', [1, 1, 1, 0])  # 根据[1, 1, 1, 0]的真假值情况，选择第一个参数'ABCD'中的元素。A, B, C
for num in rlt:
    print(num)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
#数据库 (sqlite3)
import sqlite3

# test.db is a file in the working directory.
conn = sqlite3.connect("test.db")
c = conn.cursor()
# create tables
c.execute('''CREATE TABLE IF NOT EXISTS category
      (id int primary key, sort int, name text)''')
c.execute('''CREATE TABLE IF NOT EXISTS book
      (id int primary key, 
       sort int, 
       name text, 
       price real, 
       category int,
       FOREIGN KEY (category) REFERENCES category(id))''')
# save the changes
conn.commit()
# close the connection with the database
conn.close()

#insert
try:
    conn = sqlite3.connect("test.db")
    c    = conn.cursor()
    books = [(1, 1, 'Cook Recipe', 3.12, 1),
                (2, 3, 'Python Intro', 17.5, 2),
                (3, 2, 'OS Intro', 13.6, 2),
               ]
    # execute "INSERT"
    c.execute("INSERT INTO category VALUES (1, 1, 'kitchen')")
    # using the placeholder
    c.execute("INSERT INTO category VALUES (?, ?, ?)", (2, 2, 'computer'))
    # execute multiple commands
    c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)
    conn.commit()
    conn.close()
except:
    print("have")

#select
conn = sqlite3.connect('test.db')
c = conn.cursor()
# retrieve one record
c.execute('SELECT name FROM category ORDER BY sort')
print(c.fetchone())
print(c.fetchone())
# retrieve all records as a list
c.execute('SELECT * FROM book WHERE book.category=1')
print(c.fetchall())
# iterate through the records
for row in c.execute('SELECT name, price FROM book ORDER BY sort'):
    print(row)

#update
conn = sqlite3.connect("test.db")
c = conn.cursor()
c.execute('UPDATE book SET price=? WHERE id=?',(1000, 1))
c.execute('DELETE FROM book WHERE id=2')
c.execute('DROP TABLE book')
conn.commit()
conn.close()

