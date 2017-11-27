#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 07:53:44 2017

@author: gilberto
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

#x = np.linspace(-10,10,20)

x = np.arange(-10,10,1)

sigmoid = 1 / (1 + np.exp(-x))

#Adiciona figura
fig = plt.figure()
#Define qunatos gráficos e como serão plotados (linha,coluna,posição)
ax = fig.add_subplot(1,1,1)
#Define título
ax.set_title('Sigmoid Function')

#Define posição do label de cada axis
ax.set
#Define X label
ax.set_xlabel('x')
#Define Y label
#ax.set_ylabel('y')

#Define posição do eixo Y
#ax.spines['left'].set_position('center')
ax.spines['left'].set_position(('data',0.0)) #equivalente a 'zero'
        
#Define posição do eixo X
#ax.spines['bottom'].set_position(('axes',0.0)) #equivalente a 'center'
ax.spines['bottom'].set_position('zero')

#Define cor do eixo Y
ax.spines['left'].set_color('k')
#Define cor do eixo X
ax.spines['bottom'].set_color('k')

#Desencosta eixo Y
ax.spines['left'].set_smart_bounds(True)
#Desencosta eixo X
ax.spines['bottom'].set_smart_bounds(True)

#Define onde estará os números no eixo Y
ax.yaxis.set_ticks_position('left')
#Define onde estará os números no eixo X
ax.xaxis.set_ticks_position('bottom')

#Plota o gráfico
plot = ax.plot(x,sigmoid)

#Define tipo de linha [ '-' | '--' | '-.' | ':' | 'steps' | 'None' ]
plt.setp(plot, 'linestyle','-.','color','r', 'linedwidth',2.0)