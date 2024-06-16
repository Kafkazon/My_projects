import time
import tkinter as tk
from PIL import Image,ImageTk
from sys import exit
import Camera_Code
import Telo_prog
import Visual
import Vkl_Vukl
import winsound

photo_numbvis=0
prephoto=0
ch=0
def win():

    def Vuhod():
        Vkl_Vukl.Vukl()
        winsound.PlaySound('Mus/Vyk.wav', winsound.SND_FILENAME)
        Telo_prog.ex = 1
        exit()

    def Ost():
        Telo_prog.knopka = 2
        print('3')

    def Nach():
        Telo_prog.knopka = 1
        print('1')

    def Posl():
        Telo_prog.posl = 1
        winsound.PlaySound('Mus/Pos.wav', winsound.SND_FILENAME)
        print('1')

    app = tk.Tk()
    app.title("Система Сардинова")
    app.geometry("1500x800")
    app.iconbitmap("icon.ico")

    # определение окон
    scada = tk.Frame(app, background='#60ff80')
    photo_fr = tk.Frame(app)
    knopki = tk.Frame(app)

    # определение кнопок в окне кнопок
    btn1 = tk.Button(knopki, text='Остановка', command=Ost)
    btn3 = tk.Button(knopki, text='Выключение', command=Vuhod)
    btn4 = tk.Button(knopki, text='Старт', command=Nach)
    btn5 = tk.Button(knopki, text='Последняя сборка', command=Posl)

    # определение фото
    Visual.prephoto = ImageTk.PhotoImage(Image.open('Camera_photo/Пустой.png'))
    photo = tk.Label(photo_fr,image = prephoto)
    photo_stroka = tk.Label(photo_fr, text='Время')
    photo_stroka_inf = tk.Label(photo_fr, text='Операция на снимке')

    # картинки объектов
    pre_TT1 = ImageTk.PhotoImage(Image.open('Visualization/TT1.png'))
    pre_TT2 = ImageTk.PhotoImage(Image.open('Visualization/TT2.png'))
    pre_TT3 = ImageTk.PhotoImage(Image.open('Visualization/TT3.png'))

    pre_RG1 = ImageTk.PhotoImage(Image.open('Visualization/RG1.png'))
    pre_RG2 = ImageTk.PhotoImage(Image.open('Visualization/RG2.png'))
    pre_RG3 = ImageTk.PhotoImage(Image.open('Visualization/RG3.png'))

    pre_RO_KL1 = ImageTk.PhotoImage(Image.open('Visualization/RO_KL1.png'))
    pre_RO_KL2 = ImageTk.PhotoImage(Image.open('Visualization/RO_KL2.png'))
    pre_RO_OT1 = ImageTk.PhotoImage(Image.open('Visualization/RO_OT1.png'))
    pre_RO_OT2 = ImageTk.PhotoImage(Image.open('Visualization/RO_OT2.png'))

    pre_SV1 = ImageTk.PhotoImage(Image.open('Visualization/SV1.png'))
    pre_SV2 = ImageTk.PhotoImage(Image.open('Visualization/SV2.png'))
    pre_SV3 = ImageTk.PhotoImage(Image.open('Visualization/SV3.png'))
    pre_SV4 = ImageTk.PhotoImage(Image.open('Visualization/SV4.png'))

    # определение объектов системы
    SV_pic = tk.Label(scada,image = pre_SV1) # Башня
    TT_pic = tk.Label(scada,image = pre_TT1) # Тележка
    RG_pic = tk.Label(scada,image = pre_RG1) # Погрузчик
    RO_pic = tk.Label(scada,image = pre_RO_KL1) # Оператор

    SVl = tk.Label(scada, text='Башня')  # Башня
    TT = tk.Label(scada, text='Транспортная тележка')  # Тележка
    RG = tk.Label(scada, text='Робот-грузчик')  # Погрузчик
    RO = tk.Label(scada, text='Робот-оператор')  # Оператор

    SV_pic.pack()
    TT_pic.pack(side=tk.BOTTOM)
    RG_pic.pack(side=tk.RIGHT)
    RO_pic.pack(side=tk.LEFT)

    SVl.pack()
    TT.pack(side=tk.BOTTOM)
    RG.pack(side=tk.RIGHT)
    RO.pack(side=tk.LEFT)

    # определение счётчика и информационной строки
    sch_ed = tk.Label(scada, text='Количество собранных единиц\n за смену: ' + '0')
    stroka = tk.Label(scada)

    # размещение окна конопок и самих кнопок
    knopki.pack(padx=5, pady=5, side=tk.BOTTOM, fill=tk.X)
    btn1.pack(side=tk.RIGHT, expand=1, fill=tk.X)
    btn3.pack(side=tk.RIGHT, expand=1, fill=tk.X)
    btn4.pack(side=tk.RIGHT, expand=1, fill=tk.X)
    btn5.pack(side=tk.RIGHT, expand=1, fill=tk.X)

    # размещение фрейма фото и самого фото
    photo_fr.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
    photo.pack(pady=20)
    photo_stroka.pack(side=tk.BOTTOM,pady=20)
    photo_stroka_inf.pack(side=tk.BOTTOM)

    # размещение фрейма скады
    scada.pack(ipadx=300, side=tk.RIGHT, expand=1, fill=tk.BOTH)

    # размещение счётчика собранных единиц и строки
    sch_ed.place(x=5, y=10)
    stroka.place(x=5, y=100)

    def Obrabotka_prog():
        sch_ed.config(text='Количество собранных единиц\n за смену: ' + str(Telo_prog.sch))
        stroka.config(text= Telo_prog.ind)

        if Camera_Code.Dann_Cam.photo_numb!=Visual.photo_numbvis:

            Visual.photo_numbvis=Camera_Code.Dann_Cam.photo_numb
            Visual.prephoto = ImageTk.PhotoImage(Image.open('Camera_photo/pic'+str(Camera_Code.Dann_Cam.photo_numb)+'.png'))

            photo.config(image=prephoto)
            photo_stroka.config(text=str(time.strftime("%H:%M:%S", time.localtime())))
            photo_stroka_inf.config(text= Telo_prog.photo_ind)

        if Telo_prog.command == 0:
            SV_pic.config(image=pre_SV1)
            TT_pic.config(image=pre_TT1)
            RG_pic.config(image=pre_RG1)
            RO_pic.config(image=pre_RO_KL1)

        elif Telo_prog.command == 1.1:
            TT_pic.config(image=pre_TT1)
            RG_pic.config(image=pre_RG1)
            RO_pic.config(image=pre_RO_KL1)
            SV_pic.config(image=pre_SV2)

        elif Telo_prog.command == 1.2:
            TT_pic.config(image=pre_TT1)
            RG_pic.config(image=pre_RG1)
            RO_pic.config(image=pre_RO_KL1)
            SV_pic.config(image=pre_SV3)

        elif Telo_prog.command == 1.3:
            TT_pic.config(image=pre_TT1)
            RG_pic.config(image=pre_RG1)
            RO_pic.config(image=pre_RO_KL1)
            SV_pic.config(image=pre_SV4)

        elif Telo_prog.command == 2:
            SV_pic.config(image=pre_SV1)
            RG_pic.config(image=pre_RG1)
            RO_pic.config(image=pre_RO_KL1)
            if Visual.ch==0:
                TT_pic.config(image=pre_TT2)
                Visual.ch=1
            else:
                TT_pic.config(image=pre_TT3)
                Visual.ch = 0

        elif Telo_prog.command == 3:
            TT_pic.config(image=pre_TT1)
            SV_pic.config(image=pre_SV1)
            RO_pic.config(image=pre_RO_KL1)

            if Visual.ch==0:
                RG_pic.config(image=pre_RG3)
                Visual.ch = 1

            elif Visual.ch==1:
                RG_pic.config(image=pre_RG1)
                Visual.ch = 2

            else:
                RG_pic.config(image=pre_RG2)
                Visual.ch = 0

        elif Telo_prog.command == 4.1:
            TT_pic.config(image=pre_TT1)
            SV_pic.config(image=pre_SV1)
            RG_pic.config(image=pre_RG1)
            if Visual.ch==0:
                RO_pic.config(image=pre_RO_KL2)
                Visual.ch = 1
            else:
                RO_pic.config(image=pre_RO_KL1)
                Visual.ch = 0

        elif Telo_prog.command == 4.2:
            TT_pic.config(image=pre_TT1)
            SV_pic.config(image=pre_SV1)
            RG_pic.config(image=pre_RG1)

            if Visual.ch==0:
                RO_pic.config(image=pre_RO_OT2)
                Visual.ch = 1
            else:
                RO_pic.config(image=pre_RO_OT1)
                Visual.ch = 0


        sch_ed.after(200,Obrabotka_prog)
    Obrabotka_prog()
    app.mainloop()