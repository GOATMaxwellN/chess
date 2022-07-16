import sys
from board import BoardView, BoardScene
from game import PieceMovements, ChessGame

from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                               QSizePolicy)
from PySide6.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self, parent=None, f=Qt.WindowFlags()):
        super().__init__(parent, f)
        self.setWindowTitle("Maxwell's Chess Game")
        self.setWindowState(Qt.WindowMaximized)
        self.setStyleSheet("background-color: blue")

        # ChessGame reference
        self.currentGame = None
    
        # New game button
        newGameBtn = QPushButton("New Game")
        newGameBtn.clicked.connect(self.startNewGame)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.addWidget(newGameBtn)
        self.setLayout(self.mainLayout)
        
    def startNewGame(self):
        self.emptyWindow()
        self.currentGame = ChessGame(BoardView())
        # Add game screen to window
        self.mainLayout.addWidget(self.currentGame)

    def emptyWindow(self):
        for i in reversed(range(self.mainLayout.count())):
            widget = self.mainLayout.itemAt(i).widget()
            self.mainLayout.removeWidget(widget)
            widget.hide()
            widget.destroy()


if __name__ == "__main__":
    app = QApplication([])

    main = MainWindow()
    main.show()

    sys.exit(app.exec())