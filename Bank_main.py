import datetime

class Account():
  auto_account_number = 1234567890

  def __init__(self, currency: str, initial_balance: float = 0):
    self._account_number = Account.auto_account_number
    Account.auto_account_number += 1
    self.currency = currency
    self.initial_balance = initial_balance
    self.timestamp = datetime.datetime.now()

  @property #decorators
  def account_number(self):
    return self._account_number

  @account_number.setter
  def account_number(self):
    pass

class Client:
  def __init__(self, firstname: str, lastname: str):
    self.firstname = firstname
    self.lastname = lastname
    self.timestamp = datetime.datetime.now()
    self.accounts = []
    self.transactions = []

  def add_accounts(self, account: Account):
    self.accounts.append(account)
  
  def print_accounts(self):
    print(f"Acounts of client {self.firstname} {self.lastname}:")
    for acc in self.accounts:
      print(f'{acc.account_number} {acc.currency} {acc.initial_balance}')

class Transaction:  
  def __init__(self, amount: float = 0, note: str = ''):
   self.amount = amount
   self.note = note
   self.time = datetime.datetime.now()


clients = []
clients.append(Client("Anna", "Persik"))
clients.append(Client('Jenifer', 'Uber'))
clients.append(Client('Donald', 'Proper'))

clients[0].add_accounts(Account('EUR', 200))
clients[0].add_accounts(Account('USD', 150))
clients[0].add_accounts(Account('CAD', 300))

clients[1].add_accounts(Account('EUR', 800))
clients[1].add_accounts(Account('JPY', 10000))

clients[2].add_accounts(Account('EUR'))


for client in clients:
  client.print_accounts()
