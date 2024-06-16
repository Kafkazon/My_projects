import time
import main
import Camera_Code
import Telejka_Code
import RG_Code
import RO_Code
import Vkl_Vukl

def work():
    posl = 0
    print("Начать работу?\n")
    #keyboard.wait('e')

    Vkl_Vukl.Vkl()
    Vkl_Vukl.Svet_zel_morg()

    #playsound('Mus/N.wav')

    C1 = Camera_Code.Dann_Cam
    TT1 = Telejka_Code.Dann_TT
    RG1 = RG_Code.Dann_RG
    RO1 = RO_Code.Dann_RO

    while posl != 1:
        main.command = 0
        C1.Port_Otpravka_Cam(1,0)
        print("Камера что то там\n")
        C1.Rabota_Cam(0,1,1,0,0,0)
        C1.Port_Priem_Cam(0)
        time.sleep(3)

        main.command = 1
        TT1.Port_Otpravka_TT(0,0,0,0,0)
        print("ТТ поехала за 1 партией компонентов на склад\n")
        TT1.Rabota_TT(0,1)
        TT1.Port_Priem_TT(0)
        time.sleep(3)

        main.command = 2
        RG1.Port_Otpravka_RG(1,0,0,0,C1.dx,C1.dy,C1.priem_ygol,)
        print("RG загрузил полный бак\n")
        RG1.Rabota_RG(0,1)
        RG1.Port_Priem_RG(0)
        time.sleep(3)

        main.command = 3
        RO1.Port_Otpravka_RO(1,0,1500,1200,2)
        print("RO всё забрал\n")
        RO1.Rabota_RO(0,1,0)
        RO1.Port_Priem_RO(0)
        time.sleep(3)

        #sch_ed+=sch_ed+1
        Vkl_Vukl.Svet_zel_morg()
        main.sch += 1
        print(str(main.sch))