from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_widget = QTabWidget()
        self.tab_widget.tabBar().setStyleSheet("""
            ::tab:disabled { width: 0; height: 0; margin: 0; padding: 0; border: none; }
        """)

        self.tab_widget.addTab(QPushButton('Tab 1'), 'Tab 1')
        self.tab_widget.addTab(QPushButton('Tab 2'), 'Tab 2')

        self.button = QPushButton('Show/Hide tab #2')
        self.button.setCheckable(True)
        self.button.setChecked(True)
        self.button.clicked.connect(lambda checked: self.tab_widget.setTabEnabled(1, checked))

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.tab_widget)

        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.show()

    app.exec()