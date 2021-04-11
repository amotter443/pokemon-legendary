# pokemon-legendary
>Intro ML project using binomial classification to predict whether a Pokémon is legendary or not

The [Pokémon dataset](https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6) is an encyclopedia of all the Pokémon across generations, containing information about the stats of each Pokémon. This project was created to teach a group of high school students about data science fundamentals using topical and interesting data. Using this data, the students created models to determine whether Pokémon were legendary or not. If after getting your bearings with basic data science modeling principles you find yourself asking "what's next?" this is the repo for you. 


Who is this project for?
------------------------
- Beginner data scientists looking to apply several models to a classification problem
- Early analytics/data science students looking to dip their toes into deep learning
- Data science educators looking for foundational projects to teach their students
- A "next-step" project after simple projects like housing or MNist digit that requires limited research to get acclimated with


Usage
--------
- Read `pokemon.csv` into your environment
- Familiarize yourself with the below data dictionary


Data Dictionary
-------
The data source contains 800 observations of 13 variables, including the index column. The features contain information about different attributes that are important to the Pokémon. Special thanks to [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Main_Page) for providing definitions for some of the different stats:
- `#` -- id values for the individual wines (removed upon reading in)
- `Name` -- Name of the Pokémon as listed in the Pokédex
- `Type 1` -- Value of the primary type of the Pokémon (Normal, Fire, Water, Grass, Electric, Ice, Fighting, Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Dark, Dragon, Steel, Fairy)
- `Type 2` -- If the Pokémon has a second type, the value from the above list is preserved here
- `Total` -- Sum of the following attributes of the Pokémon in the following numeric features
- `HP` -- Short for "Hit Point," it is a stat that determines how much damage a Pokémon can receive before fainting
- `Attack` -- Partly determines how much damage a Pokémon deals when using a physical move
- `Defense` -- Partly determines how much damage a Pokémon recieves when hit with a physical move
- `Sp. Atk` -- Partly determines how much damage a Pokémon deals when using a special move
- `Sp. Def` -- Partly determines how much damage a Pokémon recieves when hit with a special move
- `Speed` -- Determines the order of Pokémon that can act in battle. If Pokémon are moving with the same priority, Pokémon with higher Speed at the start of any turn will generally make a move before ones with lower Speed; in the case that two Pokémon have the same Speed, one of them will randomly go first. 
- `Generation` -- 1 (Red, Blue, Yellow), 2 (Gold, Silver, Crystal), 3 (Ruby, Sapphire, Emerald, FireRed, LeafGreen), 4 (Diamond, Pearl, Platinum, HeartGold, SoulSilver), 5 (Black, White, Black 2, White 2) 6 (X, Y, Omega Ruby, Alpha Sapphire)
- `Legendary` -- Boolean value indicating whether or not a Pokémon is legendary or not


Extension Options 
-----------------
- This project is a rather simplistic design
