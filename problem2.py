# Revision 1 BEGIN 2024-02-07
## Begin Andrew Sassine here (2024-02-07)

import random

# Pirate-themed Game of Chance
class PirateTreasureGame:
    def __init__(self, bank):
        self.treasure_chest = ["gold coin", "silver coin", "ruby", "emerald", "pearl"]
        self.bank = bank
        self.loot_stash = []

    def play(self):
        print("Welcome to the Pirate's Fortune!")
        while self.bank > 0:
            wager = random.randint(1, self.bank)
            print(f"Wagering {wager} coins!")
            self.bank -= wager
            if random.choice([True, False]):  # 50% chance to win
                loot = random.choice(self.treasure_chest)
                print(f"Yarr! Ye found a {loot}!")
                self.loot_stash.append(loot)
            else:
                print("No loot this time, matey!")
            print(f"Bank: {self.bank}, Loot Stash: {self.loot_stash}")
            if self.bank <= 0:
                print("Ye be out of coins! Game over.")
                break

game = PirateTreasureGame(100)  # Start with a bank of 100 coins
game.play()

## End Andrew Sassine here (2024-02-07)
# Revision 1 FINAL DATE 2024-02-07
