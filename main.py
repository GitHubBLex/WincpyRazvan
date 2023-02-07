# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = player1 + ' ' + str(goal_0)+', '+ player2 + ' ' + str(goal_1)
report = f'{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute'

player = 'Jan Wouters'
space_intex = player.find(' ')
first_name = player[:space_intex]

last_name_start = space_intex + 1
last_name = player[last_name_start:]
last_name_len =len(last_name)

name_short = f'{player[0]}. {player[space_intex:]}'

chant = ((first_name +'! ')*len(first_name))[:-1]
good_chant = chant[-1] !=' '


