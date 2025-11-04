from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    # Conecta no banco (usando as variáveis do container MySQL)
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='teste_db'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 'Conexão com MySQL via Docker funcionando!'")
    result = cursor.fetchone()
    conn.close()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
