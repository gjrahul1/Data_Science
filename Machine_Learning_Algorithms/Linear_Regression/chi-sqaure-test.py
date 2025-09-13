# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from scipy.stats import chisquare

result = chisquare([16, 18, 16, 14, 12, 12],f_exp = [16, 16, 16, 16, 16, 8])

print("Statistic:",result.statistic)
print("PValue:",result.pvalue)

