# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:16:18 2021

@author: wilsonte
"""

import math
import pandas as pd
import numpy as np
from tqdm import tqdm


def ProcessRun(rateReduce):
    df = pd.read_csv('output_{}_mm.csv'.format(rateReduce),
                    header=[0])
    df = df.sum()
    df['HALY_diff'] = df.HALY - df.bau_HALY
    df['COPD_reduction'] = rateReduce
    return df[['HALY_diff', 'COPD_reduction']]
    

def DoProcess(runList):
    df = pd.DataFrame()
    for rateReduce in runList:
        df = df.append(ProcessRun(rateReduce), ignore_index=True)
    df = df.set_index('COPD_reduction')
    df.to_csv('haly_diff.csv')
    
DoProcess([0.001, 0.0025, 0.005, 0.0075, 0.01, 0.02, 0.05])