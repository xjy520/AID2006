"""
    在插入和删除数据功能上,增加验证权限
    使用装饰器实现
    通过调试体会拦截的作用
"""
def add(func):

    def verif_permissions(*args,**kwargs):
        print("验证权限")
        return func(*args,**kwargs)
    return verif_permissions

@add
def insert(data):
    print("插入数据")
    return "ok"
@add
def delete(id):
    print("删除数据")
    return "no"


print(insert("新数据"))
print(delete(1001))


"""
    装饰器细节
"""