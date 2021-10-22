# rock-paper-scissors game
choice = ['rock', 'paper', 'scissors']


def check(staff):
    if staff in choice:
        return True
    else:
        return False


def game(p1, p2):
    answer = ['Drawn game', 'Player 1 wins!', 'Player 2 wins!']
    return answer[choice.index(p1) - choice.index(p2)]


def player_input():
    p1 = input('Player 1:')
    while not check(p1):
        print('Please enter: "rock", "paper" or "scissors"!')
        p1 = input('Player 1:')
    p2 = input('Player 2:')
    while not check(p2):
        print('Please enter: "rock", "paper" or "scissors"!')
        p2 = input('Player 2:')
    return p1, p2


start = 'y'
while start == 'y':
    print('Play! Please enter your choice.')
    player1, player2 = player_input()
    print(game(player1, player2))
    start = input('Again? y/n: ')
print('Finish!')
