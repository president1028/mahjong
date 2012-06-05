#! /usr/bin/env python
#coding=utf-8
__metaclass__ = type

#import MahjongClass as mc
import MahjongTestCase as mtc
import logging
import logging.config

dictMTile = {0:'1C',1:'2C',2:'3C',3:'4C',4:'5C',5:'6C',6:'7C',7:'8C',8:'9C',
         10:'1D',11:'2D',12:'3D',13:'4D',14:'5D',15:'6D',16:'7D',17:'8D',
        18:'9D',20:'1B',21:'2B',22:'3B',23:'4B',24:'5B',25:'6B',26:'7B',
        27:'8B',28:'9B',30:'EW',31:'SW',32:'WW',33:'NW',34:'RD',35:'GD',
        36:'WD',40:'SP',41:'SU',42:'AU',43:'WI',44:'PL',45:'OR',46:'BA',
        47:'CH',}

dictScoring = {1:'四风会',49:'碰碰和',19:'七对',True:'未算番',False:'诈和',
0:'待定'}
dictPoints = {1:88,49:6,19:24,True:'未算番',False:'诈和',0:'待定'}

LOG_FILENAME = 'MahjongLogging.conf'
LOG_CONTENT_NAME = 'mahjong_log'


def log_init(log_config_filename,logname):
    logging.config.fileConfig(log_config_filename)
    logger = logging.getLogger(logname)
    return logger

def findScoring(scoreNO):
    if dictScoring.has_key(scoreNO):
        return dictScoring[scoreNO]
    else:
        return None

def findPoints(scoreNO):
    if dictScoring.has_key(scoreNO):
        return dictPoints[scoreNO]
    else:
        return None

    
def isTriplet(tilelist):
    if len(tilelist) == 3:
        if tilelist[0] == tilelist[1] == tilelist[2]:
            return True
    return False

def isSequence(tilelist):
    if len(tilelist) == 3:
        if tilelist[0] + 2 == tilelist[1] + 1 == tilelist[2]:
            return True
    return False

def isTrump(tilelist):
    if len(tilelist) == 2:
        if tilelist[0] == tilelist[1]:
            return True
    return False

def isKong(tilelist):
    if len(tilelist) == 4:
        if tilelist[0] == tilelist[1] == tilelist[2] == tilelist[3]:
            return True
    return False

def isDoubleSequence(tilelist):
    if len(tilelist) == 6:
        if tilelist[0] + 2 == tilelist[1] + 2 ==  \
           tilelist[2] + 1 == tilelist[3] + 1 ==  \
           tilelist[4] == tilelist[5]:
            return True
    return False



def confict():
    pass

def findTrump(sortedTile,listToken=[]):
    '''
    第一步，找对子，即将牌，找到将牌。
    listToken存的是对子的位置
    '''
    tile = sortedTile[0]
    i = 1
    while i < len(sortedTile):
        if tile == sortedTile[i]:
            if len(listToken) == 0 or (len(listToken) != 0 and 
                sortedTile[listToken[len(listToken)-1]] != tile):
                listToken.append(i-1)
        tile = sortedTile[i]
        i += 1


def isWinBacktrack(sortedTile):
    if len(sortedTile) == 0:
        return True
    else:
        if isSequence(sortedTile[0:3]) or isTriplet(sortedTile[0:3]):
            del sortedTile[0:3]
#            print sortedTile
            return isWinBacktrack(sortedTile)
        elif isDoubleSequence(sortedTile[0:6]):
            del sortedTile[0:6]
            return isWinBacktrack(sortedTile)
        else:
            return False
        

def isWin(sortedTile,listToken):
    '''先找对子，根据不同的对子回溯找和牌的情况
    回溯找和牌的方法在 inWinBacktrack()里。
    
    测试用例 list1 = [1,2,3,3,3,3,4,5,6,6,6,6,7,7,7] 有两个解
    [123,33,345,6666,777] [123,333,456,666,777]
    '''
    
    # 先检测特殊牌型，再查看普通和牌型
    if(isSevenPairs(sortedTile)):
#        print u'七对'.encode('gb2312')
        return 'QIDUI'
        
    if(isTheThirteenOrphans(sortedTile)):
        print u'十三幺'.encode('gb2312')
        return 'SHISANYAO'
    
    if(isNotSequence(sortedTile)):
        print u'全不靠'.encode('gb2312')
        return 'QUANBUKAO'
    
    trumpToken = []
    findTrump(sortedTile,trumpToken)
    
     
    for i in trumpToken:
        tiles = sortedTile[:]
        del tiles[i:i+2]
        if (isWinBacktrack(tiles)):
            tiles = sortedTile[:]
#            print tiles[i],tiles[i+1],
            del tiles[i:i+2]
#            print tiles,
#            print u'和了'.encode('gb2312')
#            mahjong_logger.info(str(sortedTile)+":和了")
            return True
        else:
            continue

    print u'诈和!'.encode('gb2312')
    mahjong_logger.warn(str(sortedTile)+":诈和")
    return False


def isSevenPairs(sortedTile):
    '''判断是否为七对'''
    for i in range(len(sortedTile)/2):
        if sortedTile[i*2] != sortedTile[i*2+1]:
            return False
    mahjong_logger.info(str(sortedTile)+":七对")
    return True
##        print '番号  番型  番数'
##        print '19   七对   24'
##        print '---------------'

def isSerialSevenPairs(sortedTile):
    if isSevenPairs(sortedTile):
        for i in range(0,12,2):
            if sortedTile[i] + 1 != sortedTile[i + 2]:
                return False
    return True

def isTheThirteenOrphans(sortedTile):
    '''判断是否为十三幺'''
#    if 
    pass

def isNotSequence(sortedTile):
    '''判断是否为全不靠'''
    pass


def analytic(realTile):
    '''
    {暗杠}[明杠](碰)<吃>@手牌*
    '''
    realTile = "{}[](26)<2,13>@23,24,25,13,13*"
    
    concealedKong = []
    exposedKong = []
    triplet = []
    chow = []
    handTile = []
    
    revisedTile = []

    start = realTile.find('{')
    end = realTile.find('}')
    if end > start + 1:
        concealedKong = realTile[start+1:end].split(',')
    
    start = realTile.find('[')
    end = realTile.find(']')
    if end > start + 1:
        exposedKong = realTile[start+1:end].split(',')

    start = realTile.find('(')
    end = realTile.find(')')
    if end > start + 1:
        triplet = realTile[start+1:end].split(',')

    start = realTile.find('<')
    end = realTile.find('>')
    if end > start + 1:
        chow = realTile[start+1:end].split(',')

    start = realTile.find('@')
    end = realTile.find('*')
    if end > start + 1:
        handTile = realTile[start+1:end].split(',')
    concealedKongInt = changeStrListToIntList(concealedKong)*4
    concealedKongInt.sort()

    exposedKongInt = changeStrListToIntList(exposedKong)*4

    exposedKongInt.sort()

    tripletInt = changeStrListToIntList(triplet)*3

    tripletInt.sort()
    chowInt = changeStrListToIntList(chow)
    
    handTileInt = changeStrListToIntList(handTile)


    handTileInt.sort()
    for i in range(len(chowInt)):
        chowValue = chowInt[i]
        chowInt.append(chowValue-1)
        chowInt.append(chowValue+1)
        

    chowInt.sort()
    revisedTile = concealedKongInt + exposedKongInt + tripletInt + chowInt 
    + handTileInt


##    revisedTile.sort()
    print revisedTile

    return revisedTile
    revisedTileStr = concealedKong + exposedKong + triplet + chow + handTile
    

    print revisedTileStr
    
    for i in range(len(revisedTileStr)):
        tempInt = int(revisedTileStr[i])
        revisedTile.append(tempInt)

    
    print revisedTile
    for i in range(len(realTile)):
        singleTile = realTile[i]
        
        if singleTile == '{':
            pass
            
    tile = ['1','2','3','4']
    tile2 = [4,6,7]
    
    tile4 = changeStrListToIntList(tile)
    tile3 = tile4 + tile2
        
    print tile3

    for i in range(3):
        print i,
        i += 1
    
    return tile

def changeStrListToIntList(strlist):
    intlist = []
    for i in range(len(strlist)):
        intlist.append(int(strlist[i]))
    return intlist

def findMeld(tile,start,end):
    pass




def isPong():
    pass
def iskong():
    '''这个表示杠这个状态 而不是名字 杠!'''
    pass
def isChow():
    pass


def scoreTile49(sortedTile,listToken):
    '''49-碰碰和'''
    if listToken.count('T') == 12 and listToken.count('R') == 2:
        return '49'

def shuffleTile(randtile):
    pass

def sortTile(randtile):
    randtile.sort()
    return randtile

def reviseTile(randtile):
    pass

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

if __name__ == '__main__':

    mahjong_logger = log_init(LOG_FILENAME,LOG_CONTENT_NAME)
    realtile01 = "{}[](26)<2,13>,23,24,25,13,13"
    
##    tile = analytic(realtile01)
##    print randtile68Sorted

##    list1 = [1,2,3,3,3,3,4,5,6,6,6,6,7,7,7]
##    list1 = [30,30,30,31,31,31,32,32,32,33,33,33,35,35]
    list2 = [0,1,2,3,4,4,4,5,6,7,8,8,8,8]
    list1 = [1,1,1,2,2,2,3,3,3,4,4,4,5,5]
    
    mConfig = mtc.MahjongConfig()
    testCase = mConfig.getTestCase()
    mTestCases = {}
    for i in testCase:
        mTestCases[i[0]] = [int(j) for j in i[1].split(",")]
    
    for k in mTestCases:
        listToken = []
        i = mTestCases[k]
        i.sort()
        print k,
        isWin(i,listToken)