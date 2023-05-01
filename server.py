# import vlc
import requests
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import numpy
import os
from services.db.connect import Store
from datetime import datetime
import json
from pygame import mixer
os.add_dll_directory(os.getcwd())

app = Flask(__name__)
api = Api(app)
store = Store()

headers = {'Content-Type: audio/mpeg'}


@app.route("/uploads", methods=['POST'])
def upload_file():
    app.logger.info('in upload route')

    if request.method == 'POST':
        file_to_upload = request.files['file']
        # image = request.files['image']
        data = request.form['data']
        print(data)
        app.logger.info('%s file_to_upload', file_to_upload)
        if file_to_upload:
            # and image and data
            app.logger.info(file_to_upload)
            print(os.path.abspath(file_to_upload.filename))
            print(file_to_upload)
            with open(r"C:\Users\ASUS\Downloads\\" + file_to_upload.filename, "rb") as file:
                byte_array = bytearray(file.read())
            now = datetime.now()
            fileName = file_to_upload.filename.replace(
                ".mp3", "") + str(now.timestamp())
            f = open(r"assets\\radio\\" + fileName + ".mp3", "wb")
            f.write(byte_array)
            f.close()
            # store.add_music(name=fileName, image="image test",
            #                 path="path test")

            return "Add Success !!!"


@app.route("/delete-music/<id>", methods=['GET'])
def delete_music_by_id(id):
    if request.method == 'GET':
        data = store.delete_music(id)
        return "Delete Success !!!"


@app.route("/get-music/<id>", methods=['GET'])
def get_music_by_id(id):
    if request.method == 'GET':
        print(id)
        data = store.getMusicById(id)
        print(type(data))
        for item in data:
            print(item)
        return "Delete Success !!!"


@app.route("/get-all-music", methods=['GET'])
def get_all():
    if request.method == 'GET':
        data = store.getAll()

        # for item in data:
        #     # data += {"name" : item.name, "image": item.image, "path": item.path}
        #     print(type(item))

        # t = '[{"id": 1}]'
        t = '[{"id": 1, "name": "Hôm nay tôi buồn", "image": "image", "path":"1682931939.569541.mp3"}, {"id": 2, "name": "Kẹo Bông Gòn", "image": "image", "path":"1682931945.390066.mp3"}, {"id": 3, "name": "Bầu Trời Năm Ấy", "image": "image", "path":"1682931945.390066.mp3"}, {"id": 4, "name": "Về Bên Anh", "image": "image", "path":"1682931945.390066.mp3"}]'
        # , "path": "path"}, {"id": 2, "name": "Asakura Hao", "image": "D:\SGU\Opensource_Software\radio-client\assets\vuongnguyen.jpg", "path": "path"}, {"id": 3, "name": "Sesumaru", "image": "D:\SGU\Opensource_Software\radio-client\assets\vuongnhatbac.jpg", "path": "path"}]'
        return json.loads(t)


@app.route("/play-music/<name>", methods=['GET'])
def play_music(name):
    if request.method == 'GET':
        mixer.init()
        mixer.music.load(
            r"D:\\SGU\\Opensource_Software\\radio-server\\assets\\radio\\" + str(name))
        mixer.music.play()
        # return "<svg fill='WindowText' height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'><path d='M6 19h4V5H6v14zm8-14v14h4V5h-4z'/><path d='M0 0h24v24H0z' fill='none'/></svg>"
        return "success"


if __name__ == '__main__':
    app.run()

# with wave.open("sound1.mp3", "w") as f:
#     # 2 Channels.
#     f.setnchannels(2)
#     # 2 bytes per sample.
#     f.setsampwidth(2)
#     f.setframerate(samplerate)
#     f.writeframes(byte_array)
# data = open('filename.mp3', 'rb').read()

# song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
# play(song)
