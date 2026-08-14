# *args and **kwargs

# args = args collects multiple positional arguments into a tuple.
# *args → many positional arguments → tuple


# def total(*args):
#     print(sum(args))

# total(1,2,3,14)

def create_user(**kwargs):
    print(kwargs)


create_user( first_name = "ahmed",
            Last_name = "mohamed",
            Age = 20,
            Country = "Somalia",
            Universty = "Somaville")


 #Parameters
 
# def create_user(name, age, country):
#     name = input("Enter your name: ")
#     Age = int(input("Enter your age: "))
#     Country = input("Enter your country: ")

#     return ("name:", name,
#           "age:", age,
#           "country:", country,)


# create_user()


