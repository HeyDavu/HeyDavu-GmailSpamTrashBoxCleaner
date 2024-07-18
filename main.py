import pyautogui as bot
import time

bot.PAUSE = 0.5

bot.press("win")
bot.write("edge")
bot.press("enter")
bot.write("https://mail.google.com/mail/u/0/#inbox")
bot.press("enter")
bot.click(x=113, y=421) #posição do botão "mais" que abre a lista onde fica a caixa de spam
bot.click(x=113, y=421) 
bot.click(x=111, y=556) #posição da caixa de spam
bot.click(x=357, y=285) #posição da caixa que seleciona todos os emails
bot.click(x=443, y=273) #posição do botão de delete dos emails
bot.click(x=119, y=602) #posição da lixeira
bot.click(x=353, y=279) #posição da caixa que seleciona todos os emails
bot.click(x=457, y=277) #posição do botão de delete dos emails



