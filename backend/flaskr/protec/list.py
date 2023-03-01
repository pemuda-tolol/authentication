from configur import app,db,jsonify,HTTPStatus

@app.route("/list/<id>")
def list(id): 
    listSelectUser = [] 
    for i in db.select(f"select id_user,name,username,email,gender,picture from tbl_user where id_user = {id}"):
        listSelectUser.append({
            "id": i[0],
            "name": i[1],
            "username": i[2], 
            "email": i[3], 
            "gender": i[4],
            "picture": i[5]
        })
    print(listSelectUser)
    response = {
            "data": [listSelectUser],
            "message": "Success"
        }
    return jsonify(response),HTTPStatus.OK