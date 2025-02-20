class Robot:
    def __init__(self,model,energy_level = 100):
        self._model = model
        self.__energy_level = energy_level

    def get_energy(self):
        return self.__energy_level
    
    def set_energy(self,energy):
        if 0<= energy <= 100:
            self.__energy_level = energy
        else:
            print("Invalid energy level")
    
    def charge(self,amount):
        new_energy = self.__energy_level+amount
        if new_energy >100:
            self.__energy_level = 100
        else:
            self.__energy_level = new_energy

robot = Robot("t1000")

try:
    print(robot.__energy_level)
except AttributeError as e:
    print(f"error:{e}")            

print(f"current energy:{robot.get_energy()}")
robot.set_energy(85)
print(f"updated energy:{robot.get_energy()}")
robot.set_energy(1)
robot.charge(4)
print(f"charged energy level:{robot.get_energy()}")



