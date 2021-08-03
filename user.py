class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f'User: {self.first_name} {self.last_name}, Balance: {self.account_balance}')
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

brian = User('Brian', 'Gaudet', 'brian@gaudet.com')
biggie = User('Christopher', 'Wallace', 'NotoriousBIG@badboy.com')
daft1 = User('Guy-Manuel', 'de Homem-Christo', 'guy-man@daftpunk.com')

brian.make_deposit(200)
brian.make_deposit(200)
brian.make_deposit(200)
brian.make_withdrawal(50)
brian.display_user_balance()

biggie.make_deposit(100000)
biggie.make_deposit(250000)
biggie.make_withdrawal(25000)
biggie.display_user_balance()

daft1.make_deposit(1000000)
daft1.make_withdrawal(50000)
daft1.display_user_balance()

brian.transfer_money(daft1, 12)
brian.display_user_balance()
daft1.display_user_balance()
