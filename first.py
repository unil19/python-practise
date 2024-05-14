# python 基础练习
# r不转义
import functools
from functools import reduce

rn = r'\n'

# '''可换行字符串
ddd = '''hello
world'''

# 格式化输出
fm = "hello,%s,your score is %.2f"
ns = fm % ("xiao ming", 98)
fmkh = "hello,{0}, your score is {1:.2f}".format("xiao ming", 98)

# list
classmates = ["liu", "wang", "zhang"]
classmates.append("xu")
classmates.insert(1, "zheng")
classmates.pop()

# tuple 不可变数组
classtuple = ("liu", "wang", "zhang")

# if elif else判断

# for in 循环
for student in classtuple:
    student += "s"

# range
sum = 0
for x in range(101):
    sum += x

# dict字典 key是不可变对象:整数、字符串、tuple
scores = {"zhangsan": 95, "wang": 97, "li": 87}
wangScore = scores.get("wang")
liScore = scores["li"]
scores["xu"] = 87
scores[classtuple] = 77

# set
firstSet = set([1, 2, 1, 1, 1])
secondSet = set([2, 3, 4, 23, 3, 4, 5])
andSet = firstSet & secondSet
orSet = firstSet | secondSet


# print(andSet)
# print(orSet)

# 对于不变对象(整除、浮点数、字符串、布尔值)来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的

# 函数定义def
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type for my_abs")
    if x > 0:
        return x
    else:
        return -x


# 多个返回值时返回tuple
def return_many():
    return 13, 14


x, y = return_many()


# 默认参数
def my_pow(x, n=2):
    result = 1
    for i in range(n):
        result = result * x
    return result


# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# 可变参数 参数前加*
def pow_sum(*numbers):
    sum = 0
    for number in numbers:
        sum += number * number
    return sum


sumSingle = pow_sum(1, 2, 3)
sumList = pow_sum(*[1, 2, 3])


# 关键字参数 **kw
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def register(name, **other):
    print("name:", name, "other:", other)


liuwh_other = {"height": 180, "age": 18}


# 命名关键字参数,命名关键字参数无缺省值时比传
def user_info(name, *, age):
    print("name:", name, "age:", age)


# user_info("liu", age=18)
# 位置参数调用时也可以使用关键字参数的调用方法
# user_info(name="liu", age=18)

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。

# 递归函数
def fact(n=1):
    if not isinstance(n, int):
        raise TypeError("method fact need int param")
    if n < 0:
        raise TypeError("method fact need must bigger or equal 0")
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


# 切片操作
yh = ["yue", "hua", "gong", "si"]
list100 = list(range(100))
yhstr = "yueHuaGongSi"
# print(list100[-1::-5])

# 迭代
todayWater = {"branch": "nongfushanquan", "volume": "550ml", "ph": "7.3"}
for key, value in todayWater.items():
    # print(key, value)
    pass

for i, value in enumerate(yh):
    # print(i, value)
    pass

# 列表生成式
wiley = list(range(0, 10))
wileyf = [x * x for x in range(0, 10) if x % 2 == 0]

# 双层循环 x在外层,y在内层
wileyd = [x + y for x in "ABC" for y in "123"]

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
gxf = (x * x for x in range(10))
for i in gxf:
    pass
    # print(i)


# 斐波那契函数的生成器
def fib(length):
    index, prev, current = 0, 0, 1
    while (index < length):
        yield current
        prev, current = current, prev + current
        index += 1


# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

# 杨辉三角
def triangles():
    currentArr = [1]
    length = 1
    while True:
        yield currentArr
        nextArr = []
        for index in range(length + 1):
            if index == 0:
                nextArr.append(1)
            elif index == length:
                nextArr.append(1)
            else:
                nextArr.append(currentArr[index - 1] + currentArr[index])
        currentArr = nextArr
        length += 1


count = 0
for arr in triangles():
    if count < 10:
        print(arr)
        count += 1
    else:
        break


# 可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

# mapReduce
def normalize(name):
    return name.upper()[0:1] + name.lower()[1:]


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def muti(x, y):
        return x * y

    return reduce(muti, L)


if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):
    zeroIndex = s.find(".")
    if zeroIndex == -1:
        return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], s))
    else:
        sn = s.replace(".", "")
        le = len(sn)
        return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], sn)) / pow(10, le) * pow(10, zeroIndex)


# map/filter回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

# 排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[1]


L2 = sorted(L, key=by_name)


# 装饰器 本质上，decorator就是一个返回函数的高阶函数

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s()" % func.__name__)
        return func(*args, **kw)

    return wrapper


def paramLog(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper
    return decorator


@paramLog("excute")
def sayHi():
    print("hi")


#偏函数
int2 = functools.partial(int, base=2)

#_abc为私有变量
