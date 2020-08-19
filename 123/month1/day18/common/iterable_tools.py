class IterableHelper:
    """
        集成操作框架(可迭代对象助手类)
    """
    # 静态方法:表达一种工具,不能(需要)操作对象或类成员
    # 使用方式:类.静态方法名()
    @staticmethod
    def find_all(iterable, func_condition):
        """
            在可迭代对象中根据条件查找满足的元素
        :param iterable: 可迭代对象
        :param func_condition: 查找条件
        :return: 生成器,推算满足条件的元素
        """
        for item in iterable:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(iterable,func_condition):
        for item in iterable:
            if func_condition(item):
                return item

    @staticmethod
    def find_all_phone(iterable,condition):
        for item in iterable:
            yield condition(item)

    @staticmethod
    def delete(iterable,condition):
        for i in range(len(iterable)-1,-1,-1):
            if condition(iterable[i]):
                iterable.remove(iterable[i])

    @staticmethod
    def find_max(iterable,condition):
        max = iterable[0]
        for i in range(1,len(iterable)):
            if condition(max) < condition(iterable[i]):
                max = iterable[i]
        return max

    @staticmethod
    def count(iterable,condition):
        count = 0
        for item in iterable:
            if condition(item):
                count+=1
        return count

    @staticmethod
    def verdict(iterable,condition):
        for item in iterable:
            if condition(item):
                return True
        return False

    @staticmethod
    def sort(iterable,condition):
        for i in range(0,len(iterable)-1):
            for c in range(i+1,len(iterable)):
                if condition(iterable[i]) > condition(iterable[c]):
                    iterable[i],iterable[c] = iterable[c],iterable[i]



