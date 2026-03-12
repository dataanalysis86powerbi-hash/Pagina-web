from flask import Flask, render_template, request, redirect, flash
import pandas as pd
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para mensajes de confirmación

DB_FILE = 'database.db'
EXCEL_FILE = 'contactos.xlsx'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            mensaje TEXT NOT NULL,
            fecha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_to_excel(data):
    if os.path.exists(EXCEL_FILE):
        df_old = pd.read_excel(EXCEL_FILE)
        df_new = pd.DataFrame([data])
        df_combined = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df_combined = pd.DataFrame([data])
    
    df_combined.to_excel(EXCEL_FILE, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto', methods=['POST'])
def contacto():
    nombre = request.form.get('nombre', 'No proporcionado')
    email = request.form.get('email')
    mensaje = request.form.get('mensaje', 'No proporcionado')
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        'nombre': nombre,
        'email': email,
        'mensaje': mensaje,
        'fecha': fecha
    }

    # Guardar en SQLite
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO contactos (nombre, email, mensaje, fecha) VALUES (?, ?, ?, ?)', 
                   (nombre, email, mensaje, fecha))
    conn.commit()
    conn.close()

    # Guardar en Excel
    save_to_excel(data)

    flash('¡Mensaje enviado con éxito!')
    print(f"Nuevo contacto recibido: {email}")
    
    return redirect('/#contacto')

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
