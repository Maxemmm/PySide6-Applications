import sys
import asyncio
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QThreadPool, QRunnable, Signal, QObject
from multiprocessing import Process, Queue
from pyppeteer import launch

from ui_interface import Ui_MainWindow

class BrowserWorkerSignals(QObject):
    finished = Signal()
    result = Signal(str)
    progress = Signal(int)

def browser_process(url, result_queue):
    async def run_async():
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)
        content = await page.content()
        await browser.close()
        return content

    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(run_async())
    loop.close()
    result_queue.put(result)

class BrowserWorker(QRunnable):
    def __init__(self, url, result_queue):
        super().__init__()
        self.url = url
        self.result_queue = result_queue
        self.signals = BrowserWorkerSignals()

    def run(self):
        result_queue = Queue()
        process = Process(target=browser_process, args=(self.url, result_queue))
        process.start()
        process.join()

        result = result_queue.get()
        self.signals.result.emit(result)
        self.signals.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Make sure to call setupUi to set up the UI components

        self.setWindowTitle("Threaded Browser Example")
        self.setGeometry(100, 100, 400, 200)

        self.threadpool = QThreadPool()
        self.ui.pushButton.clicked.connect(self.launch_browser)

    def launch_browser(self):
        url = "https://www.example.com"
        worker = BrowserWorker(url, None)
        worker.signals.result.connect(self.handle_result)
        worker.signals.finished.connect(self.handle_finished)
        worker.signals.progress.connect(self.handle_progress)
        self.threadpool.start(worker)

    def handle_result(self, result):
        print("Browser content:", result)

    def handle_progress(self, progress):
        self.ui.progressBar.setValue(progress)

    def handle_finished(self):
        print("Browser thread finished")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
