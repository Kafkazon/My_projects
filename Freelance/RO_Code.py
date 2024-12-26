import Vkl_Vukl
import Telo_prog
import time
import winsound
from sys import exit
class Dann_RO:
    """
   	расшифровка исходящей управляющей команды для РГ
	операция		  |деталь1				  |деталь2				  |номер штыря
					  |						  |						  |
	ничего		     0|ничего				 0|ничего				 0|i
	установка штыря  1|панель 1500			 1|панель 1500			 1|
	уборка штыря	 2|панель 1400			 2|панель 1400			 2|
					  |панель 1300			 3|панель 1300			 3|
					  |панель 1200			 4|панель 1200			 4|
					  |панель 1100			 5|панель 1100			 5|

	операция		  |деталь1				  |деталь2				  |номер винта
					  |						  |						  |
	вкручивание винта3|ничего				 0|ничего				 0|i
					  |панель 1500			 1|панель 1500			 1|
					  |панель 1400			 2|панель 1400			 2|
					  |панель 1300			 3|панель 1300			 3|
					  |панель 1200			 4|панель 1200			 4|
					  |панель 1100			 5|панель 1100			 5|
	"""
    def Port_Otpravka_RO(self, instr, panel1, panel2, nomer):
        try:
            RO = open('Ports/RO.txt', 'w')
            RO.write(str(instr) + ' ' + str(panel1) + ' ' + str(panel2) + ' ' + str(nomer))
            RO.close()
        except:
            print("Ошибка отправки сообщения на РО")
    def Rabota_RO(self, flag, oshibka):
        RO = open('Ports/RO.txt', 'w')
        RO.write(str(flag) + ' ' + str(oshibka))
        RO.close()
    def Port_Priem_RO(self):
        with open('Ports/RO.txt', 'r') as RO:
            flag, oshibka = RO.read().split()
        RO.close()
        if int(flag)==0:

            if int(oshibka) == 0:
                Vkl_Vukl.Svet_krasn()
                Telo_prog.ind = "Ошибка работы РО. Нажмите \'Стоп\',чтобы\n выключить программу, и проведите диагностику РО\n"
                winsound.PlaySound('Mus/Ro.wav', winsound.SND_FILENAME)
                while Telo_prog.knopka != 2:
                    time.sleep(0.1)
                    if Telo_prog.ex == 1:
                        exit()

            if int(oshibka) == 1:
                Telo_prog.ind = "Потерян штырь. Верните штырь в кассету для штырей и нажмите \'Старт\'\n"
                winsound.PlaySound('Mus/Poter_Shtur.wav', winsound.SND_FILENAME)
                Vkl_Vukl.Svet_jelt()
                Telo_prog.knopka = 2
                if Telo_prog.knopka == 2:
                    while Telo_prog.knopka != 2:
                        time.sleep(0.1)
                        if Telo_prog.ex == 1:
                            exit()
                winsound.PlaySound('Mus/Prod.wav', winsound.SND_FILENAME)
                Vkl_Vukl.Svet_zel_morg()

            if int(oshibka) == 2:
                Telo_prog.ind = "Потерян винт.Верните винт в бункер для винтов и нажмите \'Старт\'\n"
                winsound.PlaySound('Mus/oter_Vintu.wav', winsound.SND_FILENAME)
                Vkl_Vukl.Svet_jelt()
                Telo_prog.knopka = 2
                while Telo_prog.knopka != 2:
                    time.sleep(0.1)
                    if Telo_prog.ex == 1:
                        exit()
                winsound.PlaySound('Mus/Prod.wav', winsound.SND_FILENAME)
                Vkl_Vukl.Svet_zel_morg()

            if int(oshibka) == 3:
                Telo_prog.ind = "В бункере кончились винты. Пополните бункер для винтов и нажмите \'Старт\'\n"
                winsound.PlaySound('Mus/Kon_Vintu.wav', winsound.SND_FILENAME)
                Vkl_Vukl.Svet_jelt()
                Telo_prog.knopka = 2
                if Telo_prog.knopka == 2:
                    while Telo_prog.knopka != 2:
                        time.sleep(0.1)
                        if Telo_prog.ex == 1:
                            exit()
                winsound.PlaySound('Mus/Prod.wav', winsound.SND_FILENAME)
                Vkl_Vukl.Svet_zel_morg()
