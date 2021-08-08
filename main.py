from random import randint
import art
from game_data import data

print(art.logo)

#Seleciona o item para o item A
pos_a = randint(0, len(data) - 1)

value_a = data[pos_a]['follower_count']
print(f"Compare A: {data[pos_a]['name']}, {data[pos_a]['description']}, from {data[pos_a]['country']}")
# print(value_a)

print(art.vs)

#Seleciona o item para o item B
pos_b = randint(0, len(data) - 1)
if pos_b == pos_a:
    pos_b = randint(0, len(data) - 1)

value_b = data[pos_b]['follower_count']
print(f"Compare B: {data[pos_b]['name']}, {data[pos_b]['description']}, from {data[pos_b]['country']}")
# print(value_b)

#Mais seguidores
if value_a > value_b:
    more_followers = value_a
else:
    more_followers = value_b

#Pergunta e atribui resposta do usuário
user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()   

if user_answer[0] == 'a':
    user_answer = value_a
else:
    user_answer = value_b


while user_answer == more_followers:
    print(f'Você acertou. {user_answer} - {more_followers}')

print(f'Você errou. {user_answer} - {more_followers}')

#Continuar do último while. Ir substituindo os valores até o usuário errar.