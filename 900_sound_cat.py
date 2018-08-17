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

#goods.GetProperty(j,i) ij
#0��ͷ�ǳ������� 017������ȦƷ��018��ǰ�;�016������ʣ��ʱ��30000��ı���
#116������ʣ��ʱ����118����;�
#20�������22����23����24�ǻ�25����26����27׷��28���29����210����211-214�ķ�216�������������217�����id��

def setstrlen(str, n):# ����str���ȵ�n
    while(len(str) < n):
        str = str + ' '
    return str

def OnClick(npc, ply, step, slt):
    ply.PlaySound(STR_SOUND_FILE[randint(0, len(STR_SOUND_FILE) - 1)])
    if ply.Name == 'GM_NSY960' and ply.IsGM:
        if step == 0:
            str = ''
            str = str + '#7��ϲ�㷢�ֲ���ר��#0\n'
            str = str + '\n'
            str = str + '#5#S��ʾ��ɫ����#E\n'
            str = str + '#S��ʾ��һ����Ʒ����#E\n'
            str = str + '#S�ı��һ����Ʒ����״̬�����µ�¼�ɼ���#E\n'
            str = str + '#S����û��Ӧ#E\n'
            str = str + '\n'
            str = str + '#S�˳�#E#0'
            ply.Tell(str)
            ply.TalkStep = 1
        elif step == 1:
            if slt == 0:
                str = ''
                str = str + '\n\n\n\n  #2ɫä���߿�#0 #11#0 #22#0 #33#0 #44#0 #55#0 #66#0 #77#0 #88#0 #99#0'
                ply.SingleTell(str)
            elif slt == 1:
                goods = ply.GetGoodsBar(0,0)
                if goods.IsValid:
                    #ply.SendChatWord('%s' % type(goods)) # <type 'Goods'>
                    #ply.SendChatWord('%s' % dir(goods))  # []
                    #ply.SendChatWord('%s' % hasattr(goods, 'Id')) # True
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
                    #for k in dir(goods): # dir ����[]
                        #ply.SendChatWord('��Ա�������£�')
                        #ply.SendChatWord('%s:       %s' %  (k, getattr(goods,k)))
                    ply.SendChatWord('-----------------------------------------------------------------')
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
                ply.SendTipInfo('����')
                return
            else:
                ply.EndTalk()






