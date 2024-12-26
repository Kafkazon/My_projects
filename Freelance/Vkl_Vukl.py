import time
import Telo_prog

def Vkl():

    Vkluch="Включение периферии"
    tt = open('Ports/TT.txt', 'w')
    tt.write(Vkluch)
    tt.close()

    cam = open('Ports/Camera.txt', 'w')
    cam.write(Vkluch)
    cam.close()

    RG = open('Ports/RG.txt', 'w')
    RG.write(Vkluch)
    RG.close()

    RO = open('Ports/RO.txt', 'w')
    RO.write(Vkluch)
    RO.close()

def Vukl():

    Vukluch="Выключение периферии"
    tt = open('Ports/TT.txt', 'w')
    tt.write(Vukluch)
    tt.close()

    cam = open('Ports/Camera.txt', 'w')
    cam.write(Vukluch)
    cam.close()

    RG = open('Ports/RG.txt', 'w')
    RG.write(Vukluch)
    RG.close()

    RO = open('Ports/RO.txt', 'w')
    RO.write(Vukluch)
    RO.close()

    svet = open('Ports/Svetofor.txt', 'w')
    svet.write(Vukluch)
    svet.close()

    Telo_prog.command=1.3
    time.sleep(1)

def Svet_zel_morg():

    svet = open('Ports/Svetofor.txt', 'w')
    svet.write('1')
    svet.close()

    Telo_prog.command=1.1

    time.sleep(1)

    svet = open('Ports/Svetofor.txt', 'w')
    svet.write('0')
    svet.close()


def Svet_jelt():

    svet = open('Ports/Svetofor.txt', 'w')
    svet.write('2')
    svet.close()

    Telo_prog.command=1.2

def Svet_krasn():

    svet = open('Ports/Svetofor.txt', 'w')
    svet.write('3')
    svet.close()

    Telo_prog.command=1.3

def Svet_sbros():

    svet = open('Ports/Svetofor.txt', 'w')
    svet.write('0')
    svet.close()

    Telo_prog.command=1.0