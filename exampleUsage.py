'''
Title           :exampleUsage.py
Description     :Example usage of the MicroExpNet
Author          :Ilke Cugu & Eren Sener & Emre Akbas
Date Created    :20171210
Date Modified   :20171210
version         :1.0
python_version  :2.7.11
'''
from __future__ import print_function
from time import gmtime, strftime 
from MicroExpNet import *
import tensorflow as tf
import numpy as np
import cv2
import sys
import os
import dlib

labels = ("neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise")
