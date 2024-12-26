import Vkl_Vukl
import Telo_prog
import time
import winsound
from sys import exit
class Dann_TT:
    """
	расшифровка расшифровка исходящей управляющей команды для ТТ
	участок прибытия|что загрузить			|что разгрузить			|участок возвращения
					|					    |					    |
	гараж		   0|ничего				   0|ничего				   0|гараж		    0
	участок сборки 1|стапель		  1500 1|стапель		  1500 1|участок сборки 1
	склад		   2|стапель		  1400 2|стапель		  1400 2|склад		    2
	контроль	   3|стапель		  1200 3|стапель		  1200 3|контроль	    3
					|кассета с 1100 и 1300 4|кассета с 1100 и 1300 4|
					|стапель общей сборки  5|стапель общей сборки  5|
	"""
    def Port_Otpravka_TT(self,mesto1,zagr,razgr,mesto2):
        try:
            tt = open('Ports/TT.txt', 'w')
            tt.write(str(mesto1) + ' ' + str(zagr) + ' ' + str(razgr) + ' ' + str(mesto2))
            tt.close()
        except:
            print("Ошибка отправки сообщения на ТТ")
    def Rabota_TT(self,oshibka):
        tt = open('Ports/TT.txt', 'w')
        tt.write(str(oshibka))
        tt.close()
    def Port_Priem_TT(self):
        tt = open('Ports/TT.txt', 'r')
        priem=tt.read()
        tt.close()
        if int(priem)==0:
            Vkl_Vukl.Svet_krasn()
            Telo_prog.ind = "Ошибка работы TT. Нажмите \'Стоп\',чтобы\n выключить программу, и проведите диагностику TT\n"
            winsound.PlaySound('Mus/TT.wav', winsound.SND_FILENAME)
            while Telo_prog.knopka != 2:
                time.sleep(0.1)
                if Telo_prog.ex == 1:
                    exit()
        Telo_prog.ind = "Тележка выполнила задачу"
        time.sleep(1)








