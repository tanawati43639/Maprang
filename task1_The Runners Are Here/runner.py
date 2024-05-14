from custom_errors import *

class Runner:

    def __init__(self, name, age, country, sprint_speed, endurance_speed):
        if not all(x.isalpha() or x.isspace() for x in name): raise CustomValueError('name is value invalid')
        if not isinstance(age, int): raise CustomTypeError('age is invalid type')
        if age < 5 and age > 120: raise CustomValueError('check range value of age')
        if not isinstance(country, str): raise CustomTypeError('country is invalid type')
        if not isinstance(sprint_speed, float): raise CustomTypeError('sprint_speed is invalid type')
        if sprint_speed < 2.2 and sprint_speed > 6.8: raise CustomValueError('check range value of sprint_speed')
        if not isinstance(endurance_speed, float): raise CustomTypeError('endurance_speed is invalid type')
        if endurance_speed < 1.8 and endurance_speed > 5.4: raise CustomValueError('check range value of endurance_speed')
        
        self.max_energy = 1000
        self.name = name
        self.age = age
        self.country = country
        self.sprint_speed = sprint_speed
        self.endurance_speed = endurance_speed
        self.energy = self.max_energy
    
    def drain_energy(self, drain_points):
        if not isinstance(drain_points, int): raise CustomTypeError('drain_points is of invalid type')
        if drain_points < 0: raise CustomValueError('drain_points less than 0')
        if drain_points > self.max_energy: raise CustomValueError('drain_points more than max energy')
        self.energy -= drain_points
        if self.energy <= 0: self.energy = 0
        return self.energy
    
    def recover_energy(self, recovery_amount):
        if not isinstance(recovery_amount, int): raise CustomTypeError('recovery_amount is of invalid type')
        self.energy += recovery_amount
        if self.energy >= self.max_energy: self.energy = self.max_energy
        return self.energy
    
    def run_race(self, race_type, distance):
        if type(distance) != float: raise CustomTypeError('distance is of invalid type')
        speed = self.sprint_speed if race_type == 'short' else self.endurance_speed
        time_taken = round(distance * speed, 2)
        return time_taken
    
    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Country: {self.country}"

if __name__ == '__main__':
    
    runner = Runner('Elijah', 18, 'South Africa', 5.8, 4.4)

    runner.drain_energy(1000)
    print(runner.energy)
    runner.drain_energy(1)
    print(runner.energy)
    runner.recover_energy(10)
    print(runner.energy)

    # running a short race
    time_taken = runner.run_race('short', 2.0)
    print(f"Runner {runner.name} took {time_taken} seconds to run 2km!")
    


