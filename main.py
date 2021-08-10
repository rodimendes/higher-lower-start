from random import randint
import art
from game_data import data
import replit

def item_a():
    #Seleciona o item para o item A
    pos_a = randint(0, len(data) - 1)

    value_a = data[pos_a]['follower_count']

    return data[pos_a]['name'], data[pos_a]['description'], data[pos_a]['country'], value_a

def item_b():
    #Seleciona o item para o item B
    pos_b = randint(0, len(data) - 1)

    value_b = data[pos_b]['follower_count']
    
    return data[pos_b]['name'], data[pos_b]['description'], data[pos_b]['country'], value_b

def followers():
    #Mais seguidores
    if option_a[3] > option_b[3]:
        more_followers = option_a[3]
        return more_followers
    else:
        more_followers = option_b[3]
        return more_followers

def user_choice(op_a, op_b):
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_answer[0] == 'a':
        user_answer = op_a
        return user_answer
    else:
        user_answer = op_b
        return user_answer

print(art.logo)

option_a = item_a()

print(f"Compare A: {option_a[0]}, {option_a[1]}, from {option_a[2]}.")

print(art.vs)

option_b = item_b()
while option_b == option_a:
    option_b = item_b()
print(f"Compare B: {option_b[0]}, {option_b[1]}, from {option_b[2]}.")

followers_battle = followers()

#Pergunta e atribui resposta do usuário
user_answer = user_choice(option_a[3], option_b[3])

score = 0
while user_answer == followers_battle:
    replit.clear()
    print(art.logo)
    score += 1
    print(f"Você acertou. Pontuação: {score}")
    if option_a[3] < option_b[3]:
        option_a = option_b
    print(f"Compare A: {option_a[0]}, {option_a[1]}, from {option_a[2]}.")
    
    print(art.vs)

    option_b = item_b()
    while option_b == option_a:
        option_b = item_b()
    print(f"Compare B: {option_b[0]}, {option_b[1]}, from {option_b[2]}.")

    followers_battle = followers()
    user_answer = user_choice(option_a[3], option_b[3])

replit.clear()
print(art.logo)
print(f'Você errou. Sua pontuação final foi {score}')