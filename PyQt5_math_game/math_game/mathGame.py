from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from math_utils import createRandomExercises
import time
import sys

class startMathGame(QMainWindow):
     def __init__(self):
          super().__init__()
          self.setFixedSize(400,420)
          self.setWindowTitle('start')
          self.setStyleSheet("background-color:#b3e6ff;")

          self.imageLabel = QLabel(self)
          self.imageLabel.setGeometry(0,0,400,350)
          self.pixmap = QPixmap('./mathGameImage_1.jpg')
          self.changeSize = self.pixmap.scaled(400,350)
          self.imageLabel.setPixmap(self.changeSize)

          self.start = QPushButton('play',self)
          self.start.setGeometry(75,355,250,50)
          self.start.setFont(QFont('Arial',18))
          self.start.clicked.connect(self.stGame)
          self.start.setStyleSheet("""
          background-color:#00cccc;
          color:#000000;
          border-radius:15px;
          border:2px solod 00b3b;
          """)
     def resGame(self):
          self.playAgain = QPushButton('restart again',self)
          self.playAgain.setGeometry(75,355,250,50)
          self.playAgain.setFont(QFont('Arial',14))
          self.playAgain.clicked.connect(self.stGame)
          self.playAgain.setStyleSheet("""
          background-color:#00cccc;
          color:#000000;
          border-radius:15px;
          border:2px solod 00b3b;
          """)
     def stGame(self):
          self.seconWinForGame = PlayMathGame()
          self.seconWinForGame.startGame()
          self.seconWinForGame.show()
          self.close()


class PlayMathGame(QWidget):
     
     points= 0
     difficulty = 2
     exercises = ""
     nextStepCounts = [5,6,8,12,12,13,14,14,14,14,14]
     step = 5
     triesCount = 0
     answer = 0
     nextStepIndex = 0
     def __init__(self):
          super().__init__()
          self.mainWindow()
     def mainWindow(self):
          self.countProgress = 100
          self.setFixedSize(400,420)
          self.setWindowTitle('play game')
          self.setStyleSheet("background-color:#33adff;")

          self.randomExercises = createRandomExercises(self.difficulty)
          self.checkExercises = self.randomExercises
          self.answer = self.randomExercises["answer"]
          self.exercises = self.randomExercises["exercises"]+"=?"
          
          self.label = QLabel(self.exercises,self)
          self.label.setFont(QFont('Arial',18))
          self.label.setAlignment(Qt.AlignCenter)

          self.timer = QTimer(self)
          self.timer.timeout.connect(self.checkGameEnd)

          self.image = QLabel(self)
          self.image.setGeometry(120,50,150,150)
          self.pix = QPixmap('./mathGameImage_2.png')
          self.changeSize = self.pix.scaled(150,150)
          self.image.setPixmap(self.changeSize)
          self.image.setAlignment(Qt.AlignCenter)

          self.one = QPushButton('1',self)
          self.one.setStyleSheet("font-size:30px;")
          self.one.clicked.connect(self.oneButton)

          self.two = QPushButton('2',self)
          self.two.setStyleSheet("font-size:30px;")
          self.two.clicked.connect(self.twoButton)

          self.three = QPushButton('3',self)
          self.three.setStyleSheet("font-size:30px;")
          self.three.clicked.connect(self.threeButton)

          self.progress = QProgressBar(self)
          self.progress.setValue(self.countProgress)
          self.progress.setTextVisible(False)

          self.point = QLabel("0",self)
          self.point.setStyleSheet("font-size:30px;")
          self.point.setAlignment(Qt.AlignCenter)
          
          self.layout = QVBoxLayout()
          self.layout.addWidget(self.point)
          self.layout.addStretch()
          self.layout.addWidget(self.image)
          self.layout.addWidget(self.label)
          self.layout.addWidget(self.progress)
          self.layout.addWidget(self.one)
          self.layout.addWidget(self.two)
          self.layout.addWidget(self.three)
          self.setLayout(self.layout)

     def oneButton(self):
          self.checkAnswer(1)
     def twoButton(self):
          self.checkAnswer(2)
     def threeButton(self):
          self.checkAnswer(3)

     def checkAnswer(self,answer):
          if self.answer==answer:
               self.points = self.points + self.countProgress/20 * self.difficulty
               self.point.setText(str(round(self.points,3)))
               self.triesCount += 1
               if self.triesCount >= self.step:
                    self.nextStepIndex += 1
                    self.step = self.nextStepCounts[self.nextStepIndex]
                    self.triesCount = 0
                    self.difficulty += 1
               time.sleep(0.5)
               self.countProgress = 100
               self.progress.setValue(self.countProgress)
               newExercises = createRandomExercises(self.difficulty)
               if(newExercises == self.checkExercises):
                    self.randomExercises = createRandomExercises(self.difficulty)
                    self.checkExercises = self.randomExercises
               else:
                    self.randomExercises = newExercises
               self.answer = self.randomExercises["answer"]
               self.exercises = self.randomExercises["exercises"]+"=?"
               self.label.setText(self.exercises)
          else:
               self.gameEnd()
               self.gameMessage()
     def startGame(self):
          self.timer.start(20)
     def checkGameEnd(self):
          self.countProgress-=1
          self.progress.setValue(self.countProgress)
          if self.countProgress==0:
               self.gameEnd()
               self.gameMessage()
     
     def gameMessage(self):
          msg = QMessageBox(self)
          msg.setStyleSheet("background-color:#00cccc;")
          msg.setText(f"game over\nyour score: {round(self.points,3)}")
          msg.exec_()
          self.progressCount = 100
          self.progress.setValue(self.progressCount)
          self.points = 0
          self.step = self.nextStepCounts[0]
          self.nextStepIndex = 0
          self.triesCount = 0
          self.difficulty = 2
          self.randomExercises = createRandomExercises(self.difficulty)
          self.answer = self.randomExercises["answer"]
          self.exercises = self.randomExercises["exercises"]+"=?"
          self.label.setText(self.exercises)
     def gameEnd(self):
          self.timer.stop()
          self.restartGame = startMathGame()
          self.restartGame.resGame()
          self.restartGame.show()
          self.close()

app = QApplication(sys.argv)
window = startMathGame()
window.show()
app.exec_()
