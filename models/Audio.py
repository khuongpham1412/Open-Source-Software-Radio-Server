from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import numpy
import os
from connect import Store
from datetime import datetime
import json
from pygame import mixer

os.add_dll_directory(os.getcwd())

app = Flask(__name__)
api = Api(app)

store = Store


class Audio():
    def __init__(self, name, image, path):
        self.name = name
        self.image = image
        self.path = path

    @app.route("/uploads", methods=['POST'])
    def upload_file():
        app.logger.info('in upload route')

        if request.method == 'POST':
            file_to_upload = request.files['file']
            image = request.files['image']
            data = request.form['data']
            app.logger.info('%s file_to_upload', file_to_upload)
            if file_to_upload and image and data:
                app.logger.info(file_to_upload)
                print(os.path.abspath(file_to_upload.filename))
                print(file_to_upload)
                # with open(r"C:\Users\ASUS\Downloads\\" + file_to_upload.filename, "rb") as file:
                #     byte_array = bytearray(file.read())
                # now = datetime.now()
                # fileName = file_to_upload.filename
                # f = open(r"assets\\radio\\" + fileName +
                #          str(now.timestamp()) + ".mp3", "wb")
                # f.write(byte_array)
                # f.close()
                # test = Store()
                # test.add_music(name="name test",
                #                image="image test", path="path test")
                # data = test.getAll()
                # for item in data:
                #     print(item)
                return "success"

    @app.route("/delete-music", methods=['GET'])
    def delete_music_by_id():
        if request.method == 'GET':
            data = store.delete_music(1)
            return "Delete Success !!!"

    @app.route("/get-music", methods=['GET'])
    def get_music_by_id():
        if request.method == 'GET':
            print(id)
            data = store.getMusicById(11)
            print(type(data))
            for item in data:
                print(item)
            return "Delete Success !!!"

    @app.route("/get-all-music", methods=['GET'])
    def get_all():
        if request.method == 'GET':
            data = store.getAll()
            t = '[{"id": 1, "name": "Hôm nay tôi buồn", "image": "image", "path": "path"}, {"id": 2, "name": "Asakura Hao", "image": "image", "path": "path"}, {"id": 3, "name": "Sesumaru", "image": "image", "path": "path"}]'
            return json.loads(t)

    @app.route("/play-music", methods=['GET'])
    def play_music():
        if request.method == 'GET':
            mixer.init()
            mixer.music.load(
                r"D:\\SGU\\Opensource_Software\\radio-server\\assets\\radio\\sample-12s.mp31682745564.174417.mp3")
            mixer.music.play()


api.add_resource(Audio, '/audio')
