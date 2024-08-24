# Использование %:
team1_name = 'Мастера кода'
team1_num = 5
print('В команде %(team_name)s участников: %(team_num)s !' % {'team_name': team1_name, 'team_num': team1_num})
# В команде Мастера кода участников: 5 !
team2_num = 6
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
# Итого сегодня в командах участников: 5 и 6 !

# Использование format():
team2_name = 'Волшебники данных'
team2_score = 42
print('Команда {} решила задач: {} !'.format(team2_name, team2_score))
# Команда Волшебники данных решила задач: 42 !
team2_time = 18015.2
print('{1} решили задачи за {0} с !'.format(team2_time, team2_name))
# Волшебники данных решили задачи за 18015.2 с !

# Использование f-строк:
team1_score = 40
print(f'Команды решили {team1_score} и {team2_score} задач.')
# Команды решили 40 и 42 задач.
team1_time = 10717.6
print(f'Сегодня было решено {team1_score + team2_score} задач, в среднем по '
      f'{round((team1_time + team2_time) / (team1_score + team2_score), 1)} секунды на задачу!')
# 'Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!'


team1_time = 1552.512
team2_time = 2153.31451
time_total = team1_time + team2_time
tasks_total = team1_score + team2_score
time_avg = round((time_total / tasks_total), 1)
if team1_score == team2_score:
    challenge_result = 'Ничья.'
else:
    challenge_result = f'Победа команды {team1_name if team1_score > team2_score else team2_name}!'
print(challenge_result)
# Победа команды Волшебники данных!
