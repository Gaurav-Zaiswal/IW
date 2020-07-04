# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?

class Bank_account:
    bank_details = {
        'bank_name': 'State Bank of Nepal',
        'bank_address': 'suryabinayak, Bhaktapur',
        'bank_ceo': 'Gaurav Jaiswal',
        'bank_registration_no': '123-456-0-12',
        'bank_branches': ['Kathmandu', 'Biratnagar','Janakpur', 'Pokhara', 'Dang', 'Butwal', 'Mahendranagar']
    }
    def __init__(self,
                 account_holder_name,
                 account_holder_address,
                 account_number,
                 balance):
        self.account_holder_name = account_holder_name
        self.account_holder_address = account_holder_address
        self.balance = balance

    @classmethod
    def get_bank_details(cls):
        return cls.bank_details

    def deposite(self, amount) -> None:
        '''

        :param amount: number
        :return: None
        '''
        self.balance += amount


    def withdraw(self, amount):
        '''
        returns true if transaction is successfull, false otherwise
        :param amount: number
        :return: boolean
        '''
        if self.balance < amount:
            return False

        self.balance -= amount
        return True

    def get_balance(self):
        '''

        :return: amount
        '''
        return self.balance


Ram = Bank_account('Ram Bahadur',
                   'Kathmandu',
                   '134-34567-9000-91',
                   '1000')
print('Bank Details:\n', Bank_account.get_bank_details())
# print(Bank_account.bank_name)
