import Vkl_Vukl
import Telo_prog
import time
import shutil
import Camera_Code
import winsound
from sys import exit
flag_1=0
class Dann_Cam:
    photo_numb= 0
    zad=None
    dx=None
    dy=None
    priem_ygol=None
    """
	расшифровка исходящей управляющей команды для камеры, через запятую по столбцам
    операция

    поиск лишних предметов							0
	проверка позиционирования стапеля 1500			1
	проверка позиционирования стапеля 1400			2
	проверка позиционирования стапеля 1200			3
	проверка позиционирования кассеты с 1100 и 1300	4
	проверка позиционирования при сборке 1500		5
	проверка позиционирования при сборке 1300		6
	"""
    def Port_Otpravka_Cam(self,zad):
        Dann_Cam.zad=zad
        try:
            cam = open('Ports/Camera.txt', 'w')
            cam.write(str(zad))
            cam.close()
        except:
            print("Ошибка отправки сообщения на камеру")
    def Rabota_Cam(self,oshibka,flag,x1,y1,ygol):
        cam = open('Ports/Camera.txt', 'w')
        cam.write(str(oshibka) + ' ' + str(flag) + ' ' + str(x1) + ' ' + str(y1) + ' ' + str(ygol))
        cam.close()

    def Port_Priem_Cam(self):
        with open('Ports/Camera.txt', 'r') as cam:
            priem_osh, priem_flag, priem_x1, priem_y1, Dann_Cam.priem_ygol = cam.read().split()
        cam.close()

        Camera_Code.flag_1=priem_flag
        Dann_Cam.photo_numb+=1

        source='Camera_photo_source/'+str(Dann_Cam.zad)+str(priem_osh)+str(priem_flag)+'.png'
        vuh='Camera_photo/pic'+str(Dann_Cam.photo_numb)+'.png'
        dest = shutil.copy(source, vuh)

        if int(priem_osh)==0:
            Vkl_Vukl.Svet_krasn()
            Telo_prog.ind = "Ошибка работы камеры. Нажмите \'Стоп\',чтобы\n выключить программу, и проведите диагностику камеры\n"
            winsound.PlaySound('Mus/Camera.wav', winsound.SND_FILENAME)
            while Telo_prog.knopka != 2:
                time.sleep(0.1)
                if Telo_prog.ex == 1:
                    exit()
        if int(priem_flag)==0:
            if int(Dann_Cam.zad)==0:
                Vkl_Vukl.Svet_jelt()
                Telo_prog.ind = "На столе обнаружены посторонние предметы. Уберите их и нажмите \'Старт\'\n"
                winsound.PlaySound('Mus/Post.wav', winsound.SND_FILENAME)
                Telo_prog.knopka = 2
                if Telo_prog.knopka == 2:
                    while Telo_prog.knopka != 2:
                        time.sleep(0.1)
                        if Telo_prog.ex == 1:
                            exit()
                winsound.PlaySound('Mus/Prod.wav', winsound.SND_FILENAME)
                Vkl_Vukl.Svet_zel_morg()
            else:
                float(Dann_Cam.priem_ygol)
                if int(Dann_Cam.zad)==1:
                    x0=0 # правильные координаты стапеля 1500
                    y0=0
                    Dann_Cam.dx=x0-float(priem_x1)
                    Dann_Cam.dy=y0-float(priem_y1)
                if Dann_Cam.zad == 2:
                    x0=0 # правильные координаты стапеля 1400
                    y0=0
                    Dann_Cam.dx=x0-float(priem_x1)
                    Dann_Cam.dy=y0-float(priem_y1)
                if Dann_Cam.zad == 3:
                    x0=0 # правильные координаты стапеля 1200
                    y0=0
                    Dann_Cam.dx=x0-float(priem_x1)
                    Dann_Cam.dy=y0-float(priem_y1)
                if Dann_Cam.zad == 4:
                    x0=0 # правильные координаты кассеты
                    y0=0
                    Dann_Cam.dx=x0-float(priem_x1)
                    Dann_Cam.dy=y0-float(priem_y1)
                if Dann_Cam.zad == 5:
                    x0=0 # правильные координаты панели 1500
                    y0=0
                    Dann_Cam.dx=x0-float(priem_x1)
                    Dann_Cam.dy=y0-float(priem_y1)
                if Dann_Cam.zad == 6:
                    x0=0 # правильные координаты панели 1300
                    y0=0
                    Dann_Cam.dx=x0-float(priem_x1)
                    Dann_Cam.dy=y0-float(priem_y1)
                if Dann_Cam.zad == 7:
                    x0=0 # правильные координаты панели 1100
                    y0=0
                    Dann_Cam.dx=x0-float(priem_x1)
                    Dann_Cam.dy=y0-float(priem_y1)