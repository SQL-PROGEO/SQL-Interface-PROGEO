import sys
from PyQt6.QtWidgets import QApplication
from interface import MainWindow  # Importa a janela principal do arquivo interface.py

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Cria a aplicação PyQt
    window = MainWindow()  # Cria a janela principal
    window.show()  # Exibe a janela
    sys.exit(app.exec())  # Executa o loop do aplicativo