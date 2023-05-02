# import vlc
import speech_recognition as sr
import requests
from flask import Flask, request, render_template, send_file
from flask_restful import Resource, Api, reqparse
import numpy
import os
from services.db.connect import Store
from datetime import datetime
import json
from pygame import mixer
import base64
os.add_dll_directory(os.getcwd())

r = sr.Recognizer()

app = Flask(__name__)
app.config['UPLOAD_DIR'] = 'assets\\radio'
api = Api(app)
store = Store()

headers = {'Content-Type: audio/mpeg'}


@app.route("/uploads", methods=['POST'])
def upload_file():
    app.logger.info('in upload route')

    if request.method == 'POST':
        file_to_upload = request.files['file']
        # image = request.files['image']
        data = json.loads(request.form['data'])
        if file_to_upload and data:
            fileName = str(datetime.now().timestamp()) + ".mp3"
            file_to_upload.save(os.path.join(
                app.config['UPLOAD_DIR'], fileName))
            store.add_music(name=data['name'], image=data['image'],
                            path=fileName)
            return "Upload Success !!!"
        # app.logger.info('%s file_to_upload', file_to_upload)
        # if file_to_upload:
        #     # and image and data
        #     app.logger.info(file_to_upload)
        #     print(os.path.abspath(file_to_upload.filename))
        #     print(file_to_upload)
        #     with open(r"C:\Users\ASUS\Downloads\\" + file_to_upload.filename, "rb") as file:
        #         byte_array = bytearray(file.read())
        #     now = datetime.now()
        #     fileName = file_to_upload.filename.replace(
        #         ".mp3", "") + str(now.timestamp())
        #     f = open(r"assets\\radio\\" + fileName + ".mp3", "wb")
        #     f.write(byte_array)
        #     f.close()
        #     # store.add_music(name=fileName, image="image test",
        #     #                 path="path test")

        # return byte_array


@app.route("/delete-music/<id>", methods=['GET'])
def delete_music_by_id(id):
    if request.method == 'GET':
        music = store.getMusicById(id)
        if (len(music) > 0):
            file_name = music[0][3]
            file_path = str(os.path.abspath(file_name)).split("\\")
            file_path.remove(file_path[len(file_path) - 1])
            res = ""
            for item in file_path:
                res += item + "\\"
            res += "assets\\radio\\" + file_name
            if os.path.exists(res):
                os.remove(res)
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
                res = '{"id": ' + str(row[0]) + ',"image": "' + str(row[1]) + \
                    '","name": "' + str(row[2]) + \
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
                res += '{"id": ' + str(row[0]) + ',"image": "' + str(row[1]) + \
                    '","name": "' + str(row[2]) + \
                    '","path": "' + str(row[3]) + '"},'
            res += "]"
            res = res.replace(res[len(res) - 2:], '')
            res += "]"
            return json.loads(res)
        return "List Music Is Empty !!!"


@app.route("/play-music/<name>", methods=['GET'])
def play_music(name):
    if request.method == 'GET':
        file = open(
            r"D:\\SGU\\Opensource_Software\\radio-server\\assets\\radio\\" + str(name), 'rb')
        print(file)
        path = r"D:\\SGU\\Opensource_Software\\radio-server\\assets\\radio\\" + \
            str(name)
        return send_file(path, mimetype="audio/wav")


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


# data = base64.b64encode(file).decode('ascii')
    # mixer.init()
    # mixer.music.load(
    #     r"D:\\SGU\\Opensource_Software\\radio-server\\assets\\radio\\" + str(name))
    # mixer.music.play()
    # return "<svg fill='WindowText' height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'><path d='M6 19h4V5H6v14zm8-14v14h4V5h-4z'/><path d='M0 0h24v24H0z' fill='none'/></svg>"
    # file_audio = sr.AudioFile('file_audio.wav')

    # with file as source:
    #     audio_text = r.record(source)

    # print(type(audio_text))
    # print(r.recognize_google(audio_text))
    # file_content = file.read()
    # print(type(file_content))
    # t = "data:audio/wav;base64," + str(file_content)
    # return "data:audio/wav;base64," + str(file_content)
    # return "<audio controls autobuffer='autobuffer' autoplay='autoplay'><source src='" + str(file) + "'/></audio>"
