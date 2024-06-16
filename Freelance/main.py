import threading
import Visual
import Telo_prog

if __name__ == "__main__":
    #обеспечение многопоточности
    main_thread = threading.Thread(target=Telo_prog.work)
    tkinter_thread = threading.Thread(target=Visual.win)
    main_thread.start()
    tkinter_thread.start()

    tkinter_thread.join()
    main_thread.join()


