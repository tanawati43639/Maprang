from race import *
from runner import Runner


class Competition:
    MAX_ROUNDS = 3

    def __get_ordinal(self, n):
        # Helper function to return the ordinal string for a given integer
        # NOTE : You can ignore this method, you don't need to comment
        # or do any checks on it whatsoever
        suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
        if 11 <= n % 100 <= 13:
            suffix = 'th'
        else:
            suffix = suffixes.get(n % 10, 'th')
        return f"{n}{suffix}"

    def __init__(self, runners, rounds, distances_short, distances_marathon):
        
        if runners is str:
            raise CustomValueError('Runners must be list')
        self.runners = runners

        if rounds <= 0:
            raise CustomValueError('rounds must be more than 0') 
        if rounds > self.MAX_ROUNDS:
            raise CustomValueError('rounds more than MAX_ROUNDS') 
        self.rounds = rounds

        if len(distances_short) != rounds:
            raise CustomValueError('list distances_short more than rounds')
        self.distances_short = distances_short

        if len(distances_marathon) != rounds:
            raise CustomValueError('list distances_marathon more than rounds')
        self.distances_marathon = distances_marathon

        self.leaderboard = {}

        for i in range(1, len(self.runners) + 1):
            self.leaderboard[self.__get_ordinal(i)] = None

    def conduct_competition(self):
        current_round = 1
        i = 0
        while current_round <= self.rounds:
            # Conduct the short race with all runners
            short_race = ShortRace(self.distances_short[i], runners = self.runners)
            short_race.runners = self.runners
            short_result = self.conduct_race(short_race)

            # Conduct the Marathon race with all runners
            marathon_rance = MarathonRace(self.distances_marathon[i], runners = self.runners)
            marathon_rance.runners = self.runners
            marathon_result = self.conduct_race(marathon_rance)

            # Recover energy for all DNF runners
            for runner in self.runners:
                if runner.energy == 0:
                    runner.recover_energy(1000)

            current_round += 1
            self.update_leaderboard(short_result)
            self.update_leaderboard(marathon_result)

        return self.leaderboard

    def conduct_race(self, race):
        return race.conduct_race()

    def update_leaderboard(self, results):
        sorted_result = sorted(results, key=lambda x: x[1])
        #print('sorted_result', [i[0].name + ',' + str(i[1]) for i in sorted_result])
        leaderboard_keys = list(self.leaderboard.keys())
        for i, runner_time in enumerate(sorted_result):
            if self.leaderboard[leaderboard_keys[i]] is None:
                self.leaderboard[leaderboard_keys[i]] = (runner_time[0].name, len(results) - (i+1))
            else:
                for key, value in self.leaderboard.items():
                    if value[0] ==  runner_time[0].name and runner_time[1] != 'DNF':
                        self.leaderboard[key] = (runner_time[0].name, len(results) - (i+1) + value[1])
        
        # reorder rank
        tuple_runner = [value for key,value in self.leaderboard.items() if value is not None]
        tuple_runner = sorted(tuple_runner, key=lambda x:x[1], reverse=True)
        for index,runner in enumerate(tuple_runner):
            self.leaderboard[self.__get_ordinal(index + 1)] = runner

        #print(self.leaderboard)
        return self.leaderboard

    def print_leaderboard(self):
        print("Leaderboard\n\n")
        for key, value in self.leaderboard.items():
            print(f"{key} - {value[0]} ({value[1]})")

if __name__ == '__main__':
    # Example usage
    runners = [
        Runner("Elijah", 19, 'Australia', 6.4, 5.2),
        Runner("Rupert", 67, 'Botswana', 2.2, 1.8),
        Runner("Phoebe", 12, 'France', 3.4, 2.8),
        Runner("Lauren", 13, 'Iceland', 4.4, 5.1),
        Runner("Chloe", 21, 'Timor-Leste', 5.2, 1.9)
    ]

    competition = Competition(runners, 3, [0.5, 0.6, 1.2], [4.0, 11.0, 4.5])
    _ = (competition.conduct_competition())
    competition.print_leaderboard()

