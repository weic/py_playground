#! python3
# --------------------------------------------------------------
# create 2 type physicists (theoretical physicists 
# /experimental physicists ) from physicist class 
# make both inherits from physicists
# --------------------------------------------------------------

class Physicist():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def research(self, field):
        print('{0} research {1}'.format(self.name, field))

    def intrduction(self):
        print('My name is ', self.name)
        print('I\'m a physicist that working on ', self.description)

class TheoreticalPhysicist(Physicist):
    def __init__(self, math_model, name, description):
        self.math_model = math_model
        super().__init__(name, description)
    

class ExperimentalPhysicist(Physicist):
    def __init__(self, lab_expreiment, name, description):
        self.lab_expreiment = lab_expreiment
        super().__init__(name, description)
    
    def experiment(self):
        print('{0} is in lab experiment.'.format(self.name))

#weic = ExperimentalPhysicist('Basic Physic', 'Wei', 'Physics student')

