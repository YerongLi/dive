from collections import *

def solutionC(inputs):
    frauds = set(inputs[1].split(','))
    limits = [s.split(',') for s in inputs[2]]
    limits = {k : float(v) for k, v in limits}
    mmc = [s.split(',') for s in inputs[3]]
    mmc = {k : v for k, v in mmc}
    m = defaultdict(int)
    total = defaultdict(int)
    ans = set()
    chm = {}
    for x in inputs[5]:
        line = x.split(',')
        if len(line) == 5 and line[0] == 'CHARGE':
            _, chid, acct, _, t = line
            chm[chid] = [acct, t]
            if t in frauds:
                m[acct]+= 1
            total[acct]+= 1
            if m[acct] / total[acct] >= limits[mmc[acct]]:
                ans.add(acct)
        else:
            _, chid = line

            if chm[chid][1] in frauds:
                m[chm[chid][0]]-= 1

                if m[chm[chid][0]] / total[chm[chid][0]] < limits[chm[chid][0]]:
                    ans.remove(chm[chid][0])
    ans = list(ans)
    ans.sort()
    return ','.join(ans)
def solutionB(inputs):
    frauds = set(inputs[1].split(','))
    limits = [s.split(',') for s in inputs[2]]
    limits = {k : float(v) for k, v in limits}
    mmc = [s.split(',') for s in inputs[3]]
    mmc = {k : v for k, v in mmc}
    m = defaultdict(int)
    total = defaultdict(int)
    ans = set()
    for x in inputs[5]:
        line = x.split(',')
        if len(line) == 5 and line[0] == 'CHARGE':
            _, _, acct, _, t = line
            if t in frauds:
                m[acct]+= 1
            total[acct]+= 1
            if m[acct] / total[acct] >= limits[mmc[acct]]:
                ans.add(acct)  
    ans = list(ans)
    ans.sort()
    return ','.join(ans)

def solutionA(inputs):
    frauds = set(inputs[1].split(','))
    limits = [s.split(',') for s in inputs[2]]
    limits = {k : int(v) for k, v in limits}
    mmc = [s.split(',') for s in inputs[3]]
    mmc = {k : v for k, v in mmc}
    m = defaultdict(int)
    for x in inputs[5]:
        _, _, acct, _, t = x.split(',')
        if t in frauds:
            m[acct]+= 1
    ans = []
    for acct in mmc:
        if m[acct] >= limits[mmc[acct]]:
            ans.append(acct)
    ans.sort()
    return ','.join(ans)

inputs = [
    'approved,invalid_pin,expired_card',
    'do_not_honor,stolen_card,lost_card',
    ['retail,5',
    'airline,2',
    'venue,3'],
    ['acct_1,airline',
    'acct_2,venue',
    'acct_3,retail'],
    0,
    ['CHARGE,ch_1,acct_1,100,do_not_honor',
    'CHARGE,ch_2,acct_1,200,approved',
    'CHARGE,ch_3,acct_1,300,do_not_honor',
    'CHARGE,ch_4,acct_2,100,lost_card',
    'CHARGE,ch_5,acct_2,200,lost_card',
    'CHARGE,ch_6,acct_2,300,lost_card',
    'CHARGE,ch_7,acct_3,100,lost_card',
    'CHARGE,ch_8,acct_2,200,stolen_card',
    'CHARGE,ch_9,acct_3,100,approved']
]
expected = 'acct_1,acct_2'
print(solutionA(inputs))


inputs = [
    'approved,invalid_pin,expired_card',
    'do_not_honor,stolen_card,lost_card',
    ['retail,0.8',
    'venue,0.25'],
    ['acct_1,retail',
    'acct_2,retail'],
    2,
    ['CHARGE,ch_1,acct_1,100,do_not_honor',
    'CHARGE,ch_2,acct_1,200,approved',
    'CHARGE,ch_3,acct_1,300,do_not_honor',
    'DISPUTE,ch_2',
    'CHARGE,ch_4,acct_2,400,approved',
    'CHARGE,ch_5,acct_2,500,lost_card']
]
print(solutionB(inputs))

inputs = [
    'approved,invalid_pin,expired_card',
    'do_not_honor,stolen_card,lost_card',
    ['retail,0.8',
    'venue,0.25'],
    ['acct_1,retail',
    'acct_2,retail'],
    2,
    ['CHARGE,ch_1,acct_1,100,do_not_honor',
    'CHARGE,ch_2,acct_1,200,approved',
    'CHARGE,ch_3,acct_1,300,do_not_honor',
    'DISPUTE,ch_2',
    'CHARGE,ch_4,acct_2,400,approved',
    'CHARGE,ch_5,acct_2,500,lost_card']
]
print(solutionC(inputs))