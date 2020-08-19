import dal
from bll import HouseManagerController

class HouseView:
    def __init__(self):
        self.controller = HouseManagerController()

    def dispaly(self):
        print("1)显示所有房源信息")

    def select(self):
        item = input("")
        if item == "1":
            self.show_house(self.controller)

    def show_house(self, house):
        print("%d|%s|%s|%s+|%s|%s|%s|%s|%d|%d|%s" % (
            house.id, house.title, house.community, house.years, house.house_type, house.area, house.floor,
            house.description, house.total_price, house.unit_price, house.follow_info))


  
    def main(self):
        while True:
            self.dispaly()
            self.select()

