# File: x (Python 2.3)

from BXQT import *
from whrandom import randint


def OnClick(npc, ply, step, slt):
    baoshi_tab = [
        1574,
        1575,
        1576,
        1577,
        1578,
        1579,
        1580,
        1581,
        1582,
        1583,
        1584,
        1591,
        1592,
        1593,
        1594,
        1595,
        1596,
        1597,
        1598,
        1599,
        1611,
        1612,
        1613,
        963]
    ZHUFUKA = 884
    if ply.TalkStep == 0:
        ply.Tell(
            '#3%s\xa3\xba#0\n\xa1\xa1\xa1\xa1\xc4\xe3\xba\xc3\xa3\xac\xce\xd2\xca\xc7\xd7\xb0\xb1\xb8\xcf\xe2\xc7\xb6\xca\xa6\xa3\xac\xbb\xb6\xd3\xad\xc4\xe3\xc0\xb4\xb5\xbd\xb1\xcc\xd1\xa9\xc7\xe9\xcc\xec\xa3\xac\xcf\xeb\xd2\xaa\xd2\xbb\xcc\xd7\xb3\xc6\xd0\xc4\xc8\xe7\xd2\xe2\xb5\xc4\xbc\xab\xc6\xb7\xd7\xb0\xb1\xb8\xc2\xf0\xa3\xbf\xce\xd2\xbf\xc9\xd2\xd4\xcd\xea\xb3\xc9\xc4\xe3\xb5\xc4\xd0\xc4\xd4\xb8\xa1\xa3\n#6\xcb\xb5\xc3\xf7\xa3\xba\xce\xd2\xbf\xc9\xd2\xd4\xcf\xe2\xc7\xb6\xb5\xc4\xd7\xb0\xb1\xb8\xbd\xf6\xb0\xfc\xc0\xa8\xce\xe4\xc6\xf7\xa1\xa2\xd2\xc2\xbc\xd7\xa1\xa2\xbf\xf8\xc3\xb1\xa1\xa2\xbd\xe4\xd6\xb8\xa1\xa2\xd1\xa5\xd7\xd3\xba\xcd\xcf\xee\xc1\xb4\xa3\xbb\n\xd7\xb0\xb1\xb8\xcf\xe2\xc7\xb6\xb5\xc4\xb3\xc9\xb9\xa6\xc2\xca\xa3\xac\xb5\xda\xd2\xbb\xb4\xce\xcf\xe2\xc7\xb6\xb5\xc4\xb3\xc9\xb9\xa6\xc2\xca\xce\xaa100\xa3\xa5\xa3\xac\xc3\xbf\xb6\xe0\xcf\xe2\xc7\xb6\xd2\xbb\xb4\xce\xa3\xac\xb3\xc9\xb9\xa6\xc2\xca\xbd\xb5\xb5\xcd2\xa3\xa5\xa3\xac\xcf\xe2\xc7\xb6\xb1\xa6\xca\xaf\xca\xb1\xc8\xe7\xb9\xfb\xcb\xe6\xc9\xed\xd0\xaf\xb4\xf8#0#3\xd7\xa3\xb8\xa3\xbf\xa8#0#6\xbb\xe1\xb0\xb4\xc3\xbf\xd5\xc5\xbf\xa8\xcc\xe1\xb8\xdf10\xa3\xa5\xb5\xc4\xb3\xc9\xb9\xa6\xc2\xca\xbc\xc6\xcb\xe3\xa3\xac\xca\xb9\xd3\xc3\xd7\xa3\xb8\xa3\xbf\xa8\xd7\xee\xb6\xe0\xbf\xc9\xd2\xd4\xcc\xe1\xb8\xdf30\xa3\xa5\xb5\xc4\xb3\xc9\xb9\xa6\xc2\xca\xa3\xbb\n\xcf\xe2\xc7\xb6\xb3\xc9\xb9\xa6\xca\xb1\xb1\xa6\xca\xaf\xb5\xc4\xb8\xbd\xbc\xd3\xca\xf4\xd0\xd4\xbb\xe1\xd7\xaa\xd2\xc6\xb5\xbd\xd7\xb0\xb1\xb8\xc9\xcf\xa3\xac\xb1\xa6\xca\xaf\xba\xcd\xd7\xa3\xb8\xa3\xbf\xa8\xcf\xfb\xca\xa7\xa3\xac\xca\xa7\xb0\xdc\xba\xf3\xd7\xb0\xb1\xb8\xb2\xbb\xbb\xe1\xcb\xf0\xca\xa7\xa3\xbb\n\xcf\xe2\xc7\xb6\xca\xb1\xa3\xac\xc7\xeb\xb0\xd1\xd7\xb0\xb1\xb8\xc7\xeb\xb7\xc5\xd4\xda\xce\xef\xc6\xb7\xc0\xb8\xb5\xda\xd2\xbb\xb8\xf1\xa3\xac\xb1\xa6\xca\xaf\xc7\xeb\xb7\xc5\xd4\xda\xce\xef\xc6\xb7\xc0\xb8\xb5\xda\xb6\xfe\xb8\xf1\xa3\xbb\n\xd7\xbc\xb1\xb8\xba\xc3\xba\xf3\xa3\xac\xc7\xeb\xb5\xe3\xbb\xf7\xcf\xc2\xc3\xe6\xb5\xc4\xbf\xaa\xca\xbc\xcf\xe2\xc7\xb6\xa1\xa3#0\n\n#5#S\xbf\xaa\xca\xbc\xcf\xe2\xc7\xb6#E\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1#S\xb9\xd8\xb1\xd5#E#0' % npc.Name)
        ply.TalkStep = 1
    elif ply.TalkStep == 1:
        if slt == 0:
            GOODS = ply.GetGoodsBar(0, 0)
            BAOSHI = ply.GetGoodsBar(1, 0)
            if GOODS.IsValid and BAOSHI.IsValid:
                if GOODS.Id >= 1230 and GOODS.Id <= 1572 and GOODS.Id >= 1620 and GOODS.Id <= 1709:
                    ibs = 0
                    while ibs < len(baoshi_tab):
                        if BAOSHI.Id == baoshi_tab[ibs]:
                            ibs = 1000

                        ibs += 1
                    if ibs < 1000:
                        ply.SingleTell(
                            '#3%s#0\xa3\xba\n\n\xc4\xe3\xb4\xf8\xc0\xb4\xb5\xc4\xd5\xe2\xca\xc7\xca\xb2\xc3\xb4\xb1\xa6\xca\xaf\xa3\xac\xcb\xa1\xce\xd2\xd1\xdb\xd7\xbe\xb2\xbb\xc8\xcf\xca\xb6\xc4\xe3\xb4\xf8\xc0\xb4\xb5\xc4\xb1\xa6\xb1\xb4\xa3\xa1' % npc.Name)
                        return 0
                    elif GOODS.Type == 1 and GOODS.Type == 2 and GOODS.Type == 3 and GOODS.Type == 4 and GOODS.Type == 5 and GOODS.Type == 13 or BAOSHI.Type == 12:
                        if GOODS.Level < 10:
                            GOODS.Level = 10

                        Count_ZFK = ply.CountGoodsAtBar(ZHUFUKA)
                        if Count_ZFK > 3:
                            Count_ZFK = 3

                        if 100 < (GOODS.Level - 10) * 2:
                            tempCGL = 0
                        else:
                            tempCGL = 100 - (GOODS.Level - 10) * 2
                        ChengGL = tempCGL + Count_ZFK * 10
                        while ChengGL >= 110:
                            Count_ZFK -= 1
                            ChengGL = tempCGL + Count_ZFK * 10
                        if ChengGL > 100:
                            ChengGL = 100

                        ply.Tell(
                            '#3%s\xa3\xba#0\n\n\xa1\xa1\xa1\xa1\xc4\xe3\xd2\xaa\xcf\xe2\xc7\xb6\xb5\xc4\xd7\xb0\xb1\xb8\xca\xc7#6%s#0\xa3\xac\xcf\xe2\xc7\xb6\xb5\xc4\xb3\xc9\xb9\xa6\xc2\xca\xce\xaa#6%s\xa3\xa5#0\xa3\xac\xd0\xe8\xd2\xaa\xcf\xfb\xba\xc4\xd7\xa3\xb8\xa3\xbf\xa8#6%s\xd5\xc5#0\xa3\xac\xd0\xe8\xd2\xaa\xd1\xa9\xb1\xd2#6%d\xc1\xbd#0\xa1\xa3\xc4\xe3\xc8\xb7\xb6\xa8\xd2\xaa\xbd\xf8\xd0\xd0\xcf\xe2\xc7\xb6\xc2\xf0\xa3\xbf\n\n\n\n#5#S\xc8\xb7\xb6\xa8#E\xa1\xa1\xa1\xa1\xa1\xa1\xa1\xa1#S\xb9\xd8\xb1\xd5#E#0' % (
                            npc.Name, GOODS.Name, ChengGL, Count_ZFK, 100 * GOODS.Level))
                        ply.TalkStep = 2
                    else:
                        ply.SingleTell(
                            '#3%s#0\xa3\xba\n\n\xc4\xe3\xb4\xf8\xc0\xb4\xb5\xc4\xd5\xe2\xca\xc7\xca\xb2\xc3\xb4\xce\xef\xc6\xb7\xa3\xac\xcb\xa1\xce\xd2\xd1\xdb\xd7\xbe\xb2\xbb\xc8\xcf\xca\xb6\xc4\xe3\xb4\xf8\xc0\xb4\xb5\xc4\xb1\xa6\xb1\xb4\xa3\xa1' % npc.Name)
                else:
                    ply.SingleTell(
                        '#3%s#0\xa3\xba\n\n\xc4\xe3\xb4\xf8\xc0\xb4\xb5\xc4\xd5\xe2\xca\xc7\xca\xb2\xc3\xb4\xce\xef\xc6\xb7\xa3\xac\xd5\xe2\xd1\xf9\xb5\xc4\xce\xef\xc6\xb7\xce\xd2\xce\xde\xb7\xa8\xcd\xea\xb3\xc9\xcf\xe2\xc7\xb6\xa3\xa1' % npc.Name)
            else:
                ply.SingleTell(
                    '#3%s#0\xa3\xba\n\n\xc7\xeb\xb0\xd1\xc4\xe3\xd2\xaa\xcf\xe2\xc7\xb6\xb5\xc4\xd7\xb0\xb1\xb8\xb7\xc5\xd4\xda\xc4\xe3\xce\xef\xc6\xb7\xc0\xb8\xb5\xc4\xb5\xda\xd2\xbb\xb8\xf1\xa3\xac\xb0\xd1\xd2\xaa\xcf\xe2\xc7\xb6\xc9\xcf\xb5\xc4\xb1\xa6\xca\xaf\xb7\xc5\xd4\xda\xc4\xe3\xb5\xc4\xce\xef\xc6\xb7\xd1\xf9\xb5\xc4\xb5\xda\xb6\xfe\xb8\xf1\xb0\xc9\xa3\xa1' % npc.Name)
        else:
            ply.EndTalk()
    elif ply.TalkStep == 2:
        if slt == 0:
            GOODS = ply.GetGoodsBar(0, 0)
            BAOSHI = ply.GetGoodsBar(1, 0)
            if GOODS.IsValid and BAOSHI.IsValid:
                if GOODS.Id >= 1230 and GOODS.Id <= 1572 and GOODS.Id >= 1620 and GOODS.Id <= 1709:
                    ibs = 0
                    while ibs < len(baoshi_tab):
                        if BAOSHI.Id == baoshi_tab[ibs]:
                            ibs = 1000

                        ibs += 1
                    if ibs < 1000:
                        ply.SingleTell(
                            '#3%s#0\xa3\xba\n\n\xc4\xe3\xb4\xf8\xc0\xb4\xb5\xc4\xd5\xe2\xca\xc7\xca\xb2\xc3\xb4\xb1\xa6\xca\xaf\xa3\xac\xcb\xa1\xce\xd2\xd1\xdb\xd7\xbe\xb2\xbb\xc8\xcf\xca\xb6\xc4\xe3\xb4\xf8\xc0\xb4\xb5\xc4\xb1\xa6\xb1\xb4\xa3\xa1' % npc.Name)
                        return 0

                    if GOODS.Type == 1 and GOODS.Type == 2 and GOODS.Type == 3 and GOODS.Type == 4 and GOODS.Type == 5 and GOODS.Type == 13 or BAOSHI.Type == 12:
                        if GOODS.Level < 10:
                            GOODS.Level = 10

                        if GOODS.Level > 69:
                            ply.SingleTell(
                                '#3%s#0\xa3\xba\n\n\xc4\xe3\xb5\xc4\xd7\xb0\xb1\xb8\xb5\xc8\xbc\xb6\xcc\xab\xb8\xdf\xc1\xcb\xa3\xac\xce\xd2\xbc\xba\xbe\xad\xce\xde\xc4\xdc\xce\xaa\xc1\xa6\xc1\xcb\xa3\xa1' % npc.Name)
                            return 0

                        if ply.Money < 100 * GOODS.Level:
                            ply.SingleTell(
                                '#3%s#0\xa3\xba\n\n\xc4\xe3\xb4\xf8\xb5\xc4\xd1\xa9\xb1\xd2\xb2\xbb\xb9\xbb\xb0\xa1\xa3\xa1' % npc.Name)
                            return 0

                        ply.Jump(npc.Scene.Id, ply.Position[0] + 1, ply.Position[1] + 1)
                        ply.AddMoney(-(100 * GOODS.Level))
                        Count_ZFK = ply.CountGoodsAtBar(ZHUFUKA)
                        if Count_ZFK > 3:
                            Count_ZFK = 3

                        if 100 < (GOODS.Level - 10) * 2:
                            tempCGL = 0
                        else:
                            tempCGL = 100 - (GOODS.Level - 10) * 2
                        ChengGL = tempCGL + Count_ZFK * 10
                        while ChengGL >= 110:
                            Count_ZFK -= 1
                            ChengGL = tempCGL + Count_ZFK * 10
                        if ChengGL > 100:
                            ChengGL = 100

                        i = randint(0, 100)
                        if i <= ChengGL or ply.IsGM:
                            GOODS.Level += 1
                            i = 0
                            if GOODS.RequirLevel < BAOSHI.RequirLevel:
                                GOODS.RequirLevel = BAOSHI.RequirLevel

                            while i <= 3:
                                j = 0
                                while j <= 14:
                                    n1 = GOODS.GetProperty(j, i)
                                    n2 = BAOSHI.GetProperty(j, i)
                                    n1 += n2
                                    GOODS.SetProperty(j, i, n1)
                                    j += 1
                                i += 1
                            ply.DelGoodsAtBar(BAOSHI.Id, 1)
                            ply.DelGoodsAtBar(ZHUFUKA, Count_ZFK)
                            ply.SingleTell(
                                '#3%s#0\xa3\xba\n\n\xb9\xa7\xcf\xb2\xc4\xe3\xa3\xac\xcf\xe2\xc7\xb6\xb3\xc9\xb9\xa6\xc1\xcb\xa3\xa1\n\xcf\xc2\xcf\xdf\xd6\xd8\xc9\xcf\xbb\xf2\xbd\xab\xd7\xb0\xb1\xb8\xb6\xaa\xb5\xf4\xd4\xd9\xbc\xf1\xc6\xf0\xbc\xb4\xbf\xc9\xbf\xb4\xb5\xbd\xb3\xc9\xb9\xa6\xba\xf3\xb5\xc4\xd0\xa7\xb9\xfb\xa1\xa3' % npc.Name)
                        else:
                            ply.DelGoodsAtBar(BAOSHI.Id, 1)
                            ply.DelGoodsAtBar(ZHUFUKA, Count_ZFK)
                            ply.SingleTell(
                                '#3%s#0\xa3\xba\n\n\xb1\xa7\xc7\xb8\xa3\xac\xcf\xe2\xc7\xb6\xca\xa7\xb0\xdc\xc1\xcb\xa3\xa1' % npc.Name)
                    else:
                        ply.SingleTell(
                            '#3%s#0\xa3\xba\n\n\xc4\xe3\xb4\xf8\xc0\xb4\xb5\xc4\xd5\xe2\xca\xc7\xca\xb2\xc3\xb4\xce\xef\xc6\xb7\xa3\xac\xcb\xa1\xce\xd2\xd1\xdb\xd7\xbe\xb2\xbb\xc8\xcf\xca\xb6\xc4\xe3\xb4\xf8\xc0\xb4\xb5\xc4\xb1\xa6\xb1\xb4\xa3\xa1' % npc.Name)
                else:
                    ply.SingleTell(
                        '#3%s#0\xa3\xba\n\n\xc4\xe3\xb4\xf8\xc0\xb4\xb5\xc4\xd5\xe2\xca\xc7\xca\xb2\xc3\xb4\xce\xef\xc6\xb7\xa3\xac\xd5\xe2\xd1\xf9\xb5\xc4\xce\xef\xc6\xb7\xce\xd2\xce\xde\xb7\xa8\xcd\xea\xb3\xc9\xcf\xe2\xc7\xb6\xa3\xa1' % npc.Name)
            else:
                ply.SingleTell(
                    '#3%s#0\xa3\xba\n\n\xc7\xeb\xb0\xd1\xc4\xe3\xd2\xaa\xcf\xe2\xc7\xb6\xb5\xc4\xd7\xb0\xb1\xb8\xb7\xc5\xd4\xda\xc4\xe3\xce\xef\xc6\xb7\xc0\xb8\xb5\xc4\xb5\xda\xd2\xbb\xb8\xf1\xa3\xac\xb0\xd1\xd2\xaa\xcf\xe2\xc7\xb6\xc9\xcf\xb5\xc4\xb1\xa6\xca\xaf\xb7\xc5\xd4\xda\xc4\xe3\xb5\xc4\xce\xef\xc6\xb7\xd1\xf9\xb5\xc4\xb5\xda\xb6\xfe\xb8\xf1\xb0\xc9\xa3\xa1' % npc.Name)
        else:
            ply.EndTalk()


