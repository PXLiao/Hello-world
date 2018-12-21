class Account:
  """ An account has a balance and holder.
	All accounts share a common interest rate.
  >>> a=Account('John')
  >>> a.holder
  'John'
  >>> a.deposit(100)
  100
  >>> a.withdraw(90)
  10
  >>> a.withdraw(90)
  'Insufficient funds'
  >>> a.balance
  10
  >>> a.interest
  0.02
  >>> Account.interest=0.04
  >>> a.interest
  0.04
  """
  interest=0.02 # A class attribute

  def __init__(self,account_holder):
    self.holder=account_holder
    
    self.balance=0

  def deposit(self,amount):
    """add amount to balance"""
    self.balance=self.balance+amount
    return self.balance
		
  def withdraw(self,amount):
    """subtract amount from balance."""
    
    if self.balance<amount:
      return 'Insufficient funds'
    self.balance=self.balance-amount
    return self.balance


class CheckingAccount(Account):
  """ A bank account that charges for withdraw."""
  withdraw_fee=1
  interest=0.01
  def withdraw(self,amount):
    return Account.withdraw(self,amount+self.withdraw_fee) 

class Bank:
  """A bank *has* accounts
  >>> bank=Bank()
  >>> john=bank.open_account('john',10)
  >>> jack=bank.open_account('jack',5,CheckingAccount)
  >>> john.interest
  0.04
  >>> jack.interest
  0.01
  >>> bank.pay_interest()
  >>> john.balance
  10.4
  >>> bank.too_big_to_fail()
  True
  """
  def __init__(self):
    self.accounts=[]     #attribute in instance
    
  def open_account(self,holder,amount,kind=Account):
    account=kind(holder)
    account.deposit(amount)
    self.accounts.append(account)
    return account

  def pay_interest(self):
    for a in self.accounts:
      a.deposit(a.balance*a.interest)

  def too_big_to_fail(self):
    return len(self.accounts)>1


  #using  py -i name.py     to run the script
  #using  py -m doctest name.py  to test the doctest

class SavingsAccount(Account):
  deposit_fee=2
  def deposit(self,amount):
    return Account.deposit(self,amount-self.deposit_fee)

class AsSeenOnTvAccount(CheckingAccount,SavingsAccount):
  def __init__(self,account_holder):
    self.holder=account_holder
    self.balance=1    # a free dollar!
