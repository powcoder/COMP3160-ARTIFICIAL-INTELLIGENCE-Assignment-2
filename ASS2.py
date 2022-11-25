https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:14:57 2020

@author: Mr Simon
"""

import deap
def NestArray(columns, rows):
    array = []
    for i in range(columns):
        column = []
        for k in range(rows):
            column.append(0)
        array.append(column)
    return array

MoveHistory = NestArray(6,64)
NextMove = []

for x in range (64):
    NextMove.append(0)

PayMatrix = [[0,2,4],[1,3,5]]
    
def payoff_to_ind1(individual1, individual2, individual3, game):
    return PayMatrix[individual1][2 - individual2 -individual3]

def move_by_indl(individual1, individual2, individual3, game):
    strat = MoveHistory.index(individual1 + individual2 + individual3)
    return NextMove[strat]
