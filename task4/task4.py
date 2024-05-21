from race import Runner
from competition import Competition
from custom_errors import *

def create_runner(runner_name, runner_age, runner_country, sprint_speed, endurance_speed):
    return Runner(runner_name, runner_age, runner_country, sprint_speed, endurance_speed)

def create_competition(runners, rounds, distances_short, distances_long):
    return Competition(runners, rounds, distances_short, distances_long)

def main():
    # Ask the user to create runners (until they decide to add no more)
    runners = []

    while True:
        try:
            runner = input("Add runner - name/age/country/sprint speed/marathon speed (blank line stops): ")
            if runner.strip() == '':
                print('Done creating runners! \n')
                break
            list_runner = runner.split('/')
            runner_name = list_runner[0]
            runner_age = int(list_runner[1])
            runner_country = list_runner[2]
            sprint_speed = float(list_runner[3])
            endurance_speed = float(list_runner[4]) 
            new_runner =  create_runner(runner_name, runner_age, runner_country, sprint_speed, endurance_speed)
            runners.append(new_runner)
        except:
            print('ERROR: Incorrect number of fields')
    
    # TODO: Take input for several runners until the user choses to quit

    # Ask the user to create a competition
    rounds = None
    distances_short = []
    distances_long = []

    while True:
        try:
            compet = input("Create competition - rounds/sprint distances/marathon distances: ")
            list_compet = compet.split('/')
            rounds = int(list_compet[0])
            sprint_distances = list_compet[1].split(',')
            marathon_distances = list_compet[2].split(',')
            if len(sprint_distances) != int(rounds):
                print('ERROR : There must be as many sprint distances as there are rounds')
            else:
                distances_short = [float(str(dist).strip()) for dist in sprint_distances]
            if len(marathon_distances) != int(rounds):
                print('ERROR : There must be as many marathon distances as there are rounds')
            else:
                distances_long = [float(str(dist).strip()) for dist in marathon_distances]

            if len(distances_short) == rounds and len(marathon_distances) == rounds:
                comp = create_competition(runners, rounds, distances_short, distances_long)
                print('Done creating competition \n\n')
                break
        except:
            print('ERROR: Incorrect number of fields')


    # Conduct the competition
    comp.conduct_competition()

    # Reveal the results!
    comp.print_leaderboard()

if __name__ == '__main__':
    main()

