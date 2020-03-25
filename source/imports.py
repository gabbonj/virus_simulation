from random import randint, random
import matplotlib.pyplot as plt
from time import sleep
from . import settings
import tkinter as tk
import numpy as np
import threading
import pygame

from .screen.screen import start_screen
from .screen.interface import Interface
from .classes.gradient import Gradient
from .classes.disease import Disease
from .classes.pearson import Pearson
from .data.listener import Listener
from .classes.health import Health
from .data.plotter import plot_data
from .data.data import listen_data
from .classes.scene import Scene
from .app import App
