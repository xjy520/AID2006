"""
    可迭代对象工具模块
    价值1 :
        自定义高阶函数类,功能比内置高阶函数多的多
    价值2 :
        真正领悟函数式编程思想:
            分
            隔
            做
    价值3 :
        面试吹牛 : 精通函数式编程
            步骤:
                1.根据需求实现功能
                2.将所有变化点定义为函数
                3.用参数隔离变化
                4.调用通用函数
                5.将通用代码定义到IterableHelper类
                6.用lambda代替变化点
            源于微软Linq框架
    编程范式
        面向过程 : 考虑实现步骤
        面向对象 : 考虑实现的人(软件架构)
        函数式 : 将函数作为参数传递(功能)
"""