from flask import Flask, jsonify, request
app= Flask(__name__)
@app.route('/')

def root():
    return "Home"

'''
GET-> Obtener información
POST-> Crear Información
PUT-> Actualizar Información
DELETE-> Borrar Información
'''
#Operación GET
@app.route("/user/<user_id>")
def get_user(user_id):
    user = {"id":user_id, "name":"test", "telefono":"999-666-333"}
    #/users/2560/?query=query_test
    query = request.args.get('quey')
    if query:
        user["query"]=query
    return jsonify(user),200

#Operación POST
@app.route("/users",methods=["POST"])

def create_user():
    data = request.get_json()
    data["status"]="user created"
    return jsonify(data),201
    
    

if __name__== '__main__':
    app.run(debug=True)
    