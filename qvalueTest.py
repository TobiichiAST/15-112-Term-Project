import json
from itertools import chain

# The json and itertolls are from the flappy bird bot as in credit


# This loop, the ai, is written by me
qval = {}
for xDifference in chain(list(range(-200,200,10))):
    for yDifference in chain(list(range(-200,200,40))):
        for enemyState in ['attack','stand','rollingAttack','crawl','roll','jump','jumpAttack','run']:
            for myState in ['stand','crawl','roll','jump','run']:
                for attackHeightDifference in range(-2,3):
                    qval[str(xDifference)+'_'+str(yDifference)+'_'+enemyState+'_'+myState+'_'+str(attackHeightDifference)] = [0,0,0,0,0,0]


# not by me
fd = open('qvalues.json', 'w')
json.dump(qval, fd)
fd.close()
