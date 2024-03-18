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
    status_message = Signal(str)

def browser_process(url, result_queue, progress_queue, status_queue):
    async def run_async():
        browser = await launch(
            executablePath='C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
            ignoreHTTPSErrors=True,
            headless=False
        )

        status_queue.put("Browser launched")
        progress_queue.put(20)

        page = await browser.newPage()
        await page.setViewport({'width': 1920, 'height': 1080})
        await page.setJavaScriptEnabled(True)

        status_queue.put("New page created")
        progress_queue.put(40)

        await page.goto(url)
        status_queue.put("Page navigated")
        progress_queue.put(60)

        content = await page.content()
        status_queue.put("Content retrieved")
        progress_queue.put(80)

        await browser.close()
        status_queue.put("Browser closed")
        progress_queue.put(100)

        return content

    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(run_async())
    loop.close()
    result_queue.put(result)

class BrowserWorker(QRunnable):
    def __init__(self, url, result_queue, progress_queue, status_queue):
        super().__init__()
        self.url = url
        self.result_queue = result_queue
        self.progress_queue = progress_queue
        self.status_queue = status_queue
        self.signals = BrowserWorkerSignals()

    def run(self):
        result_queue = Queue()
        progress_queue = Queue()
        status_queue = Queue()

        process = Process(target=browser_process, args=(self.url, result_queue, progress_queue, status_queue))
        process.start()

        while process.is_alive():
            while not progress_queue.empty():
                progress = progress_queue.get()
                self.signals.progress.emit(progress)

            while not status_queue.empty():
                status = status_queue.get()
                self.signals.status_message.emit(status)

        process.join()

        result = result_queue.get()
        self.signals.result.emit(result)
        self.signals.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Threaded Browser Example")

        self.threadpool = QThreadPool()
        self.ui.pushButton.clicked.connect(self.launch_browser)

        self.ui.progressBar.setValue(0)
        self.ui.statusbar.showMessage("")

    def launch_browser(self):
        url = "https://www.google.com"
        worker = BrowserWorker(url, None, None, None)
        worker.signals.result.connect(self.handle_result)
        worker.signals.finished.connect(self.handle_finished)
        worker.signals.progress.connect(self.handle_progress)
        worker.signals.status_message.connect(self.handle_status_message)
        self.threadpool.start(worker)

    def handle_result(self, result):
        print("Browser content:", result)

    def handle_finished(self):
        print("Browser thread finished")

    def handle_progress(self, progress):
        self.ui.progressBar.setValue(progress)

    def handle_status_message(self, message):
        self.ui.statusbar.showMessage(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
