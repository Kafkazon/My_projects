import keyboard
import os
import time
from playsound import playsound

"""
q 113 - остановка на текущей операции/ её продолжение
w 119 - доработать цикл до конца и выключится
e 101 - экстренное выключение/запуск бесконечного цикла
"""

class Cl_Prer:

	path = "Svetofor.txt"

	def Preruv_play(self,mus_str):

		playsound('C:/Users/ilsar/PycharmProjects/Diplom/Mus/'+mus_str+'.wav')


	def Preruv(self):
		a=0
		if keyboard.is_pressed("q"):

			print("Остановка программы. Чтобы продолжить, нажмите \'q\', либо нажмите \'e\' для выключения\n")
			Cl_Prer.Preruv_play("rab_priost")
			while(a!=1):
				if keyboard.is_pressed("q"):
					a=1
				if keyboard.is_pressed("e"):
					exit()
				if keyboard.is_pressed('q'):
					print("123")
					keyboard.release('q')
				keyboard.wait('w')
			"""
			prer = 0;
			switch (prer)
			{
			case 101:

				PlaySound(L"Выключение.wav", NULL, SND_FILENAME | SND_ASYNC);
				Sleep(4000);

				exit(0);

				break;
			case 113:



				while (prer != 113)
				{
					if (_kbhit())
						prer = _getch();
					if (prer == 101)
					{
						PlaySound(L"Выключение.wav", NULL, SND_FILENAME | SND_ASYNC);
						Sleep(4000);

						exit(0);
					}
				}
				cout << "Продолжается выполнение программы\n";

				PlaySound(L"Работа продолжена.wav", NULL, SND_FILENAME | SND_ASYNC);

				b.open(path);
				b << 1;
				b.close();

				Sleep(2000);

				b.open(path);
				b << 0;
				b.close();

				break;

			case 119:

				PlaySound(L"Последняя.wav", NULL, SND_FILENAME | SND_ASYNC);
				Sleep(4000);

				prov=1;

				break;
			default: break;
			"""


