from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import numpy
import os
os.add_dll_directory(os.getcwd())

app = Flask(__name__)
api = Api(app)


# @app.route("/upload", methods=['POST'])
# def upload_file():
#     app.logger.info('in upload route')

#     if request.method == 'POST':
#         file_to_upload = request.files['file']
#         app.logger.info('%s file_to_upload', file_to_upload)
#         if file_to_upload:
#             app.logger.info(file_to_upload)
#             # print(os.path.abspath(file_to_upload.filename))
#             with open(r"C:\Users\ASUS\Downloads\\"+file_to_upload.filename, "rb") as file:
#                 byte_array = bytearray(file.read())
#             f = open("sample.mp3", "wb")
#             f.write(byte_array)
#             f.close()
#             # with wave.open("sound1.mp3", "w") as f:
#             #     # 2 Channels.
#             #     f.setnchannels(2)
#             #     # 2 bytes per sample.
#             #     f.setsampwidth(2)
#             #     f.setframerate(samplerate)
#             #     f.writeframes(byte_array)
#             # data = open('filename.mp3', 'rb').read()

#             # song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
#             # play(song)
#         return "success"


@app.route("/upload", methods=['GET'])
def upload_file():

    if request.method == 'GET':
        print("hi chó khoa")
        return "success"
# @app.route("/stream", methods=['GET'])
# def stream_file():

#     if request.method == 'GET':
#         p = vlc.MediaPlayer("sample.mp3")
#         p.play()
#         return "success"


if __name__ == '__main__':
    app.run()

# về viết xong api server + kết nối nó vô
#  Viết xong giao diện của client
# Hôm sau chỉ Khoa call API
