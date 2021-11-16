# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# QT CORE
# Change for PySide Or PyQt
# ///////////////////////// WARNING: ////////////////////////////
# Remember that changing to PyQt too many modules will have 
# problems because some classes have different names like: 
# Property (pyqtProperty), Slot (pyqtSlot), Signal (pyqtSignal)
# among others.
# ///////////////////////////////////////////////////////////////
# from PyQt6.QtCore import *
# from PyQt6.QtGui import *
# from PyQt6.QtWidgets import *
# from PyQt6.QtSvgWidgets import *

from PyQt6.QtCore import Qt
from PyQt6.QtCore import QMetaObject
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtCore import PYQT_SIGNAL, PYQT_SLOT
from PyQt6.QtCore import QEvent
from PyQt6.QtCore import QSize
from PyQt6.QtCore import QRect
from PyQt6.QtCore import QPoint
from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtCore import QEasingCurve
from PyQt6.QtCore import QParallelAnimationGroup

from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QColor
from PyQt6.QtGui import QPainter
from PyQt6.QtGui import QPen
from PyQt6.QtGui import QCursor
from PyQt6.QtGui import QBrush
from PyQt6.QtGui import QPixmap

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QFrame
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtWidgets import QScrollArea
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtWidgets import QSizeGrip
from PyQt6.QtWidgets import QSpacerItem
from PyQt6.QtWidgets import QHeaderView
from PyQt6.QtWidgets import QAbstractItemView
from PyQt6.QtWidgets import QTableWidget
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QSlider
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
# missing QSvgWidget in PyQt6