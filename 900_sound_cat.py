# File: 9 (Python 2.3)

from BXQT import *
from whrandom import randint
STR_SOUND_FILE = [
    'snd\\0221-è��1_s.wav',
    'snd\\0222-è��2_s.wav']

#ply.GetGoodsBar(2,0)���1��3�е���Ʒ
#ply.DelGoodsAtBar(goods.Id,1)ɾ��1��goods
#ply.GiveGoods2Bar(goods.Id,0)��1��,0����Ʒ�ȼ���
#ply.CountGoodsAtBar(goods.Id)������

#custom_function���
#CountBar(ply)�ո���������
#CountEmptyBarID(ply)[0]
#CountEmptyBarID(ply)[1]���ؿո��ӵ�λ�� �ֱ��ӦGetGoodsBar()��ǰ��������
#��CountBarȷ���ո���������Ȼ��CountEmptyBarIDȷ����һ���ո���λ�ã�Ȼ��GiveGoods2Bar�����GetGoodsBar��ø��Ķ��� ����������

#ply.AddMoney(100)
#ply.Exp
#ply.Level
#ply.PropertyValue
#ply.Convert2Npc.SetProperty(1,1,1)

#ply.SendTipInfo('')
#ply.SendChatWord('')


#npc.Life
#npc.MaxLife

#goods.GetProperty(j,i) ij
#0��ͷ�ǳ������� 017������ȦƷ��018��ǰ�;�016������ʣ��ʱ��30000��ı���
#116������ʣ��ʱ����118����;�
#20�������22����23����24�ǻ�25����26����27׷��28���29����210����211-214�ķ�216�������������217�����id��

#sce.IsAttack
#sce.IsArena
#sce,PlyNumb
#sce.GetPly(0)
#sce.SendTipInfo()
#sce.SendChatWord()

#world.SendChatWord()

def setstrlen(str, n):# ����str���ȵ�n
    while(len(str) < n):
        str = str + ' '
    return str

def page0(npc,ply,step,slt): #��ʼҳ��
    str = ''
    str = str + '#7��ϲ�㷢�ֲ���ר��#0\n'
    str = str + '\n'
    str = str + '#5#S��ʾ��ɫ����#E\n'                        #0
    str = str + '#S��ʾ��һ����Ʒ����#E\n'                    #1
    str = str + '#S�ı��һ����Ʒ����״̬�����µ�¼�ɼ���#E\n'#2
    str = str + '#S�������\n#E'                              #3
    str = str + '#S����û��Ӧ#E\n'                            #4
    str = str + '#S��ʾ����Event#E\n'                        #5
    str = str + '\n'
    str = str + '#S�˳�#E#0'
    ply.Tell(str)

def showgoods(ply, goods):  #��ʾ��Ʒ����
    # ply.SendChatWord('%s' % type(goods)) # <type 'Goods'>
    # ply.SendChatWord('%s' % dir(goods))  # []
    # ply.SendChatWord('%s' % hasattr(goods, 'Id')) # True
    str1 = '��    ��: %s' % goods.Name
    str1 = setstrlen(str1, 30)
    str1 = str1 + 'Id:       %s' % goods.Id
    ply.SendChatWord(str1)  #
    str1 = '��    ��: %s' % goods.Type
    str1 = setstrlen(str1, 30)
    str1 = str1 + '��    ��: %s' % goods.Level
    ply.SendChatWord(str1)
    str1 = '��Ҫ�ȼ�: %s' % goods.RequirLevel
    str1 = setstrlen(str1, 30)
    str1 = str1 + '�;�����: %s' % goods.getHardiness
    ply.SendChatWord(str1)
    str1 = '�ܷ�����: %s' % goods.EnableBuy
    str1 = setstrlen(str1, 30)
    str1 = str1 + ''
    ply.SendChatWord(str1)
    # str1 = ' '
    # str1 = setstrlen(str1, 30)
    # str1 = str1 + ' '
    # ply.SendChatWord(str1)
    for i in range(20):
        for j in range(100):
            if goods.GetProperty(j, i) != 0:
                str1 = ''
                str1 = str1 + '%d' % i
                str1 = setstrlen(str1, 5)
                str1 = str1 + '%d' % j
                str1 = setstrlen(str1, 10)
                str1 = str1 + '=  %s' % goods.GetProperty(j, i)
                ply.SendChatWord(str1)
    # for k in dir(goods): # dir ����[]
    # ply.SendChatWord('��Ա�������£�')
    # ply.SendChatWord('%s:       %s' %  (k, getattr(goods,k)))
    ply.SendChatWord('-----------------------------------------------------------------')

def showplyevent(ply):      #��ʾ����Event
    ply.SendChatWord('�������֣�%s' % ply.Name)
    j = 0
    str = ''
    for i in range(0,2001):
        value = ply.GetEvent(i)
        if value != 0:
            j = j + 1
            str = str + setstrlen('%d:' % i, 6) + setstrlen('%d' % value, 10)
            if j % 4 == 0:
                ply.SendChatWord(str)
                str = ''
    if len(str) != 0:
        ply.SendChatWord(str)
    ply.SendChatWord('-----------------------------------------------------------------')


def OnClick(npc, ply, step, slt):
    ply.PlaySound(STR_SOUND_FILE[randint(0, len(STR_SOUND_FILE) - 1)])
    if ply.Name == 'GM_NSY960' and ply.IsGM:
        if step == 0:
            page0(npc,ply,step,slt)
            ply.TalkStep = 1
        elif step == 1:
            if slt == 0:
                str = '\n\n\n\n  #2ɫä���߿�#0 #11#0 #22#0 #33#0 #44#0 #55#0 #66#0 #77#0 #88#0 #99#0'
                ply.SingleTell(str)
            elif slt == 1:
                goods = ply.GetGoodsBar(0,0)
                if goods.IsValid:
                    showgoods(ply, goods)
                    ply.SendTipInfo('ע�⿴������')
                    ply.EndTalk()
                else:
                    ply.SingleTell('\n\n\n\n    �ֵ��������ŵ�һ�񣡣�')
            elif slt == 2:
                goods = ply.GetGoodsBar(0,0)
                if goods.IsValid:
                    if goods.EnableBuy == 0:
                        goods.EnableBuy = 1
                        ply.SendTipInfo('�Ѿ���Ϊ�ɽ��ף������µ�¼')
                    elif goods.EnableBuy == 1:
                        goods.EnableBuy = 0
                        ply.SendTipInfo('�Ѿ���Ϊ���ɽ��ף����µ�¼��������ʰȡ��Ч')
                    else:
                        ply.SendTipInfo('Warning��%s' % goods.EnableBuy)
                    ply.EndTalk()
                else:
                    ply.SingleTell('\n\n\n\n  �ֵ��������ŵ�һ��')
            elif slt == 3:
                str = '#5'
                str = str + '#S����824#E\n'   #0
                str = str + '#S����825#E\n'   #1
                str = str + '#Sɮ��834#E\n'   #2
                str = str + '#S����835#E\n'   #3
                str = str + '#S����836#E\n'   #4
                str = str + '\n'
                str = str + '#S+1#E\n'        #5
                str = str + '#S-1#E\n'        #6
                str = str + '\n'
                str = str + '#S����#E\n'        #7
                str = str + '\n'
                str = str + '#S�˳�#E#0'      #8
                ply.Tell(str)
                ply.SendChatWord('��ǰ������룺 %s' % ply.OriginSprId)
                ply.TalkStep = 100 #�������
            elif slt == 4:
                i = randint(0, 100)
                ply.SendTipInfo('����(%s)' % i)
                return
            elif slt == 5:
                showplyevent(ply)
                ply.SendTipInfo('ע�⿴������')
                ply.EndTalk()
            else:
                ply.EndTalk()
        elif step == 100: #�������
            if slt >= 0 and slt <= 4:
                dict_waiguan = {0: 824, 1: 825, 2: 834, 3: 835, 4: 836}
                ply.OriginSprId = dict_waiguan[slt]
                ply.SendTipInfo('�任�ɹ�����ǰ�������Ϊ%s' % ply.OriginSprId)
            elif slt == 5:
                ply.OriginSprId = ply.OriginSprId + 1
                ply.SendTipInfo('�任�ɹ�����ǰ�������Ϊ%s' % ply.OriginSprId)
            elif slt == 6:
                ply.OriginSprId = ply.OriginSprId - 1
                ply.SendTipInfo('�任�ɹ�����ǰ�������Ϊ%s' % ply.OriginSprId)
            elif slt == 7:
                page0(npc, ply, step, slt)
                ply.TalkStep = 1
            else:
                ply.EndTalk()






