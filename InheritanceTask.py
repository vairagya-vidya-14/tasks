#----------------Single Inheritance---------------------
# 1. Single Inheritance without Constructor
# class father:
#     def house(self):
#         print("father has a house")
# class son(father):
#     def bike(self):
#         print("son has a bike")
# s=son()
# s.house()
# s.bike()

# 2. Single Inheritance with Constructor
# class father:
#     def __init__(self,name):
#         self.name=name
#     def display_father(self):
#         print("father name:",self.name)
# class son(father):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display_son(self):
#         print("father name:",self.name)
#         print("son age : ",self.age)
# s=son("ramesh",20)
# s.display_father()
# s.display_son()

# 3. Single Inheritance with Constructor + super()
# class father:
#     def __init__(self,name):
#         self.name=name
#     def display_father(self):
#         print("father name:",self.name)
# class son(father):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#     def display_son(self):
#         super().display_father()
#         print("son age : ",self.age)
# s=son("ramesh",20)
# s.display_son()

# 4. Single Inheritance with Constructor + super() — Different Real-World Example
# class vehicle:
#     def __init__(self,brand):
#         self.brand=brand
#     def display_brand(self):
#         print("Brand : ",self.brand)
# class car(vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model=model
#     def display_model(self):
#         super().display_brand()
#         print("model :",self.model)
# c=car("toyota","Fortuner")
# c.display_model()


# -----------------------multiple inheritance----------------------
# 1. Multiple Inheritance without Constructor
# class father:
#     def house(self):
#         print("father has a house")
# class mother:
#     def car(self):
#         print("mother has a car")
# class son(father,mother):
#     def bike(self):
#         print("son has a bike")
# s=son()
# s.house()
# s.car()
# s.bike()

# 2. Multiple Inheritance with Constructor
# class father:
#     def __init__(self,fname):
#         self.fname=fname
#     def display_father(self):
#         print("Father : ",self.fname)
# class mother:
#     def __init__(self,mname):
#         self.mname=mname
#     def display_mother(self):
#         print("mother : ",self.mname)
# class son(father,mother):
#     def __init__(self,fname,mname,sname):
#         self.fname=fname
#         self.mname=mname
#         self.sname=sname
#     def display_son(self):
#         print("father : ",self.fname)
#         print("mother : ",self.mname)
#         print("son : ",self.sname)
# s=son("father","mother","son")
# s.display_son()

# 3. Multiple Inheritance with Constructor + super()
# class father:
#     def __init__(self,fname):
#         self.fname=fname
#     def display_father(self):
#         print("Father : ",self.fname)
# class mother:
#     def __init__(self,fname,mname):
#         super().__init__(fname)
#         self.mname=mname
#     def display_mother(self):
#         print("mother : ",self.mname)
# class son(mother,father):
#     def __init__(self,fname,mname,sname):
#         super().__init__(fname,mname)
#         self.sname=sname
#     def display_son(self):
#         super().display_mother()
#         super().display_father()
#         print("son : ",self.sname)
# s=son("father","mother","son")
# s.display_son()

# 4. Multiple Inheritance with Constructor + super() — Real-World Example
class Camera:
    def __init__(self, megapixel):
        self.megapixel = megapixel
    def take_photo(self):
        print("Taking photo with", self.megapixel, "MP camera")
class Phone:
    def __init__(self, brand):
        super().__init__(brand)
        self.brand = brand
    def make_call(self):
        print("Calling from", self.brand)
class Smartphone(Camera, Phone):
    def __init__(self, megapixel, brand):
        super().__init__(megapixel,brand)
    def display(self):
        print("Brand:", self.brand)
        print("Camera:", self.megapixel, "MP")
s = Smartphone(108, "Samsung")
s.display()



