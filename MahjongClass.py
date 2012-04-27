# -*- coding:gb2312 -*- #
# Created 2012-3-7
__metaclass__ = type
import re
#Mahjong Class

class Tile:
    def __init__(self,Mname="",Mvalue=0):
        self.Mname = Mname
        self.Mvalue = Mvalue
    def MyName(self):
        print self.Mname
    def MyValue(self):
        print self.Mvalue

class Character(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Character,self).__init__(Mname,Mvalue)
  
class Dot(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Dot,self).__init__(Mname,Mvalue)
        
class Bamboo(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Bamboo,self).__init__(Mname,Mvalue)
        

class Dragon(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Dragon,self).__init__(Mname,Mvalue)
        

class Wind(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Wind,self).__init__(Mname,Mvalue)
        

class Flower(Tile):
    def __init__(self,Mname="",Mvalue=0):
        super(Flower,self).__init__(Mname,Mvalue)


class Triplet:
    def __init__(self,tValue=0,isPong=True):
        self.tValue = tValue
        self.isPong = isPong


class Sequence:
    def __init__(self,sValue=0,cValue=0,isChow=True):
        self.sValue = sValue
        self.cValue = cValue
        self.isChow = isChow

class Trump:
    def __init__(self,tValue=0):
        self.tValue = tValue

    
        
dictMTile = {0:'1C',1:'2C',2:'3C',3:'4C',4:'5C',5:'6C',6:'7C',7:'8C',8:'9C',
         10:'1D',11:'2D',12:'3D',13:'4D',14:'5D',15:'6D',16:'7D',17:'8D',18:'9D',
         20:'1B',21:'2B',22:'3B',23:'4B',24:'5B',25:'6B',26:'7B',27:'8B',28:'9B',
         30:'EW',31:'SW',32:'WW',33:'NW',34:'RD',35:'GD',36:'WD',
         40:'SP',41:'SU',42:'AU',43:'WI',44:'PL',45:'OR',46:'BA',47:'CH',}

dictPoints = {'SIFENGHUI':'四风会'}
SiFengHui = re.compile('\d{28}')


def isWin(sortedTile):
    '''确认是否和牌
       2012-3-13 功能1,判断和牌的普通牌型
       最终功能,需要将解析出来的刻子 顺子 杠 将牌解析出来
    '''
    flagT = 1  # 将牌/刻子/杠标志
    flagS = 1  # 顺子标志
    numTr = 0 # 将牌个数
    tile = sortedTile[0]
    for i in range(1,len(sortedTile)):
        
        if tile != sortedTile[i]:
            if flagT == 2:
                flagT = 1
                numTr += 1
                print 'trump',tile
            elif flagT == 3:
                flagT = 1
                print 'triplet:',tile
            elif flagT == 4:
                flagT = 1
                print 'kong:',tile
            if flagS == 3:
                flagS = 1
                print 'sequence',tile
        
        if tile == sortedTile[i]:
            flagT += 1

        if tile + 1 == sortedTile[i]:
            flagS += 1
            
        tile = sortedTile[i]
        i += 1

    if flagT == 2:
        flagT = 1
        numTr += 1
        print 'trump',tile
    elif flagT == 3:
        flagT = 1
        print 'triplet:',tile
    elif flagT == 4:
        flagT = 1
        print 'kong:',tile
    if flagS == 3:
        flagS = 1
        print 'sequence',tile
            
    if flagT == 1 and flagS == 1 and numTr == 1:
        print '确实为和牌,让我们看看有几番...'
    else:
        print '小子,诈和??!!'

def isSevenPairs(sortedTile):
    '''判断是否为七对'''
    pass

def isTheThirteenOrphans(sortedTile):
    '''判断是否为十三幺'''
    pass

def isNotSequence(sortedTile):
    '''判断是否为全不靠'''
    pass


def isPong():
    pass
def isKong():
    pass
def isChow():
    pass



def scoreTile49(sortedTile):
    '''49-碰碰和'''
    
    pass





def shuffleTile(randtile):
    pass

def sortTile(randtile):
    randtile.sort()
    return randtile


def reviseTile(randtile):
    pass

if __name__ == '__main__':

##    for i in range(48):
##        if i==9 or i==19 or i==29 or i==37 or i==38 or i ==39:
##            continue
##        print i+1,MTile[i],i
        
    t = Character(dictMTile[0],0)
##    randtilea = ['EW','EW','EW','SW','SW','SW','WW','WW','WW','NW','NW','NW','RD','RD']
    randtile00 = [30,30,30,31,31,31,32,32,32,33,33,33,35,35]
    randtile49 = [7,7,7,17,17,17,27,27,27,36,36,36,30,30]
    randtile48 = [1,2,3,12,13,14,23,24,25,26,26,26,13,13]
    isWin(randtile49)
    
     
