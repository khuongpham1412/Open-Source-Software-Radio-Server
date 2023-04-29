class Audio(Resource):
    def get(self):
        return "<h1>hello world</h1>"


api.add_resource(Audio, '/audio')
