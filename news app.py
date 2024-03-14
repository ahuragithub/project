import requests
import tkinter as tj
from customtkinter import *
from tkinter import ttk
window=CTk()
root=tj.Tk()
root.title('news app')
root.geometry('542x300')



def news_api():

        url =  (f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=b3dbc06d47bc40d3ab80afe3693af5f8')
        url3 = (f'https://newsapi.org/v2/everything?domains=wsj.com&apiKey=b3dbc06d47bc40d3ab80afe3693af5f8')
        url4 = (f'https://newsapi.org/v2/everything?q=apple&from=2024-02-28&to=2024-02-28&sortBy=popularity&apiKey=b3dbc06d47bc40d3ab80afe3693af5f8')
        
        response3 = requests.get(url3)
        response=requests.get(url)
        response4 = requests.get(url4)
        data3 = response3.json()
        data=response.json()
        data4 = response4.json()
        news_label.config(text=f'{formatt(data,data3,data4)}')
       





       
 
def formatt(data,data3,data4):
        
        format_data =f"\n☺☺{data['articles'][0]['title']}☺\n" 
        format_data +=f"\n☺☺{data3["articles"][0]["title"]}☺\n"
        format_data +=f"\n☺☺{data4["articles"][0]["title"]}☺\n"

        return format_data



tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill="both")

tab = ttk.Frame(tab_control)
tab_control.add(tab, text="news")
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="articles")
text =tj.Text(tab2,font=(10))
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text="about")

label=tj.Label(tab,text='welcome to news app',font=30,bg='blue',fg='black',height=1,width=32)
label.pack()
tj.Label(tab,text='Date information')
CTkLabel(tab,text='Press the news button to get information').pack()

b=button=tj.Button(tab,text='news button',command=news_api,font=29,activebackground='green',height=1,width=32,bd=4)
b.pack()
news_label=tj.Label(tab2,text='result',font=14,fg='orange',justify='center')
news_label.pack(fill=BOTH,expand = True)
tj.Label(tab3,font=25,text='''1: Manufacturer: Ahura Islami
2: All this information is taken from the news api site
3: This information is from Tesla, apple, wsj.com and business companies
4: After this program was created, the developer lost his mind!''').pack(fill=BOTH,expand = True)
root.mainloop()
                                   

                                   