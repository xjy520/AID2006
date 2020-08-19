"""
    模块(文件)
        程序结构清晰
        利于多人开发
        快捷键 : 正确写出需要导入的成员
                alt + 回车 -->
"""
#   标记当前文件夹为根目录
#   在当前文件夹中右键 --> Mark Directory as --> sources

# 方式一
# 语法 : import 文件名
# 使用 : 文件名.成员


# 方式二
# 语法 : from 文件名 import 成员名      导单个 : from module01 import g01
# 使用 : 通过成员名调用                  导全部 : from module01 import *
# 本质 : 将成员导入到当前模块作用域中