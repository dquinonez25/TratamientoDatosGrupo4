#Archivo con el codigo para la API

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/") # Ruta principal
def home():
    return jsonify({"message": "Bienvenido a la API de Microservicio Base - Grupo 4"})

import random

# Crear una lista de boletos (ID, Sección, Estado)
secciones = ["VIP", "General", "Grada"]
num_boletos = 100

boletos = []

for i in range(1, num_boletos + 1):
    seccion = random.choice(secciones)
    boleto = {
        "id": f"B{i:03}",
        "seccion": seccion,
        "vendido": False
    }
    boletos.append(boleto)

# Mostrar los boletos disponibles
print("Boletos disponibles:")
for b in boletos:
    if not b["vendido"]:
        print(f"{b['id']} - {b['seccion']}")

# Simular la venta de boletos
def vender_boleto(boleto_id):
    for b in boletos:
        if b["id"] == boleto_id and not b["vendido"]:
            b["vendido"] = True
            print(f"Boleto {boleto_id} vendido exitosamente.")
            return
    print(f"Boleto {boleto_id} no está disponible.")

# Usuario compra un boleto
user_input = input("\nIntroduce el ID del boleto que quieres comprar: ")
vender_boleto(user_input)

@app.route("/api/info", methods=['GET'])
def info():
    return jsonify({
        'equipo': 'Grupo 4',
        'autores': ['Angel Jativa', 'Ricardo Penafiel', 'Daniel Quinonez'],
        'proyecto': 'Microservicio Base - Grupo 4',
        'descripcion':'Este microservicio proporciona una API para gestionar la venta de boletos para un concierto',
    })


if __name__ == "__main__": # Ejecutar la aplicación Flask
   app.run(debug=True, host='0.0.0.0', port=8080) # Permite que la aplicación sea accesible desde cualquier IP en el puerto 8080
   

   ############################################# Version mejorada por Ricardo Penafiel

   from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Crear una lista de boletos (ID, Sección, Estado)
secciones = ["VIP", "General", "Grada"]
num_boletos = 100

boletos = [
    {
        "id": f"B{i:03}",
        "seccion": random.choice(secciones),
        "vendido": False
    }
    for i in range(1, num_boletos + 1)
]

@app.route("/")  # Ruta principal
def home():
    return jsonify({"message": "Bienvenido a la API de Microservicio Base - Grupo 4"})

@app.route("/api/boletos", methods=['GET'])
def obtener_boletos():
    boletos_disponibles = [b for b in boletos if not b["vendido"]]
    return jsonify(boletos_disponibles)

@app.route("/api/vender", methods=['POST'])
def vender_boleto():
    data = request.json
    boleto_id = data.get("id")

    for b in boletos:
        if b["id"] == boleto_id:
            if not b["vendido"]:
                b["vendido"] = True
                return jsonify({"message": f"Boleto {boleto_id} vendido exitosamente."}), 200
            else:
                return jsonify({"error": f"Boleto {boleto_id} ya ha sido vendido."}), 400

    return jsonify({"error": f"Boleto {boleto_id} no está disponible."}), 404

@app.route("/api/info", methods=['GET'])
def info():
    return jsonify({
        'equipo': 'Grupo 4',
        'autores': ['Angel Jativa', 'Ricardo Penafiel', 'Daniel Quinonez'],
        'proyecto': 'Microservicio Base - Grupo 4',
        'descripcion': 'Este microservicio proporciona una API para gestionar la venta de boletos para un concierto',
    })

if __name__ == "__main__":  # Ejecutar la aplicación Flask
    app.run(debug=True, host='0.0.0.0', port=8080)  # Permite que la aplicación sea accesible desde cualquier IP en el puerto 8080
