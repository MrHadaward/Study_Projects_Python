
from operator import le, length_hint


class Category:

    def __str__(self):
        display = '{:*^30}'.format(self.name)[:30] + '\n'
        
        for element in self.ledger:
            display += '{:<23}'.format(element['description'])[:23] + '{:>7.2f}'.format(element['amount'])[:7] + '\n'
        
        display += 'Total: {:.2f}'.format(self.get_balance())

        return display

    def __init__(self, name):
        self.ledger = []
        self.name = name
    
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        balance = 0
        for element in self.ledger:
            balance += element['amount']

        return balance
    
    def  check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        
        else:
            return True


    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        
        else:
            self.ledger.append({"amount": -amount, "description": description})
            return True
    
    def transfer(self, amount, categ):
        if self.withdraw(amount, description='Transfer to {}'.format(categ.name)):
            categ.deposit(amount, description='Transfer from {}'.format(self.name))
            return True
        
        else:
            return False


def create_spend_chart(categories):
    spend_list = []

    for categ in categories:
        acumulator = 0
        for spent in categ.ledger:
            if spent['amount'] < 0:
                acumulator += spent['amount']
        
        spend_list.append(acumulator)
    
    total_spent = sum(spend_list)
    
    chart = 'Percentage spent by category\n'

    for ypoint in range(11):
        y_axis = 100 - ypoint*10
        chart += '{:3}|'.format(y_axis)

        for element in spend_list:
            percentage = (element/total_spent) * 100

            if y_axis - percentage  < 5:
                chart += ' o '
            
            else:
                chart += '   '
        
        chart += ' \n'
    
    chart += '    ' + '-' * (len(categories)*3 + 1) + '\n'

    biggest_name = 0
    for nam in categories:
        if len(nam.name) > biggest_name:
            biggest_name = len(nam.name)

    for rep in range(biggest_name):
        chart += '    '
        for line in categories:
            if line.name[rep:(rep+1)] == '':
                chart += '   '
            
            else:
                chart += ' {} '.format(line.name[rep:(rep+1)])

        chart += ' \n'

    return chart
