import sys
from PyQt5.QtWidgets import QApplication
from alpha_beta_tree_gui import AlphaBetaTreeGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlphaBetaTreeGUI()
    ex.show()
    sys.exit(app.exec_())