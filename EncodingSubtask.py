# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:06:06 2019

@author: Francois
"""
import os
import pandas as pd
from psychopy import core
#from psychopy import data
from psychopy import event
from psychopy import visual
from Categories import Categories
from randSign import randSign

class Encoding(object):
    def __init__(self,nTrial,nStim):
        self.nTrial = nTrial
        self.nStim = nStim
        self.categs = Categories(nTrial,nStim)
        self.stims = self.categs.encDF
#        self.trials = data.TrialHandler(self.stims,
#                                        1, 
#                                        method='sequential')
        self.poslist = []        

    def setstimpos(self):
        self.stimpos = (randSign()*250, randSign()*250)
        return self.stimpos
            
    def runEnc(self):
        self.win = visual.Window(size=(1000, 1000), 
                                color=(0, 0 , 0), 
                                units = 'pix')
        self.instructionStart = visual.TextStim(self.win, 
                                               text = 'Memorize the \
                                               following images and \
                                               their location on screen.\
                                               Press space to start.')
        self.instructionStart.draw()
        self.win.flip()
        event.waitKeys(keyList=["space"],clearEvents=False)
        for index in self.stims.index:
            for stim in range(self.nStim):
                stimulus = visual.ImageStim(self.win,
                                            self.stims.loc[index][stim],
                                            color=(1,1,1), 
                                            pos = self.setstimpos(), 
                                            size = (500, 500),
                                            name=self.stims.loc[index][stim])
                stimulus.draw()
                self.win.flip()
                stimTuple = (stimulus.name, stimulus.pos)
                self.poslist.append(stimTuple)
                core.wait(1)
        self.win.close()
        self.stimDF = pd.DataFrame(self.poslist).to_csv(os.getcwd()+'\\stimDF.csv')
        return self.stimDF

# Usage examples:
#encObj = Encoding(2,3)
#task = encObj.runEnc()   