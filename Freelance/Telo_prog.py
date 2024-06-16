import time
import Telo_prog
import Camera_Code
import Telejka_Code
import RG_Code
import RO_Code
import Vkl_Vukl
import winsound
from sys import exit

sch = 0
stop = False
command = 0
posl = 0
knopka = 0
ex=0
posl_vis = 0
i=0
j=0
ind='Начать работу?'
photo_ind=''
command_buf=0

def prov():
    if knopka==2:
        Telo_prog.command_buf = Telo_prog.command
        Telo_prog.command=0
        winsound.PlaySound('Mus/Ost.wav', winsound.SND_FILENAME)
        while  knopka!=1:
            time.sleep(0.1)
            if Telo_prog.ex == 1:
                exit()
        Vkl_Vukl.Svet_zel_morg()
        Telo_prog.command=Telo_prog.command_buf
        winsound.PlaySound('Mus/Prod.wav', winsound.SND_FILENAME)
    if Telo_prog.ex==1:
        exit()

def work():

    while Telo_prog.knopka!=1:
        if ex == 1:
            exit()
        time.sleep(0.1)
    Telo_prog.knopka=0
    Telo_prog.posl=0
    Telo_prog.ind="Работа начата\n"
    Vkl_Vukl.Vkl()
    Vkl_Vukl.Svet_zel_morg()

    winsound.PlaySound('Mus/N.wav', winsound.SND_FILENAME)
    C1 = Camera_Code.Dann_Cam
    TT1 = Telejka_Code.Dann_TT
    RG1 = RG_Code.Dann_RG
    RO1 = RO_Code.Dann_RO

    while Telo_prog.posl != 1:

        C1.Port_Otpravka_Cam(0,0)
        C1.Rabota_Cam(0,1,1,0,0,0)
        prov()
        C1.Port_Priem_Cam(0)
        Telo_prog.photo_ind = "Поиск посторонних предметов\n"

        Telo_prog.command = 2
        TT1.Port_Otpravka_TT(0,2,234,0,1)
        Telo_prog.ind="ТТ поехала за 1 партией компонентов на склад\n"
        TT1.Rabota_TT(0,1)
        Telo_prog.i = 0
        while Telo_prog.i!=6:
            Telo_prog.i+=1
            time.sleep(0.5)
            prov()
        TT1.Port_Priem_TT(0)

        Camera_Code.flag_1=0
        while Camera_Code.flag_1==0:
            Telo_prog.command = 3
            RG1.Port_Otpravka_RG(0,1,0,4,C1.dx,C1.dy,C1.priem_ygol,)
            Telo_prog.ind="Робот-грузчик разгружает с ТТ кассету с панелями\n"
            RG1.Rabota_RG(0,1)
            Telo_prog.i = 0
            while Telo_prog.i!=6:
                Telo_prog.i+=1
                time.sleep(0.5)
                prov()
            RG1.Port_Priem_RG(0)

            C1.Port_Otpravka_Cam(0,4)
            C1.Rabota_Cam(0,1,1,0,0,0)
            prov()
            C1.Port_Priem_Cam(0)
            Telo_prog.photo_ind = "Проверка правильности позиционирования кассеты\n"

        RG1.Port_Otpravka_RG(0, 4, 0, 0, C1.dx, C1.dy, C1.priem_ygol, )
        RG1.Rabota_RG(0, 1)
        RG1.Port_Priem_RG(0)

        Camera_Code.flag_1=0
        while Camera_Code.flag_1 ==0:
            Telo_prog.command = 3
            RG1.Port_Otpravka_RG(0, 1, 0, 3, C1.dx, C1.dy, C1.priem_ygol, )
            Telo_prog.ind = "Робот-грузчик разгружает с ТТ стапель с панелью 1200\n"
            RG1.Rabota_RG(0, 1)
            Telo_prog.i = 0
            while Telo_prog.i != 6:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()
            RG1.Port_Priem_RG(0)

            C1.Port_Otpravka_Cam(0, 3)
            C1.Rabota_Cam(0, 1, 1, 0, 0, 0)
            prov()
            C1.Port_Priem_Cam(0)
            Telo_prog.photo_ind = "Проверка правильности позиционирования стапеля с панелью 1200\n"

        RG1.Port_Otpravka_RG(0, 4, 0, 0, C1.dx, C1.dy, C1.priem_ygol, )
        RG1.Rabota_RG(0, 1)
        RG1.Port_Priem_RG(0)

        Camera_Code.flag_1=0
        while Camera_Code.flag_1 == 0:
            Telo_prog.command = 3
            RG1.Port_Otpravka_RG(0, 1, 0, 2, C1.dx, C1.dy, C1.priem_ygol, )
            Telo_prog.ind = "Робот-грузчик разгружает с ТТ стапель с панелью 1400\n"
            RG1.Rabota_RG(0, 1)
            Telo_prog.i = 0
            while Telo_prog.i != 6:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()
            RG1.Port_Priem_RG(0)

            C1.Port_Otpravka_Cam(0, 2)
            C1.Rabota_Cam(0, 1, 1, 0, 0, 0)
            prov()
            C1.Port_Priem_Cam(0)
            Telo_prog.photo_ind = "Проверка правильности позиционирования стапеля с панелью 1400\n"

        RG1.Port_Otpravka_RG(0, 4, 0, 0, C1.dx, C1.dy, C1.priem_ygol, )
        RG1.Rabota_RG(0, 1)
        RG1.Port_Priem_RG(0)

        Telo_prog.command = 3
        RG1.Port_Otpravka_RG(0, 2, 3, 0, C1.dx, C1.dy, C1.priem_ygol, )
        Telo_prog.ind = "Робот-грузчик разгружает переносит панель 1200 в стапель общей сборки\n"
        RG1.Rabota_RG(0, 1)
        Telo_prog.i = 0
        while Telo_prog.i != 6:
            Telo_prog.i += 1
            time.sleep(0.5)
            prov()
        RG1.Port_Priem_RG(0)

        Telo_prog.command = 3
        RG1.Port_Otpravka_RG(0, 2, 2, 0, C1.dx, C1.dy, C1.priem_ygol, )
        Telo_prog.ind = "Робот-грузчик переносит панель 1400 в стапель общей сборки\n"
        RG1.Rabota_RG(0, 1)
        Telo_prog.i = 0
        while Telo_prog.i != 6:
            Telo_prog.i += 1
            time.sleep(0.5)
            prov()
        RG1.Port_Priem_RG(0)

        Telo_prog.command = 3
        RG1.Port_Otpravka_RG(0, 1, 23, 0, C1.dx, C1.dy, C1.priem_ygol, )
        Telo_prog.ind = "Робот-грузчик переносит пустые стапели на ТТ\n"
        RG1.Rabota_RG(0, 1)
        Telo_prog.i = 0
        while Telo_prog.i != 6:
            Telo_prog.i += 1
            time.sleep(0.5)
            prov()
        RG1.Port_Priem_RG(0)

        Telo_prog.command = 2
        TT1.Port_Otpravka_TT(0,2,0,23,0)
        Telo_prog.ind="ТТ увозит пустые стапеля на склад\n"
        TT1.Rabota_TT(0,1)
        Telo_prog.i = 0
        while Telo_prog.i!=6:
            Telo_prog.i+=1
            time.sleep(0.5)
            prov()
        TT1.Port_Priem_TT(0)

        Camera_Code.flag_1=0
        while Camera_Code.flag_1 == 0:
            Telo_prog.command = 3
            RG1.Port_Otpravka_RG(0, 2, 6, 0, C1.dx, C1.dy, C1.priem_ygol, )
            Telo_prog.ind = "Робот-грузчик переносит панель 1300 в стапель общей сборки\n"
            RG1.Rabota_RG(0, 1)
            Telo_prog.i = 0
            while Telo_prog.i != 6:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()
            RG1.Port_Priem_RG(0)

            C1.Port_Otpravka_Cam(0, 6)
            C1.Rabota_Cam(0, 1, 1, 0, 0, 0)
            prov()
            C1.Port_Priem_Cam(0)
            Telo_prog.photo_ind = "Проверка правильности позиционирования панели 1300 на общей сборке\n"

        RG1.Port_Otpravka_RG(0, 4, 0, 0, C1.dx, C1.dy, C1.priem_ygol, )
        RG1.Rabota_RG(0, 1)
        RG1.Port_Priem_RG(0)

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0,1,1300,1200,Telo_prog.j)
            Telo_prog.ind = "RO устанавливает соосность отверстий панелей 1300 и 1200 штырём "+str(Telo_prog.j)+"\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0,1,0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0, 1, 1300, 1400, Telo_prog.j)
            Telo_prog.ind = "RO устанавливает соосность отверстий панелей 1300 и 1400 штырём "+str(Telo_prog.j)+"\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 1
        while Telo_prog.j != 23:
            RO1.Port_Otpravka_RO(0, 3, 1300, 1200, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет винтовое соединение панелей 1300 и 1200, вкручиванием винта "+str(Telo_prog.j)+"\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()


        Telo_prog.command = 4.2
        Telo_prog.j = 1
        while Telo_prog.j != 23:
            RO1.Port_Otpravka_RO(0, 3, 1300, 1400, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет винтовое соединение панелей 1300 и 1400, вкручиванием винта "+str(Telo_prog.j)+"\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0, 2, 1300, 1200, Telo_prog.j)
            Telo_prog.ind = "RO убирает штырь " + str(Telo_prog.j) + " из отверстия панелей 1300 и 1200\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0, 2, 1300, 1400, Telo_prog.j)
            Telo_prog.ind = "RO убирает штырь " + str(Telo_prog.j) + " из отверстия панелей 1300 и 1400\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 23
        while Telo_prog.j != 25:
            RO1.Port_Otpravka_RO(0, 3, 1300, 1200, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет дозакручивание винта "+str(Telo_prog.j)+" в отверстие панелей 1300 и 1200\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 23
        while Telo_prog.j != 25:
            RO1.Port_Otpravka_RO(0, 3, 1300, 1400, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет дозакручивание винта "+str(Telo_prog.j)+" в отверстие панелей 1300 и 1400\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 3
        RG1.Port_Otpravka_RG(0, 2, 5, 0, C1.dx, C1.dy, C1.priem_ygol, )
        Telo_prog.ind = "Робот-грузчик переносит панель 1100 в стапель общей сборки\n"
        RG1.Rabota_RG(0, 1)
        Telo_prog.i = 0
        while Telo_prog.i != 6:
            Telo_prog.i += 1
            time.sleep(0.5)
            prov()
        RG1.Port_Priem_RG(0)

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0, 1, 1100, 1200, Telo_prog.j)
            Telo_prog.ind = "RO устанавливает соосность отверстий панелей 1100 и 1200 штырём " + str(
                Telo_prog.j) + "\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0, 1, 1100, 1400, Telo_prog.j)
            Telo_prog.ind = "RO устанавливает соосность отверстий панелей 1100 и 1400 штырём " + str(
                Telo_prog.j) + "\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 1
        while Telo_prog.j != 12:
            RO1.Port_Otpravka_RO(0, 3, 1100, 1200, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет винтовое соединение панелей 1100 и 1200, вкручиванием винта "+str(Telo_prog.j)+"\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 1
        while Telo_prog.j != 12:
            RO1.Port_Otpravka_RO(0, 3, 1100, 1400, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет винтовое соединение панелей 1100 и 1400, вкручиванием винта "+str(Telo_prog.j)+"\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 1
        while Telo_prog.j != 14:
            RO1.Port_Otpravka_RO(0, 3, 1100, 1300, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет винтовое соединение панелей 1100 и 1300, вкручиванием винта " + str(Telo_prog.j) + "\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0, 2, 1100, 1200, Telo_prog.j)
            Telo_prog.ind = "RO убирает штырь " + str(Telo_prog.j) + " из отверстия панелей 1100 и 1200\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0, 2, 1100, 1400, Telo_prog.j)
            Telo_prog.ind = "RO убирает штырь " + str(Telo_prog.j) + " из отверстия панелей 1100 и 1400\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 12
        while Telo_prog.j != 14:
            RO1.Port_Otpravka_RO(0, 3, 1100, 1200, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет дозакручивание винта "+str(Telo_prog.j)+" в отверстие панелей 1100 и 1200\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 12
        while Telo_prog.j != 14:
            RO1.Port_Otpravka_RO(0, 3, 1100, 1400, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет дозакручивание винта "+str(Telo_prog.j)+" в отверстие панелей 1100 и 1400\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 2
        TT1.Port_Otpravka_TT(0, 2, 1, 0, 1)
        Telo_prog.ind = "ТТ направляется в склад и загружается там стапелем с панельню 1500\n"
        time.sleep(1)
        TT1.Rabota_TT(0, 1)
        Telo_prog.i = 0
        #тележечный финт

        Telo_prog.command = 3
        RG1.Port_Otpravka_RG(0, 5, 0, 0, C1.dx, C1.dy, C1.priem_ygol, )
        Telo_prog.ind = "Робот-грузчик поднимает сборку, переворачивает её\n на 180 градусов и возвращает в стапель общей сборки по КФО\n"
        RG1.Rabota_RG(0, 1)
        Telo_prog.i = 0
        while Telo_prog.i != 6:
            Telo_prog.i += 1
            time.sleep(0.5)
            prov()
        RG1.Port_Priem_RG(0)

        Telo_prog.command = 2
        TT1.Port_Priem_TT(0)

        Camera_Code.flag_1 = 0
        while Camera_Code.flag_1 == 0:
            Telo_prog.command = 3
            RG1.Port_Otpravka_RG(0, 1, 0, 1, C1.dx, C1.dy, C1.priem_ygol, )
            Telo_prog.ind = "Робот-грузчик разгружает с ТТ стапель с панелью 1500\n"
            RG1.Rabota_RG(0, 1)
            Telo_prog.i = 0
            while Telo_prog.i != 6:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()
            RG1.Port_Priem_RG(0)

            C1.Port_Otpravka_Cam(0, 1)
            C1.Rabota_Cam(0, 1, 1, 0, 0, 0)
            prov()
            C1.Port_Priem_Cam(0)
            Telo_prog.photo_ind = "Проверка правильности позиционирования стапеля с панелью 1500\n"

        RG1.Port_Otpravka_RG(0, 4, 0, 0, C1.dx, C1.dy, C1.priem_ygol, )
        RG1.Rabota_RG(0, 1)
        RG1.Port_Priem_RG(0)

        Camera_Code.flag_1 = 0
        while Camera_Code.flag_1 == 0:
            Telo_prog.command = 3
            RG1.Port_Otpravka_RG(0, 2, 5, 0, C1.dx, C1.dy, C1.priem_ygol, )
            Telo_prog.ind = "Робот-грузчик переносит панель 1500 в стапель общей сборки\n"
            RG1.Rabota_RG(0, 1)
            Telo_prog.i = 0
            while Telo_prog.i != 6:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()
            RG1.Port_Priem_RG(0)

            C1.Port_Otpravka_Cam(0, 5)
            C1.Rabota_Cam(0, 1, 1, 0, 0, 0)
            prov()
            C1.Port_Priem_Cam(0)
            Telo_prog.photo_ind = "Проверка правильности позиционирования панели 1500 на общей сборке\n"

        RG1.Port_Otpravka_RG(0, 4, 0, 0, C1.dx, C1.dy, C1.priem_ygol, )
        RG1.Rabota_RG(0, 1)
        RG1.Port_Priem_RG(0)

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0, 1, 1500, 1200, Telo_prog.j)
            Telo_prog.ind = "RO устанавливает соосность отверстий панелей 1500 и 1200 штырём " + str(Telo_prog.j) + "\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0, 1, 1500, 1400, Telo_prog.j)
            Telo_prog.ind = "RO устанавливает соосность отверстий панелей 1500 и 1400 штырём " + str(Telo_prog.j) + "\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 3
        RG1.Port_Otpravka_RG(0, 1, 14, 0, C1.dx, C1.dy, C1.priem_ygol, )
        Telo_prog.ind = "Робот-грузчик переносит пустой стапель и кассету на ТТ\n"
        RG1.Rabota_RG(0, 1)
        Telo_prog.i = 0
        while Telo_prog.i != 6:
            Telo_prog.i += 1
            time.sleep(0.5)
            prov()
        RG1.Port_Priem_RG(0)

        Telo_prog.command = 2
        TT1.Port_Otpravka_TT(0, 2, 5, 14, 1)
        Telo_prog.ind = "ТТ направляется в склад и разгружается стапелем\n с панельню 1500, загружает стапель общей сборки\n"
        time.sleep(1)
        TT1.Rabota_TT(0, 1)
        Telo_prog.i = 0

        Telo_prog.command = 4.2
        Telo_prog.j = 1
        while Telo_prog.j != 23:
            RO1.Port_Otpravka_RO(0, 3, 1500, 1200, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет винтовое соединение панелей 1500 и 1200, вкручиванием винта "+str(Telo_prog.j)+"\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 1
        while Telo_prog.j != 23:
            RO1.Port_Otpravka_RO(0, 3, 1500, 1400, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет винтовое соединение панелей 1500 и 1400, вкручиванием винта "+str(Telo_prog.j)+"\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 1
        while Telo_prog.j != 16:
            RO1.Port_Otpravka_RO(0, 3, 1500, 1100, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет винтовое соединение панелей 1500 и 1100, вкручиванием винта " + str(Telo_prog.j) + "\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0, 2, 1500, 1200, Telo_prog.j)
            Telo_prog.ind = "RO убирает штырь " + str(Telo_prog.j) + " из отверстия панелей 1500 и 1200\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.1
        Telo_prog.j = 1
        while Telo_prog.j != 3:
            RO1.Port_Otpravka_RO(0, 2, 1500, 1400, Telo_prog.j)
            Telo_prog.ind = "RO убирает штырь " + str(Telo_prog.j) + " из отверстия панелей 1500 и 1400\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 23
        while Telo_prog.j != 25:
            RO1.Port_Otpravka_RO(0, 3, 1500, 1200, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет дозакручивание винта "+str(Telo_prog.j)+" в отверстие панелей 1500 и 1200\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 4.2
        Telo_prog.j = 23
        while Telo_prog.j != 25:
            RO1.Port_Otpravka_RO(0, 3, 1500, 1400, Telo_prog.j)
            Telo_prog.ind = "RO осуществляет дозакручивание винта "+str(Telo_prog.j)+" в отверстие панелей 1500 и 1400\n"
            Telo_prog.j += 1
            RO1.Rabota_RO(0, 1, 0)
            RO1.Port_Priem_RO(0)
            Telo_prog.i = 0
            while Telo_prog.i != 2:
                Telo_prog.i += 1
                time.sleep(0.5)
                prov()

        Telo_prog.command = 2
        TT1.Port_Priem_TT(0)

        Telo_prog.command = 3
        RG1.Port_Otpravka_RG(0, 1, 5, 0, C1.dx, C1.dy, C1.priem_ygol, )
        Telo_prog.ind = "Робот-грузчик переносит собранную единицу на ТТ в стапель общей сборки\n"
        RG1.Rabota_RG(0, 1)
        Telo_prog.i = 0
        while Telo_prog.i != 6:
            Telo_prog.i += 1
            time.sleep(0.5)
            prov()
        RG1.Port_Priem_RG(0)


        Telo_prog.command = 2
        TT1.Port_Otpravka_TT(0, 3, 0, 5, 0)
        Telo_prog.ind = "ТТ отвозит готовую сборочную единицу на участок контроля\n"
        TT1.Rabota_TT(0, 1)
        Telo_prog.i = 0
        while Telo_prog.i != 6:
            Telo_prog.i += 1
            time.sleep(0.5)
            prov()
        TT1.Port_Priem_TT(0)


        Vkl_Vukl.Svet_zel_morg()
        Telo_prog.sch += 1
        winsound.PlaySound('Mus/Sobrana.wav', winsound.SND_FILENAME)

    Telo_prog.command = 0
    Telo_prog.ind="Продолжить работу?"

    while knopka != 1:
        if ex == 1:
            exit()
    work()
