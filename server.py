from flask import Flask, request, render_template, send_file
from flask_restful import Resource, Api, reqparse
import os
from services.db.connect import Store
from datetime import datetime
import json
os.add_dll_directory(os.getcwd())

app = Flask(__name__)
app.config['UPLOAD_RADIO_DIR'] = 'assets\\radio'
app.config['UPLOAD_IMAGE_DIR'] = 'assets\\image'
api = Api(app)
store = Store()

headers = {'Content-Type: audio/mpeg'}


@app.route("/uploads", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        try:
            file_to_upload = request.files['file']
            image = ""
            if "image" in request.files:
                image = request.files['image']

            data = json.loads(request.form['data'])
            if file_to_upload and data:
                now = str(datetime.now().timestamp())
                radio_name = now + ".mp3"
                file_to_upload.save(os.path.join(
                    app.config['UPLOAD_RADIO_DIR'], radio_name))
                image_name = ""
                if (image != ""):
                    split_tup = os.path.splitext(image.filename)
                    file_extension = split_tup[1]
                    image_name = now + file_extension
                    image.save(os.path.join(
                        app.config['UPLOAD_IMAGE_DIR'], image_name))
                store.add_music(name=data['name'],
                                image=image_name, path=radio_name)
                return "Upload Success !!!"
        except:
            return "Oh No! Exception :(((("


@app.route("/delete-music/<id>", methods=['GET'])
def delete_music_by_id(id):
    if request.method == 'GET':
        music = store.getMusicById(id)
        if (len(music) > 0):
            image_name = music[0][2]
            if image_name != "":
                image_path = os.path.abspath("assets/image/" + image_name)
                if os.path.exists(image_path):
                    os.remove(image_path)

            radio_name = music[0][3]
            radio_path = os.path.abspath("assets/radio/" + radio_name)
            if os.path.exists(radio_path):
                os.remove(radio_path)
                data = store.delete_music(id)
                return "Delete Success !!!"
            else:
                return "Oh Noooo ! File Not Exists !!!"
        return "ID Music Not Exists !!!"


@app.route("/get-music/<id>", methods=['GET'])
def get_music_by_id(id):
    if request.method == 'GET':
        data = store.getMusicById(id)
        if (len(data) > 0):
            for row in data:
                res = '{"id": ' + str(row[0]) + ',"name": "' + str(row[1]) + \
                    '","image": "' + str(row[2]) + \
                    '","path": "' + str(row[3]) + '"}'
            return json.loads(res)

        return "ID Music Not Exists !!!"


@app.route("/get-all-music", methods=['GET'])
def get_all():
    if request.method == 'GET':
        data = store.getAll()
        if (len(data) > 0):
            res = "["
            for row in data:
                res += '{"id": ' + str(row[0]) + ',"name": "' + str(row[1]) + \
                    '","image": "' + str(row[2]) + \
                    '","path": "' + str(row[3]) + '"},'
            res += "]"
            res = res.replace(res[len(res) - 2:], '')
            res += "]"
            return json.loads(res)
        return "List Music Is Empty !!!"


@app.route("/play-music/<name>", methods=['GET'])
def play_music(name):
    if request.method == 'GET':
        path = os.path.abspath("assets/radio/" + name)
        file = open(
            path, 'rb')
        file.close()
        return send_file(path, mimetype="audio/wav")


@app.route("/photo/<name>", methods=['GET'])
def get_photo(name):
    if request.method == 'GET':
        path = os.path.abspath("assets/image/" + name)
        file = open(
            path, 'rb')
        file.close()
        return send_file(path, mimetype="image/png")


if __name__ == '__main__':
    app.run()
