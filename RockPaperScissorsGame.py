import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
      if computer == "scissors":
        return "Rock smashes scissors!!! You Win!! Good Job"
      else:
        return "Paper covers rock!! You Lose Jive Turkey!!!!"

    elif player == "paper":
      if computer == "rock":
        return "Paper covers rock!!! You Win!! Good Job"
      else:
        return "Scissors cuts paper!! You Lose Jive Turkey!!!!"

    elif player == "scissors":
      if computer == "paper":
        return "Scissors cuts paper!!! You Win!! Good Job"
      else:
        return "Rock smashes scissors! You Lose Jive Turkey!!!!"

choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)