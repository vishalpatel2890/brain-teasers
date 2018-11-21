import numpy as np
class Monty:
    #pass in number of doors to  create
    def __init__(self, doors):
        self.doors= doors

    #create list of doors
    def create_doors(self, doors):
        self.list_doors = [None] * doors
        #generate a random index for the list above
        self.prize_index = np.random.randint(doors)
        #set random index as "Prize" door
        self.list_doors[self.prize_index] = 'Prize'

    #if no pick is manually selected randomly pick a door
    def pick(self, user_pick = None):
        if user_pick:
            self.user_picker = user_pick
        else:
            self.user_pick = np.random.randint(len(self.list_doors))

    #function to run if you wish to stay at the door you chose
    def stay(self):
        #if you picked the winning door you win otherwise you lose
        if self.list_doors[self.user_pick] == 'Prize':
            return 'win'

    #function to run if yu wish to switch the door you chose
    def switch(self):
        #if you picked the winning door you lose otherwise you win
        if self.list_doors[self.user_pick] == 'Prize':
            return 'lose'
    #pass in choice to stay or switch, run appropriate function
    #and return 'lose' or 'win' depending on outcome
    def run(self, choice):
        self.create_doors(self.doors)
        self.pick()
        if choice == 'stay':
            if self.stay() == 'win':
                return 'win'
            else:
                return 'lose'
        else:
            if self.switch() == 'lose':
                return 'lose'
            else:
                return 'win'

#run monty hall simulator (pass in number of doors to create,
#experiments to run, and choice to stay or switch)
class Simulator:
    def __init__(self, doors, experiments, choice):
        self.win_count = 0
        self.doors = doors
        self.experiments = experiments
        self.choice = choice

    def run(self):
        #for number of experiments create Monty class and run monty.run(choice)
        for i in range(self.experiments):
            monty = Monty(self.doors)
            #if simulation results in a win add 1 to win counter
            if monty.run(self.choice) == 'win':
                self.win_count += 1
        return self.win_count/self.experiments

#to run
sim = Simulator(3, 100000, 'switch')
print(sim.run())
