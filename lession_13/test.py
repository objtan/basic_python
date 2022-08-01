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

def get_info_car():
    car = Car(
            int(input('ID Car: ')),
            input('Brand Car: '),
            input('Type Car: '),
            numbers_to_strings(int(input('Color Car: '))),
            int(input('Year Product Car: '))
    )
    return car

def display_info_car(car):
    print('ID Car: ', car.id_car)
    print('Brand Car: ', car.brand_car)
    print('Type Car: ', car.type_car)
    print('Color Car: ', car.color_car)
    print('Year Product Car: ', car.year_prod_car)

def get_info_cars():
    cars = []      
    total_car = int(input('Enter how many cars: '))
    print()
    for i in range(total_car):
        print('Enter info car ',i+1)
        # ele = [input(), int(input())]
        car = get_info_car()
        cars.append(car)
        print('-----------------')
    return cars

def display_info_cars(cars):
    for i in range(len(cars)):
        print('Display info car ',i+1)
        print()
        display_info_car(cars[i])
        print('-----------------')

def write_cars_txt(cars):
    total = len(cars)
    with open('data.txt', 'w') as fileOut:
        fileOut.write(str(total) + '\n')
        for i in range(total):
            fileOut.write(str(cars[i].id_car) + '\n')
            fileOut.write(str(cars[i].brand_car)+ '\n')
            fileOut.write(str(cars[i].type_car)+ '\n')
            fileOut.write(str(cars[i].color_car)+ '\n')
            fileOut.write(str(cars[i].year_prod_car)+ '\n')

def read_cars_from_txt():
    read_cars_txt_list = []
    with open('data.txt', 'r') as fileOut:
        total = fileOut.readline()
        for i in range(int(total)):
            id_car = fileOut.readline()
            brand_car = fileOut.readline()
            type_car = fileOut.readline()
            color_car = fileOut.readline()
            year_prod_car = fileOut.readline()
            car = Car(id_car, brand_car, type_car, color_car, year_prod_car)
            read_cars_txt_list.append(car)
        return read_cars_txt_list

def conv_list_to_json(cars):
    info_cars = []
    for i in range(len(cars)):
        # a = map(strings_to_numbers(str(cars[i].color_car)), cars)
        # print(type(a))
        # print('Display info car map func ',i+1)
        info_car = dict()
        info_car['id_car'] = cars[i].id_car
        info_car['brand_car'] = cars[i].id_car
        info_car['type_car'] = cars[i].id_car
        info_car['color_car'] = cars[i].id_car
        info_car['year_prod_car'] = cars[i].id_car
        info_cars.append(info_car)
        # strings_to_numbers(str(cars[i].color_car))
        # print(strings_to_numbers(str(cars[i].color_car)))
        # display_info_car(cars[i])
    print(info_cars)
    print('-----------------')
    return info_car

# def display_info_cars_filter(cars):
#     def myFunc(car):
#         for i in range(len(car)):
#             if str(cars[i].color_car) == 'black':
#                  display_info_car(car[i])


#     adults = filter(myFunc(cars), cars)
#     for x in adults:
#         print(x)
    # for i in range(len(cars)):
    #     resu= filter(lambda i: type(cars[i].color_car) == int, cars)
    # # display_info_car(resu)
    #     print(list(resu))
    #     print('XXXXXX')
        # if str(cars[i].color_car) == 'black':
        #     display_info_car(cars[i])

        # item = '1'
        # if str(cars[i].color_car) == item:
        #     print('xxxxxxx')
    
    # item = '1'
    # output = list(filter(lambda x:item in x, cars))
    # print('fliterring list of tuples =\n',output)
    # filtered = []
    # for i in range(len(cars)):
    #     cars[i]
    #     # filtered = filter(lambda color, year_p: color_car.cars[i] == , scores)
    #     # filtered.append(filtere)

    #     print(list(filtered))

def display_info_cars_filter(info_car):
    resu = filter(lambda x: x['color_car'] == 2 and x['year_prod_car'] == 1, info_car)
    print(list(resu))


def main():
    # obj_car = Car
    

    obj_cars = get_info_cars()
    write_cars_txt(obj_cars)
    display_info_cars(obj_cars)
    # obj_read_cars = read_cars_from_txt()
    # display_info_cars(obj_read_cars)]
    json_cars = conv_list_to_json(obj_cars)
    # display_info_cars_map(json_cars)
    display_info_cars_filter(json_cars)

    # obj_car = get_info_car()
    # myFunc()
    # display_info_cars_filter(obj_cars)

if __name__ == '__main__':
    main()
