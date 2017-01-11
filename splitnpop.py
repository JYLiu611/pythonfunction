# -- coding: UTF-8 -- 
#shenmegui
data=open("C:\Users\ljy\pythonfunction\splitnpop.txt").read()
print data#
print data.split()#默认空格分割
print data.split(',')[0].split()#，分割取前部空格分割
print data.split(' ',1)#空格分隔一次
s=data.split()
print s.pop(0)#提取第一个展示
print s.pop(1)#提取第二个（原第三个）
print s.pop(-1)#提取最后一个