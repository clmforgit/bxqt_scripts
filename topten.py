# File: t (Python 2.3)

from BXQT import *
from wupin_list import *

def OnClick(npc, ply, step, slt):
    if ply.IsGM and 'GM_NSY960' == ply.Name:
        str = '��������������#3�ǣ͹����̨#0\n\
\n\
#5#S�ҵĵȼ�#E��#S�ҵĴ���#E��#S�ҵ�����#E��#S�ҵļ���#E\n\
\n\
#5#S��Ա�ȼ�#E��#S��Ա����#E��#S��Ա����#E��#S��Ա����#E\n\
\n\
#S�ҵ�pkֵ#E��#S�ҵ�ѩ��#E��#S�ҵ���Ʒ#E��#S�ҵı���#E\n\
\n\
#S������Ʒ#E��#S������#E��#S��Ҫ�޵�#E��#Sά������#E\n\
\n\
#S�鿴ʮ��#E��#SNPC����#E�� #S��Ҫ����#E��#S��Ա����#E\n\
\n\
#S�ҵİﹱ#E��#S�������#E��#S�ҵĳ���#E��#S��Աpkֵ#E\n\
\n\
#S������Ϣ#E��#S��ͼ��Ϣ#E��#S�������#E��#S�졡����#E\n\
#S�ҵľ���#E��#S��Ա����#E\n\
#S�� ��#E#0'
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
                ply.Tell('����������������#3�ҵĵȼ�#0\n\
\n\
#5#S+1��#E����#S+5��#E����#S+10��#E����#S+50��#E\n\
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
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 100
            elif slt == 1:
                ply.Tell('��������������#3���Ҵ��쾭��#0\n\
\n\
#5#S+1W#E����#S+10W#E����#S+100W#E����#S+750W#E\n\
\n\
#S-1W#E����#S-10W#E����#S-100W#E����#S-750W#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 200
            elif slt == 2:
                ply.Tell('��������������#3�ҵ����Ե�#0\n\
\n\
#5#S+1#E����#S+10#E����#S+100#E����#S+1000#E\n\
\n\
#S-1#E����#S-10#E����#S-100#E����#S-1000#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 300
            elif slt == 3:
                ply.Tell('��������������#3�ҵļ��ܵ�#0\n\
\n\
#5#S+1#E����#S+10#E����#S+100#E����#S-1#E����#S-10#E����#S-100#E\n\
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
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 400
            elif slt == 4:
                ply.Tell('����������������#3��Ա�ȼ�#0\n\
\n\
#5#S+1��#E����#S+5��#E����#S+10��#E����#S+50��#E\n\
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
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 500
            elif slt == 5:
                ply.Tell('��������������#3��Ա���쾭��#0\n\
\n\
#5#S+1W#E����#S+10W#E����#S+100W#E����#S+1000W#E\n\
\n\
#S-1W#E����#S-10W#E����#S-100W#E����#S-1000W#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 600
            elif slt == 6:
                ply.Tell('��������������#3��Ա���Ե�#0\n\
\n\
#5#S+1#E����#S+10#E����#S+100#E����#S+1000#E\n\
\n\
#S-1#E����#S-10#E����#S-100#E����#S-1000#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 700
            elif slt == 7:
                ply.Tell('��������������#3��Ա���ܵ�#0\n\
\n\
#5#S+1#E����#S+10#E����#S+100#E����#S-1#E����#S-10#E����#S-100#E\n\
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
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 800
            elif slt == 8:
                ply.Tell('��������������#3�ҵ�pkֵ#0\n\
\n\
#5#S+1#E����#S+10#E����#S+100#E����#S-1#E����#S-10#E����#S-100#E\n\
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
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 900
            elif slt == 9:
                ply.Tell('����������������#3�ҵ�ѩ��#0\n\
\n\
#5#S+1000ѩ��#E����#S+1Wѩ��#E����#S+10Wѩ��#E\n\
\n\
#S+100Wѩ��#E����#S+1000Wѩ��#E����#S+1��ѩ��#E\n\
\n\
#S-1000ѩ��#E����#S-1Wѩ��#E����#S-10Wѩ��#E\n\
\n\
#S-100Wѩ��#E����#S-1000Wѩ��#E����#S-1��ѩ��#E\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 1000
            elif slt == 10:
                ply.Tell('������������ #3��Ʒ����������#0\n\
\n\
�뽫Ҫ��������Ʒ������Ʒ����һ�񣬲�ѡ����Ҫ�ĵȼ���\n\
\n\
#5#S1��#E��#S2��#E��#S3��#E��#S4��#E��#S5��#E��#S6��#E��#S7��#E\n\
\n\
#S��Ʒ����#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 1100
            elif slt == 11:
                ply.Tell('����������������#3�ǣͱ���#0\n\
\n\
#5#S���ֵ�#E��#S20����#E��#S40����#E��#S60����#E��#S80����#E\n\
\n\
#S���ֹ�#E��#S20����#E��#S40����#E��#S60����#E��#S80����#E\n\
\n\
#S���ֵ�#E��#S20����#E��#S40����#E��#S60����#E��#S80����#E\n\
\n\
#S���ֽ�#E��#S20����#E��#S40����#E��#S60����#E��#S80����#E\n\
\n\
#S����ɮ#E��#S20��ɮ#E��#S40��ɮ#E��#S60��ɮ#E��#S80��ɮ#E\n\
\n\
#S����ָ��Ա#E��#S�ٶ�֮ì#E��#S��ѩ����#E��#SС���#E\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 1200
            elif slt == 12:
                ply.Tell('����������������#3������Ʒ#0\n\
\n\
#5#SСѪƿ99��#E����#S��Ѫƿ99��#E����#S��Ѫƿ99��#E\n\
\n\
#SС��ƿ99��#E����#S�о�ƿ99��#E����#S��ƿ99��#E\n\
\n\
#SСѪ��99��#E����#S��Ѫ��99��#E����#S��Ѫ��99��#E\n\
\n\
#S��Ʒ����ϵͳ����#E\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 1300
            elif slt == 13:
                str1 = '����������������#3��ȡ����#0\n\
\n\
#5'
                jishu = 0
                yshu = 1
                while jishu < feny:
                    if jishu < len(GUAIWU_LIST):
                        str1 = str1 + '#S' + GUAIWU_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S��#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '��'
                str1 = str1 + '\n\
\n\
'
                if jishu < len(GUAIWU_LIST):
                    str1 = str1 + '#S��ҳ#E��'
                
                yshu = yshu + 1
                str1 = str1 + '#S����#E��#S�˳�#E#0'
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                str1 = str1 + '\n\
%s��%s��%s��%s��%s��%s��%s��%s' % (ID_JISHU_BAK, ID_YSHU_BAK, jishu, yshu, ID_JISHU, ID_YSHU, ply.GetEvent(ID_JISHU), ply.GetEvent(ID_YSHU))
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
                ply.SendTipInfo('�޵��������óɹ���')
            elif slt == 15:
                bxqt_get_world().SendChatWord('<ϵͳ>�����������������Ӻ�����������ά������ԣ�Լ����Ӻ�ָ��������Ҽ�ʱ���߱��棬�Ա������ݵĶ�ʧ���𻵣�лл��ҳ���������֧����񰮣����ǽ�Ŭ���������õ���Ϸ�������ô����ĸ�Ϊ��죡')
            elif slt == 16:
                ply.Tell('���������������� #3���а�#0\n\
\n\
����#6#Sʮ��������а�#E\n\
����#Sʮ�������а�#E\n\
����#Sʮ��Ӣ�����а�#E\n\
����#6#S����׷ɱ��#E\n\
\n\
\n\
\n\
\n\
\n\
#5#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 1500
            elif slt == 17:
                str1 = '����������������#3NPC����#0\n\
\n\
#5'
                jishu = 0
                yshu = 1
                while jishu < feny:
                    if jishu < len(NPC_LIST):
                        str1 = str1 + '#S' + NPC_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S��#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '��'
                str1 = str1 + '\n\
\n\
'
                if jishu < len(NPC_LIST):
                    str1 = str1 + '#S��ҳ#E��'
                
                yshu = yshu + 1
                str1 = str1 + '#S����#E��#S�˳�#E#0'
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                str1 = str1 + '\n\
%s��%s��%s��%s��%s��%s��%s��%s' % (ID_JISHU_BAK, ID_YSHU_BAK, jishu, yshu, ID_JISHU, ID_YSHU, ply.GetEvent(ID_JISHU), ply.GetEvent(ID_YSHU))
                ply.Tell(str1)
                ply.TalkStep = 1401
            elif slt == 18:
                ply.Tell('����������������#3�ҵ�����#0\n\
\n\
#5#S+1#E����#S+100#E����#S+1000#E����#S+1W#E\n\
\n\
#S-1#E����#S-100#E����#S-1000#E����#S-1W#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 1600
            elif slt == 19:
                ply.Tell('����������������#3��Ա����#0\n\
\n\
#5#S+1#E����#S+100#E����#S+1000#E����#S+1W#E\n\
\n\
#S-1#E����#S-100#E����#S-1000#E����#S-1W#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 1700
            elif slt == 20:
                ply.Tell('����������������#3�ҵİﹱ#0\n\
\n\
#5#S+1#E����#S+40#E����#S+100#E\n\
\n\
#S-1#E����#S-40#E����#S-100#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 1800
            elif slt == 21:
                ply.Tell('��������������#3�ҵİ������#0\n\
\n\
#5#S+1#E����#S+50#E����#S+100#E\n\
\n\
#S-1#E����#S-50#E����#S-100#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 1900
            elif slt == 22:
                if ply.Pet.IsValid:
                    ply.Tell('��������������#3�޸ĳ�������#0\n\
\n\
#5#S���ӳ��ﾭ��#E\n\
#5#S��������#E #5#S���Ӽ��ܵȼ�#E\n\
#5#S������С������#E #5#S�������������#E\n\
#5#S�����������#E\n\
#5#S��������#E #5#S���Ӷ���#E\n\
#5#S+���#E #5#S+���#E #5#S+����#E #5#S+����#E\n\
#S�� ��#E#0')
                    ply.TalkStep = 2000
                else:
                    ply.SendTipInfo('��ĳ����أ�')
            elif slt == 23:
                ply.Tell('��������������#3��Աpkֵ#0\n\
\n\
#5#S+1#E����#S+10#E����#S+100#E����#S-1#E����#S-10#E����#S-100#E\n\
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
#S����#E\t\t#S�˳�#E#0')
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
                strs = '������Ҽ�λ���뼶��'
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
                            strs = '������:%s ��ͼ:%s ����:%s:%s �ȼ�:%d��' % (str1, str2, str3, str4, ply_sce.Level)
                            ply.SendChatWord(strs)
                            psum = psum + 1
                            continue
                ply.SendChatWord('������ҹ��ƣ�%d��' % psum)
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
                    strs = '%s NPC�����嵥��' % sce.Name
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
                            strs = '��NPC��:%s ID_TYPE:%s ����:%s:%s IdForMap:%d��' % (str1, str2, str3, str4, numb)
                            ply.SendChatWord(strs)
                        
                        numb = numb + 1
                        Npc = sce.GetNpcByNpcId(numb)
                    ply.SendChatWord('%s ������NPC��%d��' % (sce.Name, numb))
                
            elif slt == 26:
                if 'GM_NSY960' == ply.Name:
                    ply.Tell('\n\
\n\
����ǰ��۴���Ϊ��#3%d#0\n\
\n\
#5#S��һ��#E����#S��һ��#E\n\
\n\
#S�ر�#E#0' % ply.OriginSprId)
                    ply.TalkStep = 2200
                
            elif slt == 27:
                if 'GM_NSY960' == ply.Name:
                    if ply.GetGoodsBar(0, 0).IsValid == 0 and ply.GetGoodsBar(1, 0).IsValid == 0:
                        ply.GiveGoods2Bar(872, 0)
                        ply.GiveGoods2Bar(872, 0)
                        ply.GetGoodsBar(0, 0).EnableBuy = 0
                        ply.GetGoodsBar(1, 0).EnableBuy = 0
                    else:
                        ply.SendTipInfo('�����Ʒ��ǰ������գ�')
                
            elif slt == 28:
                ply.Tell('����������������#3�ҵľ���#0\n\
\n\
#5#S+10��#E����#S+100��#E����#S+1000��#E����#S+1��#E\n\
\n\
#S-10��#E����#S-100��#E����#S-1000��#E����#S-1��#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 2300
            elif slt == 29:
                ply.Tell('����������������#3��Ա����#0\n\
\n\
#5#S+10��#E����#S+100��#E����#S+1000��#E����#S+1��#E\n\
\n\
#S-10��#E����#S-100��#E����#S-1000��#E����#S-1��#E\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 2400
            else:
                ply.EndTalk()
        elif step == 100:
            if slt == 0:
                if ply.Level < 99:
                    ply.Level = ply.Level + 1
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Level)
                else:
                    ply.SendTipInfo('�������ȼ����ޣ��޷�������')
            elif slt == 1:
                if ply.Level < 95:
                    ply.Level = ply.Level + 5
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Level)
                else:
                    ply.SendTipInfo('�������ȼ����ޣ��޷�������')
            elif slt == 2:
                if ply.Level < 90:
                    ply.Level = ply.Level + 10
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Level)
                else:
                    ply.SendTipInfo('�������ȼ����ޣ��޷�������')
            elif slt == 3:
                if ply.Level < 50:
                    ply.Level = ply.Level + 50
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Level)
                else:
                    ply.SendTipInfo('�������ȼ����ޣ��޷�������')
            elif slt == 4:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 200:
            if slt == 0:
                ply.FourdyScore = ply.FourdyScore + 10000
                ply.SendTipInfo('��ǰ���쾭��Ϊ��%d' % ply.FourdyScore)
            elif slt == 1:
                ply.FourdyScore = ply.FourdyScore + 100000
                ply.SendTipInfo('��ǰ���쾭��Ϊ��%d' % ply.FourdyScore)
            elif slt == 2:
                ply.FourdyScore = ply.FourdyScore + 1000000
                ply.SendTipInfo('��ǰ���쾭��Ϊ��%d' % ply.FourdyScore)
            elif slt == 3:
                ply.FourdyScore = ply.FourdyScore + 7500000
                ply.SendTipInfo('��ǰ���쾭��Ϊ��%d' % ply.FourdyScore)
            elif slt == 4:
                if ply.FourdyScore >= 10000:
                    ply.FourdyScore = ply.FourdyScore - 10000
                    ply.SendTipInfo('��ǰ���쾭��Ϊ��%d' % ply.FourdyScore)
                else:
                    ply.SendTipInfo('��ǰ���쾭�鲻�㣡')
            elif slt == 5:
                if ply.FourdyScore >= 100000:
                    ply.FourdyScore = ply.FourdyScore - 100000
                    ply.SendTipInfo('��ǰ���쾭��Ϊ��%d' % ply.FourdyScore)
                else:
                    ply.SendTipInfo('��ǰ���쾭�鲻�㣡')
            elif slt == 6:
                if ply.FourdyScore >= 1000000:
                    ply.FourdyScore = ply.FourdyScore - 1000000
                    ply.SendTipInfo('��ǰ���쾭��Ϊ��%d' % ply.FourdyScore)
                else:
                    ply.SendTipInfo('��ǰ���쾭�鲻�㣡')
            elif slt == 7:
                if ply.FourdyScore >= 7500000:
                    ply.FourdyScore = ply.FourdyScore - 7500000
                    ply.SendTipInfo('��ǰ���쾭��Ϊ��%d' % ply.FourdyScore)
                else:
                    ply.SendTipInfo('��ǰ���쾭�鲻�㣡')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 300:
            if slt == 0:
                ply.PropertyValue = ply.PropertyValue + 1
                ply.SendTipInfo('��ǰ���Ե�Ϊ��%d' % ply.PropertyValue)
            elif slt == 1:
                ply.PropertyValue = ply.PropertyValue + 10
                ply.SendTipInfo('��ǰ���Ե�Ϊ��%d' % ply.PropertyValue)
            elif slt == 2:
                ply.PropertyValue = ply.PropertyValue + 100
                ply.SendTipInfo('��ǰ���Ե�Ϊ��%d' % ply.PropertyValue)
            elif slt == 3:
                ply.PropertyValue = ply.PropertyValue + 1000
                ply.SendTipInfo('��ǰ���Ե�Ϊ��%d' % ply.PropertyValue)
            elif slt == 4:
                if ply.PropertyValue >= 1:
                    ply.PropertyValue = ply.PropertyValue - 1
                    ply.SendTipInfo('��ǰ���Ե�Ϊ��%d' % ply.PropertyValue)
                else:
                    ply.SendTipInfo('��ǰ���Ե㲻�㣡')
            elif slt == 5:
                if ply.PropertyValue >= 10:
                    ply.PropertyValue = ply.PropertyValue - 10
                    ply.SendTipInfo('��ǰ���Ե�Ϊ��%d' % ply.PropertyValue)
                else:
                    ply.SendTipInfo('��ǰ���Ե㲻�㣡')
            elif slt == 6:
                if ply.PropertyValue >= 100:
                    ply.PropertyValue = ply.PropertyValue - 100
                    ply.SendTipInfo('��ǰ���Ե�Ϊ��%d' % ply.PropertyValue)
                else:
                    ply.SendTipInfo('��ǰ���Ե㲻�㣡')
            elif slt == 7:
                if ply.PropertyValue >= 1000:
                    ply.PropertyValue = ply.PropertyValue - 1000
                    ply.SendTipInfo('��ǰ���Ե�Ϊ��%d' % ply.PropertyValue)
                else:
                    ply.SendTipInfo('��ǰ���Ե㲻�㣡')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 400:
            if slt == 0:
                ply.SkillValue = ply.SkillValue + 1
                ply.SendTipInfo('��ǰ���ܵ�Ϊ��%d' % ply.SkillValue)
            elif slt == 1:
                ply.SkillValue = ply.SkillValue + 10
                ply.SendTipInfo('��ǰ���ܵ�Ϊ��%d' % ply.SkillValue)
            elif slt == 2:
                ply.SkillValue = ply.SkillValue + 100
                ply.SendTipInfo('��ǰ���ܵ�Ϊ��%d' % ply.SkillValue)
            elif slt == 3:
                if ply.SkillValue >= 1:
                    ply.SkillValue = ply.SkillValue - 1
                    ply.SendTipInfo('��ǰ���ܵ�Ϊ��%d' % ply.SkillValue)
                else:
                    ply.SendTipInfo('��ǰ���ܵ㲻�㣡')
            elif slt == 4:
                if ply.SkillValue >= 10:
                    ply.SkillValue = ply.SkillValue - 10
                    ply.SendTipInfo('��ǰ���ܵ�Ϊ��%d' % ply.SkillValue)
                else:
                    ply.SendTipInfo('��ǰ���ܵ㲻�㣡')
            elif slt == 5:
                if ply.SkillValue >= 100:
                    ply.SkillValue = ply.SkillValue - 100
                    ply.SendTipInfo('��ǰ���ܵ�Ϊ��%d' % ply.SkillValue)
                else:
                    ply.SendTipInfo('��ǰ���ܵ㲻�㣡')
            elif slt == 6:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 500:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Level < 99:
                    ply.GetTeamMember(1).Level = ply.GetTeamMember(1).Level + 1
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Level)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Level)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա�������ȼ����ޣ��޷�������')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Level < 95:
                    ply.GetTeamMember(1).Level = ply.GetTeamMember(1).Level + 5
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Level)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Level)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա�������ȼ����ޣ��޷�������')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Level < 90:
                    ply.GetTeamMember(1).Level = ply.GetTeamMember(1).Level + 10
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Level)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Level)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա�������ȼ����ޣ��޷�������')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Level < 50:
                    ply.GetTeamMember(1).Level = ply.GetTeamMember(1).Level + 50
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Level)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Level)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա�������ȼ����ޣ��޷�������')
            elif slt == 4:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 600:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore + 10000
                    ply.SendTipInfo('��Ա�ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore + 100000
                    ply.SendTipInfo('��Ա�ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore + 1000000
                    ply.SendTipInfo('��Ա�ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore + 7500000
                    ply.SendTipInfo('��Ա�ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).FourdyScore >= 10000:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore - 10000
                    ply.SendTipInfo('��Ա�ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���쾭�鲻�㣡')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).FourdyScore >= 100000:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore - 100000
                    ply.SendTipInfo('��Ա�ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���쾭�鲻�㣡')
            elif slt == 6:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).FourdyScore >= 1000000:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore - 1000000
                    ply.SendTipInfo('��Ա�ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���쾭�鲻�㣡')
            elif slt == 7:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).FourdyScore >= 7500000:
                    ply.GetTeamMember(1).FourdyScore = ply.GetTeamMember(1).FourdyScore - 7500000
                    ply.SendTipInfo('��Ա�ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���쾭��Ϊ��%d' % ply.GetTeamMember(1).FourdyScore)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���쾭�鲻�㣡')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 700:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue + 1
                    ply.SendTipInfo('��Ա�ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue + 10
                    ply.SendTipInfo('��Ա�ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue + 100
                    ply.SendTipInfo('��Ա�ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue + 1000
                    ply.SendTipInfo('��Ա�ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PropertyValue >= 1:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue - 1
                    ply.SendTipInfo('��Ա�ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���Ե㲻�㣡')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PropertyValue >= 10:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue - 10
                    ply.SendTipInfo('��Ա�ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���Ե㲻�㣡')
            elif slt == 6:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PropertyValue >= 100:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue - 100
                    ply.SendTipInfo('��Ա�ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���Ե㲻�㣡')
            elif slt == 7:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PropertyValue >= 1000:
                    ply.GetTeamMember(1).PropertyValue = ply.GetTeamMember(1).PropertyValue - 1000
                    ply.SendTipInfo('��Ա�ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���Ե�Ϊ��%d' % ply.GetTeamMember(1).PropertyValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���Ե㲻�㣡')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 800:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue + 1
                    ply.SendTipInfo('��Ա�ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue + 10
                    ply.SendTipInfo('��Ա�ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue + 100
                    ply.SendTipInfo('��Ա�ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).SkillValue >= 1:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue - 1
                    ply.SendTipInfo('��Ա�ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���ܵ㲻�㣡')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).SkillValue >= 10:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue - 10
                    ply.SendTipInfo('��Ա�ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���ܵ㲻�㣡')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).SkillValue >= 100:
                    ply.GetTeamMember(1).SkillValue = ply.GetTeamMember(1).SkillValue - 100
                    ply.SendTipInfo('��Ա�ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ���ܵ�Ϊ��%d' % ply.GetTeamMember(1).SkillValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���ܵ㲻�㣡')
            elif slt == 6:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 900:
            if slt == 0:
                ply.PkValue = ply.PkValue + 1
                ply.SendTipInfo('��ǰPKֵΪ��%d' % ply.PkValue)
            elif slt == 1:
                ply.PkValue = ply.PkValue + 10
                ply.SendTipInfo('��ǰPKֵΪ��%d' % ply.PkValue)
            elif slt == 2:
                ply.PkValue = ply.PkValue + 100
                ply.SendTipInfo('��ǰPKֵΪ��%d' % ply.PkValue)
            elif slt == 3:
                if ply.PkValue >= 1:
                    ply.PkValue = ply.PkValue - 1
                    ply.SendTipInfo('��ǰPKֵΪ��%d' % ply.PkValue)
                else:
                    ply.SendTipInfo('PKֵ�����㣡')
            elif slt == 4:
                if ply.PkValue >= 10:
                    ply.PkValue = ply.PkValue - 10
                    ply.SendTipInfo('��ǰPKֵΪ��%d' % ply.PkValue)
                else:
                    ply.SendTipInfo('PKֵ�����㣡')
            elif slt == 5:
                if ply.PkValue >= 100:
                    ply.PkValue = ply.PkValue - 100
                    ply.SendTipInfo('��ǰPKֵΪ��%d' % ply.PkValue)
                else:
                    ply.SendTipInfo('PKֵ�����㣡')
            elif slt == 6:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1000:
            if slt == 0:
                ply.AddMoney(1000)
                ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
            elif slt == 1:
                ply.AddMoney(10000)
                ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
            elif slt == 2:
                ply.AddMoney(100000)
                ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
            elif slt == 3:
                ply.AddMoney(1000000)
                ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
            elif slt == 4:
                ply.AddMoney(10000000)
                ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
            elif slt == 5:
                ply.AddMoney(100000000)
                ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
            elif slt == 6:
                if ply.Money >= 1000:
                    ply.AddMoney(-1000)
                    ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
                else:
                    ply.SendTipInfo('��ǰѩ�Ҳ��㣡')
            elif slt == 7:
                if ply.Money >= 10000:
                    ply.AddMoney(-10000)
                    ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
                else:
                    ply.SendTipInfo('��ǰѩ�Ҳ��㣡')
            elif slt == 8:
                if ply.Money >= 100000:
                    ply.AddMoney(-100000)
                    ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
                else:
                    ply.SendTipInfo('��ǰѩ�Ҳ��㣡')
            elif slt == 9:
                if ply.Money >= 10000000:
                    ply.AddMoney(-10000000)
                    ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
                else:
                    ply.SendTipInfo('��ǰѩ�Ҳ��㣡')
            elif slt == 10:
                if ply.Money >= 10000000:
                    ply.AddMoney(-10000000)
                    ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
                else:
                    ply.SendTipInfo('��ǰѩ�Ҳ��㣡')
            elif slt == 11:
                if ply.Money >= 1000000000:
                    ply.AddMoney(-1000000000)
                    ply.SendTipInfo('��ǰѩ��Ϊ��%d' % ply.Money)
                else:
                    ply.SendTipInfo('��ǰѩ�Ҳ��㣡')
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
                    ply.SendTipInfo('�뽫��Ʒ������Ʒ���ĵ�һ��')
            elif slt == 7:
                if ply.GetGoodsBar(0, 0).IsValid:
                    ID = ply.GetGoodsBar(0, 0).Id
                    ply.GiveGoods2Bar(ID, 0)
                else:
                    ply.SendTipInfo('�뽫��Ʒ������Ʒ���ĵ�һ��')
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
                ply.SendTipInfo('����ɹ���')
            elif slt > 4 and slt <= 9:
                ply.OriginSprId = 4006 + slt
                ply.Profession = 2
                ply.ProfLevel = slt - 5
                ply.SendTipInfo('����ɹ���')
            elif slt > 9 and slt <= 14:
                ply.OriginSprId = 4011 + slt
                ply.Profession = 3
                ply.ProfLevel = slt - 10
                ply.SendTipInfo('����ɹ���')
            elif slt > 14 and slt <= 19:
                ply.OriginSprId = 4016 + slt
                ply.Profession = 4
                ply.ProfLevel = slt - 15
                ply.SendTipInfo('����ɹ���')
            elif slt > 19 and slt <= 24:
                ply.OriginSprId = 4021 + slt
                ply.Profession = 5
                ply.ProfLevel = slt - 20
                ply.SendTipInfo('����ɹ���')
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
                bxqt_get_world().SendChatWord('<ϵͳ>�������Ӻ����ϣǣͽ�����ʯ�����ҷ���ҩƷ������Ҫ������뵽������')
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
                str1 = '����������������#3��ȡ����#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(GUAIWU_LIST):
                        str1 = str1 + '#S' + GUAIWU_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S��#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '��'
                str1 = str1 + '\n\
%s��pre1��%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S��ҳ#E��'
                
                if jishu < len(GUAIWU_LIST):
                    str1 = str1 + '#S��ҳ#E��'
                
                str1 = str1 + '#S����#E��#S�˳�#E#0'
                yshu = yshu + 1
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                ply.Tell(str1)
                ply.TalkStep = 1400
            elif slt == feny and jishu < len(GUAIWU_LIST):
                str1 = '����������������#3��ȡ����#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(GUAIWU_LIST):
                        str1 = str1 + '#S' + GUAIWU_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S��#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '��'
                str1 = str1 + '\n\
%s��next1��%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S��ҳ#E��'
                
                if jishu < len(GUAIWU_LIST):
                    str1 = str1 + '#S��ҳ#E��'
                
                str1 = str1 + '#S����#E��#S�˳�#E#0'
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
                str1 = '����������������#3��ȡ����#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(GUAIWU_LIST):
                        str1 = str1 + '#S' + GUAIWU_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S��#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '��'
                str1 = str1 + '\n\
%s��next2��%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S��ҳ#E��'
                
                if jishu < len(GUAIWU_LIST):
                    str1 = str1 + '#S��ҳ#E��'
                
                str1 = str1 + '#S����#E��#S�˳�#E#0'
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
                str1 = '����������������#3NPC����#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(NPC_LIST):
                        str1 = str1 + '#S' + NPC_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S��#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '��'
                str1 = str1 + '\n\
%s��pre1��%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S��ҳ#E��'
                
                if jishu < len(NPC_LIST):
                    str1 = str1 + '#S��ҳ#E��'
                
                str1 = str1 + '#S����#E��#S�˳�#E#0'
                yshu = yshu + 1
                ply.SetEvent(ID_JISHU, jishu)
                ply.SetEvent(ID_YSHU, yshu)
                ply.Tell(str1)
                ply.TalkStep = 1401
            elif slt == feny and jishu < len(NPC_LIST):
                str1 = '����������������#3NPC����#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(NPC_LIST):
                        str1 = str1 + '#S' + NPC_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S��#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '��'
                str1 = str1 + '\n\
%s��next1��%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S��ҳ#E��'
                
                if jishu < len(NPC_LIST):
                    str1 = str1 + '#S��ҳ#E��'
                
                str1 = str1 + '#S����#E��#S�˳�#E#0'
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
                str1 = '����������������#3NPC����#0\n\
\n\
#5'
                while jishu < yshu * feny:
                    if jishu < len(NPC_LIST):
                        str1 = str1 + '#S' + NPC_LIST[jishu][0] + '#E'
                    else:
                        str1 = str1 + '#S��#E'
                    jishu = jishu + 1
                    if 0 == divmod(jishu, 3)[1]:
                        str1 = str1 + '\n\
'
                        continue
                    str1 = str1 + '��'
                str1 = str1 + '\n\
%s��next2��%s\n\
' % (jishu, yshu)
                if jishu > feny:
                    str1 = str1 + '#S��ҳ#E��'
                
                if jishu < len(NPC_LIST):
                    str1 = str1 + '#S��ҳ#E��'
                
                str1 = str1 + '#S����#E��#S�˳�#E#0'
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
��������  ������#5ʮ�����#6\n\
\n\
'
                ttLevelMsg += bxqt_get_tt_level()
                ttLevelMsg += '\n\
\n\
��������#5#S������#E��������������#S��  ��#E#0'
                bxqt_tell(npc, ply, ttLevelMsg)
                bxqt_set_step(npc, ply, 1501)
            elif slt == 1:
                ttLevelMsg = '\n\
����������  ����#5ʮ����#6\n\
\n\
\n\
'
                ttLevelMsg += bxqt_get_tt_money()
                ttLevelMsg += '\n\
\n\
��������#5#S������#E��������������#S��  ��#E#0'
                bxqt_tell(npc, ply, ttLevelMsg)
                bxqt_set_step(npc, ply, 1501)
            elif slt == 2:
                theWorld = bxqt_get_world()
                ttLevelMsg = '\n\
����������  ����#5ʮ��Ӣ��#6\n\
\n\
\n\
'
                ttLevelMsg += theWorld.HeroHand
                ttLevelMsg += '\n\
\n\
��������#5#S������#E��������������#S��  ��#E#0'
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
                ply.Tell('���������������� #3���а�#0\n\
\n\
����#6#Sʮ��������а�#E\n\
����#Sʮ�������а�#E\n\
����#Sʮ��Ӣ�����а�#E\n\
����#6#S����׷ɱ��#E\n\
\n\
\n\
\n\
\n\
\n\
#5#S����#E\t\t#S�˳�#E#0')
                ply.TalkStep = 1500
            else:
                ply.EndTalk()
        elif step == 1600:
            if slt == 0:
                ply.ValueLeft = ply.ValueLeft + 1
                ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.ValueLeft)
            elif slt == 1:
                ply.ValueLeft = ply.ValueLeft + 100
                ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.ValueLeft)
            elif slt == 2:
                ply.ValueLeft = ply.ValueLeft + 1000
                ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.ValueLeft)
            elif slt == 3:
                ply.ValueLeft = ply.ValueLeft + 10000
                ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.ValueLeft)
            elif slt == 4:
                if ply.ValueLeft >= 1:
                    ply.ValueLeft = ply.ValueLeft - 1
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.ValueLeft)
                else:
                    ply.SendTipInfo('��ǰ�������㣡')
            elif slt == 5:
                if ply.ValueLeft >= 100:
                    ply.ValueLeft = ply.ValueLeft - 100
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.ValueLeft)
                else:
                    ply.SendTipInfo('��ǰ�������㣡')
            elif slt == 6:
                if ply.ValueLeft >= 1000:
                    ply.ValueLeft = ply.ValueLeft - 1000
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.ValueLeft)
                else:
                    ply.SendTipInfo('��ǰ�������㣡')
            elif slt == 7:
                if ply.ValueLeft >= 10000:
                    ply.ValueLeft = ply.ValueLeft - 10000
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.ValueLeft)
                else:
                    ply.SendTipInfo('��ǰ�������㣡')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1700:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft + 1
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft + 100
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft + 1000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft + 10000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).ValueLeft >= 1:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft - 1
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ�������㣡')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).ValueLeft >= 100:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft - 100
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ�������㣡')
            elif slt == 6:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).ValueLeft >= 1000:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft - 1000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ�������㣡')
            elif slt == 7:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).ValueLeft >= 10000:
                    ply.GetTeamMember(1).ValueLeft = ply.GetTeamMember(1).ValueLeft - 10000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).ValueLeft)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ�������㣡')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1800:
            if ply.Organize.IsValid == 0:
                ply.SendTipInfo('�㻹û�м�������أ�')
                return 0
            elif slt == 0:
                ply.Contribute = ply.Contribute + 1
                ply.SendTipInfo('��ǰ�ﹱΪ��%d' % ply.Contribute)
            elif slt == 1:
                ply.Contribute = ply.Contribute + 40
                ply.SendTipInfo('��ǰ�ﹱΪ��%d' % ply.Contribute)
            elif slt == 2:
                ply.Contribute = ply.Contribute + 100
                ply.SendTipInfo('��ǰ�ﹱΪ��%d' % ply.Contribute)
            elif slt == 3:
                if ply.Contribute >= 1:
                    ply.Contribute = ply.Contribute - 1
                    ply.SendTipInfo('��ǰ�ﹱΪ��%d' % ply.Contribute)
                else:
                    ply.SendTipInfo('��ǰ�ﹱ���㣡')
            elif slt == 4:
                if ply.Contribute >= 40:
                    ply.Contribute = ply.Contribute - 40
                    ply.SendTipInfo('��ǰ�ﹱΪ��%d' % ply.Contribute)
                else:
                    ply.SendTipInfo('��ǰ�ﹱ���㣡')
            elif slt == 5:
                if ply.Contribute >= 100:
                    ply.Contribute = ply.Contribute - 100
                    ply.SendTipInfo('��ǰ�ﹱΪ��%d' % ply.Contribute)
                else:
                    ply.SendTipInfo('��ǰ�ﹱ���㣡')
            elif slt == 6:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 1900:
            if ply.Organize.IsValid == 0:
                ply.SendTipInfo('�㻹û�м�������أ�')
                return 0
            elif slt == 0:
                ply.Organize.Honor = ply.Organize.Honor + 1
                ply.SendTipInfo('��ǰ�������Ϊ��%d' % ply.Organize.Honor)
            elif slt == 1:
                ply.Organize.Honor = ply.Organize.Honor + 50
                ply.SendTipInfo('��ǰ�������Ϊ��%d' % ply.Organize.Honor)
            elif slt == 2:
                ply.Organize.Honor = ply.Organize.Honor + 100
                ply.SendTipInfo('��ǰ�������Ϊ��%d' % ply.Organize.Honor)
            elif slt == 3:
                if ply.Organize.Honor >= 1:
                    ply.Organize.Honor = ply.Organize.Honor - 1
                    ply.SendTipInfo('��ǰ�������Ϊ��%d' % ply.Organize.Honor)
                else:
                    ply.SendTipInfo('��ǰ����������㣡')
            elif slt == 4:
                if ply.Organize.Honor >= 50:
                    ply.Organize.Honor = ply.Organize.Honor - 50
                    ply.SendTipInfo('��ǰ�������Ϊ��%d' % ply.Organize.Honor)
                else:
                    ply.SendTipInfo('��ǰ����������㣡')
            elif slt == 5:
                if ply.Organize.Honor >= 100:
                    ply.Organize.Honor = ply.Organize.Honor - 100
                    ply.SendTipInfo('��ǰ�������Ϊ��%d' % ply.Organize.Honor)
                else:
                    ply.SendTipInfo('��ǰ����������㣡')
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
                    ply.SendTipInfo('��Ա�ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PkValue = ply.GetTeamMember(1).PkValue + 10
                    ply.SendTipInfo('��Ա�ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).PkValue = ply.GetTeamMember(1).PkValue + 100
                    ply.SendTipInfo('��Ա�ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PkValue >= 1:
                    ply.GetTeamMember(1).PkValue = ply.GetTeamMember(1).PkValue - 1
                    ply.SendTipInfo('��Ա�ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰpkֵ���㣡')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PkValue >= 10:
                    ply.GetTeamMember(1).PkValue = ply.GetTeamMember(1).PkValue - 10
                    ply.SendTipInfo('��Ա�ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰpkֵ���㣡')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).PkValue >= 100:
                    ply.GetTeamMember(1).PkValue = ply.GetTeamMember(1).PkValue - 100
                    ply.SendTipInfo('��Ա�ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰpkֵΪ��%d' % ply.GetTeamMember(1).PkValue)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰpkֵ���㣡')
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
����ǰ��۴���Ϊ��#3%d#0\n\
\n\
#5#S��һ��#E����#S��һ��#E\n\
\n\
#S�ر�#E#0' % ply.OriginSprId)
                ply.TalkStep = 2200
            elif slt == 1:
                ply.OriginSprId = ply.OriginSprId + 1
                ply.Tell('\n\
\n\
����ǰ��۴���Ϊ��#3%d#0\n\
\n\
#5#S��һ��#E����#S��һ��#E\n\
\n\
#S�ر�#E#0' % ply.OriginSprId)
                ply.TalkStep = 2200
            else:
                ply.EndTalk()
        elif step == 2300:
            if slt == 0:
                ply.Exp = ply.Exp + 100000
                ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Exp)
            elif slt == 1:
                ply.Exp = ply.Exp + 1000000
                ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Exp)
            elif slt == 2:
                ply.Exp = ply.Exp + 10000000
                ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Exp)
            elif slt == 3:
                ply.Exp = ply.Exp + 100000000
                ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Exp)
            elif slt == 4:
                if ply.Exp >= 100000:
                    ply.Exp = ply.Exp - 100000
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Exp)
                else:
                    ply.SendTipInfo('��ǰ���鲻�㣡')
            elif slt == 5:
                if ply.Exp >= 1000000:
                    ply.Exp = ply.Exp - 1000000
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Exp)
                else:
                    ply.SendTipInfo('��ǰ���鲻�㣡')
            elif slt == 6:
                if ply.Exp >= 10000000:
                    ply.Exp = ply.Exp - 10000000
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Exp)
                else:
                    ply.SendTipInfo('��ǰ���鲻�㣡')
            elif slt == 7:
                if ply.Exp >= 100000000:
                    ply.Exp = ply.Exp - 100000000
                    ply.SendTipInfo('��ǰ����Ϊ��%d' % ply.Exp)
                else:
                    ply.SendTipInfo('��ǰ���鲻�㣡')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        elif step == 2400:
            if slt == 0:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp + 100000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 1:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp + 1000000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 2:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp + 10000000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 3:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp + 100000000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա��')
            elif slt == 4:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Exp >= 100000:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp - 100000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���鲻�㣡')
            elif slt == 5:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Exp >= 1000000:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp - 1000000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���鲻�㣡')
            elif slt == 6:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Exp >= 10000000:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp - 10000000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���鲻�㣡')
            elif slt == 7:
                if ply.TeamMemberNumb == 2 and ply.GetTeamMember(0).IsGM and ply.GetTeamMember(1).Exp >= 100000000:
                    ply.GetTeamMember(1).Exp = ply.GetTeamMember(1).Exp - 100000000
                    ply.SendTipInfo('��Ա�ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                    ply.GetTeamMember(1).SendTipInfo('��ĵ�ǰ����Ϊ��%d' % ply.GetTeamMember(1).Exp)
                else:
                    ply.SendTipInfo('���⣺�ӳ������ǣǣͣ�ֻ����һ����Ա����Ա��ǰ���鲻�㣡')
            elif slt == 8:
                bxqt_tell(npc, ply, str)
                bxqt_set_step(npc, ply, 1)
            else:
                ply.EndTalk()
        
    elif step == 0:
        str = '\n\
����  ����������#5���а�\n\
\n\
����#6#Sʮ��������а�#E\n\
����#Sʮ�������а�#E\n\
����#Sʮ��Ӣ�����а�#E\n\
\n\
#S��Ҫ���ܵ�#E\n\
\n\
\n\
\n\
\n\
����������������#S��  ��#E#0'
        bxqt_tell(npc, ply, str)
        bxqt_set_step(npc, ply, 1)
    elif step == 1:
        if slt == 0:
            ttLevelMsg = '\n\
��������  ������#5ʮ�����#6\n\
\n\
'
            ttLevelMsg += bxqt_get_tt_level()
            ttLevelMsg += '\n\
\n\
��������#5#S������#E��������������#S��  ��#E#0'
            bxqt_tell(npc, ply, ttLevelMsg)
            bxqt_set_step(npc, ply, 2)
        elif slt == 1:
            ttLevelMsg = '\n\
����������  ����#5ʮ����#6\n\
\n\
\n\
'
            ttLevelMsg += bxqt_get_tt_money()
            ttLevelMsg += '\n\
\n\
��������#5#S������#E��������������#S��  ��#E#0'
            bxqt_tell(npc, ply, ttLevelMsg)
            bxqt_set_step(npc, ply, 2)
        elif slt == 2:
            theWorld = bxqt_get_world()
            ttLevelMsg = '\n\
����������  ����#5ʮ��Ӣ��#6\n\
\n\
\n\
'
            ttLevelMsg += theWorld.HeroHand
            ttLevelMsg += '\n\
\n\
��������#5#S������#E��������������#S��  ��#E#0'
            bxqt_tell(npc, ply, ttLevelMsg)
            bxqt_set_step(npc, ply, 2)
        elif slt == 3:
            if ply.SkillValue < 100:
                ply.SkillValue = ply.SkillValue + 1
                ply.SendTipInfo('��ǰ���ܵ�Ϊ��%d' % ply.SkillValue)
            else:
                bxqt_end_talk(ply)
        else:
            bxqt_end_talk(ply)
    elif step == 2:
        if slt == 0:
            str = '\n\
����  ����������#5���а�\n\
\n\
����#6#Sʮ��������а�#E\n\
����#Sʮ�������а�#E\n\
����#Sʮ��Ӣ�����а�#E\n\
\n\
#S��Ҫ���ܵ�#E\n\
\n\
\n\
\n\
\n\
����������������#S��  ��#E#0'
            bxqt_tell(npc, ply, str)
            bxqt_set_step(npc, ply, 1)
        elif slt == 1:
            bxqt_end_talk(ply)
        
    

