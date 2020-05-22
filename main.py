from ctypes import *
import os
import pyautogui as pg
import time
import tkinter as tk


def copy():
    pg.keyDown('ctrl')
    pg.press('c')
    pg.keyUp('ctrl')

def get_browsers(): #получить имена браузеров
    f = open(os.getcwd()+ '\\browsers')
    browsers = f.read().split('\n')
    return browsers

def get_text_from_buff(): #возвращает текст из буфера обмена
    c = tk.Tk()
    c.withdraw()
    clip = c.clipboard_get()
    c.update()
    c.destroy()
    return clip

def equaling(): #проверяем браузер ли
    pg.click()
    time.sleep(0.5)
    pg.click()
    copy()
    for browser in browsers:
        path = get_text_from_buff()
        if path.find(browser) >=0:
            return True
        else:
            return False

def search_browser(): #ище браузер
    width, height = pg.size()
    founded = False
    for i in range(30,width,50):
        for j in range(30,height-60,20):
            pg.moveTo(i,j)
            founded = equaling()
            if founded:
                return i, j
                break
        if founded:
            break
    return -1,-1


def move_and_click(x,y):
    proportion_x = 1042 / 1920
    proportion_y = 572 / 1080
    time.sleep(4)
    pg.moveTo(pg.size()[0] * proportion_x, pg.size()[1] * proportion_y)
    pg.click()


if __name__ == '__main__':
    login = ''
    password = ''
    card_owner = ''
    num_of_card = ''
    month = ''
    year = ''
    cvc =''
    comp_name = ''
    lend_url = ''
    time.sleep(5)
    browsers = get_browsers()
    search_browser()
    pg.doubleClick()
    time.sleep(1)
    pg.typewrite("facebook.com/")
    pg.press('enter')
    pg.press('f11')
    move_and_click(1080,53)
    pg.typewrite(login)
    time.sleep(1)
    move_and_click(1392,53)
    pg.typewrite(password)
    move_and_click(1230,53)
    move_and_click(1299,20)
    move_and_click(1212,213)
    move_and_click(135,21)
    move_and_click(224,572)
    move_and_click(1799,163)
    move_and_click(1395,420)
    move_and_click(1042,572)
    move_and_click(817,388)
    pg.typewrite(card_owner)
    move_and_click(794,468)
    pg.typewrite(num_of_card)
    move_and_click(1085,470)
    pg.typewrite(month)
    move_and_click(1147,467)
    pg.typewrite(year)
    move_and_click(801,575)
    pg.typewrite(cvc)
    move_and_click(1158,849)
    time.sleep(60)
    move_and_click(141,23)
    move_and_click(153, 154)
    time.sleep(10)
    move_and_click(82,283)
    move_and_click()
    pg.typewrite(comp_name)
    move_and_click(1324,1016)
    move_and_click(610,237)
    move_and_click(1320,325)
    pg.typewrite(lend_url)
    move_and_click(1837,1002)
