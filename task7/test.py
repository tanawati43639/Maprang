test_dict = {'1st': ('Elijah', 20), 
             '2nd': ('Chloe', 11), 
             '3rd': ('Lauren', 12), 
             '4th': ('Phoebe', 7), 
             '5th': ('Rupert', 0)}


def __get_ordinal(n):
    # Helper function to return the ordinal string for a given integer
    # NOTE : You can ignore this method, you don't need to comment
    # or do any checks on it whatsoever
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    if 11 <= n % 100 <= 13:
        suffix = 'th'
    else:
        suffix = suffixes.get(n % 10, 'th')
    return f"{n}{suffix}"
leaderboard = {}


new_list = sorted([value for key,value in test_dict.items()],key=lambda x: x[1],reverse=True)
print(new_list)
for index,run in enumerate(new_list):
    leaderboard[__get_ordinal(index+1)] = run
print(leaderboard)
    
