import json


class Bot(object):
    '''This bot class was originally from the bot to slove the flappy bird, it
    is re-implemented on my term project.'''
    def __init__(self):
        # The init function is "formated" to fit better with codes that are not written by me
        self.gameCNT = 0 # Game count of current run, incremented after every death
        self.DUMPING_N = 9 # Number of iterations to dump Q values to JSON after
        self.discount = 1.0
        self.r = {0: -50, 1: -1000,2:1000} # Reward function
        self.lr = 0.9
        self.load_qvalues()
        self.last_state = "190_0_stand_stand_0"
        self.last_action = 0
        self.moves = []
        self.result='notAggressive'

    def load_qvalues(self):
        # This function comes from the flappy bird bot function
        '''
        Load q values from a JSON file
        '''
        self.qvalues = {}
        try:
            fil = open('qvalues.json', 'r')
        except IOError:
            return
        self.qvalues = json.load(fil)
        fil.close()

    def act(self,xDifference,yDifference,enemyState,myState,attackHeightDifference):
        # This function is the implementation of the Q-learning.
        # It is formated into the style of the flappy bird because I want to use some other functions that are not written by me
        state = self.map_state(xDifference,yDifference,enemyState,myState,attackHeightDifference)

        self.moves.append( [self.last_state, self.last_action, state] )

        self.last_state = state
        
        self.last_action = self.qvalues[state].index(max(self.qvalues[state]))
        
        return self.last_action

    def update_scores(self):
        # This function is formated to the style of flappy bird's function because 
        # I want to use other functions that are not written by me
        
        history = list(reversed(self.moves))

        t = 1
        for exp in history:
            state = exp[0]
            act = exp[1]
            res_state = exp[2]
            if t <3:
                if self.result=='beKilled':
                    self.qvalues[state][act] = (1- self.lr) * (self.qvalues[state][act]) + (self.lr) * ( self.r[1] + (self.discount)*max(self.qvalues[res_state]) )
                elif self.result=='killed':
                    self.qvalues[state][act] = (1- self.lr) * (self.qvalues[state][act]) + (self.lr) * ( self.r[2] + (self.discount)*max(self.qvalues[res_state]) )
                else:
                    self.qvalues[state][act] = (1- self.lr) * (self.qvalues[state][act]) + (self.lr) * ( self.r[0] + (self.discount)*max(self.qvalues[res_state]))
                    

            else:
                self.qvalues[state][act] = (1- self.lr) * (self.qvalues[state][act]) + (self.lr) * ( self.r[0] + (self.discount)*max(self.qvalues[res_state]) )
            # The actions that makes the AI survive
            t += 1

        self.gameCNT += 1 #increase game count
        self.dump_qvalues() # Dump q values (if game count % DUMPING_N == 0)
        self.moves = []  #clear history after updating strategies

    def map_state(self,xDifference,yDifference,enemyState,myState,attackHeightDifference):
        return str(xDifference)+'_'+str(yDifference)+'_'+enemyState+'_'+myState+'_'+str(attackHeightDifference)

    def dump_qvalues(self):
        # this function comes from the flappy bird bot
        '''
        Dump the qvalues to the JSON file
        '''
        if self.gameCNT % self.DUMPING_N == 0:
            fil = open('qvalues.json', 'w')
            json.dump(self.qvalues, fil)
            fil.close()
            print('Q-values updated on local file.')
