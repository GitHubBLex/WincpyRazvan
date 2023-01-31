# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player1 = 'Ruud Gullit'
player2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = f'{player1} {str(goal_0)}, {player2} {str(goal_1)}'
print(scorers)
report = f'{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute'
print(report)
player = 'Jan Wouters'
player.find('Jan')
first_name = player[0:3]
print(first_name)
player.find('Wouters')
last_name_len =len(player[4:])
print(last_name_len)
#name_short: isolate and store the player's name in this format:
#G. von Examplestein
name_short = f'{player[:1]}. {player[4:]}'
print(name_short)
chant = ((first_name +'! ')*len(first_name))[:-1]
print(chant)
good_chant = chant.find(chant[:-1]) !=' '
print(good_chant)
type(good_chant)