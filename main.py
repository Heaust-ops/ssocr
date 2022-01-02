import sys
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QMouseEvent, QPainter, QPen, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow
from PIL import ImageGrab
from PIL import Image
import pytesseract
import pyperclip
from pynput import keyboard

class Canvas(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
 
        self.begin = QPoint()
        self.end = QPoint()
        self.setGeometry(0, 0, 1920, 1080)
        self.initUI()
 
    def initUI(self):
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
 
    def paintEvent(self, event):
        qp = QPainter(self)
        br = QBrush(QColor(100, 10, 10, 1))  
        qp.setBrush(br)   
        qp.drawRect(QRect(self.begin, self.end))       

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.end = event.pos()
        x = self.begin.x() if self.begin.x() < self.end.x() else self.end.x()
        y = self.begin.y() if self.begin.y() < self.end.y() else self.end.y()
        # border correction
        x+=1
        y+=1
        width = abs(self.begin.x() - self.end.x())
        height = abs(self.begin.y() - self.end.y())
        bbox = (x, y, x +  width, y + height)
        img = ImageGrab.grab(bbox=bbox)
        img.save('screenshot.png')
        text = pytesseract.image_to_string(Image.open('screenshot.png'))
        print(text)
        pyperclip.copy(text)
        self.close()

def main():
    app = QApplication(sys.argv)
    QApplication.setOverrideCursor(Qt.CrossCursor)
    window = Canvas()
    window.show()
    app.exec_()

progress = 0

def on_press(key):
    global progress
    if key == keyboard.Key.cmd:
        print(1, end="\r")
        progress+=1
    if progress == 1 and key == keyboard.Key.shift:
        print(2, end="\r")
        progress+=1
    if hasattr(key, 'char') and progress == 2:
        if key.char == 'p' or key.char == 'P':
            print(3, end="\r")
            progress=0
            return False

def on_release(key):
    global progress
    progress = 0 if progress < 1 else progress - 1
    print(str(progress), end="\r")

if __name__ == '__main__':
    while True:
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
        print("activated", end="\r")
        main()  
    