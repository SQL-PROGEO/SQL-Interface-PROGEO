from PyQt6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QStackedWidget, QLineEdit
from PyQt6.QtCore import QSize, Qt
import connectDB  # Arquivo para conexões com o banco de dados
import queries  # Arquivo com a consulta SQL
from functionsButtons import open_notas_barramento_page, abrir_fechar_notas_page, alterar_barramento_page, retroceder_carga_page, mudar_fase_page, remover_ip_page

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PROGEO SQL")
        self.setGeometry(100, 100, 400, 300)  # (x, y, largura, altura)
        
        layout = QVBoxLayout()
        
        # QStackedWidget para navegação entre telas
        self.stacked_widget = QStackedWidget()
        
        # Tela inicial
        self.page1 = QWidget()
        self.page1_layout = QVBoxLayout()
        self.label = QLabel("Escolha a base para conectar")
        self.page1_layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Botões para as conexões
        self.maranhao_button = QPushButton("Maranhão")
        self.maranhao_button.setFixedSize(QSize(250, 50))
        self.maranhao_button.clicked.connect(self.connect_MA)
        self.page1_layout.addWidget(self.maranhao_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.para_button = QPushButton("Pará")
        self.para_button.setFixedSize(QSize(250, 50))
        self.para_button.clicked.connect(self.connect_PA)
        self.page1_layout.addWidget(self.para_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.piaui_button = QPushButton("Piauí")
        self.piaui_button.setFixedSize(QSize(250, 50))
        self.piaui_button.clicked.connect(self.connect_PI)
        self.page1_layout.addWidget(self.piaui_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.alagoas_button = QPushButton("Alagoas")
        self.alagoas_button.setFixedSize(QSize(250, 50))
        self.alagoas_button.clicked.connect(self.connect_AL)
        self.page1_layout.addWidget(self.alagoas_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.page1.setLayout(self.page1_layout)

        self.maranhao_pressed = False
        self.piaui_pressed = False
        self.para_pressed = False
        self.alagoas_pressed = False
        
        
        # Tela de confirmação de conexão (Página 2)
        self.page2 = QWidget()
        self.page2_layout = QVBoxLayout()
        
        self.connection_label = QLabel("Você está conectado!")
        self.page2_layout.addWidget(self.connection_label)

        # Exibe qual base foi selecionada
        self.selected_base_label = QLabel("")
        self.page2_layout.addWidget(self.selected_base_label)
        
        # Botões adicionais
        self.button1 = QPushButton("Notas pelo barramento")
        self.button1.clicked.connect(lambda: open_notas_barramento_page(self))

        self.button2 = QPushButton("Abrir/Fechar Nota")
        self.button2.clicked.connect(lambda: abrir_fechar_notas_page(self))

        self.button3 = QPushButton("Alterar barramento")
        self.button3.clicked.connect(lambda: alterar_barramento_page(self))

        self.button4 = QPushButton("Retroceder carga do PROJ")
        self.button4.clicked.connect(lambda: retroceder_carga_page(self))

        self.button5 = QPushButton("Mudar fase do transformador")
        self.button5.clicked.connect(lambda: mudar_fase_page(self))

        self.button6 = QPushButton("Remover IP invisível")
        self.button6.clicked.connect(lambda: remover_ip_page(self)) 
        
        self.page2_layout.addWidget(self.button1)
        self.page2_layout.addWidget(self.button2)
        self.page2_layout.addWidget(self.button3)
        self.page2_layout.addWidget(self.button4)
        self.page2_layout.addWidget(self.button5)
        self.page2_layout.addWidget(self.button6)

        self.page2.setLayout(self.page2_layout)

        # Adicionar as páginas ao QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        layout.addWidget(self.stacked_widget)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Variáveis para manter conexão e cursor
        self.connection = None
        self.cursor = None

    def connect_MA(self):
        self.maranhao_pressed = True

        try:
            # Conectar ao banco Maranhão
            self.connection, self.cursor = connectDB.conectar_MA()
            self.label.setText("Conexão bem-sucedida ao Maranhão!")
            self.selected_base_label.setText("Conectado à base do Maranhão")
            self.stacked_widget.setCurrentIndex(1)  # Mudar para a tela de conexão
        except Exception as e:
            self.label.setText(f"Erro ao conectar: {str(e)}")

    def connect_PA(self):
        self.para_pressed = True

        try:
            # Conectar ao banco Pará
            self.connection, self.cursor = connectDB.conectar_PA()
            self.label.setText("Conexão bem-sucedida ao Pará!")
            self.selected_base_label.setText("Conectado à base do Pará")
            self.stacked_widget.setCurrentIndex(1)
        except Exception as e:
            self.label.setText(f"Erro ao conectar: {str(e)}")

    def connect_PI(self):
        self.piaui_pressed = True

        try:
            # Conectar ao banco Maranhão
            self.connection, self.cursor = connectDB.conectar_PI()
            self.label.setText("Conexão bem-sucedida ao Piauí!")
            self.selected_base_label.setText("Conectado à base do Piauí")
            self.stacked_widget.setCurrentIndex(1)  # Mudar para a tela de conexão
        except Exception as e:
            self.label.setText(f"Erro ao conectar: {str(e)}")


    def connect_AL(self):
        self.alagoas_pressed = True

        try:
            # Conectar ao banco Alagoas
            self.connection, self.cursor = connectDB.conectar_AL()
            self.label.setText("Conexão bem-sucedida ao Alagoas!")
            self.selected_base_label.setText("Conectado à base de Alagoas")
            self.stacked_widget.setCurrentIndex(1)
        except Exception as e:
            self.label.setText(f"Erro ao conectar: {str(e)}")

    def reconnect(self):
        """Reabrir a conexão se estiver fechada"""
        try:
            if self.connection and self.maranhao_pressed:
                self.connection, self.cursor = connectDB.conectar_MA()
            elif self.connection and self.para_pressed:
                self.connection, self.cursor = connectDB.conectar_PA()
            elif self.connection and self.piaui_pressed:
                self.connection, self.cursor = connectDB.conectar_PI()
            elif self.connection and self.alagoas_pressed:
                self.connection, self.cursor = connectDB.conectar_AL()
        except Exception as e:
            self.result_label.setText(f"Erro ao reconectar: {str(e)}")
    
    def go_back(self):
        """Navegar de volta à página anterior"""
        self.stacked_widget.setCurrentIndex(1)  # Voltar à página de conexão

    def closeEvent(self, event):
        """Fechar a conexão com o banco quando a janela for fechada."""
        if self.connection:
            self.connection.close()
        event.accept()
