from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class FoodFactory:
    @staticmethod
    def create(food_type, name, price):
        if food_type == 'Bread':
            return Bread(name, price)
        elif food_type == 'Cake':
            return Cake(name, price)
        else:
            return None


class DrinksFactory:
    @staticmethod
    def create(drink_type, name, portion, brand):
        if drink_type == 'Tea':
            return Tea(name, portion, brand)
        elif drink_type == 'Water':
            return Water(name, portion, brand)
        else:
            return None


class TablesFactory:
    @staticmethod
    def create(table_type, table_number, capacity):
        if table_type == 'InsideTable':
            return InsideTable(table_number, capacity)
        elif table_type == 'OutsideTable':
            return OutsideTable(table_number, capacity)
        else:
            return None


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = [] # type of food
        self.food_names = set()
        self.drinks_menu = [] # type of drink
        self.drinks_names = set()
        self.tables_repository = []  # every table
        self.tables_numbers = set()
        self.total_income = 0  # all completed bills

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        food = FoodFactory.create(food_type, name, price)

        if name in self.food_names:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food:
            self.food_names.add(food.name)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        drink = DrinksFactory.create(drink_type, name, portion, brand)

        if name in self.drinks_names:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink:
            self.drinks_names.add(drink.name)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        table = TablesFactory.create(table_type, table_number, capacity)

        if table_number in self.tables_numbers:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table:
            self.tables_numbers.add(table_number)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        tables = [t for t in self.tables_repository if t.is_reserved is False and t.capacity >= number_of_people]

        if tables:
            table = tables[0]
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, **args):
        table = self.get_table(table_number)

        if not table:
            return f"Could not find table {table_number}"

        food_names_in_menu = [name for name in args if name in self.food_names]
        food_names_not_in_menu = [name for name in args if name not in self.food_names]

        foods = [self.get_food_by_name(food_name) for food_name in food_names_in_menu]
        [table.order_food(f) for f in foods]

        ordered_foods_str = '\n'.join(repr(f) for f in foods)
        missing_foods_str = '\n'.join(food_names_not_in_menu)
        return f'''Table {table_number} ordered:
{ordered_foods_str}
{self.name} does not have in the menu:
{missing_foods_str}'''

    def order_drink(self, table_number, **args):
        table = self.get_table(table_number)

        if not table:
            return f"Could not find table {table_number}"

        drink_names_in_menu = [d for d in args if d in self.drinks_menu]
        drink_names_not_in_menu = [d for d in args if d not in self.drinks_menu]

        drinks = [self.get_drink_by_name(drink) for drink in drink_names_in_menu]
        [table.order_drink(d) for d in drinks]

        ordered_drinks = "\n".join(repr(d) for d in drinks)
        missing_drinks = "\n".join(repr(d) for d in drink_names_not_in_menu)

        return f"Table {table_number} ordered:\n{ordered_drinks}{self.name} does not have in the menu:\n{missing_drinks}"

    def leave_table(self, table_number):
        table = self.get_table(table_number)
        if table:
            bill = table.get_bill()
            self.total_income += bill
            table.clear()
            return f"""Table: {table_number}
Bill: {bill:.2f}"""

    def get_free_tables_info(self):
        info = []
        for table in self.tables_repository:
            if table.free_table_info():
                info.append(table.free_table_info())

        return '\n'.join(info)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def get_food_by_name(self, name):
        food = [f for f in self.food_menu if f.name == name]
        if food:
            return food[0]

    def get_drink_by_name(self, name):
        drink = [f for f in self.drinks_menu if f.name == name]
        if drink:
            return drink[0]

    def get_table(self, number) -> Table:
        table = [t for t in self.tables_repository if t.table_number == number]
        if table:
            return table[0]





