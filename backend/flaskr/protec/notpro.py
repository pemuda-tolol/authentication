from configur import app,request,jsonify,HTTPStatus,secure_filename,os,uploadfolder,allowedextensions,maxcontent,db,url_for

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedextensions

@app.route("/upload/<id>",methods = ['PUT'])
def upload(id):
    try:
        if 'picture' not in request.files:
            response ={
                    "Data": "Bad Request",
                    "Message": "No Picture Selected"
                }
            return jsonify(response),HTTPStatus.BAD_REQUEST
        files = request.files.getlist('picture')
        success = False
        for user in db.select(f"select id_user,picture from tbl_user where id_user = {id}"): 
            user = {
                "id_user": user[0],
                "pic_user": user[1]
            }  
        for file in files:
            if file and allowed_file(file.filename):
                try:
                    os.remove(os.path.join(uploadfolder, user['pic_user']))
                except Exception:
                    pass
                filename = secure_filename(file.filename)
                picname = str(user['id_user']) + "_" + filename
                file.save(os.path.join(uploadfolder, picname))
                success = True
            else:
                response ={
                    "Data": "Bad Request",
                    "Message": "File Type is Not Allowed"
                }
                return jsonify(response),HTTPStatus.BAD_REQUEST
        if success:
            uploadFoto = (f"update tbl_user set picture='{picname}' where id_user = {id}")
            db.execute(uploadFoto)
            resp = jsonify({'message' : 'Files successfully uploaded',
                            "data": picname})
            resp.status_code = 201
            return resp 
        else:
            response ={
                    "Data": "Bad Request",
                    "Message": "Bad"
                }
            return jsonify(response),HTTPStatus.BAD_REQUEST
    
    except Exception as err:
        response ={
                    "Data": str(err),
                    "Message": "Bad Gateway"
                }
        return jsonify(response),HTTPStatus.BAD_GATEWAY


