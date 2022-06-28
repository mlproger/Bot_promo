import configparser
import re
import pyautogui
from telethon import TelegramClient, sync
from telethon.errors import SessionPasswordNeededError
from telethon import events

from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (PeerChannel)

config = configparser.ConfigParser()
config.read("config.ini")


api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']


def res(s):
    a = re.findall(r'[A-Z0-9]', s)
    return a[0:8]

async def moveC(s):
    pyautogui.moveTo(x=809, y=750)
    pyautogui.click()
    pyautogui.write(s)
    pyautogui.press('enter')
    pyautogui.moveTo(x=827, y=587)
    pyautogui.click()


client = TelegramClient(username, api_id, api_hash)

@client.on(events.NewMessage(chats=('https://t.me/drgn_lol')))
async def normal_handler(event):

    mes = res(event.message.to_dict()['message'])
    await moveC(mes)
    print(mes)

@client.on(events.NewMessage(chats=('https://t.me/only_zoom')))
async def normal_handler(event):

    mes = res(event.message.to_dict()['message'])
    await moveC(mes)
    print(mes)

@client.on(events.NewMessage(chats=('https://t.me/drgn_vegas')))
async def normal_handler(event):

    mes = res(event.message.to_dict()['message'])
    await moveC(mes)
    print(mes)

@client.on(events.NewMessage(chats=('https://t.me/mandarinhalava')))
async def normal_handler(event):

    mes = res(event.message.to_dict()['message'])
    await moveC(mes)
    print(mes)


client.start()
client.run_until_disconnected()
print("Client Created")




if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Password: '))

