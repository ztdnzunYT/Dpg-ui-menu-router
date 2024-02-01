print(__package__)
class PasswordDatabase:
    def __init__(self,username,password):
        pass
class TestResults:
    list = []
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def show(self):
        print(f"{self.name}'s grade is a {self.score}")
        print("{}'s grade is a {}".format(self.name,self.score))


class Car(object):
    Inventory = ["none"]
    def vehicle(make,model):
        make = make
        model = model

class Porshe(Car):
    windows = 4


print(Car)

c = Car
c.vehicle("ferrari",1991)
print(c.Inventory)

my_dic = {"tay":20,"mike":14,"lol":23,}
print(my_dic.values())
dict_variable = {key:value for (key,value) in my_dic.items()}
print(dict_variable)

nested_dict = {'first':{'a':1}, 'second':{'b':2}}

for (outer_k, outer_v) in nested_dict.items():
    for (inner_k, inner_v) in outer_v.items():
        outer_v.update({inner_k: float(inner_v)})
nested_dict.update({outer_k:outer_v})

print(nested_dict["first"]["a"])



