### A Dungeon RPG Game 
import random 


class Player :
    def __init__(self , name, health =100 , attack=20 , defense =5 , gold =100  , experience=0 , max_health=100 , level=1 ,inventory=None):
        self.name= name 
        self.health= health
        self.attack = attack
        self.defense= defense 
        self.gold =gold
        self.level = level
        self.experience = experience
        self.max_health= max_health
        if inventory is None:
            inventory = ["Health Potion"]
        self.inventory = inventory


    def take_damage(self ,damage):
        self.health -= damage
        if self.health < 0:
            self.health =0
        # print(f"{damage} Damage taken !, fight harder!")
    
    def heal(self , recovery):
        self.health += recovery
        if self.health > self.max_health:
            self.health = self.max_health

    def is_alive(self):
        if self.health <=0 :
            return False
        else :
            return True

    def add_gold(self , amount):
        if amount >0:
            self.gold += amount

    def level_up(self, number ):
        self.level = number 
        self.max_health += 50
        self.add_gold(100)
        self.attack += number*2 
        self.defense += number*3
        print(f"Congrats ! You levelled up to {number}")
        print(f"Your reward : 100 Gold")
        print(f"\n----------------------------------------")
        print(f"Your stats:\n")
        print(f"Gold in the bank :{self.gold}")
        print(f"Now your maximum health is {self.max_health}")
        print(f"Attack :{self.attack} ")
        print(f"defense :{self.defense} ")

    


    def gain_xp(self , amount ):
        
        self.experience += amount

        while self.level < 5 and self.experience >= self.level * 100:
            self.level_up(self.level + 1)
        
        
    def use_item(self , item):
        
        if item not in self.inventory:
            print(f"{item} is not found in inventory.")
            return

        if item == "Health Potion":
            if self.health == self.max_health:
                print("Your health is already full.")
                return
            
            self.heal(50)
            self.inventory.remove(item)
            print("You used a Health Potion!")
            print(f"Your HP is now {self.health}/{self.max_health}")

        
        
    def display_stats(self):

        print("================================")
        print("          PLAYER STATS          ")
        print("================================")
        print(f"Name : {self.name}")
        print(f"Level : {self.level}")
        print(f"HP : {self.health}")
        print(f"Attack : {self.attack}")
        print(f"Defense : {self.defense}")
        print(f"Gold in the bank : {self.gold}")
        print(f"XP : {self.experience}")
        print("Inventory:    ")
        for item in self.inventory:
            print(item , end=" ")
        print("\n================================")
        print("================================")

    
    
class Enemy :
    def __init__(self , name, health =100, xp_reward=0 , max_health =100, attack =0, defense=0, gold_reward=0):
        self.name= name 
        self.health = health 
        self.attack = attack
        self.defense = defense
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.max_health= max_health

    
    def take_damage(self ,damage):
        self.health -= damage
        if self.health < 0:
            self.health =0
   
    def is_alive(self):
        if self.health <=0 :
            return False
        else :
            return True

    def display_stats(self):
    
        print("================================")
        print("           ENEMY STATS          ")
        print("================================")
        print(f"Name : {self.name}")
        print(f"HP : {self.health}")
        print(f"Attack : {self.attack}")
        print(f"Defense : {self.defense}")
        print("\n================================")
        print("================================")


class Game :
    def __init__(self):
        self.player = None
        self.current_enemy = None
        self.is_running = True


    def start(self):
        self.main_menu()

    def main_menu(self):
        while self.is_running:

            print("================================")
            print("          DUNGEON RPG")
            print("================================")
            print("1. New Game")
            print("2. Load Game")
            print("3. Exit")

            choice = input("Choose: ")

            match choice:

                case "1":
                    self.new_game()
                
                case "2":
                    self.load_game()
                    

                case "3":
                    self.is_running = False
                    
                case _:
                    print("Invalid choice!")
                    

    def new_game(self):

        name = input("Enter your name :")

        self.player = Player(name)
        print(f"-----Yoo , Welcome to the DUNGEON, {name} !------")
        self.game_loop()

    def game_loop(self):
       
        game_active = True

        while game_active:
            print("\n================================")
            print("            DUNGEON")
            print("================================")

            print("You are standing inside a dark dungeon.")

            print("""
                    1. Explore
                    2. Check Player
                    3. Inventory
                    4. Save Game
                    5. Main Menu
            """)

            choice = input("Choose : ")

            match choice :
                case "1":
                    self.explore()
                    if not self.player.is_alive():
                        game_active = False
                case "2":
                    self.player.display_stats()
                case "3":
                    self.show_inventory()
                case "4":
                    self.save_game()
                case "5":
                    print("Thankyou for playing my game !")
                    game_active = False
                case _:
                    print("Please choose a valid option")



    def show_inventory(self):
        print("\n================================")
        print("           INVENTORY"              )
        print("================================")
        if len(self.player.inventory) == 0:
            print("Inventory is empty.") 

        else :
            for item in self.player.inventory:
                print("-",item)
        print("================================")

    def explore(self):
        print("\nAh I see you are brave to choose explore hehehe")
        print("Better luck mySON")

        eventprob = random.randint(1,100)

        if eventprob <=50:
            self.events("enemy")
        elif eventprob <=70:
            self.events("treasure")

        elif eventprob <= 80:
            self.events("trap")

        elif eventprob <= 90:
            self.events("potion")

        else:
            self.events("nothing")
        

    def events(self, event):
        if event=="enemy":
            enemy = self.create_enemy()
            self.battle(enemy)
        elif event == "treasure":
            self.treasure_event()
        elif event == "trap":
            self.trap_event()   
        elif event== "potion":
            self.potion_event()
        elif event == "nothing":
            self.nothing_event()

    def create_enemy(self):
        enemy_num = random.randint(1,3)

        if enemy_num == 1:
            enemy = Enemy("Goblin",
            health=50,
            xp_reward=30,
            max_health=50,
            attack=20,
            defense=3,
            gold_reward=20)

        elif enemy_num == 2:
            enemy = Enemy("Vampire Lord", health=100,
            xp_reward=80,
            max_health=100,
            attack=30,
            defense=8,
            gold_reward=50)

        elif enemy_num == 3:
            enemy = Enemy("Skul",
            health=70,
            xp_reward=50,
            max_health=70,
            attack=23,
            defense=5,
            gold_reward=30)
        return enemy
    
    def battle(self, enemy):
        self.current_enemy = enemy
        print("\n================================")
        print("           BATTLE                ")
        print("================================\n")

        print(f"{enemy.name} is your enemy , Battle !")

        while self.player.is_alive() and enemy.is_alive():
            print(f"\nYour HP: {self.player.health}")
            print(f"{enemy.name} HP: {enemy.health}")

            print("\n1. Attack")
            print("2. Health potion")
            print("3. Run")

            choice = input("Choose: ")

            if choice == "1":
                self.player_attack()
                if enemy.is_alive():
                    self.enemy_attack()

            elif choice == "2":
                self.player.use_item("Health Potion")

            elif choice == "3":
                print("You escaped!")
                self.current_enemy = None
                return
            else:
                print("Please enter a valid choice nga , Im dying!")

            if not enemy.is_alive():
                self.enemy_defeated(enemy)
                return

            if not self.player.is_alive():
                self.game_over()
                return



    def player_attack(self):
        
        damage = self.player.attack - self.current_enemy.defense

        if damage < 0:
            damage = 0
            

        self.current_enemy.take_damage(damage)

        print(f"You dealt {damage} damage to {self.current_enemy.name}!")
    

    def enemy_attack(self):
        damage = self.current_enemy.attack - self.player.defense

        if damage < 0:
            damage = 0
               
        self.player.take_damage(damage)
        print(f"{self.current_enemy.name} dealt {damage} damage to you")


    def enemy_defeated (self,enemy):
        print(f"\nYou defeated the {enemy.name}!")

        print(f"You received {enemy.xp_reward} XP.")
        print(f"You received {enemy.gold_reward} gold.")

        self.player.gain_xp(enemy.xp_reward)
        self.player.add_gold(enemy.gold_reward)

        self.current_enemy = None

    def treasure_event(self):
        gold = random.randint(50 , 400)

        print("\nYou found a treasure chest!")
        print(f"You found {gold} gold!")

        self.player.add_gold(gold)
        

    def trap_event(self):
        damage = random.randint(1,30)
        print("\nYou stepped on a trap!")
        print(f"You took {damage} damage!")

        self.player.take_damage(damage)
        if not self.player.is_alive():
            self.game_over()
    
    def potion_event(self):
        print("\nYou found a Health Potion!")
        self.player.inventory.append("Health Potion")
        print("Health Potion added to your inventory.")


    def nothing_event(self):
        print("\nYou explored the dungeon...")
        print("Nothing happened.")

    def save_game(self) :
        file_path = "saved.txt"
        with open(file_path, "w") as file:  
            name = self.player.name
            health = self.player.health
            max_health = self.player.max_health
            attack = self.player.attack
            defense =self.player.defense
            gold = self.player.gold
            level   = self.player.level
            experience = self.player.experience
            inventory = self.player.inventory

            file.write(name + "\n")
            file.write(str(health) + "\n")
            file.write(str(max_health)+"\n")
            file.write(str(attack)+ "\n")
            file.write(str(defense)+ "\n")
            file.write(str(gold)+ "\n")
            file.write(str(level)+ "\n")
            file.write(str(experience)+ "\n")
            file.write(str(len(inventory))+ "\n")

            for item in inventory :
                file.write(item+ "\n")
        
            
        print("Game saved.")

    def load_game(self):
        print("\n================================")
        print("\nLoading Game...")
        print("\n================================")
        file_path = "saved.txt"
        try :
            with open(file_path , "r") as file:
                
                name = file.readline().strip()
                health = int(file.readline().strip())
                max_health = int(file.readline().strip())
                attack = int(file.readline().strip())
                defense = int(file.readline().strip())
                gold = int(file.readline().strip())
                level = int(file.readline().strip())
                experience = int(file.readline().strip())
                
                number_of_items = int(file.readline().strip())
                inventory = []
                for i in range(number_of_items):
                    item = file.readline().strip()
                    inventory.append(item)

                self.player = Player(name= name,
                    health=health,max_health=max_health,
                    attack=attack,
                    defense=defense,
                    gold=gold,
                    experience=experience,
                    level=level,
                    inventory=inventory)

                self.game_loop()

        except FileNotFoundError:
            print("No game saved before")

    def game_over(self):
        print("\n================================")
        print("           GAME OVER")
        print("================================")

        print("You died in the dungeon.")
        print("WE WOULD LOVE IF YOU REPLAY THO :))")
        
        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()




