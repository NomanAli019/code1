import asyncio
import logging
import sys
from os import getenv
from aiogram.utils.keyboard import CallbackData


class cb(CallbackData , prefix = "Call"):    
    strt : str 
    end : int 
