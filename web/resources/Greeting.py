class Greeting(Resource):
    def get(self):
        return {'message': 'Greetings from Yehui.'}