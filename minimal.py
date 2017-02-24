from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import werkzeug

app = Flask(__name__)
api = Api(app)

class FileUploader(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()
        f = args['file']
        f.save("d://file_name.jpg")
        return {'status': 'success'}

    def get(self):
        return {'hello': 'world'}

api.add_resource(FileUploader, '/upload')

if __name__ == '__main__':
    app.run(debug=True)