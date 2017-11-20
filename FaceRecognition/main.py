from tkinter import *
import os

win=Tk();

#Functions to Open files
def runFaceDetection():
   os.system('faceDetect.py')

def runDatasetCreator():
   os.system('datasetCreater.py')

def runDetector():
   os.system('detector.py')

def runTrainer():
   os.system('trainer.py')

faceDetectButton = Button(win,background="#fffBBB",text ="Face Detect", command = runFaceDetection,height=2,width=30)
faceDetectButton.pack(fill=None,expand=False)

datasetCreatorButton = Button(win,background="#fffBBB",text ="Dataset Creator", command = runDatasetCreator,height=2,width=30)
datasetCreatorButton.pack(fill=None,expand=False)

detectorButton = Button(win,background="#fffBBB",text ="Detector", command = runDetector,height=2,width=30)
detectorButton.pack(fill=None,expand=False)

trainerButton = Button(win,background="#fffBBB",text ="Trainer", command = runTrainer,height=2,width=30)
trainerButton.pack(fill=None,expand=False)

mainloop()
