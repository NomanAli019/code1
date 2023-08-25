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
from btn import startKeyboard , walletdecisionkeyboard ,deleteconfirmation ,backtotophome
from callback import cb


TOKEN = getenv("TOKEN")

dp =  Dispatcher()
router = Router()


# for start command 
@router.message(CommandStart())
async def Start(message : Message )->None:
    await message.answer(f"seclect One of the option {message.from_user.full_name}  \n" , reply_markup=startKeyboard.as_markup())
  
# start with button 
@router.callback_query(cb.filter(F.strt == "tostart"))
async def Start(query : CallbackQuery)->None:
    await query.message.answer(f"seclect One of the option \n" , reply_markup=startKeyboard.as_markup())
  
# for mananging the wallet 
@router.callback_query(cb.filter(F.strt == "Managewallet"))
async def Managewallet(query: CallbackQuery)->None:
    await query.message.answer(f"if your have wallet then select delete wallet \n if your don't have wallet click on create wallet \n " , reply_markup=walletdecisionkeyboard.as_markup())



# for confirmation of  deleting the wallet 
@router.callback_query(cb.filter(F.strt == "deletewallet" ))
async def deletingtext(query:CallbackQuery):
    await query.message.answer(f"Are you sure you want to delete you wallet ?" , reply_markup=deleteconfirmation.as_markup())

# wallet deletion confirmed 
@router.callback_query(cb.filter(F.strt == "yestodelete"))
async def walletdeletiondone(query:CallbackQuery):
    await query.message.answer(f"your account has been deleted! " , reply_markup=backtotophome.as_markup())


# for creating the wallet 
@router.callback_query(cb.filter(F.strt == "createwallet"))
async def deletingtext(query:CallbackQuery):

    await query.message.answer(f"your wallet has been created! ")

# for claiming 
@router.callback_query(cb.filter(F.strt == "Claim"))
async def claiming(query:CallbackQuery)->None:
    await query.message.answer(f"yet not decided anything for this section  !")


async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())