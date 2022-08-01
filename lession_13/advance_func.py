# lambda functions

# 1. Rewrite the below funtion, using lamda
def cube(x):
    return x*x*x

key = lambda x: x*x*x

# 2. Create a list as follow: [10,20,30,40,50,60,70,80,90,100], using lambda function

my_list = [lambda x: x*10 for x in range(1,11)]

# new_list = list(map(lambda x: x * 10 , my_list))

# 3. Given a list: [[2,3,1],[1,4,19,13],[5,9,2,0,6]]
# create a list with max values of each item in above list: Expected [2,13,6] (using lamba function)

list_1 = [[2,3,1],[1,4,19,13],[5,9,2,0,6]]

sorted_item_list = lambda x: (sorted(item) for item in x)

second_max_list = lambda x, f: [ y[len(y) -2] for y in f(x)]

second_max_list_resul = second_max_list(list_1, sorted_item_list)
# print(second_max_list_resul)

def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]
    return inner

@decorator_list
def add_together(a,b):
    return a + b

print(add_together([(1,3)]))

# add_together = decorator_list(add_together)
print(add_together([(1,3), (3,17), (5,5), (6,7)]))

