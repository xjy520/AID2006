"""
    参数:使用功能时给制作功能传递的信息
    制作
            def 函数名(参数1,参数2):
                函数体
    使用
            函数名(数据1,数据2)

"""
from pyecharts.charts import Bar
#创建柱状图
bar=Bar()
#向X轴添加信息
bar.add_xaxis([])
#向y轴添加信息
bar.add_yaxis("",[])
#渲染
bar.render()