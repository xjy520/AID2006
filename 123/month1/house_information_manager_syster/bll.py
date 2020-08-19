"""
    业务逻辑层
"""
from dal import HouseDao
class HouseManagerController:
    def __init__(self):
        self.list_houses = HouseDao.load()

    # @staticmethod
    # def fand_all():
    # def