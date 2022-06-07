from flask import Flask
import os
from flask_restful import Resource, Api
from flask import request, jsonify
app = Flask(__name__)
api = Api(app)

##class HelloWorld(Resource):
##    def get(self):
##        return {'hello': 'world'}

#api.add_resource(Foo, '/foo')


@app.route('/execute_labelImg_app', methods=['GET'])
def abc():
    print("button1 working")
    os.system(r"C:\Users\Admin\Desktop\KJSCE_Object_Detection\upload_image.bat")
    return jsonify([{'status':'success'}])

@app.route('/execute_start_ml', methods=['GET'])
def defg():
    print("button2 working")
    os.system(r"C:\Users\Admin\Desktop\KJSCE_Object_Detection\start_learning_process.py")
    os.system(r"C:\Users\Admin\Desktop\KJSCE_Object_Detection\test_with_code_v1.bat")
    return jsonify([{'status':'success'}])

@app.route('/execute_stop_ml', methods=['GET'])
def hij():
    print("button3 working")
    os.system(r"C:\Users\Admin\Desktop\KJSCE_Object_Detection\stop_learning_process.py")
    return jsonify([{'status':'success'}])

@app.route('/execute_send_to_bot', methods=['GET'])
def klm():
    print("button4 working")
    os.system(r"C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\training\generate_graph.py")
    os.system(r"C:\Users\Admin\Desktop\KJSCE_Object_Detection\delete_from_dropbox.py")
    os.system(r"C:\Users\Admin\Desktop\KJSCE_Object_Detection\upload_to_dropbox.py")
    print("uploading successfull")
    return jsonify([{'status':'success'}])


@app.route('/execute_installation', methods=['GET'])
def nop():
    print("Start Installation")
    os.system(r"C:\Users\Admin\Desktop\KJSCE_Object_Detection\Install_dependencies.bat")
    print("Sucessfully Installed")
    return jsonify([{'status':'success'}])

if __name__ == '__main__':
    app.run(host='192.168.43.97', port=5001, debug=True, threaded=True)

#<button id="ul" onclick="window.location.href='/C:/Users/Admin/Desktop/api.py' method="post";" </button> [ {{ panServoAngle }} ] <button id="ur" onclick="window.location.href='/pan/+';">&rarr;</button>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<button  id="fwd" onclick="window.location.href='/forward';">Forward</button></h5>
