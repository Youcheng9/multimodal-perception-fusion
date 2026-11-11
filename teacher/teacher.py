'''
This file is to define teacher architecture.

The model will be a heavyweight transformer model, used to train a smaller version of a transformer model (student) 
to detect and recognize necessary objects

Use this file to define architecture and wire it up in main.


Note: It is not for running.
'''

import torch
from transformers import DetrForObjectDetection, DetrImageProcessor
from PIL import Image
import requests



