# File: t (Python 2.3)

from BXQT import *
from wupin_list import *

def OnClick(npc, ply, step, slt):
    if ply.IsGM and 'GM_NSY960' == ply.Name:
        str = '　　　　　　　#3ＧＭ管理后台#0\n\
\n\
#5#S我的等级#E　#S我的打造#E　#S我的属性#E　#S我的技能#E\n\
\n\
#5#S队员等级#E　#S队员打造#E　#S队员属性#E　#S队员技能#E\n\
\n\
#S我的pk值#E　#S我的雪币#E　#S我的物品#E　#S我的变身#E\n\
\n\
#S发放物品#E　#S领变身符#E　#S我要无敌#E　#S维护公告#E\n\
\n\
#S查看十大#E　#SNPC变身#E　 #S我要纹银#E　#S队员纹银#E\n\
\n\
#S我的帮贡#E　#S帮会声誉#E　#S我的宠物#E　#S队员pk值#E\n\
\n\
#S在线信息#E　#S地图信息#E　#S形象代码#E　#S红　　包#E\n\
#S我的经验#E　#S队员经验#E\n\
#S退 出#E#0'
        ID_JISHU = 123
        ID_YSHU = 124
        ID_JISHU_BAK = ply.GetEvent(ID_JISHU)
        ID_YSHU_BAK = ply.GetEvent(ID_YSHU)
        feny = 30
        if step == 0:
            bxqt_tell(npc, ply, str)
            bxqt_set_step(npc, ply, 1)
        elif step == 1:
            if slt == 0:
                ply.Tell('　　　　　　　　#3我的等级#0\n\
\n\
#5#S+1级#E　　#S+5级#E　　#S+10级#E　　#S+50级#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 100
            elif slt == 1:
                ply.Tell('　　　　　　　#3自我打造经验#0\n\
\n\
#5#S+1W#E　　#S+10W#E　　#S+100W#E　　#S+750W#E\n\
\n\
#S-1W#E　　#S-10W#E　　#S-100W#E　　#S-750W#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 200
            elif slt == 2:
                ply.Tell('　　　　　　　#3我的属性点#0\n\
\n\
#5#S+1#E　　#S+10#E　　#S+100#E　　#S+1000#E\n\
\n\
#S-1#E　　#S-10#E　　#S-100#E　　#S-1000#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 300
            elif slt == 3:
                ply.Tell('　　　　　　　#3我的技能点#0\n\
\n\
#5#S+1#E　　#S+10#E　　#S+100#E　　#S-1#E　　#S-10#E　　#S-100#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 400
            elif slt == 4:
                ply.Tell('　　　　　　　　#3队员等级#0\n\
\n\
#5#S+1级#E　　#S+5级#E　　#S+10级#E　　#S+50级#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 500
            elif slt == 5:
                ply.Tell('　　　　　　　#3队员打造经验#0\n\
\n\
#5#S+1W#E　　#S+10W#E　　#S+100W#E　　#S+1000W#E\n\
\n\
#S-1W#E　　#S-10W#E　　#S-100W#E　　#S-1000W#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 600
            elif slt == 6:
                ply.Tell('　　　　　　　#3队员属性点#0\n\
\n\
#5#S+1#E　　#S+10#E　　#S+100#E　　#S+1000#E\n\
\n\
#S-1#E　　#S-10#E　　#S-100#E　　#S-1000#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 700
            elif slt == 7:
                ply.Tell('　　　　　　　#3队员技能点#0\n\
\n\
#5#S+1#E　　#S+10#E　　#S+100#E　　#S-1#E　　#S-10#E　　#S-100#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 800
            elif slt == 8:
                ply.Tell('　　　　　　　#3我的pk值#0\n\
\n\
#5#S+1#E　　#S+10#E　　#S+100#E　　#S-1#E　　#S-10#E　　#S-100#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 900
            elif slt == 9:
                ply.Tell('　　　　　　　　#3我的雪币#0\n\
\n\
#5#S+1000雪币#E　　#S+1W雪币#E　　#S+10W雪币#E\n\
\n\
#S+100W雪币#E　　#S+1000W雪币#E　　#S+1亿雪币#E\n\
\n\
#S-1000雪币#E　　#S-1W雪币#E　　#S-10W雪币#E\n\
\n\
#S-100W雪币#E　　#S-1000W雪币#E　　#S-1亿雪币#E\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 1000
            elif slt == 10:
                ply.Tell('　　　　　　 #3物品复制与升级#0\n\
\n\
请将要升级的物品放在物品栏第一格，并选择需要的等级：\n\
\n\
#5#S1级#E　#S2级#E　#S3级#E　#S4级#E　#S5级#E　#S6级#E　#S7级#E\n\
\n\
#S物品复制#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 1100
            elif slt == 11:
                ply.Tell('　　　　　　　　#3ＧＭ变身#0\n\
\n\
#5#S新手刀#E　#S20级刀#E　#S40级刀#E　#S60级刀#E　#S80级刀#E\n\
\n\
#S新手弓#E　#S20级弓#E　#S40级弓#E　#S60级弓#E　#S80级弓#E\n\
\n\
#S新手道#E　#S20级道#E　#S40级道#E　#S60级道#E　#S80级道#E\n\
\n\
#S新手剑#E　#S20级剑#E　#S40级剑#E　#S60级剑#E　#S80级剑#E\n\
\n\
#S新手僧#E　#S20级僧#E　#S40级僧#E　#S60级僧#E　#S80级僧#E\n\
\n\
#S新手指导员#E　#S速度之矛#E　#S碧雪雕像#E　#S小神龟#E\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 1200
            elif slt == 12:
                ply.Tell('　　　　　　　　#3发放物品#0\n\
\n\
#5#S小血瓶99个#E　　#S中血瓶99个#E　　#S大血瓶99个#E\n\
\n\
#S小精瓶99个#E　　#S中精瓶99个#E　　#S大精瓶99个#E\n\
\n\
#S小血精99个#E　　#S中血精99个#E　　#S大血精99个#E\n\
\n\
#S物品发放系统公告#E\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 1300
            elif slt == 13:
                str1 = '　　　　　　　　#3领取变身#0\n\
\n\
#5'
                jishu = 0
                yshu = 1
                while jishu < feny:
                    if jishu < len(GUAIWU_LIST):
                        str1 = str1 + '#S' + GUAIWU_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S空#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '　'
                str1 = str1 + '\n\
\n\
'
                if jishu < len(GUAIWU_LIST):
                    str1 = str1 + '#S下页#E　'
                
                yshu = yshu + 1
                str1 = str1 + '#S返回#E　#S退出#E#0'
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                str1 = str1 + '\n\
%s　%s　%s　%s　%s　%s　%s　%s' % (ID_JISHU_BAK, ID_YSHU_BAK, jishu, yshu, ID_JISHU, ID_YSHU, ply.GetEvent(ID_JISHU), ply.GetEvent(ID_YSHU))
                ply.Tell(str1)
                ply.TalkStep = 1400
            elif slt == 14:
                ply.Convert2Npc.SetLife(1, 30000)
                ply.Convert2Npc.SetProperty(0, 0, 30001)
                ply.Convert2Npc.SetProperty(1, 0, 30002)
                ply.Convert2Npc.SetProperty(4, 0, 100000)
                ply.Convert2Npc.SetProperty(6, 0, 30004)
                ply.Convert2Npc.SetProperty(7, 0, 30005)
                ply.Convert2Npc.SetProperty(8, 0, 30006)
                ply.Convert2Npc.SetProperty(9, 0, 30007)
                ply.Convert2Npc.SetProperty(10, 0, 30008)
                ply.Convert2Npc.SetProperty(11, 0, 30009)
                ply.Convert2Npc.SetProperty(12, 0, 30010)
                ply.Convert2Npc.SetProperty(13, 0, 30011)
                ply.Convert2Npc.SetProperty(14, 0, 30012)
                ply.SendTipInfo('无敌属性设置成功！')
            elif slt == 15:
                bxqt_get_world().SendChatWord('<系统>：服务器将于三分钟后重启，进行维护与调试，约五分钟后恢复；请各玩家及时下线保存，以避免数据的丢失与损坏，谢谢大家长期以来的支持与厚爱，我们将努力创造良好的游戏环境，让大家玩的更为愉快！')
            elif slt == 16:
                ply.Tell('　　　　　　　　 #3排行榜#0\n\
\n\
　　#6#S十大高手排行榜#E\n\
　　#S十大富翁排行榜#E\n\
　　#S十大英雄排行榜#E\n\
　　#6#S悬赏追杀榜#E\n\
\n\
\n\
\n\
\n\
\n\
#5#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 1500
            elif slt == 17:
                str1 = '　　　　　　　　#3NPC变身#0\n\
\n\
#5'
                jishu = 0
                yshu = 1
                while jishu < feny:
                    if jishu < len(NPC_LIST):
                        str1 = str1 + '#S' + NPC_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S空#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '　'
                str1 = str1 + '\n\
\n\
'
                if jishu < len(NPC_LIST):
                    str1 = str1 + '#S下页#E　'
                
                yshu = yshu + 1
                str1 = str1 + '#S返回#E　#S退出#E#0'
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                str1 = str1 + '\n\
%s　%s　%s　%s　%s　%s　%s　%s' % (ID_JISHU_BAK, ID_YSHU_BAK, jishu, yshu, ID_JISHU, ID_YSHU, ply.GetEvent(ID_JISHU), ply.GetEvent(ID_YSHU))
                ply.Tell(str1)
                ply.TalkStep = 1401
            elif slt == 18:
                ply.Tell('　　　　　　　　#3我的纹银#0\n\
\n\
#5#S+1#E　　#S+100#E　　#S+1000#E　　#S+1W#E\n\
\n\
#S-1#E　　#S-100#E　　#S-1000#E　　#S-1W#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 1600
            elif slt == 19:
                ply.Tell('　　　　　　　　#3队员纹银#0\n\
\n\
#5#S+1#E　　#S+100#E　　#S+1000#E　　#S+1W#E\n\
\n\
#S-1#E　　#S-100#E　　#S-1000#E　　#S-1W#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 1700
            elif slt == 20:
                ply.Tell('　　　　　　　　#3我的帮贡#0\n\
\n\
#5#S+1#E　　#S+40#E　　#S+100#E\n\
\n\
#S-1#E　　#S-40#E　　#S-100#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 1800
            elif slt == 21:
                ply.Tell('　　　　　　　#3我的帮会声誉#0\n\
\n\
#5#S+1#E　　#S+50#E　　#S+100#E\n\
\n\
#S-1#E　　#S-50#E　　#S-100#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 1900
            elif slt == 22:
                if ply.Pet.IsValid:
                    ply.Tell('　　　　　　　#3修改宠物属性#0\n\
\n\
#5#S增加宠物经验#E\n\
#5#S增加生命#E #5#S增加技能等级#E\n\
#5#S增加最小物理攻击#E #5#S增加最大物理攻击#E\n\
#5#S增加物理防御#E\n\
#5#S增加命中#E #5#S增加躲闪#E\n\
#5#S+光防#E #5#S+火防#E #5#S+冰防#E #5#S+毒防#E\n\
#S退 出#E#0')
                    ply.TalkStep = 2000
                else:
                    ply.SendTipInfo('你的宠物呢！')
            elif slt == 23:
                ply.Tell('　　　　　　　#3队员pk值#0\n\
\n\
#5#S+1#E　　#S+10#E　　#S+100#E　　#S-1#E　　#S-10#E　　#S-100#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 2100
            elif slt == 24:
                DITUID = [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                    27,
                    28,
                    29,
                    30,
                    31,
                    32,
                    33,
                    34,
                    35,
                    36,
                    37,
                    40,
                    41,
                    42,
                    43,
                    44,
                    45,
                    46,
                    47,
                    48,
                    49,
                    50,
                    51,
                    52,
                    53,
                    54,
                    55,
                    56,
                    57,
                    58,
                    59,
                    60,
                    61,
                    62,
                    63,
                    64,
                    65,
                    66,
                    70,
                    71,
                    72,
                    73,
                    74,
                    75,
                    76,
                    77,
                    78,
                    79,
                    80,
                    81,
                    82,
                    87,
                    88,
                    89,
                    101,
                    102,
                    103,
                    107,
                    111,
                    112,
                    120,
                    130]
                idt = 0
                psum = 0
                world = bxqt_get_world()
                strs = '在线玩家及位置与级别：'
                ply.SendChatWord(strs)
                while idt < len(DITUID):
                    sce = world.GetScene(DITUID[idt])
                    idt += 1
                    numb = sce.PlyNumb - 1
                    while numb >= 0:
                        ply_sce = sce.GetPly(numb)
                        numb = numb - 1
                        if ply_sce.IsValid:
                            str1 = '%s' % ply_sce.Name
                            while 15 > len(str1):
                                str1 = str1 + ' '
                            str2 = '%s' % sce.Name
                            while 14 > len(str2):
                                str2 = str2 + ' '
                            str3 = '%s' % ply_sce.Position[0]
                            while 3 > len(str3):
                                str3 = str3 + ' '
                            str4 = '%s' % ply_sce.Position[1]
                            while 3 > len(str4):
                                str4 = str4 + ' '
                            strs = '【名子:%s 地图:%s 坐标:%s:%s 等级:%d】' % (str1, str2, str3, str4, ply_sce.Level)
                            ply.SendChatWord(strs)
                            psum = psum + 1
                            continue
                ply.SendChatWord('在线玩家共计：%d人' % psum)
            elif slt == 25:
                if 'GM_NSY960' == ply.Name:
                    i = 0
                    j = 0
                    DITUID = 0
                    while j < 3:
                        if ply.GetGoodsBar(i, j).IsValid:
                            DITUID = DITUID + i * 10 ** j
                            i = 0
                            j = j + 1
                            continue
                        i = i + 1
                        if 9 < i:
                            i = 0
                            j = j + 1
                            continue
                    world = bxqt_get_world()
                    sce = world.GetScene(DITUID)
                    strs = '%s NPC数据清单：' % sce.Name
                    ply.SendChatWord(strs)
                    i = 0
                    numb = 1
                    maxnumb = 201
                    while i < 9:
                        if ply.GetGoodsBar(i, 3).IsValid:
                            numb = i * 200 + 1
                            maxnumb = numb + 200
                            i = 10
                        
                        i = i + 1
                    Npc = sce.GetNpcByNpcId(numb)
                    while numb <= maxnumb:
                        if Npc.IsValid:
                            str1 = '%s' % Npc.Name
                            while 16 > len(str1):
                                str1 = str1 + ' '
                            str2 = '%s' % Npc.Type
                            while 4 > len(str2):
                                str2 = str2 + ' '
                            str3 = '%s' % Npc.Position[0]
                            while 3 > len(str3):
                                str3 = str3 + ' '
                            str4 = '%s' % Npc.Position[1]
                            while 3 > len(str4):
                                str4 = str4 + ' '
                            strs = '【NPC名:%s ID_TYPE:%s 坐标:%s:%s IdForMap:%d】' % (str1, str2, str3, str4, numb)
                            ply.SendChatWord(strs)
                        
                        numb = numb + 1
                        Npc = sce.GetNpcByNpcId(numb)
                    ply.SendChatWord('%s 共计有NPC：%d个' % (sce.Name, numb))
                
            elif slt == 26:
                if 'GM_NSY960' == ply.Name:
                    ply.Tell('\n\
\n\
　当前外观代码为：#3%d#0\n\
\n\
#5#S上一个#E　　#S下一个#E\n\
\n\
#S关闭#E#0' % ply.OriginSprId)
                    ply.TalkStep = 2200
                
            elif slt == 27:
                if 'GM_NSY960' == ply.Name:
                    if ply.GetGoodsBar(0, 0).IsValid == 0 and ply.GetGoodsBar(1, 0).IsValid == 0:
                        ply.GiveGoods2Bar(872, 0)
                        ply.GiveGoods2Bar(872, 0)
                        ply.GetGoodsBar(0, 0).EnableBuy = 0
                        ply.GetGoodsBar(1, 0).EnableBuy = 0
                    else:
                        ply.SendTipInfo('请把物品栏前两格清空！')
                
            elif slt == 28:
                ply.Tell('　　　　　　　　#3我的经验#0\n\
\n\
#5#S+10万#E　　#S+100万#E　　#S+1000万#E　　#S+1亿#E\n\
\n\
#S-10万#E　　#S-100万#E　　#S-1000万#E　　#S-1亿#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 2300
            elif slt == 29:
                ply.Tell('　　　　　　　　#3队员经验#0\n\
\n\
#5#S+10万#E　　#S+100万#E　　#S+1000万#E　　#S+1亿#E\n\
\n\
#S-10万#E　　#S-100万#E　　#S-1000万#E　　#S-1亿#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 2400
            else:
                ply.EndTalk()
        elif step == 100:
            if slt == 0:
                if ply.Level < 99:
                    ply.Level = ply.Level + 1
                    ply.SendTipInfo('当前级别为：%d' % ply.Level)
                else:
                    ply.SendTipInfo('己超出等级上限，无法提升！')
            elif slt == 1:
                if ply.Level < 95:
                    ply.Level = ply.Level + 5
                    ply.SendTipInfo('当前级别为：%d' % ply.Level)
                else:
                    ply.SendTipInfo('己超出等级上限，无法提升！')
            elif slt == 2:
                if ply.Level < 90:
                    ply.Level = ply.Level + 10
                    ply.SendTipInfo('当前级别为：%d' % ply.Level)
                else:
                    ply.SendTipInfo('己超出等级上限，无法提升！')
            elif slt == 3:
                if ply.Level < 50:
                    ply.Level = ply.Level + 50
                    ply.SendTipInfo('当前级别为：%d' % ply.Level)
                else:
                    ply.SendTipInfo('己超出等级上限，无法提升！')
            elif slt == 4:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 200:
            if slt == 0:
                ply.FourdyScore = ply.FourdyScore + 10000
                ply.SendTipInfo('当前打造经验为：%d' % ply.FourdyScore)
            elif slt == 1:
                ply.FourdyScore = ply.FourdyScore + 100000
                ply.SendTipInfo('当前打造经验为：%d' % ply.FourdyScore)
            elif slt == 2:
                ply.FourdyScore = ply.FourdyScore + 1000000
                ply.SendTipInfo('当前打造经验为：%d' % ply.FourdyScore)
            elif slt == 3:
                ply.FourdyScore = ply.FourdyScore + 7500000
                ply.SendTipInfo('当前打造经验为：%d' % ply.FourdyScore)
            elif slt == 4:
                if ply.FourdyScore >= 10000:
                    ply.FourdyScore = ply.FourdyScore - 10000
                    ply.SendTipInfo('当前打造经验为：%d' % ply.FourdyScore)
                else:
                    ply.SendTipInfo('当前打造经验不足！')
            elif slt == 5:
                if ply.FourdyScore >= 100000:
                    ply.FourdyScore = ply.FourdyScore - 100000
                    ply.SendTipInfo('当前打造经验为：%d' % ply.FourdyScore)
                else:
                    ply.SendTipInfo('当前打造经验不足！')
            elif slt == 6:
                if ply.FourdyScore >= 1000000:
                    ply.FourdyScore = ply.FourdyScore - 1000000
                    ply.SendTipInfo('当前打造经验为：%d' % ply.FourdyScore)
                else:
                    ply.SendTipInfo('当前打造经验不足！')
            elif slt == 7:
                if ply.FourdyScore >= 7500000:
                    ply.FourdyScore = ply.FourdyScore - 7500000
                    ply.SendTipInfo('当前打造经验为：%d' % ply.FourdyScore)
                else:
                    ply.SendTipInfo('当前打造经验不足！')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 300:
            if slt == 0:
                ply.PropertyValue = ply.PropertyValue + 1
                ply.SendTipInfo('当前属性点为：%d' % ply.PropertyValue)
            elif slt == 1:
                ply.PropertyValue = ply.PropertyValue + 10
                ply.SendTipInfo('当前属性点为：%d' % ply.PropertyValue)
            elif slt == 2:
                ply.PropertyValue = ply.PropertyValue + 100
                ply.SendTipInfo('当前属性点为：%d' % ply.PropertyValue)
            elif slt == 3:
                ply.PropertyValue = ply.PropertyValue + 1000
                ply.SendTipInfo('当前属性点为：%d' % ply.PropertyValue)
            elif slt == 4:
                if ply.PropertyValue >= 1:
                    ply.PropertyValue = ply.PropertyValue - 1
                    ply.SendTipInfo('当前属性点为：%d' % ply.PropertyValue)
                else:
                    ply.SendTipInfo('当前属性点不足！')
            elif slt == 5:
                if ply.PropertyValue >= 10:
                    ply.PropertyValue = ply.PropertyValue - 10
                    ply.SendTipInfo('当前属性点为：%d' % ply.PropertyValue)
                else:
                    ply.SendTipInfo('当前属性点不足！')
            elif slt == 6:
                if ply.PropertyValue >= 100:
                    ply.PropertyValue = ply.PropertyValue - 100
                    ply.SendTipInfo('当前属性点为：%d' % ply.PropertyValue)
                else:
                    ply.SendTipInfo('当前属性点不足！')
            elif slt == 7:
                if ply.PropertyValue >= 1000:
                    ply.PropertyValue = ply.PropertyValue - 1000
                    ply.SendTipInfo('当前属性点为：%d' % ply.PropertyValue)
                else:
                    ply.SendTipInfo('当前属性点不足！')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 400:
            if slt == 0:
                ply.SkillValue = ply.SkillValue + 1
                ply.SendTipInfo('当前技能点为：%d' % ply.SkillValue)
            elif slt == 1:
                ply.SkillValue = ply.SkillValue + 10
                ply.SendTipInfo('当前技能点为：%d' % ply.SkillValue)
            elif slt == 2:
                ply.SkillValue = ply.SkillValue + 100
                ply.SendTipInfo('当前技能点为：%d' % ply.SkillValue)
            elif slt == 3:
                if ply.SkillValue >= 1:
                    ply.SkillValue = ply.SkillValue - 1
                    ply.SendTipInfo('当前技能点为：%d' % ply.SkillValue)
                else:
                    ply.SendTipInfo('当前技能点不足！')
            elif slt == 4:
                if ply.SkillValue >= 10:
                    ply.SkillValue = ply.SkillValue - 10
                    ply.SendTipInfo('当前技能点为：%d' % ply.SkillValue)
                else:
                    ply.SendTipInfo('当前技能点不足！')
            elif slt == 5:
                if ply.SkillValue >= 100:
                    ply.SkillValue = ply.SkillValue - 100
                    ply.SendTipInfo('当前技能点为：%d' % ply.SkillValue)
                else:
                    ply.SendTipInfo('当前技能点不足！')
            elif slt == 6:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 500:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Level < 99:
                    ply.GetTeamMember(1).Level = ply.GetTeamMember(1).Level + 1
                    ply.SendTipInfo('队员的当前级别为：%d' % ply.GetTeamMember(1).Level)
                    ply.GetTeamMember(1).SendTipInfo('你的当前级别为：%d' % ply.GetTeamMember(1).Level)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员己超出等级上限，无法提升！')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Level < 95:
                    ply.GetTeamMember(1).Level = ply.GetTeamMember(1).Level + 5
                    ply.SendTipInfo('队员的当前级别为：%d' % ply.GetTeamMember(1).Level)
                    ply.GetTeamMember(1).SendTipInfo('你的当前级别为：%d' % ply.GetTeamMember(1).Level)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员己超出等级上限，无法提升！')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Level < 90:
                    ply.GetTeamMember(1).Level = ply.GetTeamMember(1).Level + 10
                    ply.SendTipInfo('队员的当前级别为：%d' % ply.GetTeamMember(1).Level)
                    ply.GetTeamMember(1).SendTipInfo('你的当前级别为：%d' % ply.GetTeamMember(1).Level)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员己超出等级上限，无法提升！')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Level < 50:
                    ply.GetTeamMember(1).Level = ply.GetTeamMember(1).Level + 50
                    ply.SendTipInfo('队员的当前级别为：%d' % ply.GetTeamMember(1).Level)
                    ply.GetTeamMember(1).SendTipInfo('你的当前级别为：%d' % ply.GetTeamMember(1).Level)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员己超出等级上限，无法提升！')
            elif slt == 4:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 600:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore + 10000
                    ply.SendTipInfo('队员的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('你的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore + 100000
                    ply.SendTipInfo('队员的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('你的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore + 1000000
                    ply.SendTipInfo('队员的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('你的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore + 7500000
                    ply.SendTipInfo('队员的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('你的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).FourdyScore >= 10000:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore - 10000
                    ply.SendTipInfo('队员的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('你的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前打造经验不足！')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).FourdyScore >= 100000:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore - 100000
                    ply.SendTipInfo('队员的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('你的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前打造经验不足！')
            elif slt == 6:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).FourdyScore >= 1000000:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore - 1000000
                    ply.SendTipInfo('队员的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('你的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前打造经验不足！')
            elif slt == 7:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).FourdyScore >= 7500000:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore - 7500000
                    ply.SendTipInfo('队员的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('你的当前打造经验为：%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前打造经验不足！')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 700:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue + 1
                    ply.SendTipInfo('队员的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue + 10
                    ply.SendTipInfo('队员的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue + 100
                    ply.SendTipInfo('队员的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue + 1000
                    ply.SendTipInfo('队员的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PropertyValue >= 1:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue - 1
                    ply.SendTipInfo('队员的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前属性点不足！')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PropertyValue >= 10:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue - 10
                    ply.SendTipInfo('队员的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前属性点不足！')
            elif slt == 6:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PropertyValue >= 100:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue - 100
                    ply.SendTipInfo('队员的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前属性点不足！')
            elif slt == 7:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PropertyValue >= 1000:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue - 1000
                    ply.SendTipInfo('队员的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前属性点为：%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前属性点不足！')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 800:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue + 1
                    ply.SendTipInfo('队员的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue + 10
                    ply.SendTipInfo('队员的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue + 100
                    ply.SendTipInfo('队员的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).SkillValue >= 1:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue - 1
                    ply.SendTipInfo('队员的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前技能点不足！')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).SkillValue >= 10:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue - 10
                    ply.SendTipInfo('队员的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前技能点不足！')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).SkillValue >= 100:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue - 100
                    ply.SendTipInfo('队员的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前技能点为：%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前技能点不足！')
            elif slt == 6:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 900:
            if slt == 0:
                ply.PkValue = ply.PkValue + 1
                ply.SendTipInfo('当前PK值为：%d' % ply.PkValue)
            elif slt == 1:
                ply.PkValue = ply.PkValue + 10
                ply.SendTipInfo('当前PK值为：%d' % ply.PkValue)
            elif slt == 2:
                ply.PkValue = ply.PkValue + 100
                ply.SendTipInfo('当前PK值为：%d' % ply.PkValue)
            elif slt == 3:
                if ply.PkValue >= 1:
                    ply.PkValue = ply.PkValue - 1
                    ply.SendTipInfo('当前PK值为：%d' % ply.PkValue)
                else:
                    ply.SendTipInfo('PK值己不足！')
            elif slt == 4:
                if ply.PkValue >= 10:
                    ply.PkValue = ply.PkValue - 10
                    ply.SendTipInfo('当前PK值为：%d' % ply.PkValue)
                else:
                    ply.SendTipInfo('PK值己不足！')
            elif slt == 5:
                if ply.PkValue >= 100:
                    ply.PkValue = ply.PkValue - 100
                    ply.SendTipInfo('当前PK值为：%d' % ply.PkValue)
                else:
                    ply.SendTipInfo('PK值己不足！')
            elif slt == 6:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1000:
            if slt == 0:
                ply.AddMoney(1000)
                ply.SendTipInfo('当前雪币为：%d' % ply.Money)
            elif slt == 1:
                ply.AddMoney(10000)
                ply.SendTipInfo('当前雪币为：%d' % ply.Money)
            elif slt == 2:
                ply.AddMoney(100000)
                ply.SendTipInfo('当前雪币为：%d' % ply.Money)
            elif slt == 3:
                ply.AddMoney(1000000)
                ply.SendTipInfo('当前雪币为：%d' % ply.Money)
            elif slt == 4:
                ply.AddMoney(10000000)
                ply.SendTipInfo('当前雪币为：%d' % ply.Money)
            elif slt == 5:
                ply.AddMoney(100000000)
                ply.SendTipInfo('当前雪币为：%d' % ply.Money)
            elif slt == 6:
                if ply.Money >= 1000:
                    ply.AddMoney(-1000)
                    ply.SendTipInfo('当前雪币为：%d' % ply.Money)
                else:
                    ply.SendTipInfo('当前雪币不足！')
            elif slt == 7:
                if ply.Money >= 10000:
                    ply.AddMoney(-10000)
                    ply.SendTipInfo('当前雪币为：%d' % ply.Money)
                else:
                    ply.SendTipInfo('当前雪币不足！')
            elif slt == 8:
                if ply.Money >= 100000:
                    ply.AddMoney(-100000)
                    ply.SendTipInfo('当前雪币为：%d' % ply.Money)
                else:
                    ply.SendTipInfo('当前雪币不足！')
            elif slt == 9:
                if ply.Money >= 10000000:
                    ply.AddMoney(-10000000)
                    ply.SendTipInfo('当前雪币为：%d' % ply.Money)
                else:
                    ply.SendTipInfo('当前雪币不足！')
            elif slt == 10:
                if ply.Money >= 10000000:
                    ply.AddMoney(-10000000)
                    ply.SendTipInfo('当前雪币为：%d' % ply.Money)
                else:
                    ply.SendTipInfo('当前雪币不足！')
            elif slt == 11:
                if ply.Money >= 1000000000:
                    ply.AddMoney(-1000000000)
                    ply.SendTipInfo('当前雪币为：%d' % ply.Money)
                else:
                    ply.SendTipInfo('当前雪币不足！')
            elif slt == 12:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1100:
            if slt <= 6:
                if ply.GetGoodsBar(0, 0).IsValid:
                    ID = ply.GetGoodsBar(0, 0).Id
                    ply.GiveGoods2Bar(ID, -(slt + 1))
                else:
                    ply.SendTipInfo('请将物品放于物品栏的第一格')
            elif slt == 7:
                if ply.GetGoodsBar(0, 0).IsValid:
                    ID = ply.GetGoodsBar(0, 0).Id
                    ply.GiveGoods2Bar(ID, 0)
                else:
                    ply.SendTipInfo('请将物品放于物品栏的第一格')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1200:
            if slt <= 4:
                ply.OriginSprId = 4001 + slt
                ply.Profession = 1
                ply.ProfLevel = slt
                ply.SendTipInfo('变身成功！')
            elif slt > 4 and slt <= 9:
                ply.OriginSprId = 4006 + slt
                ply.Profession = 2
                ply.ProfLevel = slt - 5
                ply.SendTipInfo('变身成功！')
            elif slt > 9 and slt <= 14:
                ply.OriginSprId = 4011 + slt
                ply.Profession = 3
                ply.ProfLevel = slt - 10
                ply.SendTipInfo('变身成功！')
            elif slt > 14 and slt <= 19:
                ply.OriginSprId = 4016 + slt
                ply.Profession = 4
                ply.ProfLevel = slt - 15
                ply.SendTipInfo('变身成功！')
            elif slt > 19 and slt <= 24:
                ply.OriginSprId = 4021 + slt
                ply.Profession = 5
                ply.ProfLevel = slt - 20
                ply.SendTipInfo('变身成功！')
            elif slt == 25:
                ply.OriginSprId = 31
            elif slt == 26:
                ply.OriginSprId = 704
            elif slt == 27:
                ply.OriginSprId = 803
            elif slt == 28:
                ply.OriginSprId = 805
            elif slt == 29:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1300:
            if slt <= 8:
                for x in range(99):
                    ply.GiveGoods2Bar(782 + slt, 0)
                
            elif slt == 9:
                bxqt_get_world().SendChatWord('<系统>：三分钟后线上ＧＭ将在碣石村给大家发放药品，有需要的玩家请到村来拣！')
            elif slt == 10:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1400:
            jishu = ply.GetEvent(ID_JISHU)
            yshu = ply.GetEvent(ID_YSHU)
            if slt < feny:
                if jishu > len(GUAIWU_LIST):
                    if slt < feny - jishu - len(GUAIWU_LIST) - 3:
                        ply.GiveGoods2Bar(1017, 0)
                        N = ply.FindGoodsAtBar(1017)
                        N.SetProperty(17, 2, GUAIWU_LIST[slt + (jishu - feny)][1])
                    
                else:
                    ply.GiveGoods2Bar(1017, 0)
                    N = ply.FindGoodsAtBar(1017)
                    if jishu > feny:
                        N.SetProperty(17, 2, GUAIWU_LIST[slt + (jishu - feny)][1])
                    else:
                        N.SetProperty(17, 2, GUAIWU_LIST[slt][1])
            elif slt == feny and jishu > feny:
                yshu = yshu - 2
                if 0 != divmod(jishu, feny)[1]:
                    jishu = jishu - divmod(jishu, feny)[1] - feny
                else:
                    jishu = jishu - feny * 2
                str1 = '　　　　　　　　#3领取变身#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(GUAIWU_LIST):
                        str1 = str1 + '#S' + GUAIWU_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S空#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '　'
                str1 = str1 + '\n\
%s　pre1　%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S上页#E　'
                
                if jishu < len(GUAIWU_LIST):
                    str1 = str1 + '#S下页#E　'
                
                str1 = str1 + '#S返回#E　#S退出#E#0'
                yshu = yshu + 1
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                ply.Tell(str1)
                ply.TalkStep = 1400
            elif slt == feny and jishu < len(GUAIWU_LIST):
                str1 = '　　　　　　　　#3领取变身#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(GUAIWU_LIST):
                        str1 = str1 + '#S' + GUAIWU_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S空#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '　'
                str1 = str1 + '\n\
%s　next1　%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S上页#E　'
                
                if jishu < len(GUAIWU_LIST):
                    str1 = str1 + '#S下页#E　'
                
                str1 = str1 + '#S返回#E　#S退出#E#0'
                yshu = yshu + 1
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                ply.Tell(str1)
                ply.TalkStep = 1400
            elif slt == feny and jishu >= len(GUAIWU_LIST) and jishu <= feny:
                ply.SetEvent(ID_JISHU, ID_JISHU_BAK)
                ply.SetEvent(ID_YSHU, ID_YSHU_BAK)
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            elif slt == feny + 1 and jishu < len(GUAIWU_LIST) and jishu != feny:
                str1 = '　　　　　　　　#3领取变身#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(GUAIWU_LIST):
                        str1 = str1 + '#S' + GUAIWU_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S空#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '　'
                str1 = str1 + '\n\
%s　next2　%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S上页#E　'
                
                if jishu < len(GUAIWU_LIST):
                    str1 = str1 + '#S下页#E　'
                
                str1 = str1 + '#S返回#E　#S退出#E#0'
                yshu = yshu + 1
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                ply.Tell(str1)
                ply.TalkStep = 1400
            elif slt == feny + 1 and jishu <= len(GUAIWU_LIST) and jishu == feny:
                ply.SetEvent(ID_JISHU, ID_JISHU_BAK)
                ply.SetEvent(ID_YSHU, ID_YSHU_BAK)
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            elif slt == feny + 1 and jishu >= len(GUAIWU_LIST) and jishu != feny:
                ply.SetEvent(ID_JISHU, ID_JISHU_BAK)
                ply.SetEvent(ID_YSHU, ID_YSHU_BAK)
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            elif slt == feny + 2 and jishu > feny and jishu <= len(GUAIWU_LIST):
                ply.SetEvent(ID_JISHU, ID_JISHU_BAK)
                ply.SetEvent(ID_YSHU, ID_YSHU_BAK)
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.SetEvent(ID_JISHU, ID_JISHU_BAK)
                ply.SetEvent(ID_YSHU, ID_YSHU_BAK)
                ply.EndTalk()
        elif step == 1401:
            jishu = ply.GetEvent(ID_JISHU)
            yshu = ply.GetEvent(ID_YSHU)
            if slt < feny:
                if jishu > len(NPC_LIST):
                    if slt < feny - jishu - len(NPC_LIST):
                        ply.OriginSprId = NPC_LIST[slt + (jishu - feny)][1]
                    
                elif jishu > feny:
                    ply.OriginSprId = NPC_LIST[slt + (jishu - feny)][1]
                else:
                    ply.OriginSprId = NPC_LIST[slt][1]
            elif slt == feny and jishu > feny:
                yshu = yshu - 2
                if 0 != divmod(jishu, feny)[1]:
                    jishu = jishu - divmod(jishu, feny)[1] - feny
                else:
                    jishu = jishu - feny * 2
                str1 = '　　　　　　　　#3NPC变身#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(NPC_LIST):
                        str1 = str1 + '#S' + NPC_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S空#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '　'
                str1 = str1 + '\n\
%s　pre1　%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S上页#E　'
                
                if jishu < len(NPC_LIST):
                    str1 = str1 + '#S下页#E　'
                
                str1 = str1 + '#S返回#E　#S退出#E#0'
                yshu = yshu + 1
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                ply.Tell(str1)
                ply.TalkStep = 1401
            elif slt == feny and jishu < len(NPC_LIST):
                str1 = '　　　　　　　　#3NPC变身#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(NPC_LIST):
                        str1 = str1 + '#S' + NPC_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S空#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '　'
                str1 = str1 + '\n\
%s　next1　%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S上页#E　'
                
                if jishu < len(NPC_LIST):
                    str1 = str1 + '#S下页#E　'
                
                str1 = str1 + '#S返回#E　#S退出#E#0'
                yshu = yshu + 1
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                ply.Tell(str1)
                ply.TalkStep = 1401
            elif slt == feny and jishu >= len(NPC_LIST) and jishu <= feny:
                ply.SetEvent(ID_JISHU, ID_JISHU_BAK)
                ply.SetEvent(ID_YSHU, ID_YSHU_BAK)
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            elif slt == feny + 1 and jishu < len(NPC_LIST) and jishu != feny:
                str1 = '　　　　　　　　#3NPC变身#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(NPC_LIST):
                        str1 = str1 + '#S' + NPC_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S空#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '　'
                str1 = str1 + '\n\
%s　next2　%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S上页#E　'
                
                if jishu < len(NPC_LIST):
                    str1 = str1 + '#S下页#E　'
                
                str1 = str1 + '#S返回#E　#S退出#E#0'
                yshu = yshu + 1
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                ply.Tell(str1)
                ply.TalkStep = 1401
            elif slt == feny + 1 and jishu <= len(NPC_LIST) and jishu == feny:
                ply.SetEvent(ID_JISHU, ID_JISHU_BAK)
                ply.SetEvent(ID_YSHU, ID_YSHU_BAK)
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            elif slt == feny + 1 and jishu >= len(NPC_LIST) and jishu != feny:
                ply.SetEvent(ID_JISHU, ID_JISHU_BAK)
                ply.SetEvent(ID_YSHU, ID_YSHU_BAK)
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            elif slt == feny + 2 and jishu > feny and jishu <= len(NPC_LIST):
                ply.SetEvent(ID_JISHU, ID_JISHU_BAK)
                ply.SetEvent(ID_YSHU, ID_YSHU_BAK)
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.SetEvent(ID_JISHU, ID_JISHU_BAK)
                ply.SetEvent(ID_YSHU, ID_YSHU_BAK)
                ply.EndTalk()
        elif step == 1500:
            if slt == 0:
                ttLevelMsg = '\n\
　　　　  　　　#5十大高手#6\n\
\n\
'
                ttLevelMsg += bxqt_get_tt_level()
                ttLevelMsg += '\n\
\n\
　　　　#5#S返　回#E　　　　　　　#S退  出#E#0'
                bxqt_tell(npc, ply, ttLevelMsg)
                bxqt_set_step(npc, ply, 1501)
            elif slt == 1:
                ttLevelMsg = '\n\
　　　　　  　　#5十大富翁#6\n\
\n\
\n\
'
                ttLevelMsg += bxqt_get_tt_money()
                ttLevelMsg += '\n\
\n\
　　　　#5#S返　回#E　　　　　　　#S退  出#E#0'
                bxqt_tell(npc, ply, ttLevelMsg)
                bxqt_set_step(npc, ply, 1501)
            elif slt == 2:
                theWorld = bxqt_get_world()
                ttLevelMsg = '\n\
　　　　　  　　#5十大英雄#6\n\
\n\
\n\
'
                ttLevelMsg += theWorld.HeroHand
                ttLevelMsg += '\n\
\n\
　　　　#5#S返　回#E　　　　　　　#S退  出#E#0'
                bxqt_tell(npc, ply, ttLevelMsg)
                bxqt_set_step(npc, ply, 1501)
            elif slt == 3:
                pass
            elif slt == 4:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1501:
            if slt == 0:
                ply.Tell('　　　　　　　　 #3排行榜#0\n\
\n\
　　#6#S十大高手排行榜#E\n\
　　#S十大富翁排行榜#E\n\
　　#S十大英雄排行榜#E\n\
　　#6#S悬赏追杀榜#E\n\
\n\
\n\
\n\
\n\
\n\
#5#S返回#E\t\t#S退出#E#0')
                ply.TalkStep = 1500
            else:
                ply.EndTalk()
        elif step == 1600:
            if slt == 0:
                ply.ValueLeft = ply.ValueLeft + 1
                ply.SendTipInfo('当前纹银为：%d' % ply.ValueLeft)
            elif slt == 1:
                ply.ValueLeft = ply.ValueLeft + 100
                ply.SendTipInfo('当前纹银为：%d' % ply.ValueLeft)
            elif slt == 2:
                ply.ValueLeft = ply.ValueLeft + 1000
                ply.SendTipInfo('当前纹银为：%d' % ply.ValueLeft)
            elif slt == 3:
                ply.ValueLeft = ply.ValueLeft + 10000
                ply.SendTipInfo('当前纹银为：%d' % ply.ValueLeft)
            elif slt == 4:
                if ply.ValueLeft >= 1:
                    ply.ValueLeft = ply.ValueLeft - 1
                    ply.SendTipInfo('当前纹银为：%d' % ply.ValueLeft)
                else:
                    ply.SendTipInfo('当前纹银不足！')
            elif slt == 5:
                if ply.ValueLeft >= 100:
                    ply.ValueLeft = ply.ValueLeft - 100
                    ply.SendTipInfo('当前纹银为：%d' % ply.ValueLeft)
                else:
                    ply.SendTipInfo('当前纹银不足！')
            elif slt == 6:
                if ply.ValueLeft >= 1000:
                    ply.ValueLeft = ply.ValueLeft - 1000
                    ply.SendTipInfo('当前纹银为：%d' % ply.ValueLeft)
                else:
                    ply.SendTipInfo('当前纹银不足！')
            elif slt == 7:
                if ply.ValueLeft >= 10000:
                    ply.ValueLeft = ply.ValueLeft - 10000
                    ply.SendTipInfo('当前纹银为：%d' % ply.ValueLeft)
                else:
                    ply.SendTipInfo('当前纹银不足！')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1700:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft + 1
                    ply.SendTipInfo('队员的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('你的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft + 100
                    ply.SendTipInfo('队员的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('你的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft + 1000
                    ply.SendTipInfo('队员的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('你的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft + 10000
                    ply.SendTipInfo('队员的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('你的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).ValueLeft >= 1:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft - 1
                    ply.SendTipInfo('队员的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('你的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前纹银不足！')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).ValueLeft >= 100:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft - 100
                    ply.SendTipInfo('队员的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('你的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前纹银不足！')
            elif slt == 6:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).ValueLeft >= 1000:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft - 1000
                    ply.SendTipInfo('队员的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('你的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前纹银不足！')
            elif slt == 7:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).ValueLeft >= 10000:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft - 10000
                    ply.SendTipInfo('队员的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('你的当前纹银为：%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前纹银不足！')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1800:
            if ply.Organize.IsValid == 0:
                ply.SendTipInfo('你还没有加入帮派呢！')
                return 0
            elif slt == 0:
                ply.Contribute = ply.Contribute + 1
                ply.SendTipInfo('当前帮贡为：%d' % ply.Contribute)
            elif slt == 1:
                ply.Contribute = ply.Contribute + 40
                ply.SendTipInfo('当前帮贡为：%d' % ply.Contribute)
            elif slt == 2:
                ply.Contribute = ply.Contribute + 100
                ply.SendTipInfo('当前帮贡为：%d' % ply.Contribute)
            elif slt == 3:
                if ply.Contribute >= 1:
                    ply.Contribute = ply.Contribute - 1
                    ply.SendTipInfo('当前帮贡为：%d' % ply.Contribute)
                else:
                    ply.SendTipInfo('当前帮贡不足！')
            elif slt == 4:
                if ply.Contribute >= 40:
                    ply.Contribute = ply.Contribute - 40
                    ply.SendTipInfo('当前帮贡为：%d' % ply.Contribute)
                else:
                    ply.SendTipInfo('当前帮贡不足！')
            elif slt == 5:
                if ply.Contribute >= 100:
                    ply.Contribute = ply.Contribute - 100
                    ply.SendTipInfo('当前帮贡为：%d' % ply.Contribute)
                else:
                    ply.SendTipInfo('当前帮贡不足！')
            elif slt == 6:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1900:
            if ply.Organize.IsValid == 0:
                ply.SendTipInfo('你还没有加入帮派呢！')
                return 0
            elif slt == 0:
                ply.Organize.Honor = ply.Organize.Honor + 1
                ply.SendTipInfo('当前帮会声誉为：%d' % ply.Organize.Honor)
            elif slt == 1:
                ply.Organize.Honor = ply.Organize.Honor + 50
                ply.SendTipInfo('当前帮会声誉为：%d' % ply.Organize.Honor)
            elif slt == 2:
                ply.Organize.Honor = ply.Organize.Honor + 100
                ply.SendTipInfo('当前帮会声誉为：%d' % ply.Organize.Honor)
            elif slt == 3:
                if ply.Organize.Honor >= 1:
                    ply.Organize.Honor = ply.Organize.Honor - 1
                    ply.SendTipInfo('当前帮会声誉为：%d' % ply.Organize.Honor)
                else:
                    ply.SendTipInfo('当前帮会声誉不足！')
            elif slt == 4:
                if ply.Organize.Honor >= 50:
                    ply.Organize.Honor = ply.Organize.Honor - 50
                    ply.SendTipInfo('当前帮会声誉为：%d' % ply.Organize.Honor)
                else:
                    ply.SendTipInfo('当前帮会声誉不足！')
            elif slt == 5:
                if ply.Organize.Honor >= 100:
                    ply.Organize.Honor = ply.Organize.Honor - 100
                    ply.SendTipInfo('当前帮会声誉为：%d' % ply.Organize.Honor)
                else:
                    ply.SendTipInfo('当前帮会声誉不足！')
            elif slt == 6:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 2000:
            if ply.Pet.IsValid:
                Pet = ply.Pet
                Ao = Pet.GetProperty(0, 0)
                A1 = Pet.GetProperty(1, 0)
                A2 = Pet.GetProperty(2, 0)
                A3 = Pet.GetProperty(3, 0)
                A4 = Pet.GetProperty(4, 0)
                A5 = Pet.GetProperty(5, 0)
                A6 = Pet.GetProperty(6, 0)
                A7 = Pet.GetProperty(7, 0)
                A8 = Pet.GetProperty(8, 0)
                A9 = Pet.GetProperty(9, 0)
                A10 = Pet.GetProperty(10, 0)
                A11 = Pet.GetProperty(11, 0)
                A12 = Pet.GetProperty(12, 0)
                A13 = Pet.GetProperty(13, 0)
                A14 = Pet.GetProperty(14, 0)
                if slt == 0:
                    Pet.NpcExp = Pet.NpcExp + 50000
                    ply.SendTipInfo('%d' % Pet.NpcExp)
                elif slt == 1:
                    Pet.SetProperty(0, 0, Ao + 10)
                    a = Pet.GetProperty(0, 0)
                    ply.SendTipInfo('%d' % a)
                elif slt == 2:
                    Pet.SkillLevel = Pet.SkillLevel + 1
                    ply.SendTipInfo('%d' % Pet.SkillLevel)
                elif slt >= 3 and slt < 12:
                    X = Pet.GetProperty(slt + 3, 0)
                    Pet.SetProperty(slt + 3, 0, X + 10)
                    Y = Pet.GetProperty(slt + 3, 0)
                    ply.SendTipInfo('%d' % Y)
                else:
                    ply.EndTalk()
            else:
                ply.EndTalk()
        elif step == 2100:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PkValue = ply.GetTeamMember(1).PkValue + 1
                    ply.SendTipInfo('队员的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PkValue = ply.GetTeamMember(1).PkValue + 10
                    ply.SendTipInfo('队员的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PkValue = ply.GetTeamMember(1).PkValue + 100
                    ply.SendTipInfo('队员的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PkValue >= 1:
                    ply.GetTeamMember(1).PkValue = ply.GetTeamMember(1).PkValue - 1
                    ply.SendTipInfo('队员的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前pk值不足！')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PkValue >= 10:
                    ply.GetTeamMember(1).PkValue = ply.GetTeamMember(1).PkValue - 10
                    ply.SendTipInfo('队员的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前pk值不足！')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PkValue >= 100:
                    ply.GetTeamMember(1).PkValue = ply.GetTeamMember(1).PkValue - 100
                    ply.SendTipInfo('队员的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('你的当前pk值为：%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前pk值不足！')
            elif slt == 6:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 2200:
            if slt == 0:
                ply.OriginSprId = ply.OriginSprId - 1
                ply.Tell('\n\
\n\
　当前外观代码为：#3%d#0\n\
\n\
#5#S上一个#E　　#S下一个#E\n\
\n\
#S关闭#E#0' % ply.OriginSprId)
                ply.TalkStep = 2200
            elif slt == 1:
                ply.OriginSprId = ply.OriginSprId + 1
                ply.Tell('\n\
\n\
　当前外观代码为：#3%d#0\n\
\n\
#5#S上一个#E　　#S下一个#E\n\
\n\
#S关闭#E#0' % ply.OriginSprId)
                ply.TalkStep = 2200
            else:
                ply.EndTalk()
        elif step == 2300:
            if slt == 0:
                ply.Exp = ply.Exp + 100000
                ply.SendTipInfo('当前经验为：%d' % ply.Exp)
            elif slt == 1:
                ply.Exp = ply.Exp + 1000000
                ply.SendTipInfo('当前经验为：%d' % ply.Exp)
            elif slt == 2:
                ply.Exp = ply.Exp + 10000000
                ply.SendTipInfo('当前经验为：%d' % ply.Exp)
            elif slt == 3:
                ply.Exp = ply.Exp + 100000000
                ply.SendTipInfo('当前经验为：%d' % ply.Exp)
            elif slt == 4:
                if ply.Exp >= 100000:
                    ply.Exp = ply.Exp - 100000
                    ply.SendTipInfo('当前经验为：%d' % ply.Exp)
                else:
                    ply.SendTipInfo('当前经验不足！')
            elif slt == 5:
                if ply.Exp >= 1000000:
                    ply.Exp = ply.Exp - 1000000
                    ply.SendTipInfo('当前经验为：%d' % ply.Exp)
                else:
                    ply.SendTipInfo('当前经验不足！')
            elif slt == 6:
                if ply.Exp >= 10000000:
                    ply.Exp = ply.Exp - 10000000
                    ply.SendTipInfo('当前经验为：%d' % ply.Exp)
                else:
                    ply.SendTipInfo('当前经验不足！')
            elif slt == 7:
                if ply.Exp >= 100000000:
                    ply.Exp = ply.Exp - 100000000
                    ply.SendTipInfo('当前经验为：%d' % ply.Exp)
                else:
                    ply.SendTipInfo('当前经验不足！')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 2400:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp + 100000
                    ply.SendTipInfo('队员的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('你的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp + 1000000
                    ply.SendTipInfo('队员的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('你的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp + 10000000
                    ply.SendTipInfo('队员的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('你的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp + 100000000
                    ply.SendTipInfo('队员的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('你的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Exp >= 100000:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp - 100000
                    ply.SendTipInfo('队员的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('你的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前经验不足！')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Exp >= 1000000:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp - 1000000
                    ply.SendTipInfo('队员的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('你的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前经验不足！')
            elif slt == 6:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Exp >= 10000000:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp - 10000000
                    ply.SendTipInfo('队员的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('你的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前经验不足！')
            elif slt == 7:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Exp >= 100000000:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp - 100000000
                    ply.SendTipInfo('队员的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('你的当前经验为：%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('问题：队长必须是ＧＭ；只能组一个队员；队员当前经验不足！')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        
    elif step == 0:
        str = '\n\
　　  　　　　　#5排行榜\n\
\n\
　　#6#S十大高手排行榜#E\n\
　　#S十大富翁排行榜#E\n\
　　#S十大英雄排行榜#E\n\
\n\
#S我要技能点#E\n\
\n\
\n\
\n\
\n\
　　　　　　　　#S退  出#E#0'
        bxqt_tell(npc, ply, str)
        bxqt_set_step(npc, ply, 1)
    elif step == 1:
        if slt == 0:
            ttLevelMsg = '\n\
　　　　  　　　#5十大高手#6\n\
\n\
'
            ttLevelMsg += bxqt_get_tt_level()
            ttLevelMsg += '\n\
\n\
　　　　#5#S返　回#E　　　　　　　#S退  出#E#0'
            bxqt_tell(npc, ply, ttLevelMsg)
            bxqt_set_step(npc, ply, 2)
        elif slt == 1:
            ttLevelMsg = '\n\
　　　　　  　　#5十大富翁#6\n\
\n\
\n\
'
            ttLevelMsg += bxqt_get_tt_money()
            ttLevelMsg += '\n\
\n\
　　　　#5#S返　回#E　　　　　　　#S退  出#E#0'
            bxqt_tell(npc, ply, ttLevelMsg)
            bxqt_set_step(npc, ply, 2)
        elif slt == 2:
            theWorld = bxqt_get_world()
            ttLevelMsg = '\n\
　　　　　  　　#5十大英雄#6\n\
\n\
\n\
'
            ttLevelMsg += theWorld.HeroHand
            ttLevelMsg += '\n\
\n\
　　　　#5#S返　回#E　　　　　　　#S退  出#E#0'
            bxqt_tell(npc, ply, ttLevelMsg)
            bxqt_set_step(npc, ply, 2)
        elif slt == 3:
            if ply.SkillValue < 100:
                ply.SkillValue = ply.SkillValue + 1
                ply.SendTipInfo('当前技能点为：%d' % ply.SkillValue)
            else:
                bxqt_end_talk(ply)
        else:
            bxqt_end_talk(ply)
    elif step == 2:
        if slt == 0:
            str = '\n\
　　  　　　　　#5排行榜\n\
\n\
　　#6#S十大高手排行榜#E\n\
　　#S十大富翁排行榜#E\n\
　　#S十大英雄排行榜#E\n\
\n\
#S我要技能点#E\n\
\n\
\n\
\n\
\n\
　　　　　　　　#S退  出#E#0'
            bxqt_tell(npc, ply, str)
            bxqt_set_step(npc, ply, 1)
        elif slt == 1:
            bxqt_end_talk(ply)
        
    

