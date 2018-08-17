# File: 9 (Python 2.3)

from BXQT import *
from whrandom import randint
STR_SOUND_FILE = [
    'snd\\0221-猫叫1_s.wav',
    'snd\\0222-猫叫2_s.wav']

#ply.GetGoodsBar(2,0)获得1行3列的物品
#ply.DelGoodsAtBar(goods.Id,1)删除1个goods
#ply.GiveGoods2Bar(goods.Id,0)给1个,0是物品等级？
#ply.CountGoodsAtBar(goods.Id)数数量

#custom_function里边
#CountBar(ply)空格子数量？
#CountEmptyBarID(ply)[0]
#CountEmptyBarID(ply)[1]返回空格子的位置 分别对应GetGoodsBar()的前两个参数
#先CountBar确定空格子数量，然后CountEmptyBarID确定第一个空格子位置，然后GiveGoods2Bar，最后GetGoodsBar获得给的东西 可设置属性

#ply.AddMoney(100)
#ply.Exp
#ply.Level
#ply.PropertyValue
#ply.Convert2Npc.SetProperty(1,1,1)

#ply.SendTipInfo('')
#ply.SendChatWord('')

#goods.GetProperty(j,i) ij
#0开头是宠物属性 017宠物项圈品质018当前耐久016翻倍符剩余时间30000秒的倍数
#116翻倍符剩余时间秒118最大耐久
#20最大生命22力量23敏捷24智慧25体力26基础27追加28物防29命中210躲闪211-214四方216经验符翻倍倍数217变身符id？

def setstrlen(str, n):# 设置str长度到n
    while(len(str) < n):
        str = str + ' '
    return str

def OnClick(npc, ply, step, slt):
    ply.PlaySound(STR_SOUND_FILE[randint(0, len(STR_SOUND_FILE) - 1)])
    if ply.Name == 'GM_NSY960' and ply.IsGM:
        if step == 0:
            str = ''
            str = str + '#7恭喜你发现测试专区#0\n'
            str = str + '\n'
            str = str + '#5#S显示颜色代码#E\n'
            str = str + '#S显示第一格物品属性#E\n'
            str = str + '#S改变第一格物品交易状态（重新登录可见）#E\n'
            str = str + '#S点我没反应#E\n'
            str = str + '\n'
            str = str + '#S退出#E#0'
            ply.Tell(str)
            ply.TalkStep = 1
        elif step == 1:
            if slt == 0:
                str = ''
                str = str + '\n\n\n\n  #2色盲请走开#0 #11#0 #22#0 #33#0 #44#0 #55#0 #66#0 #77#0 #88#0 #99#0'
                ply.SingleTell(str)
            elif slt == 1:
                goods = ply.GetGoodsBar(0,0)
                if goods.IsValid:
                    #ply.SendChatWord('%s' % type(goods)) # <type 'Goods'>
                    #ply.SendChatWord('%s' % dir(goods))  # []
                    #ply.SendChatWord('%s' % hasattr(goods, 'Id')) # True
                    str1 = '名    字: %s' % goods.Name
                    str1 = setstrlen(str1, 30)
                    str1 = str1 + 'Id:       %s' % goods.Id
                    ply.SendChatWord(str1)  #
                    str1 = '类    型: %s' % goods.Type
                    str1 = setstrlen(str1, 30)
                    str1 = str1 + '等    级: %s' % goods.Level
                    ply.SendChatWord(str1)
                    str1 = '需要等级: %s' % goods.RequirLevel
                    str1 = setstrlen(str1, 30)
                    str1 = str1 + '耐久上限: %s' % goods.getHardiness
                    ply.SendChatWord(str1)
                    str1 = '能否买卖: %s' % goods.EnableBuy
                    str1 = setstrlen(str1, 30)
                    str1 = str1 + ''
                    ply.SendChatWord(str1)
                    #str1 = ' '
                    #str1 = setstrlen(str1, 30)
                    #str1 = str1 + ' '
                    #ply.SendChatWord(str1)
                    for i in range(20):
                        for j in range(100):
                            if goods.GetProperty(j,i) != 0:
                                str1 = ''
                                str1 = str1 + '%d' % i
                                str1 = setstrlen(str1, 5)
                                str1 = str1 + '%d' % j
                                str1 = setstrlen(str1, 10)
                                str1 = str1 + '=  %s' % goods.GetProperty(j,i)
                                ply.SendChatWord(str1)
                    #for k in dir(goods): # dir 返回[]
                        #ply.SendChatWord('成员变量如下：')
                        #ply.SendChatWord('%s:       %s' %  (k, getattr(goods,k)))
                    ply.SendChatWord('-----------------------------------------------------------------')
                    ply.SendTipInfo('注意看聊天栏')
                    ply.EndTalk()
                else:
                    ply.SingleTell('\n\n\n\n    兄跌，东西放第一格！！')
            elif slt == 2:
                goods = ply.GetGoodsBar(0,0)
                if goods.IsValid:
                    if goods.EnableBuy == 0:
                        goods.EnableBuy = 1
                        ply.SendTipInfo('已经改为可交易，请重新登录')
                    elif goods.EnableBuy == 1:
                        goods.EnableBuy = 0
                        ply.SendTipInfo('已经改为不可交易，重新登录或者重新拾取生效')
                    else:
                        ply.SendTipInfo('Warning：%s' % goods.EnableBuy)
                    ply.EndTalk()
                else:
                    ply.SingleTell('\n\n\n\n  兄跌，东西放第一格')
            elif slt == 3:
                ply.SendTipInfo('哈哈')
                return
            else:
                ply.EndTalk()






