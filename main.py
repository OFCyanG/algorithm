
class Humidity():
    def __init__(self, curHum, preHum, down_thresh=15, up_thresh=60, water_level=[0, 5, 20], v_thresh=3, penalty=100):
        self.curHum = curHum
        self.preHum = preHum
        self.up_thresh = up_thresh
        self.down_thresh = down_thresh
        self.action = [0, 1, 2]
        self.water_level = water_level
        self.v_thresh = v_thresh
        self.penalty = penalty


        self.alpha = (self.water_level[2] - self.water_level[1])/(self.v_thresh*(self.action[2]-self.action[1]))
        self.delta = self.preHum - self.curHum
        self.curState = None
        self.nextState = None 

        self.maxReward = -2000
        self.tmpReward = 0

    def setCurState(self):
        if self.curHum < self.down_thresh:
            self.curState = -1
        elif self.curHum > self.up_thresh:
            self.curState = 1
        else:
            self.curState = 0
    
    def setNextState(self, nextHum):
        if nextHum < self.down_thresh:
            self.nextState = -1
        elif nextHum > self.up_thresh:
            self.nextState = 1
        else:
            self.nextState = 0

    def Reward(self, index):
        p = 0
        if self.nextState != int(0):
            p = 100
        r = - self.alpha * self.curState * self.delta * self.action[index] - self.water_level[index] - p
        return r

    def MakeDecision(self):
        self.setCurState()
        index = None
        nextHum = None
        index = None
        for i in self.action:
            nextHum = self.curHum - self.delta + self.water_level[i]
            self.setNextState(nextHum)
            self.tmpReward = self.Reward(i)
            if self.tmpReward > self.maxReward:
                self.maxReward = self.tmpReward
                index = i
        
        return index



