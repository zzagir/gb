my_age = 17
my_weight = 60.1
my_name = 'Zagir'
my_list = ['11', 'a']
my_turple = ('22', 'b')
my_dict = {'city': 'Moscow', 'county': 'Russia'}

all_list = [my_age, my_weight, my_name, my_list, my_turple, my_dict]
for i in all_list:
    print(f'{i} is {type(i)}')
