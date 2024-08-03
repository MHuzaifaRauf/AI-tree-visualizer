import sys
from PyQt5.QtWidgets import QApplication
from minimax_tree_gui import MinimaxTreeGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MinimaxTreeGUI()
    ex.show()
    sys.exit(app.exec_())