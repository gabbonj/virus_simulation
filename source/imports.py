from random import randint, random
import matplotlib.pyplot as plt
from time import sleep
from . import settings
import numpy as np
import threading
import pygame

from .screen.screen import start_screen
from .classes.gradient import Gradient
from .classes.disease import Disease
from .classes.pearson import Pearson
from .data.listener import Listener
from .classes.health import Health
from .data.data import start_data
from .classes.scene import Scene
