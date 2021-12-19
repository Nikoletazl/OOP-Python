from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)
        self.correct_table_number(table_number)

    def correct_table_number(self, table_number):
        if table_number not in range(51, 101):
            raise ValueError("Inside table's number must be between 51 and 100 inclusive!")