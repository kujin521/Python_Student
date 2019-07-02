# @Time :2019/6/29 0029 10:10
# @Author:库金
# 序列解包
q=1,34,4
print(q[1])

def student_info(name,age=18,sex='男',stuname='丰阳完小'):
    print('我的姓名：'+name)
    print('我的年龄：'+str(age))
    print('我的性别：'+sex)
    print('我的学校：'+stuname)

student_info('库津')
print('~~~~~~~~~~~~~~')
student_info('库津',stuname='德州职业学院')




