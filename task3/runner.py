from custom_errors import *

class Runner:
    max_energy = 1000

    def __init__(self, name, age, country, sprint_speed, endurance_speed):
        #Name limitations
        if type(name) is not str:
            raise CustomTypeError('name must be string')
        self.name = name

        #Age limitations of data type and age range
        if type(age) is not int: 
            raise CustomTypeError('age must be integer')
        if age < 5 or age > 120: 
            raise CustomValueError('check range value of age')
        self.age = age

        #Country limitations of data type and check country in the list
        if type(country) is not str:
            raise CustomTypeError('country must be string')
        country_list = []
        with open("countries.csv","r") as file:
            for row in file:
                country_name = row.strip().split(',')[-1]
                country_list.append(country_name)
        if country not in country_list:
            raise CustomValueError('country does not exist in the list')
        self.country = country

        #Sprint speed limitations of data type and sprint speed range
        if type(sprint_speed) is not float:
            raise CustomTypeError('age must be float')
        if sprint_speed < 2.2 or sprint_speed > 6.8:
            raise CustomValueError('check range value of Sprint Speed')
        self.sprint_speed = sprint_speed

        #Endurance speed limitations of data type and sprint endurance range
        if type(endurance_speed) is not float:
            raise CustomTypeError('age must be float')
        if endurance_speed < 1.8 or endurance_speed > 5.4:
            raise CustomValueError('check range value of Endurance Speed')
        self.endurance_speed = endurance_speed
    
        self.energy = self.max_energy
        
    def drain_energy(self, drain_points):
        if type(drain_points) is not int:
            raise CustomTypeError('Drain points must be integer')
        if drain_points < 0:
            raise CustomValueError('drain_points less than 0')
        if drain_points > self.max_energy: 
            raise CustomValueError('drain_points more than max energy')
        self.energy -= drain_points
        #Check energy exceed the minimum
        if self.energy <= 0: 
            self.energy = 0
        return self.energy
    
    def recover_energy(self, recovery_amount):
        if type(recovery_amount) is not int:
            raise CustomTypeError('Recover amount must be integer')
        if recovery_amount < 0:
            raise CustomValueError('Recover amount less than 0')
        if recovery_amount > self.max_energy: 
            raise CustomValueError('Recover amount more than max energy')
        self.energy += recovery_amount
        #Check energy exceed the maximum
        if self.energy > self.max_energy: 
            self.energy = self.max_energy
        return self.energy
    
    def run_race(self, race_type, distance):
        if type(race_type) is not str:
            raise CustomTypeError('Race type must be string')
        if race_type.lower() not in ('short', 'long'):
            raise CustomValueError('Race type must be Short or Long')
        if type(distance) is not float: 
            raise CustomTypeError('Distance must be float')
        if distance < 0:
            raise CustomValueError('Distanct less than 0')

        if race_type.lower() == 'short':
            time_taken = round((distance*1000)/ self.sprint_speed, 2)
        else:
            time_taken = round((distance*1000)/ self.endurance_speed, 2)

        return time_taken
    
    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Country: {self.country}"

if __name__ == '__main__':
    runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
    
    # running a short race
    time_taken = runner.run_race('short', 2.0)
    print(f"Runner {runner.name} took {time_taken} seconds to run 2km!")
    

