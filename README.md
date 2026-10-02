# Dungeon-RPG-textbased-game in Python

Game Structutre :

main
  │
  └── Game()
        │
        └── start()
             │
             └── main_menu()
                    │
                    ├── new_game()
                    │      │
                    │      └── game_loop()
                    │             │
                    │             ├── explore()
                    │             │     └── events()
                    │             │           ├── battle()
                    │             │           ├── treasure
                    │             │           ├── trap
                    │             │           ├── potion
                    │             │           └── nothing
                    │             │
                    │             ├── player stats
                    │             ├── inventory
                    │             └── save
                    │
                    ├── load_game()
                    │
                    └── exit
