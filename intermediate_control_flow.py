import random

def adventure_game():
    player_health = 100
    player_gold = 0
    monsters = ["Goblin", "Orc", "Troll", "Dragon"]
    
    print("Welcome to the Python Adventure Game!")
    
    while True:
        print(f"\nYour current status: Health: {player_health}, Gold: {player_gold}")
        
        choice = input("Choose your action:\n1. Explore\n2. Rest\n3. Shop\n4. Quit\nYour choice: ")
        
        if choice == '1':
            # Explore
            print("\nYou venture into the dark forest...")
            
            if random.random() < 0.7:  # 70% chance of encountering a monster
                monster = random.choice(monsters)
                print(f"You encounter a {monster}!")
                
                fight_choice = input("Do you want to fight? (y/n): ").lower()
                
                if fight_choice == 'y':
                    damage = random.randint(10, 30)
                    player_health -= damage
                    gold_reward = random.randint(10, 50)
                    player_gold += gold_reward
                    
                    print(f"You defeated the {monster}!")
                    print(f"You took {damage} damage and gained {gold_reward} gold.")
                    
                    if player_health <= 0:
                        print("Game Over! You have been defeated.")
                        break
                else:
                    print("You ran away safely!")
            else:
                print("You found a peaceful clearing. Nothing happened.")
        
        elif choice == '2':
            # Rest
            if player_gold >= 10:
                player_gold -= 10
                heal_amount = random.randint(10, 20)
                player_health = min(100, player_health + heal_amount)
                print(f"You rested and healed {heal_amount} health points. It cost you 10 gold.")
            else:
                print("You don't have enough gold to rest.")
        
        elif choice == '3':
            # Shop
            print("\nWelcome to the shop!")
            print("1. Health Potion (20 gold) - Restores 50 health")
            print("2. Lucky Charm (50 gold) - Increases gold finds")
            
            shop_choice = input("What would you like to buy? (1/2/cancel): ")
            
            if shop_choice == '1' and player_gold >= 20:
                player_gold -= 20
                player_health = min(100, player_health + 50)
                print("You bought a Health Potion and used it immediately.")
            elif shop_choice == '2' and player_gold >= 50:
                player_gold -= 50
                print("You bought a Lucky Charm. Your gold finds will increase!")
            elif shop_choice.lower() == 'cancel':
                print("You left the shop without buying anything.")
            else:
                print("Invalid choice or not enough gold.")
        
        elif choice == '4':
            # Quit
            print("Thank you for playing. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        adventure_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")