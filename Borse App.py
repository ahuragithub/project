from tkinter import *
from tkinter import messagebox
import requests
from tkinter import ttk
from customtkinter import*
class graphik_and_apiclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('650x300+300+300')
        self.root.title('Borse App')
        self.root.config(bg='#ac20e8')
        LeftMenu =Frame(self.root, bd=12, relief=RIDGE, bg="#c3d6d5")
        LeftMenu.place(width=700, height=300)

        def api_shop():
            api_key = 'TV05PRL1M257HMJL'
            url2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SHOP.TRT&outputsize=full&apikey={api_key}'
            response2 = requests.get(url2)
            data2 = response2.json()
            njk = cmb_gender3.get()

            label.config(text=f'{data2["Meta Data"][njk]}')
        def api_IBM():
            api_key = 'TV05PRL1M257HMJL'
            url2 =f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey={api_key}'
            response2 = requests.get(url2)
            data2 = response2.json()
            njk = cmb_gender.get()

            label.config(text=f'{data2["Meta Data"][njk]}')

        def api_gpv():
            api_key = 'TV05PRL1M257HMJL'
            url2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GPV.TRV&outputsize=full&apikey={api_key}'
            response2 = requests.get(url2)
            data2 = response2.json()
            njk = cmb_gender4.get()

            label.config(text=f'{data2["Meta Data"][njk]}')

        def api_mbg():
            api_key = 'TV05PRL1M257HMJL'
            url2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MBG.DEX&outputsize=full&apikey={api_key}'
            response2 = requests.get(url2)
            data2 = response2.json()
            njk = cmb_gender5.get()

            label.config(text=f'{data2["Meta Data"][njk]}')
        def api_daily():
            api_key = 'TV05PRL1M257HMJL'
            urls = {
                'IBM': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey={api_key}',
                'TSCO.LON': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey={api_key}',
                'SHOP.TRT': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SHOP.TRT&outputsize=full&apikey={api_key}',
                'GPV.TRV': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GPV.TRV&outputsize=full&apikey={api_key}',
                'MBG.DEX': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MBG.DEX&outputsize=full&apikey={api_key}',
                'RELIANCE.BSE': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey={api_key}',
                'China-Shanghai': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=600104.SHH&outputsize=full&apikey={api_key}',
                'China-Shenzhen': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=000002.SHZ&outputsize=full&apikey={api_key}'
            }

            njk = cmb_gender11.get()
            njk2 = cmb_gender14.get()
            listt = {
                "1. open": "1. open",
                "2. high": "2. high",
                "3. low": "3. low",
                "4. close": "4. close",
                "5. volume": "5. volume"
            }

            if njk in urls:
                response = requests.get(urls[njk])
                data = response.json()
                time = data.get("Time Series (Daily)",{})
                date = max(time.keys())
                addres = time[date][listt[njk2]]
                labell.config(text=f'{njk2}: {addres}')
        def api_tarikh():
            api_key = 'TV05PRL1M257HMJL'
            urls = {
                'IBM': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey={api_key}',
                'TSCO.LON': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey={api_key}',
                'SHOP.TRT': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SHOP.TRT&outputsize=full&apikey={api_key}',
                'GPV.TRV': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GPV.TRV&outputsize=full&apikey={api_key}',
                'MBG.DEX': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MBG.DEX&outputsize=full&apikey={api_key}',
                'RELIANCE.BSE': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey={api_key}',
                'China-Shanghai': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=600104.SHH&outputsize=full&apikey={api_key}',
                'China-Shenzhen': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=000002.SHZ&outputsize=full&apikey={api_key}'
            }

            njk = cmb.get()
            njk2 = entry.get()
            
            if njk in urls:
                response = requests.get(urls[njk])
                data = response.json()
                time_series = data.get("Time Series (Daily)", {})
                
                if time_series:
                    if njk2 in time_series:
                        data = time_series[njk2]
                        open = data.get("1. open")
                        high = data.get("2. high" )
                        low = data.get("3. low")
                        close = data.get("4. close")
                        volume = data.get("5. volume")

                        result_text = (f"tarikh: {njk2}\n"
                                    f"1. open: {open}\n"
                                    f"2. high: {high}\n"
                                    f"3. low: {low}\n"
                                    f"4. close: {close}\n"
                                    f"5. volume: {volume}")
                        labell.config(text=result_text)
        
        def api_weekly():
            api_key = 'TV05PRL1M257HMJL'
            urls = {

                'IBM':f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey={api_key}',
                'TSCO.LON':f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=TSCO.LON&apikey={api_key}'
            }

            njk = cmb_genderrr.get()
            njk2 = cmb_genderee.get()
            listt = {
                "1. open": "1. open",
                "2. high": "2. high",
                "3. low": "3. low",
                "4. close": "4. close",
                "5. volume": "5. volume"
            }

            if njk in urls:
                response = requests.get(urls[njk])
                data = response.json()
                time = data.get("Weekly Time Series",{})
                date = max(time.keys())
                addres = time[date][listt[njk2]]
                labell.config(text=f'{njk2}: {addres}')
                
        def api_monthly():
            api_key = 'TV05PRL1M257HMJL'
            urls = {

                'IBM':f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey={api_key}',
                'TSCO.LON':f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=TSCO.LON&apikey={api_key}'
            }

            njk = cmb_gender_monthly.get()
            njk2 = cmb_gender_monthly2.get()
            listt = {
                "1. open": "1. open",
                "2. high": "2. high",
                "3. low": "3. low",
                "4. close": "4. close",
                "5. volume": "5. volume"
            }

            if njk in urls:
                response = requests.get(urls[njk])
                data = response.json()
                time = data.get("Monthly Time Series",{})
                date = max(time.keys())
                addres = time[date][listt[njk2]]
                labell.config(text=f'{njk2}: {addres}')
                
        def api_Tsco():
            api_key = 'TV05PRL1M257HMJL'
            url2 = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSCO.LON&outputsize=full&apikey={api_key}'
            response2 = requests.get(url2)
            data2 = response2.json()
            njk = cmb_ge.get()

            label.config(text=f'{data2["Meta Data"][njk]}')

        def window():
            num = Toplevel(root)
            num.geometry("450x300+497+300")
            num.title('borse')
            Button(num, text='meta', font=("times new roman", 15), bg='#0a5380', cursor='hand2',command=meta_Buttons).pack(fill=X)
            Button(num, text='TIME_SERIES', font=("times new roman", 15), bg='#0a5380', cursor='hand2',command=time_series).pack(fill=X)
            Button(num, text='tarikh', font=("times new roman", 15), bg='#0a5380', cursor='hand2',command=tarikh).pack(fill=X)

        def IBM():
            num3 = Toplevel(root)
            num3.geometry("450x300+497+300")
            num3.title('IBM')
            frame =Frame(num3, bd=12, relief=RIDGE, bg="#909190")
            frame.place(x=10, y=60, width=450, height=200)

            var_gender = StringVar()
            global cmb_gender
            cmb_gender = ttk.Combobox(num3, textvariable=var_gender, values=("1. Information", "2. Symbol", '3. Last Refreshed', '4. Output Size', '5. Time Zone'), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb_gender.pack(fill=X, side=TOP)
            Button(num3, text='click', font=("times new roman", 15), bg='#cee004', cursor='hand2', command=api_IBM).pack(fill=X)
            global label
            label = Label(frame, text='nbm', font=("times new roman", 15), fg='#fce303', bg='#58505c')
            label.pack(fill=X, side=LEFT)
        def meta_Buttons():
            num3 = Toplevel(root)
            num3.geometry("450x300+497+300")
            num3.title('meta_Buttons')
            
            Button(num3, text='IBM', font=("times new roman", 15), bg='#a1b51d', cursor='hand2',command=IBM).pack(fill=X)
            Button(num3, text='SHOP.TRT', font=("times new roman", 15), bg='#a1b51d', cursor='hand2', command=shop).pack(fill=X)
            Button(num3, text='GPV.TRV', font=("times new roman", 15), bg='#a1b51d', cursor='hand2', command=gpv).pack(fill=X)
            Button(num3, text='MBG.DEX', font=("times new roman", 15), bg='#a1b51d', cursor='hand2', command=mbg).pack(fill=X)
            Button(num3, text='TSCO.LON', font=("times new roman", 15), bg='#a1b51d', cursor='hand2', command=Tsco).pack(fill=X)
        def Tsco():
            num3 = Toplevel(root)
            num3.geometry("450x300+497+300")
            num3.title("TSCO.LON")
            frame =Frame(num3, bd=12, relief=RIDGE, bg="#909190")
            frame.place(x=10, y=60, width=450, height=200)

            var_gender = StringVar()
            global cmb_ge
            cmb_ge = ttk.Combobox(num3, textvariable=var_gender, values=("1. Information", '2. Symbol', '3. Last Refreshed', '4. Output Size', '5. Time Zone'), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb_ge.pack(fill=X, side=TOP)
            Button(num3, text='click', font=("times new roman", 15), bg='#12e619', cursor='hand2', command=api_Tsco).pack(fill=X)
            global label
            label = Label(frame, text='nbm', font=("times new roman", 15), fg='#fce303', bg='#58505c')
            label.pack(fill=X, side=LEFT)

        def shop():
            num3 = Toplevel(root)
            num3.geometry("450x300+497+300")
            num3.title("shop")
            frame =Frame(num3, bd=12, relief=RIDGE, bg="#909190")
            frame.place(x=10, y=60, width=450, height=200)
            var_gender = StringVar()
            global cmb_gender3
            cmb_gender3 = ttk.Combobox(num3, textvariable=var_gender, values=("1. Information", '2. Symbol', '3. Last Refreshed', '4. Output Size', '5. Time Zone'), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb_gender3.pack(fill=X, side=TOP)
            Button(num3, text='click', font=("times new roman", 15), bg='#0b8f86', cursor='hand2', command=api_shop).pack(fill=X)
            global label
            label = Label(frame, text='nbm', font=("times new roman", 15), fg='#fce303', bg='#58505c')
            label.pack(fill=X, side=LEFT)

        def gpv():
            num3 = Toplevel(root)
            num3.geometry("450x300+497+300")
            num3.title("gpv")
            frame =Frame(num3, bd=12, relief=RIDGE, bg="#9ea698")
            frame.place(x=10, y=60, width=450, height=200)

            var_gender = StringVar()
            global cmb_gender4
            cmb_gender4 = ttk.Combobox(num3, textvariable=var_gender, values=("1. Information", '2. Symbol', '3. Last Refreshed', '4. Output Size', '5. Time Zone'), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb_gender4.pack(fill=X, side=TOP)
 
            Button(num3, text='click', font=("times new roman", 15), bg='#f56d05', cursor='hand2', command=api_gpv).pack(fill=X)
            global label
            label = Label(frame, text='nbm', font=("times new roman", 15), fg='#fce303', bg='#58505c')
            label.pack(fill=X, side=LEFT)

        def mbg():
            num3 = Toplevel(root)
            num3.geometry("450x300+497+300")
            num3.title("mbg")
            frame =Frame(num3, bd=12, relief=RIDGE, bg="#4d5756")
            frame.place(x=10, y=60, width=450, height=200)

            var_gender = StringVar()
            global cmb_gender5
            cmb_gender5 = ttk.Combobox(num3, textvariable=var_gender, values=("1. Information", '2. Symbol', '3. Last Refreshed', '4. Output Size', '5. Time Zone'), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb_gender5.pack(fill=X, side=TOP)
            
            Button(num3, text='click', font=("times new roman", 15), bg='#720ac2', cursor='hand2', command=api_mbg).pack(fill=X)
            global label
            label = Label(frame, text='nbm', font=("times new roman", 15), fg='#fce303', bg='#58505c')
            label.pack(fill=X, side=LEFT)
        def time_daily():
            num3 = Toplevel(root)
            num3.geometry("450x300+497+300")
            num3.title("TIME_SERIES_DAILY")
            frame =Frame(num3, bd=12, relief=RIDGE, bg="#4d5756")
            frame.place(x=10, y=60, width=450, height=200)

            var_gender = StringVar()
            global cmb_gender11
            cmb_gender11 = ttk.Combobox(num3, textvariable=var_gender, values=('IBM','TSCO.LON','SHOP.TRT','GPV.TRV','MBG.DEX','RELIANCE.BSE','China-Shanghai','China-Shenzhen'), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb_gender11.pack(fill=X, side=TOP)
            
            var_gender = StringVar()
            global cmb_gender14
            cmb_gender14 = ttk.Combobox(num3, textvariable=var_gender, values=("1. open","2. high","3. low","4. close","5. volume"), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb_gender14.pack(fill=X, side=TOP)
            
            Button(num3, text='click', font=("times new roman", 15), bg='#720ac2', cursor='hand2', command=api_daily).pack(fill=X)
            global labell
            labell = Label(frame, text='nbm', font=("times new roman", 15), fg='#fce303', bg='#58505c')
            labell.pack(fill=X, side=LEFT)
        def time_weekly():
            
            num3 = Toplevel(root)
            num3.geometry("450x300+497+300")
            num3.title("TIME_SERIES_WEEKLY")
            frame =Frame(num3, bd=12, relief=RIDGE, bg="#4d5756")
            frame.place(x=10, y=60, width=450, height=200)

            var_gender = StringVar()
            global cmb_genderrr
            cmb_genderrr = ttk.Combobox(num3, textvariable=var_gender, values=('IBM','TSCO.LON'), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb_genderrr.pack(fill=X, side=TOP)
            
            var_gender = StringVar()
            global cmb_genderee
            cmb_genderee = ttk.Combobox(num3, textvariable=var_gender, values=("1. open","2. high","3. low","4. close","5. volume"), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb_genderee.pack(fill=X, side=TOP)
            
            Button(num3, text='click', font=("times new roman", 15), bg='#720ac2', cursor='hand2', command=api_weekly).pack(fill=X)
            global labell
            labell = Label(frame, text='nbm', font=("times new roman", 15), fg='#fce303', bg='#58505c')
            labell.pack(fill=X, side=LEFT)
            
        def time_monthly():
            
            num3 = Toplevel(root)
            num3.geometry("450x300+497+300")
            num3.title("TIME_SERIES_MONTHLY")
            frame =Frame(num3, bd=12, relief=RIDGE, bg="#4d5756")
            frame.place(x=10, y=60, width=450, height=200)

            var_gender = StringVar()
            global cmb_gender_monthly
            cmb_gender_monthly = ttk.Combobox(num3, textvariable=var_gender, values=('IBM','TSCO.LON'), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb_gender_monthly.pack(fill=X, side=TOP)
            
            var_gender = StringVar()
            global cmb_gender_monthly2
            cmb_gender_monthly2 = ttk.Combobox(num3, textvariable=var_gender, values=("1. open","2. high","3. low","4. close","5. volume"), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb_gender_monthly2.pack(fill=X, side=TOP)
            
            Button(num3, text='click', font=("times new roman", 15), bg='#720ac2', cursor='hand2', command=api_monthly).pack(fill=X)
            global labell
            labell = Label(frame, text='nbm', font=("times new roman", 15), fg='#fce303', bg='#58505c')
            labell.pack(fill=X, side=LEFT)
        def tarikh():
            num3 = Toplevel(root)
            num3.geometry("450x300+497+300")
            num3.title("tarikh")
            frame =Frame(num3, bd=12, relief=RIDGE, bg="#4d5756")
            frame.place(x=10, y=60, width=450, height=200)
            var_gender = StringVar()
            global cmb
            cmb = ttk.Combobox(num3, textvariable=var_gender, values=('IBM','TSCO.LON','SHOP.TRT','GPV.TRV','MBG.DEX','RELIANCE.BSE','China-Shanghai','China-Shenzhen'), state="readonly",justify=CENTER, font=("goudy old style", 15))
            cmb.pack(fill=X, side=TOP)
            global entry
            entry=Entry(num3,font=("goudy old style", 15),justify=CENTER,fg='#720ac2')
            entry.pack(fill=X, side=TOP)
            Button(num3, text='click', font=("times new roman", 15), bg='#046769', cursor='hand2', command=api_tarikh).pack(fill=X)
            global labell
            labell = Label(frame, text='nbm', font=("times new roman", 15), fg='#fce303', bg='#58505c')
            labell.pack(fill=X, side=LEFT)
            


        def time_series():
            num3 = Toplevel(root)
            num3.geometry("450x300+497+300")
            num3.title("time_series")
            Button(num3, text='TIME_SERIES_DAILY', font=("times new roman", 15), bg='#c45912', cursor='hand2',command=time_daily).pack(fill=X)
            Button(num3, text='TIME_SERIES_WEEKLY', font=("times new roman", 15), bg='#c45912', cursor='hand2',command=time_weekly).pack(fill=X)
            Button(num3, text='TIME_SERIES_MONTHLY', font=("times new roman", 15), bg='#c45912', cursor='hand2',command=time_monthly).pack(fill=X)
        def window2():
            num1 = Toplevel(root)
            num1.geometry("450x300+497+300")
            num1.title('about')
            Label(num1, text='''1. This program is a Python project
2. Creator of this program: Ahura Islami
3. All the information you get from this program is for (www.alphavantage.com) Is
4. I hope you enjoyed this program☺☻☺''', font=("times new roman", 15), fg='#0b8f86').pack(fill=X)

        Buttonn = Button(LeftMenu, text='borse', font=("times new roman", 15), bg='#0b8f86', cursor='hand2',command=window)
        Buttonn.pack(side=LEFT, fill=Y)
        butonn = Button(LeftMenu, text='about', font=("times new roman", 15), bg='#0b8f86', cursor='hand2',command=window2)
        butonn.pack(side=LEFT, fill=Y)
        butonn = Button(LeftMenu, text='exit', font=("times new roman", 15), bg='#0b8f86', cursor='hand2',command=self.root.destroy)
        butonn.pack(side=LEFT, fill=Y)


if __name__ == "__main__":
    root = Tk()
    obj = graphik_and_apiclass(root)
    mainloop()