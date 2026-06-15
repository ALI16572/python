class BMW:
    def fuel_type(self):
        a = input("Enter fuel_type of BMW:")
    def max_speed(self):
        b = input("Enter max_speed of BMW:")
class Ferrari:
    def fuel_type(self):
        c = input("Enter a fuel_type of ferrari:")
    def max_speed(self):
        d = input("Enter max_speed of ferrari:")
a = BMW()
b = Ferrari()
for i in (a,b):
    i.fuel_type()
    i.max_speed()                         