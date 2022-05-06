# The RPG Framework
This is a small hobby project to make a lightweight and flexible RPG Framework mostly to be used in [Luigi Bot](https://github.com/Ndymario/Luigi-Bot), but maybe it will grow into it's own thing?

## Class Reference
There are, as of now, 4 main classes: Entity, Player, Enemy, and Battle.

Here's a breakdown of the main variables that each class has:
 - Entitiy
	 - Name
		 - A string that is used when referencing an Entity, for example during dialogue
	 - Avatar
		 - A string that is used when presenting an Entity's avatar, can be a URL, File Path, or None
	 - ID
		 - An int that is used to reference an Entity internally
	 - Level
		 - An int that stores an Entity's current level
	 - EXP
		 - An int that stores an Entity's total current EXP
	 - HP
		 - An int that stores an Entity's current HP
	 - Max HP
		 - An int that stores an Entity's maximum HP
	 - SP
		 - An int that stores an Entity's current SP
	 - Max SP
		 - An int that stores an Entity's maximum SP
	 - Power
		 - An int that stores an Entity's current Power
	 - Shield
		 - An int that stores an Entity's current Shield
	 - Speed
		 - An int that stores an Entity's current Speed
	 - Luck
		 - An int that stores an Entity's current Luck
	 - Defeated
		 - A flag that stores if an Entity is defeated
- Player
	- Inventory
		- A list that stores a Player's currently held Items
 - Enemy
	 - Loot
		 - A list that stores an Enemy's possible loot. This list is managed internally when loading an Enemy file
	 - Moves
		 - A list that stores an Enemy's possible moves. This list is managed internally when loading an Enemy file
 - Battle
	 - Participants
		 - A list that stores every Entity in Battle
	 - Turn Order List
		 - A list that keeps track of the turn order of Entities, by their ID, in Battle
	 - Key List [Will most likely be deprecated]
		 - A list that stores the speed stat of all Entities in a Battle
	 - Turn Number
		 - An int that increments after an Entities has had a turn