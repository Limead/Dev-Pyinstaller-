import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt ,QCoreApplication
import numpy as np
import random
from time import sleep

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def lunch_sample(today_fit):
    category = {"특식" : ["불고기", "찜닭", "닭볶음탕", "스테이크", "월남쌈", "수육", "아귀찜", "쌈밥", "낙지볶음"],
                "찌개" : ["된장찌개", "김치찌개", "부대찌개", "순두부찌개", "동태찌개", "비지찌개", "고추장찌개"],
                "덮밥/볶음밥" : ["카레", "비빔밥", "오므라이스", "김치볶음밥", "제육덮밥", "연어덮밥", "치킨마요덮밥", "돈부리", "오징어덮밥"],
                "면" : ["라멘", "스파게티", "냉면", "국수", "비빔국수","쌀국수", "막국수", "칼국수", "우동", "콩국수"],
                "국/탕" : ["국밥", "갈비탕", "삼계탕", "추어탕", "육개장", "미역국"],
                "간편식" : ["햄버거", "샌드위치", "떡볶이", "밥버거", "도시락", "김밥/유부초밥"],
                "배달" : ["초밥", "중국집", "쌀국수", "치킨", "피자"],
                "해장" : ["라면", "해장국", "순대국", "북엇국"]}
    
    
    random_num1 = np.random.rand()
    if today_fit == "랜덤":
        if random_num1 < 0.125:
            today_fit = "특식"
        elif random_num1 < 0.25:
            today_fit = "찌개"
        elif random_num1 < 0.375:
            today_fit = "덮밥/볶음밥"
        elif random_num1 < 0.5:
            today_fit = "면"
        elif random_num1 < 0.625:
            today_fit = "국/탕"
        elif random_num1 < 0.75:
            today_fit = "간편식"
        elif random_num1 < 0.875:
            today_fit = "배달"
        else:
            today_fit = "해장"
            
    recommend_food = random.sample(category[f"{today_fit}"],1)
    return(today_fit,recommend_food)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('점심추출기',self)
        font = title.font()
        font.setPointSize(50)
        font.setFamily('Times New Roman')
        font.setBold(True)
        
        title.move(210, 25)

        
        lbl_img = QLabel(self)
        new_source = resource_path("sample_img.png")
        pixmap = QPixmap(new_source)
        lbl_img.setPixmap(QPixmap(pixmap))
        lbl_img.move(60, 290)
        
        label1 = QLabel('후보1',self)
        label1.setAlignment(Qt.AlignVCenter)
        label1.move(90, 55)
        
        self.le = QLineEdit(self)
        self.le.move(140, 55)
        self.le.resize(300,20)
        
        label2 = QLabel('후보2',self)
        label2.setAlignment(Qt.AlignVCenter)
        label2.move(90, 115)

        self.le2 = QLineEdit(self)
        self.le2.move(140, 115)
        self.le2.resize(300,20)
        
        label3 = QLabel('후보3',self)
        label3.setAlignment(Qt.AlignVCenter)
        label3.move(90, 175)

        self.le3 = QLineEdit(self)
        self.le3.move(140, 175)
        self.le3.resize(300,20)
        
        self.btn = QPushButton('추출', self)
        self.btn.move(210, 230)
        self.btn.clicked.connect(self.showDialog)
        
        self.btn = QPushButton('Quit', self)
        self.btn.move(370, 350)
        self.btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('점심추출기')
        self.setGeometry(500, 500, 500, 400)
        self.show()
        


    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', '후보를 설정해주세요 ,목록 : [랜덤,특식,찌개,덮밥/볶음밥,면,국/탕,간편식,배달,해장] ::')
        if text != "특식" or text != "찌개" or text != "덮밥/볶음밥" or text != "면" or text != "국/탕" or text != "간편식" or text != "배달" or text != "해장":
            text ="랜덤"
        
        if ok:
            self.le.setText(str(lunch_sample(text)))
            self.le2.setText(str(lunch_sample(text)))
            self.le3.setText(str(lunch_sample(text)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
