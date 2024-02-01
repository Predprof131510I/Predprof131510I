import xlsxwriter
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import random
import pathlib

plot_final=[] #Массив с Y-значениями для построения графика спрогнозированных цен
plot_start=[] #Массив с Y-значениями для построения графика изначальных цен
plot_date=[] #Массив с Х-значениями для построения графиков
file_data=open('cot.txt') #Переменная в которую мы "открываем" файл с котировками BTC
data=file_data.read() #Строка, в которую мы читаем файл из переменной file_data
massive=data.split('\n') #Массив, в который мы разбиваем строку data по символу переноса на новую строку
length=int() #На сколько дней прогнозируем
massive_final=[] #Финальный массив со спрогнозированными ценами

def graph():  
      plt.plot(plot_date, plot_final, color='red') #Создание и отрисовка графика роста/спада цен с помощью инструментария библиотеки Matplotlib
      plt.plot(plot_date, plot_start, color='blue')
      plt.xlabel('Дата')
      plt.ylabel('Цена, рубли')
      plt.xticks(rotation=-30)
      plt.legend(['Спрогнозированная цена', 'Реальная цена'])
      plt.grid()
      plt.show()

def export():                
      s1 = pd.DataFrame({'Дата':date, 'Значение':massive_final})
      writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')
      s1.to_excel(writer, sheet_name='Лист1', index=False)
      writer._save()
      Export["text"] = f"Exported"
      Export["state"]=f"disabled"
for count in range(14): #Цикл, в котором мы задаём первые 14 дней в финальный массив
      massive_final.append(massive[count])
for length in range(7): #Цикл, в котором происходит расчёт, анализ и прогнозирование роста/спада цен на BTC по дням
      massive1=[] #Массив, в котором будут отсортированы цены на BTC
      for count in range(14+(length-1)):
            massive1.append(massive[count])
      massive1.sort()
      min=int(massive1[0])
      max=int(massive1[13+(length-1)])
      srz=int()
      mdn=int()
      for count2 in range (14+(length-1)): #Расчёт среднего значения цен за период
            srz+=int(massive1[count2])
      srz=srz//(14+(length-1))
      if len(massive1)%2==0:
            mdn=int((int(massive1[(13+(length-1))//2])+int(massive1[(13+(length-1))//2+1]))//2)
      else:
            mdn=int(massive1[(13+(length-1))//2])
      final_count=round(((max+min)//2-srz*1.0125+mdn*0.975)*random.uniform(0.987325, 1.02352325))
      print(final_count)
      massive_final.append(str(final_count))
date=[]

for count in range(21): #Цикл, в котором мы готовим полученные данные для экспорта в .xlsx формате для последующего их использования в Веб-приложении
      plot_final.append(int(massive_final[count]))
      plot_start.append(int(massive[count]))
      plot_date.append(str(count+1))
      if count<9:
           date.append(str('0'+str(count+1)+'.01.24'))
      else:
           date.append(str(str(count+1)+'.01.24'))
           
root = Tk()
root.geometry("800x400")
root.title('Bot')

bg=PhotoImage(file = 'bg.png')
label1 = Label( root, image = bg) 
label1.place(x = 0,y = 0) 
 
Graph = ttk.Button(text="Graph", command=graph)
Graph.place(x=525,y=170)
Export = ttk.Button(text="Export", command=export)
Export.place(x=525,y=210)
 
root.mainloop()
