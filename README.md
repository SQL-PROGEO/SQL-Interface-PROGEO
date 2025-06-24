
# SQL Interface com PyQt6

Este projeto é uma aplicação desktop desenvolvida em **Python** com **PyQt6**, que permite a interação com um banco de dados SQL por meio de uma interface gráfica intuitiva.

## 📁 Estrutura do Projeto

```

├── README.md             # Documentação do projeto
├── SQL\_Interface.spec    # Arquivo de build com PyInstaller
├── connectDB.py          # Módulo de conexão com o banco de dados
├── functionsButtons.py   # Funções dos botões e eventos da interface
├── interface.py          # Arquivo da interface gráfica principal
├── main.py               # Arquivo principal que inicia o app
├── queries.py            # Módulo com consultas SQL

````

## ⚙️ Funcionalidades

- Conexão com banco de dados SQL (Oracle)
- Interface gráfica com PyQt6
- Execução de consultas SQL pré-definidas
- Filtros e botões interativos
- Separação modular do código (interface, conexões, queries e lógica)
- Suporte a build com **PyInstaller** (`.spec` incluído)

## ▶️ Como Executar

1. **Clone o repositório**
   ```bash
   git clone https://https://github.com/SQL-PROGEO/SQL-Interface-PROGEO
   cd SQL-Interface-PROGEO


2. **Instale as dependências**

   ```bash
   pip install PyQt6
   pip install oracledb
   ```

3. **Execute o projeto**

   ```bash
   python main.py
   ```

## 🛠️ Build com PyInstaller

Para gerar um executável:

```bash
pyinstaller SQL_Interface.spec
```

## 🧠 Módulos

| Arquivo               | Descrição                                              |
| --------------------- | ------------------------------------------------------ |
| `main.py`             | Inicializa a aplicação                                 |
| `interface.py`        | Define a interface principal com PyQt6                 |
| `connectDB.py`        | Responsável pela conexão com o banco                   |
| `functionsButtons.py` | Contém a lógica dos botões e eventos                   |
| `queries.py`          | Define e executa consultas SQL                         |
| `SQL_Interface.spec`  | Arquivo de build para gerar executável com PyInstaller |

## 📄 Licença

Este produto está licenciado sob a responsabilidade da Progeo Engenharia, da Equatorial.

---
## 👤 Autor
Desenvolvido por Filipe Pinheiro.

