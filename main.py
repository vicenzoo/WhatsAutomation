import pywhatkit
import keyboard
import time
from datetime import datetime
import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile

mens = input("Digite sua Mensagem: ")
df = pd.read_csv('contacts.csv', sep=',',header=None,dtype="str")
contatos  = np.asarray(df)
print(contatos)
i = 0
    
while len(contatos) > i:
    pywhatkit.sendwhatmsg(contatos[i][0],mens,datetime.now().hour,datetime.now().minute + 2)
    i = i + 1
    time.sleep(1)
    keyboard.press_and_release('ctrl + w')
