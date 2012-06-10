# -*- coding:gb2312 -*- #
# Created 2012-6-10
__metaclass__ = type
import re
import MahjongClass as mc
import MahjongTestCase as mtc

    
class MStandardScore:
    def __init__(self,combList=[],trump=-1):
        self.combList = combList[:]
        self.trump = trump
        self.drawSelf = False
        self.tilePoints = 0
    
    def scoreTile_1_88(self):
        resultList = [self.combList[0].bvlaue,self.combList[1].bvalue,self.combList[2].bvalue,self.combList[3].bvalue]
        for i in range(30,34):
            if i not in resultList:
                return 
        self.tilePoints += 88
        print "四风会"
    
    def scoreTile_2_88(self):
        pass
    
    def scoreTile_3_88(self):
        pass
    
    def scoreTile_4_88(self):
        pass

    def scoreTile_5_88(self):
        pass

    def scoreTile_6_88(self):
        pass

    def scoreTile_7_88(self):
        pass
    

def isSevenPairs(sortedTile):
    '''判断是否为七对'''
    pass

def isTheThirteenOrphans(sortedTile):
    '''判断是否为十三幺'''
    pass

def isNotSequence(sortedTile):
    '''判断是否为全不靠'''
    pass



def scoreTile49(sortedTile):
    '''49-碰碰和'''
    
    pass



if __name__ == '__main__':
    
    tilecase1_1 = [30,30,30,31,31,31,32,32,32,33,33,33,34,34]
    pass

