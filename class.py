#! python3
# what is class

class ThisIsMe:
    '''
    define a class of me.
    '''

    def __init__(self, name):
        self.name = name
        self.gender = 1  #gender 1 is male
        self.single = False
        self.home = True
        self.job = True
        
    def who_am_I(self):
        return 'This is wei.'

weic = ThisIsMe('wei')
print(weic.name)
print(weic.gender)
print(weic.home)
print(weic.who_am_I())

