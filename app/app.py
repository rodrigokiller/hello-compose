from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    # Conecta no banco (usando as variáveis do container MySQL)
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 'Conexão com MySQL via Docker funcionando!'")
    result = cursor.fetchone()
    conn.close()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
