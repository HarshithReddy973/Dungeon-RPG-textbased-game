# Dungeon-RPG-Textbased-Game

A terminal-based Dungeon RPG game built with Python.

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
