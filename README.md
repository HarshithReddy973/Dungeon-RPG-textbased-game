# Dungeon-RPG-Textbased-Game

A terminal-based Dungeon RPG game built with Python.

## Web UI

I also turned the game into a web-based UI using **Lovable**.   
But this has some changes in logic wise !

🎮 **[Play the Web Version](https://terminal-to-triumph.lovable.app/)**

## Game Structure

```text
main()
│
└── Game()
    │
    └── start()
        │
        └── main_menu()
            │
            ├── new_game()
            │   │
            │   └── game_loop()
            │       │
            │       ├── explore()
            │       │   └── events()
            │       │       ├── battle()
            │       │       ├── treasure
            │       │       ├── trap
            │       │       ├── potion
            │       │       └── nothing
            │       │
            │       ├── player stats
            │       ├── inventory
            │       └── save game
            │
            ├── load_game()
            │
            └── exit
```
