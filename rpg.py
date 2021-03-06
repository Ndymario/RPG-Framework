#####################
# RPG Framework. Made by Nolan Y. and Trisha C.
#####################

from math import ceil
import random
import json


class Entity:
    def __init__(self, name, avatar, ent_id, level, exp, hp, sp, power, shield, spd, lk, defeated):
        self._name = name
        self._avatar = avatar
        self._id = ent_id
        self._level = level
        self._exp = exp
        self._hp = hp
        self._max_hp = hp
        self._sp = sp
        self._max_sp = sp
        self._power = power
        self._shield = shield
        self._spd = spd
        self._lk = lk
        self._defeated = defeated

    # Accessors
    def get_name(self):
        return self._name

    def get_avatar(self):
        return self._avatar

    def get_id(self):
        return self._id

    def get_level(self):
        return self._level

    def get_exp(self):
        return self._exp

    def get_hp(self):
        return self._hp

    def get_max_hp(self):
        return self._max_hp

    def get_sp(self):
        return self._sp

    def get_max_sp(self):
        return self._max_sp

    def get_power(self):
        return self._power

    def get_shield(self):
        return self._shield

    def get_spd(self):
        return self._spd

    def get_lk(self):
        return self._lk

    def get_defeated(self):
        return self._defeated

    # Mutators
    def set_name(self, name):
        self._name = name

    def set_avatar(self, avatar):
        self._avatar = avatar

    def set_id(self, ent_id):
        self._id = ent_id

    def set_level(self, level):
        self._level = level

    def set_exp(self, exp):
        self._exp = exp

    def set_hp(self, hp):
        self._hp = hp

    def set_max_hp(self, hp):
        self._max_hp = hp

    def set_sp(self, sp):
        self._sp = sp

    def set_max_sp(self, sp):
        self._max_sp = sp

    def set_power(self, power):
        self._power = power

    def set_shield(self, shield):
        self._shield = shield

    def set_spd(self, spd):
        self._spd = spd

    def set_lk(self, lk):
        self._lk = lk

    def set_defeated(self, defeated):
        self._defeated = defeated

    def __str__(self):
        return f"{self._name}: {self._level} | {self._hp}/{self._max_hp} |\
                {self._sp}/{self._max_sp} | {self._power} | {self._shield} | {self._spd} | {self._lk}"


class Player(Entity):
    # The default player stats
    def __init__(self, name="Player", avatar="None", ent_id=0, leve=1, exp=0,
                 hp=100, sp=100, power=10, shield=10, spd=10, lk=10, defeated=False, inventory=None):
        super().__init__(name, avatar, ent_id, leve, exp, hp, sp, power, shield, spd, lk, defeated)
        if inventory is None:
            inventory = []
        self._inventory = inventory

    # Accessors
    def get_inventory(self):
        return self._inventory

    # Mutators
    def set_inventory(self, inventory):
        self._inventory = inventory


class Enemy(Entity):
    # The default enemy stats
    def __init__(self, name="Enemy", avatar="None", ent_id=0, leve=1, exp=0,
                 hp=100, sp=100, power=10, shield=10, spd=10, lk=10, defeated=False, loot=None, moves=None):
        super().__init__(name, avatar, ent_id, leve, exp, hp, sp, power, shield, spd, lk, defeated)
        if moves is None:
            moves = []
        if loot is None:
            loot = []
        self._loot = loot
        self._moves = moves

    # Accessors
    def get_loot(self):
        return self._loot

    def get_moves(self):
        return self._moves

    # Mutators
    def set_loot(self, loot):
        self._loot = loot

    def set_moves(self, moves):
        self._moves = moves

    # Function that loads the stats of the passed enemy file
    def load_enemy(self, enemy_file):
        # Open the passed enemy JSON file
        with open(enemy_file, "r") as file:

            # Convert the JSON to a Python Dict
            enemy_json = json.load(file)

            # Use some RNG and pick the stats
            self.set_name(enemy_json["name"])
            self.set_avatar(enemy_json["avatar"])
            self.set_level(random.randint(enemy_json["level_min"], enemy_json["level_max"]))
            self.set_exp(random.randint(enemy_json["exp_min"], enemy_json["exp_max"]))
            hp = random.randint(enemy_json["hp_min"], enemy_json["hp_max"])
            self.set_hp(hp)
            self.set_max_hp(hp)
            sp = random.randint(enemy_json["sp_min"], enemy_json["sp_max"])
            self.set_sp(sp)
            self.set_max_sp(sp)
            self.set_power(random.randint(enemy_json["power_min"], enemy_json["power_max"]))
            self.set_shield(random.randint(enemy_json["shield_min"], enemy_json["shield_max"]))
            self.set_spd(random.randint(enemy_json["speed_min"], enemy_json["speed_max"]))
            self.set_lk(random.randint(enemy_json["lk_min"], enemy_json["lk_max"]))

            # Use some RNG to determine the loot for this enemy
            chance = 80
            common = random.randint(70, 100)
            rare = random.randint(50, 100)
            secret = random.randint(0, 80)
            loot_pool = []

            if common >= chance:
                loot_pool.append(enemy_json["loot"]["common"])

            if rare >= chance:
                loot_pool.append(enemy_json["loot"]["rare"])

            if secret >= chance:
                loot_pool.append(enemy_json["loot"]["secret"])

            self.set_loot(loot_pool)

    # Function that selects moves this enemy will have based off the move pool
    @staticmethod
    def load_moves(enemy_type):
        # Open the move pool JSON file
        with open("./rpg_files/enemy_files/move_pools.json", "r") as file:

            # Convert the JSON to a Python Dict
            move_json = json.load(file)

            # Get move pool passed
            move_pool = move_json[enemy_type]

            moves_to_assign = []

            # Use some RNG to assign moves to this enemy
            for move in move_pool:
                if random.randint(move["weight"], 100) >= (move["weight"] * 1.7):
                    moves_to_assign.append(move)


class Battle:
    def __init__(self):
        # Make a list of every entity in the battle
        self._participants = []

        # List that stores the turn order
        self._turn_order_list = []
        self._key_list = []

        # Keep track of whose turn it is
        self._turn_number = 0

    # Accessors
    def get_turn_order_list(self):
        return self._turn_order_list

    def get_key_list(self):
        return self._key_list

    def get_turn_number(self):
        return self._turn_number

    def assign_entities(self, *args):
        # Store what entities are in the current battle
        for arg in args:
            self._participants.append(arg)

    def turn_order(self):
        # Temp list to keep track of the entities to determine the turn order
        temp_list = []

        def turn_order_speed(participant):
            self._key_list = list(participant)
            key = self._key_list[0]
            return participant[key]

        # Loop through all the entities and get their speed stat
        for participants in self._participants:
            temp_list.append({participants.get_id(): participants.get_spd()})

        # Sort the turn order based on speed stat
        temp_list.sort(reverse=True, key=turn_order_speed)
        self._turn_order_list = temp_list

    def turn_number(self):
        if len(self._turn_order_list) < self._turn_number:
            self._turn_number = 0
        else:
            self._turn_number += 1

    # Define a helper function to calculate attack power based on the opponent's shield and the attacker's luck
    @staticmethod
    def attack_power(atk_stats, tar_stats):
        crit = False
        lk_multiplier = 0.1
        atk_multiplier = 0.2
        shield_multiplier = 0.1
        # First, lets determine if the attack is a crit or not
        if 1 <= atk_stats[2] * lk_multiplier + (random.randint(0, 100)) ** 2 / 10000:
            crit = True

        # Now, lets determine how much damage is being delt
        damage_total = (atk_stats[1] * atk_multiplier) - (tar_stats[2] * shield_multiplier)
        # Add a crit bonus if the entity received a crit
        if crit:
            return ceil(damage_total + (damage_total * 0.4))
        else:
            return ceil(damage_total)

    def attack(self, attacker, target):
        # Get the ID & relevant stats of the attacker and target for finding their stats in the dictionary
        atk_stats = [attacker.get_id(), attacker.get_power(), attacker.get_lk()]
        tar_stats = [target.get_id(), target.get_hp(), target.get_shield()]

        damage = self.attack_power(atk_stats, tar_stats)

        new_health = tar_stats[1] - damage

        # Just in case some weird rounding things occur, don't let the attack heal the target
        if new_health > target.get_hp():
            new_health = target.get_hp()

        target.set_hp(new_health)

        if new_health <= 0:
            target.set_defeated(True)

        self.turn_number()


'''[TODO]: Create class to handel parsing of Story files'''


class Story:
    def __int__(self):
        pass


debug_enemy = Enemy()
debug_enemy.load_enemy("./rpg_files/enemy_files/goblin.json")
print(debug_enemy)
