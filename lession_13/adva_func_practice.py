'''1. Nhập thông tin cho n chiếc xe ô tô, danh sách ô tô lưu vào trong list. Sử dụng
hàm filter để lọc ra các ô tô có màu đen và năm sản xuất kể từ 2015 đến nay.
Thông tin ô tô bao gồm: Mã, Nhãn hiệu, Dòng xe, Màu sắc (sử dụng kiểu int
để lưu trữ: 1-đen, 2-trắng, 3-đỏ, 4-xanh nước biển), Năm sản xuất.

2. Từ câu 1, hiển thị danh sách ô tô, sử dụng hàm map để chuyển đổi Màu sắc từ
dạng số sang dạng văn bản. VD: ‘3’ chuyển thành ‘đỏ’.'''
print('============================================================================================')
class Car():
    def __init__(self, id_car, brand_car, type_car, color_car, year_prod_car):
        self.id_car = id_car
        self.brand_car = brand_car
        self.type_car = type_car
        self.color_car = color_car
        self.year_prod_car = year_prod_car

    # get info
    def get_info_cars():
        cars = []      
        total_car = int(input('Enter how many cars: '))
        print()
        for i in range(total_car):
            print('Enter info car ',i+1)
            id_car = int(input('ID Car: '))
            brand_car = input('Brand Car: ')
            type_car = input('Type Car: ')
            color_car = strings_to_numbers(str(input('Color Car (1-black, 2-white, 3-red, 4-blue): ')))
            year_prod_car = int(input('Year Product Car: '))
            car = Car(id_car, brand_car, type_car, color_car, year_prod_car)
            cars.append(car)
            print('-----------------')
        return cars

    def fomat_list_of_list(cars):
        info_cars = []
        for i in range(len(cars)):
            info_car = []
            info_car.append(cars[i].id_car)
            info_car.append(cars[i].brand_car)
            info_car.append(cars[i].type_car)
            info_car.append(cars[i].color_car)
            info_car.append(cars[i].year_prod_car)
            info_cars.append(info_car)
        print('--------List fomat---------')
        print(info_cars)
        print('-----------------')
        return info_cars

    def conv_list_to_json(cars):
        info_cars = []
        for i in range(len(cars)):
            info_car = dict()
            info_car['id_car'] = cars[i].id_car
            info_car['brand_car'] = cars[i].id_car
            info_car['type_car'] = cars[i].id_car
            info_car['color_car'] = cars[i].id_car
            info_car['year_prod_car'] = cars[i].id_car
            info_cars.append(info_car)
        print('------json fomat-------')
        print(info_cars)
        print('-----------------')

    def display_info_cars_filter(info_cars):
        for i in range(len(info_cars)):
            # print(info_cars[i])
            resu = filter(lambda x: x[3] == 'black' and x[4] >= 2015, info_cars)
        print(list(resu))

    def display_info_cars_map(info_cars):
        for i in range(len(info_cars)):
            resu = map(lambda x: [x[0], x[1], x[2], numbers_to_strings(x[3]), x[4]], info_cars)
        print(list(resu))

# conver numbers <=> strings function
def numbers_to_strings(argument):
    switcher = {
        1: "black",
        2: "white",
        3: "red",
        4: "blue",
    }
    return switcher.get(argument, "nothing")

def strings_to_numbers(argument):
    switcher = {
        "black": 1,
        "white": 2,
        "red": 3,
        "blue": 4,
    }
    return switcher.get(argument, "nothing")


def main():
    obj_car = Car
    obj_1 = obj_car.get_info_cars()
    obj_2 = obj_car.fomat_list_of_list(obj_1)
    obj_car.conv_list_to_json(obj_1)

    # obj_car.display_info_cars_filter(obj_2)
    obj_car.display_info_cars_map(obj_2)

main()