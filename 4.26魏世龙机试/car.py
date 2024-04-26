class Car:
    def __init__(self, brand="", color="", model="", price=0):
        self.brand = brand
        self.color = color
        self.model = model
        self.price = price
        self.is_running = False
        self.is_flying = False
        self.is_burrowing = False
        self.is_drifting = False

    def display_info(self):
        print(f"品牌：{self.brand}")
        print(f"颜色：{self.color}")
        print(f"型号：{self.model}")
        print(f"价格：{self.price}")
        print(f"-------------------")

    def start(self):
        choice = input(f"是否启动{self.brand}汽车？(yes/no): ")
        if choice.lower() == 'yes':
            self.is_running = True
            print(f"{self.brand}汽车启动")
            self.drive()
        else:
            print(f"{self.brand}汽车未启动")

    def stop(self):
        choice = input(f"是否停止{self.brand}汽车？(yes/no): ")
        if choice.lower() == 'yes':
            self.is_running = False
            print(f"{self.brand}汽车停止")
        else:
            print(f"{self.brand}汽车继续行驶")

    def drive(self):
        while self.is_running:
            print(f"{self.brand}汽车行驶中...")
            choice = input("是否继续行驶？(yes/no): ")
            if choice.lower() == 'no':
                self.stop()
                break

    def show_menu(self):
        choice = input("是否为您展示菜单？(yes/no): ")
        if choice.lower() == 'yes':
            print("菜单：")
            print("1. 飞天")
            print("2. 遁地")
            print("3. 飘逸")
            option = input("请选择菜单选项：")
            if option == '1':
                self.fly()
            elif option == '2':
                self.burrow()
            elif option == '3':
                self.drift()
            else:
                print("无效选项")

    def fly(self):
        choice = input(f"是否开启{self.brand}汽车的飞行模式？(yes/no): ")
        if choice.lower() == 'yes':
            self.is_flying = True
            print(f"{self.brand}汽车飞行中...")
        else:
            print(f"{self.brand}汽车取消飞行模式")
            self.is_flying = False

    def burrow(self):
        choice = input(f"是否开启{self.brand}汽车的遁地模式？(yes/no): ")
        if choice.lower() == 'yes':
            self.is_burrowing = True
            print(f"{self.brand}汽车遁地中...")
        else:
            print(f"{self.brand}汽车取消遁地模式")
            self.is_burrowing = False

    def drift(self):
        choice = input(f"是否开启{self.brand}汽车的飘逸模式？(yes/no): ")
        if choice.lower() == 'yes':
            self.is_drifting = True
            print(f"{self.brand}汽车飘逸中...")
        else:
            print(f"{self.brand}汽车取消飘逸模式")
            self.is_drifting = False


class User:
    def __init__(self):
        self.username = input('请输入用户名：')
        self.sex = input('请输入性别：')
        self.age = input('请输入年龄：')
        self.phone = input('请输入手机号：')
        self.money = 400000
        self.cars = []

    def display_info(self):
        print(f"用户名：{self.username}")
        print(f"性别：{self.sex}")
        print(f"年龄：{self.age}")
        print(f"手机号：{self.phone}")
        print(f"当前余额：{self.money}元")
        print(f"-------------------")

    def buy_car(self, car):
        if self.money >= car.price:
            self.money -= car.price
            self.cars.append(car)
            print(
                f"恭喜超级无敌牛杯克拉斯的{self.username}用户高抬贵手的购买了一辆{car.brand}的汽车，当前余额为{self.money}元")
            car.start()
            car.show_menu()
        else:
            print("余额不足，请努力赚钱后再来购买汽车！")

    def display_car_history(self):
        if self.cars:
            print(f"{self.username}的购车历史：")
            for car in self.cars:
                print(f"{car.brand}{car.color} {car.model} 价格：{car.price}元")
        else:
            print("暂无购车记录")


# 创建汽车对象
brand = input('请输入品牌：')
color = input('请输入颜色：')
model = input('请输入型号：')
price = float(input('请输入价格：'))
car1 = Car(brand, color, model, price)

# 创建用户对象
user1 = User()

# 显示用户信息
user1.display_info()

# 购买汽车
user1.buy_car(car1)
