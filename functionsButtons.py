# functionsButtons.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
import queries

def open_notas_barramento_page(main_window):
    """
    Cria e exibe a página de consulta "Notas pelo Barramento".
    """
    main_window.notas_barramento_page = QWidget()
    main_window.notas_barramento_layout = QVBoxLayout()

    main_window.notas_barramento_label = QLabel("Digite o barramento:")
    main_window.notas_barramento_layout.addWidget(main_window.notas_barramento_label)

    main_window.input_field = QLineEdit()
    main_window.input_field.setPlaceholderText("Digite a variável para a consulta")
    main_window.notas_barramento_layout.addWidget(main_window.input_field)

    main_window.result_text_edit = QTextEdit()
    main_window.result_text_edit.setReadOnly(True)
    main_window.notas_barramento_layout.addWidget(main_window.result_text_edit)

    main_window.execute_button = QPushButton("Executar Consulta")
    main_window.execute_button.clicked.connect(lambda: execute_notas_barramento_query(main_window))
    main_window.notas_barramento_layout.addWidget(main_window.execute_button)

    main_window.back_button = QPushButton("Voltar")
    main_window.back_button.clicked.connect(main_window.go_back)
    main_window.notas_barramento_layout.addWidget(main_window.back_button)

    main_window.notas_barramento_page.setLayout(main_window.notas_barramento_layout)
    main_window.stacked_widget.addWidget(main_window.notas_barramento_page)
    main_window.stacked_widget.setCurrentIndex(main_window.stacked_widget.count() - 1)

def execute_notas_barramento_query(main_window):
    """
    Executa a consulta de "Notas pelo Barramento" e exibe os resultados.
    """
    try:
        if main_window.connection and main_window.cursor:
            if main_window.connection.close:
                main_window.reconnect()

            input_value = main_window.input_field.text()

            if not input_value:
                main_window.result_text_edit.setText("Erro: A variável não foi fornecida.")
                return

            query = queries.NOTAS_PELO_BARRAMENTO.format(input_value)
            #query = queries.MUDAR_FASE_1.format(input_value)  
            main_window.cursor.execute(query)
            result = main_window.cursor.fetchall()

            if result:
                result_text = "\n".join(str(row[0]) for row in result)
                main_window.result_text_edit.setText(f"Resultado da consulta: \n{result_text}")
            else:
                main_window.result_text_edit.setText("Nenhum dado encontrado.")
        else:
            main_window.result_text_edit.setText("Erro: Conexão não estabelecida.")
    except Exception as e:
        main_window.result_text_edit.setText(f"Erro ao executar consulta: {str(e)}")

def abrir_fechar_notas_page(main_window):
    """
    Cria e exibe a página "Abrir ou Fechar nota".
    """
    main_window.abertura_notas_page = QWidget()
    main_window.abertura_notas_layout = QVBoxLayout()

    main_window.abertura_notas_label = QLabel("Abrir e Fechar nota")
    main_window.abertura_notas_layout.addWidget(main_window.abertura_notas_label)

    main_window.input_field = QLineEdit()
    main_window.input_field.setPlaceholderText("Digite a nota:")
    main_window.abertura_notas_layout.addWidget(main_window.input_field)

    # Label para exibir resultados
    main_window.result_label = QLabel("")
    main_window.abertura_notas_layout.addWidget(main_window.result_label)

    # Botão de abrir nota
    main_window.abrir_nota_button = QPushButton("Abrir nota")
    main_window.abrir_nota_button.clicked.connect(lambda: abrir_nota_query(main_window))
    main_window.abertura_notas_layout.addWidget(main_window.abrir_nota_button)

    # Botão de fechar nota
    main_window.fechar_nota_button = QPushButton("Fechar nota")
    main_window.fechar_nota_button.clicked.connect(lambda: fechar_nota_query(main_window))
    main_window.abertura_notas_layout.addWidget(main_window.fechar_nota_button)

    # Botão de voltar    
    main_window.back_button = QPushButton("Voltar")
    main_window.back_button.clicked.connect(main_window.go_back)
    main_window.abertura_notas_layout.addWidget(main_window.back_button)

    main_window.abertura_notas_page.setLayout(main_window.abertura_notas_layout)

    main_window.stacked_widget.addWidget(main_window.abertura_notas_page)
    main_window.stacked_widget.setCurrentWidget(main_window.abertura_notas_page)

def abrir_nota_query(main_window):
    """
    Executa a abertura de nota.
    """
    try:
        if  main_window.connection and main_window.cursor:
            if main_window.connection.close:
                main_window.reconnect()

            input_value = main_window.input_field.text().strip()

            if not input_value:
                main_window.result_label.setText("Erro: A variável não foi fornecida.")
                return

            query = queries.ABRIR_NOTA.format(input_value)
            main_window.cursor.execute(query)
            main_window.connection.commit()  # Confirmar a alteração no banco

            main_window.result_label.setText(f"Nota {input_value} aberta com sucesso!")

    except Exception as e:
        main_window.result_label.setText(f"Erro ao executar consulta: {str(e)}")

def fechar_nota_query(main_window):
    """
    Executa a fechada de nota.
    """
    try:
        if  main_window.connection and main_window.cursor:
            if main_window.connection.close:
                main_window.reconnect()

            input_value = main_window.input_field.text().strip()

            if not input_value:
                main_window.result_label.setText("Erro: A variável não foi fornecida.")
                return

            query = queries.FECHAR_NOTA.format(input_value)
            main_window.cursor.execute(query)
            main_window.connection.commit()  # Confirmar a alteração no banco

            main_window.result_label.setText(f"Nota {input_value} fechada com sucesso!")

    except Exception as e:
        main_window.result_label.setText(f"Erro ao executar consulta: {str(e)}")

def alterar_barramento_page(main_window):
    """
    Cria e exibe a página "Alterar barramento".
    """
    main_window.alterar_barramento_page = QWidget()
    main_window.alterar_barramento_layout = QVBoxLayout()

    main_window.alterar_barramento_label = QLabel("Novo Barramento:")
    main_window.alterar_barramento_layout.addWidget(main_window.alterar_barramento_label)

    main_window.input_field1 = QLineEdit()
    main_window.input_field1.setPlaceholderText("Digite o novo barramento:")
    main_window.alterar_barramento_layout.addWidget(main_window.input_field1)

    main_window.alterar_barramento_label = QLabel("Barramento existente na base:")
    main_window.alterar_barramento_layout.addWidget(main_window.alterar_barramento_label)

    main_window.input_field2 = QLineEdit()
    main_window.input_field2.setPlaceholderText("Digite o barramento existente na base:")
    main_window.alterar_barramento_layout.addWidget(main_window.input_field2)

    # Label para exibir resultados
    main_window.result_label = QLabel("")
    main_window.alterar_barramento_layout.addWidget(main_window.result_label)

    # Botão de abrir nota
    main_window.execute_button = QPushButton("Executar")
    main_window.execute_button.clicked.connect(lambda: alterar_barramento_query(main_window))
    main_window.alterar_barramento_layout.addWidget(main_window.execute_button)

    # Botão de voltar    
    main_window.back_button = QPushButton("Voltar")
    main_window.back_button.clicked.connect(main_window.go_back)
    main_window.alterar_barramento_layout.addWidget(main_window.back_button)

    main_window.alterar_barramento_page.setLayout(main_window.alterar_barramento_layout)

    main_window.stacked_widget.addWidget(main_window.alterar_barramento_page)
    main_window.stacked_widget.setCurrentWidget(main_window.alterar_barramento_page)

def alterar_barramento_query(main_window):
    """
    Executa a alteração de barramento.
    """
    try:
        if  main_window.connection and main_window.cursor:
            if main_window.connection.close:
                main_window.reconnect()

            input_value1 = main_window.input_field1.text().strip()
            input_value2 = main_window.input_field2.text().strip()

            if not input_value1 or not input_value2:
                main_window.result_label.setText("Erro: A variável não foi fornecida.")
                return

            query = queries.ALTERAR_BARRAMENTO.format(input_value1, input_value2)
            main_window.cursor.execute(query)
            main_window.connection.commit()  # Confirmar a alteração no banco
            

            main_window.result_label.setText("Comando executado!")

    except Exception as e:
        main_window.result_label.setText(f"Erro ao executar consulta: {str(e)}")

def retroceder_carga_page(main_window):
    """
    Cria e exibe a página "Retroceder Carga".
    """
    main_window.retroceder_carga_page = QWidget()
    main_window.retroceder_carga_layout = QVBoxLayout()

    main_window.retroceder_carga_label = QLabel("Nota a retrocer a carga:")
    main_window.retroceder_carga_layout.addWidget(main_window.retroceder_carga_label)

    main_window.input_field = QLineEdit()
    main_window.input_field.setPlaceholderText("Digite o número da nota:")
    main_window.retroceder_carga_layout.addWidget(main_window.input_field)

    # Label para exibir resultados
    main_window.result_label = QLabel("")
    main_window.retroceder_carga_layout.addWidget(main_window.result_label)

    # Botão de abrir nota
    main_window.execute_button = QPushButton("Executar")
    main_window.execute_button.clicked.connect(lambda: retroceder_carga_query(main_window))
    main_window.retroceder_carga_layout.addWidget(main_window.execute_button)

    # Botão de voltar    
    main_window.back_button = QPushButton("Voltar")
    main_window.back_button.clicked.connect(main_window.go_back)
    main_window.retroceder_carga_layout.addWidget(main_window.back_button)

    main_window.retroceder_carga_page.setLayout(main_window.retroceder_carga_layout)

    main_window.stacked_widget.addWidget(main_window.retroceder_carga_page)
    main_window.stacked_widget.setCurrentWidget(main_window.retroceder_carga_page)

def retroceder_carga_query(main_window):
    """
    Executa o retrocesso de carga.
    """
    try:
        if  main_window.connection and main_window.cursor:
            if main_window.connection.close:
                main_window.reconnect()

            input_value = main_window.input_field.text().strip()

            if not input_value:
                main_window.result_label.setText("Erro: A variável não foi fornecida.")
                return

            query = queries.RETROCEDER_CARGA_1.format(input_value)
            main_window.cursor.execute(query)
            main_window.connection.commit()  # Confirmar a alteração no banco

            query = queries.RETROCEDER_CARGA_2.format(input_value)
            main_window.cursor.execute(query)
            main_window.connection.commit()  # Confirmar a alteração no banco
            

            main_window.result_label.setText("Comando executado!")

    except Exception as e:
        main_window.result_label.setText(f"Erro ao executar consulta: {str(e)}")

def mudar_fase_page(main_window):
    """
    Cria e exibe a página "Mudança de fase por transformador".
    """
    main_window.mudar_fase_page = QWidget()
    main_window.mudar_fase_layout = QVBoxLayout()

    main_window.mudar_fase_label = QLabel("Transformador que alimenta as BTs:")
    main_window.mudar_fase_layout.addWidget(main_window.mudar_fase_label)

    main_window.input_field1 = QLineEdit()
    main_window.input_field1.setPlaceholderText("Digite a placa do transformador:")
    main_window.mudar_fase_layout.addWidget(main_window.input_field1)

    main_window.mudar_fase_label = QLabel("A fase nova dos trechos alimentados (AN, ABCN, etc.):")
    main_window.mudar_fase_layout.addWidget(main_window.mudar_fase_label)

    main_window.input_field2 = QLineEdit()
    main_window.input_field2.setPlaceholderText("Digite a fase dos trechos:")
    main_window.mudar_fase_layout.addWidget(main_window.input_field2)

    # Label para exibir resultados
    main_window.result_label = QLabel("")
    main_window.mudar_fase_layout.addWidget(main_window.result_label)

    # Botão de abrir nota
    main_window.execute_button = QPushButton("Executar")
    main_window.execute_button.clicked.connect(lambda: mudar_fase_query(main_window))
    main_window.mudar_fase_layout.addWidget(main_window.execute_button)

    # Botão de voltar    
    main_window.back_button = QPushButton("Voltar")
    main_window.back_button.clicked.connect(main_window.go_back)
    main_window.mudar_fase_layout.addWidget(main_window.back_button)

    main_window.mudar_fase_page.setLayout(main_window.mudar_fase_layout)

    main_window.stacked_widget.addWidget(main_window.mudar_fase_page)
    main_window.stacked_widget.setCurrentWidget(main_window.mudar_fase_page)

def mudar_fase_query(main_window):
    """
    Muda a fase os trechos alimentado pelo transformador.
    """
    try:
        if main_window.connection and main_window.cursor:
            if main_window.connection.close:
                main_window.reconnect()

            input_value = main_window.input_field1.text()
            input_fase = main_window.input_field2.text()

            if not input_value or not input_fase:
                main_window.result_label.setText("Erro: A variável não foi fornecida.")
                return

            query = queries.MUDAR_FASE_1.format(input_value)
            #query = queries.sql
            main_window.cursor.execute(query)
            result = main_window.cursor.fetchall()

            if result:
                result_text = []
                for row in result:
                    result_text.append(str(row[0]))
                
                for i in range(len(result_text)):
                    query2 = queries.MUDAR_FASE_2.format(str(input_fase), str(result_text[i]))
                    main_window.cursor.execute(query2)
                
                main_window.connection.commit()
                main_window.result_label.setText("Fase do trecho de BT alterada com sucesso!")
            else:
                main_window.result_label.setText("Nenhum dado encontrado.")
        else:
            main_window.result_label.setText("Erro: Conexão não estabelecida.")
    except Exception as e:
        main_window.result_label.setText(f"Erro ao executar consulta: {str(e)}")

def remover_ip_page(main_window):
    """
    Cria e exibe a página "Remoção de IP invisíveis".
    """
    main_window.remover_ip_page = QWidget()
    main_window.remover_ip_layout = QVBoxLayout()

    main_window.remover_ip_label = QLabel("Poste 1 do vão de BT:")
    main_window.remover_ip_layout.addWidget(main_window.remover_ip_label)

    main_window.input_field1 = QLineEdit()
    main_window.input_field1.setPlaceholderText("Digite o barramento do poste 1:")
    main_window.remover_ip_layout.addWidget(main_window.input_field1)

    main_window.remover_ip_label = QLabel("Poste 2 do vão de BT:")
    main_window.remover_ip_layout.addWidget(main_window.remover_ip_label)

    main_window.input_field2 = QLineEdit()
    main_window.input_field2.setPlaceholderText("Digite o barramento do poste 1:")
    main_window.remover_ip_layout.addWidget(main_window.input_field2)

    # Label para exibir resultados
    main_window.result_label = QLabel("")
    main_window.remover_ip_layout.addWidget(main_window.result_label)

    # Botão de abrir nota
    main_window.execute_button = QPushButton("Executar")
    main_window.execute_button.clicked.connect(lambda: remover_ip_query(main_window))
    main_window.remover_ip_layout.addWidget(main_window.execute_button)

    # Botão de voltar    
    main_window.back_button = QPushButton("Voltar")
    main_window.back_button.clicked.connect(main_window.go_back)
    main_window.remover_ip_layout.addWidget(main_window.back_button)

    main_window.remover_ip_page.setLayout(main_window.remover_ip_layout)

    main_window.stacked_widget.addWidget(main_window.remover_ip_page)
    main_window.stacked_widget.setCurrentWidget(main_window.remover_ip_page)

def remover_ip_query(main_window):
    """
    Muda a fase os trechos alimentado pelo transformador.
    """
    try:

        if main_window.connection and main_window.cursor:
            if main_window.connection.close:
                main_window.reconnect()

            input_value1 = main_window.input_field1.text()
            input_value2 = main_window.input_field2.text()

            if not input_value1 or not input_value2:
                main_window.result_label.setText("Erro: A variável não foi fornecida.")
                return

            query1 = queries.REMOVER_IP_1.format(input_value1)
            main_window.cursor.execute(query1)
            result1 = main_window.cursor.fetchall()

            query2 = queries.REMOVER_IP_1.format(input_value2)
            main_window.cursor.execute(query2)
            result2 = main_window.cursor.fetchall()

            if result1 and result2:
                result1_text = set()
                result2_text = set()

                for row1 in result1:
                    result1_text.add(str(row1[0]))
                
                for row2 in result2:
                    result2_text.add(str(row2[0]))
                
                common_elements = result1_text.intersection(result2_text)
                if common_elements:
                    for elem in common_elements:
                        query2 = queries.REMOVER_IP_2.format(str(elem))
                        main_window.cursor.execute(query2)
                
                main_window.connection.commit()
                main_window.result_label.setText("IP invisível removida com sucesso!")
            else:
                main_window.result_label.setText("Nenhum dado encontrado.")
        else:
            main_window.result_label.setText("Erro: Conexão não estabelecida.")
    except Exception as e:
        main_window.result_label.setText(f"Erro ao executar consulta: {str(e)}")
