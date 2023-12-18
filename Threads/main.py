from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtWidgets
import sys, time

from ui_interface import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Make sure to call setupUi to set up the UI components

        self.thread = {}
        # Panel 1
        self.ui.start_thread_pnl1_btn1.clicked.connect(self.start_worker_1)
        self.ui.start_thread_pnl1_btn2.clicked.connect(self.start_worker_2)
        self.ui.start_thread_pnl1_btn3.clicked.connect(self.start_worker_3)
        self.ui.stop_thread_pnl1_btn1.clicked.connect(self.stop_worker_1)
        self.ui.stop_thread_pnl1_btn2.clicked.connect(self.stop_worker_2)
        self.ui.stop_thread_pnl1_btn3.clicked.connect(self.stop_worker_3)

        # Panel 2
        self.ui.start_thread_pnl2_btn1.clicked.connect(self.start_worker_4)
        self.ui.start_thread_pnl2_btn2.clicked.connect(self.start_worker_5)
        self.ui.start_thread_pnl2_btn3.clicked.connect(self.start_worker_6)
        self.ui.stop_thread_pnl2_btn1.clicked.connect(self.stop_worker_4)
        self.ui.stop_thread_pnl2_btn2.clicked.connect(self.stop_worker_5)
        self.ui.stop_thread_pnl2_btn3.clicked.connect(self.stop_worker_6)

    # Panel 1
    def start_worker_1(self):
        self.thread[1] = ThreadClass(parent=None, index=1)
        self.thread[1].start()
        self.thread[1].any_signal.connect(self.my_function)
        self.ui.start_thread_pnl1_btn1.setEnabled(False)

    def start_worker_2(self):
        self.thread[2] = ThreadClass(parent=None, index=2)
        self.thread[2].start()
        self.thread[2].any_signal.connect(self.my_function)
        self.ui.start_thread_pnl1_btn2.setEnabled(False)

    def start_worker_3(self):
        self.thread[3] = ThreadClass(parent=None, index=3)
        self.thread[3].start()
        self.thread[3].any_signal.connect(self.my_function)
        self.ui.start_thread_pnl1_btn3.setEnabled(False)

    def stop_worker_1(self):
        self.thread[1].stop()
        self.ui.start_thread_pnl1_btn1.setEnabled(True)
    
    def stop_worker_2(self):
        self.thread[2].stop()
        self.ui.start_thread_pnl1_btn2.setEnabled(True)

    def stop_worker_3(self):
        self.thread[3].stop()
        self.ui.start_thread_pnl1_btn3.setEnabled(True)

    # Panel 2
    def start_worker_4(self):
        self.thread[4] = ThreadClass(parent=None, index=4)
        self.thread[4].start()
        self.thread[4].any_signal.connect(self.my_function)
        self.ui.start_thread_pnl2_btn1.setEnabled(False)

    def start_worker_5(self):
        self.thread[5] = ThreadClass(parent=None, index=5)
        self.thread[5].start()
        self.thread[5].any_signal.connect(self.my_function)
        self.ui.start_thread_pnl2_btn2.setEnabled(False)

    def start_worker_6(self):
        self.thread[6] = ThreadClass(parent=None, index=6)
        self.thread[6].start()
        self.thread[6].any_signal.connect(self.my_function)
        self.ui.start_thread_pnl2_btn3.setEnabled(False)

    def stop_worker_4(self):
        self.thread[4].stop()
        self.ui.start_thread_pnl2_btn1.setEnabled(True)
    
    def stop_worker_5(self):
        self.thread[5].stop()
        self.ui.start_thread_pnl2_btn2.setEnabled(True)

    def stop_worker_6(self):
        self.thread[6].stop()
        self.ui.start_thread_pnl2_btn3.setEnabled(True)

    def my_function(self, counter):
        cnt = counter
        index = self.sender().index
        if index == 1:
            self.ui.progressBar.setValue(cnt)
        elif index == 2:
            self.ui.progressBar_2.setValue(cnt)
        elif index == 3:
            self.ui.progressBar_3.setValue(cnt)
        elif index == 4:
            self.ui.progressBar_4.setValue(cnt)
        elif index == 5:
            self.ui.progressBar_5.setValue(cnt)
        elif index == 6:
            self.ui.progressBar_6.setValue(cnt)
        else:
            raise ValueError(f'Index {index} not found')

class ThreadClass(QtCore.QThread):
    any_signal = QtCore.Signal(int)
    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index = index
        self.is_running = True

    def run(self):
        cnt = 0
        while self.is_running:
            cnt += 1
            if cnt == 100:
                cnt = 0
            time.sleep(0.01)
            self.any_signal.emit(cnt)

    def stop(self):
        self.is_running = False
        print(f'Stopping thread {self.index}')
        self.terminate()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()