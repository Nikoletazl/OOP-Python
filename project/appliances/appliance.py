class Appliance:
    def __init__(self, cost):
        self.cost = cost  #single day

    def get_monthly_expense(self):
        return self.cost * 30
