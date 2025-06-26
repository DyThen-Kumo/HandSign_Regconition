import cv2
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2, MobileNetV3Small
# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
# from tensorflow.keras.applications.mobilenet_v3 import preprocess_input, decode_predictions

from tensorflow.keras.preprocessing import image
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import os
from collections import deque, Counter
import tkinter as tk
from PIL import Image, ImageTk
import time
import timm