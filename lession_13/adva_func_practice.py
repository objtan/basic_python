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

    def get_color_car(self):
        return self.color_car

    # def display_info_car(self):
    #     return f'ID Car: {self.type_car} \nBrand Car: {self.brand_car} \nType Car: {self.type_car} \nColor Car: {self.color_car} \nYear Product Car: {self.year_prod_car}'
    # print('ID Car: ', car.id_car)
    # print('Brand Car: ', car.brand_car)
    # print('Type Car: ', car.type_car)
    # print('Color Car: ', car.color_car)
    # print('Year Product Car: ', car.year_prod_car)

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
        color_car = int(input('Color Car (1-black, 2-white, 3-red, 4-blue): '))
        year_prod_car = int(input('Year Product Car: '))
        car = Car(id_car, brand_car, type_car, color_car, year_prod_car)
        cars.append(car)
        print('-----------------')
    return cars

def display_info_car(car):
        print(f'ID Car: {car.id_car} \nBrand Car: {car.brand_car} \nType Car: {car.type_car} \nColor Car: {car.color_car} \nYear Product Car: {car.year_prod_car}')

def display_info_cars_filter(cars):
    resu = list(filter(lambda x: x.color_car == 1 and x.year_prod_car >= 2015, cars))
    print('Display Info Cars Filter')
    for i in range(len(resu)):
        print(resu[i])
        display_info_car(resu[i])
    print('-------------------')
    # for car in resu:
    #     print(car.display_info_car())
    # for i in range(len(resu)):
    #     print(resu[i])
    print('------------------------')

def display_info_cars_map(cars):
    # for i in range(len(cars)):
        # print(cars[i].color_car)
    resu = list(map(lambda x: numbers_to_strings(x.color_car), cars))
    print(resu)
    for i in range(len(resu)):
        print(resu[i])
        # resu = list(map(lambda x: [x.id_car, x.brand_car, x.type_car, numbers_to_strings(x.color_car), x.year_prod_car], cars))
    # for i, v in enumerate(resu):
    #     for car in range(len(v)):
    #         print(v[car])
            # display_info_car(v[car])
    print('-------------------')

# conver numbers <=> strings function
# def strings_to_numbers(argument):
#     switcher = {
#         "black": 1,
#         "white": 2,
#         "red": 3,
#         "blue": 4,
#     }
#     return switcher.get(argument, "nothing")

def numbers_to_strings(argument):
    switcher = {
        1: "1-black",
        2: "2-white",
        3: "3-red",
        4: "4-blue",
    }   
    return switcher.get(argument, "nothing")


def main():
    # obj_car = Car()
    obj_1 = get_info_cars()
    # obj_2 = obj_car.fomat_list_of_list(obj_1)
    # obj_car.conv_list_to_json(obj_1)

    # numbers_to_strings(obj_1.color_car)
    display_info_cars_filter(obj_1)
    display_info_cars_map(obj_1)

main()