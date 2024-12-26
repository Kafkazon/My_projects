import Vkl_Vukl
import Telo_prog
import time
import winsound
from sys import exit
class Dann_RG:
    """
    расшифровка расшифровка исходящей управляющей команды для РГ
    работа с чем	  |что загрузить		  |что разгрузить		  |  |  |
                      |						  |						  |  |  |
    ничего		     0|ничего				 0|ничего				 0|0 |0 |0
    с ТТ			 1|стапель 1500			 1|стапель 1500			 1|  |  |
                      |стапель 1400			 2|стапель 1400			 2|  |  |
                      |стапель 1200			 3|стапель 1200			 3|  |  |
                      |кассета с 1100 и 1300 4|кассета с 1100 и 1300 4|  |  |
                      |собранную единицу	 5|						  |  |  |

    работа с чем	  |что пер. в ст. общ. сб.|						  |  |  |
                      |						  |						  |  |  |
    с общим стапелем 2|ничего				 0|0					  |0 |0 |0
                      |панель 1500			 1|						  |  |  |
                      |панель 1400			 2|						  |  |  |
                      |панель 1300			 3|						  |  |  |
                      |панель 1200			 4|						  |  |  |
                      |панель 1100			 5|						  |  |  |

    работа с чем	  |						  |						  |x1|y1|ygol
                      |						  |						  |  |  |
    корректировка    3|0					  |0					  |зн|зн|зн

    работа с чем	  |						  |						  |  |  |
                      |						  |						  |  |  |
    доведение	     4|0					  |0					  |0 |0 |0


    работа с чем	  |						  |						  |  |  |
                      |						  |						  |  |  |
    переворот	     5|0					  |0					  |0 |0 |0

	"""
    def Port_Otpravka_RG(self, s_chem, zagr, razgr, x1, y1, ygol):
        try:
            RG = open('Ports/RG.txt', 'w')
            RG.write(str(s_chem) + ' ' + str(zagr) + ' ' + str(razgr) + ' ' + str(x1)+ ' ' + str(y1)+ ' ' + str(ygol))
            RG.close()
#            print(s_chem)
#            print(zagr)
#            print(razgr)
#            print(x1)
#            print(y1)
#            print(ygol)
        except:
            print("Ошибка отправки сообщения на РГ")
    def Rabota_RG(self,oshibka):
        RG = open('Ports/RG.txt', 'w')
        RG.write(str(oshibka))
        RG.close()
    def Port_Priem_RG(self):
        RG = open('Ports/RG.txt', 'r')
        priem=RG.read()
        RG.close()
        if int(priem)==0:
            Vkl_Vukl.Svet_krasn()
            Telo_prog.ind = "Ошибка работы РГ. Нажмите \'Стоп\',чтобы\n выключить программу, и проведите диагностику РГ\n"
            winsound.PlaySound('Mus/Rg.wav', winsound.SND_FILENAME)
            while Telo_prog.knopka != 2:
                time.sleep(0.1)
                if Telo_prog.ex == 1:
                    exit()
