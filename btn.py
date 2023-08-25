import asyncio
import logging
import sys
from os import getenv
import requests
from aiogram import Bot, Dispatcher, Router, types 
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command  
from aiogram.types import Message , CallbackQuery 
from aiogram.utils.markdown import hbold 
from aiogram.utils.keyboard import InlineKeyboardBuilder  , CallbackData , ReplyKeyboardBuilder
from aiogram import F
from aiogram.types.keyboard_button_poll_type import KeyboardButtonPollType
from callback import cb


# start menu button 
startKeyboard = InlineKeyboardBuilder()
startKeyboard.button(text="Manage Wallet" ,callback_data=cb(strt="Managewallet", end=11).pack())
startKeyboard.button(text="Claim" , callback_data=cb(strt="Claim", end=11).pack())
startKeyboard.adjust(2)

# wallet menu buttons 
walletdecisionkeyboard = InlineKeyboardBuilder()
walletdecisionkeyboard.button(text="Delete Wallet" , callback_data=cb(strt="deletewallet" , end=11).pack())
walletdecisionkeyboard.button(text="Create Wallet" , callback_data=cb(strt="tostart", end=11).pack())
walletdecisionkeyboard.button(text="Back" , callback_data=cb(strt="tostart" , end=11).pack())
walletdecisionkeyboard.adjust(2,1)

# delete menu button 
deleteconfirmation = InlineKeyboardBuilder()
deleteconfirmation.button(text="YES" , callback_data=cb(strt="yestodelete" , end=11).pack())
deleteconfirmation.button(text="NO" , callback_data=cb(strt="Managewallet" , end=11).pack())
deleteconfirmation.button(text="BACK" , callback_data=cb(strt="Managewallet" , end=11).pack())
deleteconfirmation.adjust(2,1)

# deleletion confirmed now move to home 
backtotophome = InlineKeyboardBuilder()
backtotophome.button(text="BACK TO HOME" , callback_data=cb(strt="tostart" , end=11).pack())


# wallet creation button 
