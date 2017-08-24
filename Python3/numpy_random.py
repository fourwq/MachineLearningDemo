# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy.random as random

random.seed(42)

#做10000次试验
n_tests = 1000

#生成每次试验的奖品所在的门的编号

winning_doors = random.randint(0,3,n_tests)
print(winning_doors)

#如果换门的中奖次数
change_mind_wins = 0

#坚持的中奖次数
insist_wins = 0

#winning_door就是正确的门牌号

for winning_door in winning_doors:
    #随机挑选一扇门
    first_try = random.randint(0,3)
    #其他门的编号
    remaining_choices = [i for i in range(3) if i != first_try]
    
    #没有奖品的门的编号，这个信息只有主持人知道
    wrong_choices = [i for i in range(3) if i !=winning_door]
    #一开始选择的门主持人没法打开，所以从主持人可以打开的门中剔除
    if first_try in wrong_choices:
        wrong_choices.remove(first_try)
    #知识wrong_choices变量及时主持人可以打开的门的编号
    #注意此时如果一开始选择正确，则可以打开的门是两扇，主持人随便开一扇门
    #如果一开始选到了空门，则主持人只能打开剩下的一扇空门
    screened_out = random.choice(wrong_choices)
    remaining_choices.remove(screened_out)
    
    
    changed_mind_try = remaining_choices[0]
    
    change_mind_wins+=1 if changed_mind_try == winning_door else 0
    insist_wins += 1 if first_try == winning_door else 0
    
    print(
    'You win {1} out of {0} tests if you changed your mind\n'
    'You win {2} out of {0} tests if you insist on the initial choice'.format(
        n_tests, change_mind_wins, insist_wins
        ))
    
    