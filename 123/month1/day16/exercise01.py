"""
    异常处理
        不是解决语法错误
        是运行时的逻辑错误(某些数据超过范围)
        现象:不在向下运行,不断向上返回
        处理目的:将异常现象改为正常现象(向下执行)
"""
# # 写法1:
# try:
#     ...
# except:
#     ...
#
# # 写法2:
# try:
#     ...
# except 错误类型:
#     ...
#
# # 写法3:
# try:
#     ...
# finally: #无论对错,最终一定执行
#     ...

def get_score():
    while True:
        try:
            score = float(input("请输入成绩:"))
            return score
        except:
            print("输入有误")

result=get_score()
print("成绩是",result)
