#Q1 一行代码实现1--100之和
print("Q1: sum of 1 to 100 = ", sum(range(1,100)))

#Q2: 如何在一个函数内部修改全局变量
a = 5
def fn1():
    global a
    a = 4
fn1()
print("Q2: modifying global var: ", a)

#Q4: 字典如何删除键和合并两个字典
dic = {"name":"sc", "age":19}
del dic["name"]
print("Q4: delete key from dict: ", dic)

dic2 = {"name":"yc"}
dic.update(dic2)
print("Q4: combine key to dict: ", dic)

#Q6: python实现列表去重的方法
listA = [11,12,12, 13, 12, 16, 15, 16, 13]
a=set(listA)
print("Q6: deduplicate listA to set: ", a)
listB = list(a)
print("Q6: convert set to list: ", listB)
