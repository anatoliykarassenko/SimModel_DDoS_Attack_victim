from PyQt5.QtWidgets import QApplication
from uiControl.MainWindowControl import MainWindowControl
from tornado.ioloop import IOLoop



def main():
    app = QApplication([])
    io_loop = IOLoop.current()
    window = MainWindowControl(io_loop)
    # tornado.
    window.show()
    app.exec_()

    # io_loop.start()


if __name__ == '__main__':
    main()
