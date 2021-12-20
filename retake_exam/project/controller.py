from project.player import Player


class Controller:
    valid_sustenance = ["Food", "Drink"]

    def __init__(self):
        self.players = []
        self.supplies = []
        self.names = []

    def add_player(self, *args):
        players = [Player(player.name, player.age, player.stamina) for player in args]

        for player in players:
            try:
                self.add_name(player.name)
                self.players.append(player)
            except Exception:
                return f"Successfully added: "

        return f"Successfully added: {', '.join(self.names)}"

    def add_supply(self, *args):
        self._add_supplies_to_list(*args)

    def sustain(self, player_name, sustenance_type):
        supply = self._get_sustenance(sustenance_type)
        player = self._get_player(player_name)
        result = ""

        if sustenance_type in self.valid_sustenance:
            if not supply:
                if sustenance_type == "Drink":
                    raise Exception("There are no drink supplies left!")

                elif sustenance_type == "Food":
                    raise Exception("There are no food supplies left!")
            else:
                if player.stamina + supply.energy > 100:
                    player.stamina = 100
                    self.supplies.remove(supply)
                    result += f"{player_name} sustained successfully with {supply.name}."
                else:
                    player.stamina += supply.energy
                    self.supplies.remove(supply)
                    result += f"{player_name} sustained successfully with {supply.name}."

        return result

    def duel(self, first_player_name, second_player_name):
        first_player = self._get_player(first_player_name)
        second_player = self._get_player(second_player_name)
        first_player_stamina = first_player.stamina
        second_player_stamina = second_player.stamina
        result = ""

        if first_player_stamina == 0 or first_player_stamina is None and second_player_stamina == 0 or second_player_stamina is None:
            result += f"Player {first_player_name} does not have enough stamina.\n"
            result += f"Player {second_player_name} does not have enough stamina."
        elif first_player_stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif second_player_stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if first_player_stamina > second_player_stamina:
            second_player_stamina -= first_player_stamina / 2
        else:
            first_player_stamina -= second_player_stamina / 2

        if first_player_stamina <= 0:
            first_player.stamina = 0
            return f"Winner: {second_player_name}"
        elif second_player_stamina <= 0:
            second_player.stamina = 0
            return f"Winner: {first_player_name}"
        elif first_player_stamina > second_player_stamina:
            first_player.stamina = first_player_stamina
            second_player.stamina = second_player_stamina
            return f"Winner: {first_player_name}"
        else:
            first_player.stamina = first_player_stamina
            second_player.stamina = second_player_stamina
            return f"Winner: {second_player_name}"

    def next_day(self):
        for player in self.players:
            curr_stamina = player.stamina - player.age * 2
            if curr_stamina < 0:
                player.stamina = 0
            else:
                player.stamina = curr_stamina
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def add_name(self, player_name):
        if player_name not in self.names:
            self.names.append(player_name)
        else:
            raise Exception(f"Name {player_name} is already used!")

        return self.names

    # def _append_players(self, *args):
    #     players = [player for player in args if player.name in player.names]
    #     if players:
    #         for player in players:
    #             self.players.append(player)

    def _add_supplies_to_list(self, *args):
        for supply in args:
            self.supplies.append(supply)

        return self.supplies

    def _get_sustenance(self, sustenance_type):
        supplies = [supply for supply in self.supplies if supply.__class__.__name__ == sustenance_type]
        if supplies:
            return supplies[-1]

    def _get_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
