# -*- coding:utf-8 -*- #
__metaclass__ = type
import ConfigParser

CONFIGNAME = "MahjongTestCase.ini"
ITEMSNAME = "MahjongTestCase"

class MahjongConfig:
    def __init__(self):
        self.Mconfig = ConfigParser.ConfigParser()
    
    def getTestCase(self):
        try:
            self.Mconfig.readfp(open(CONFIGNAME))    
        except ConfigParser.Error:
            print 'read sina_weibo_config.ini failed.'
        
        return self.Mconfig.items(ITEMSNAME)

if __name__ == "__main__":
    
    m = MahjongConfig()
    print len(m.getTestCase())




#        for i in range(1,17):
#            for j in range(1,5):
#                tilecaseName = "tilecase" + str(i) + "_" + str(j)
#                try:
#                    tilecaseVar = vars()[tilecaseName]
#                    TileCases.append(tilecaseVar)
#                except KeyError:
#                    print 'key'
#                    break    # 如果发现没有此变量就找下一个
