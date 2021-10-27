from flask import Flask, request, redirect, jsonify
from blood_calculator import hdl_analysis

app = Flask(__name__)

# Use decorator to know which methods app should run
@app.route("/", methods=["GET"])
def server_status():
    return "Server is on"


@app.route("/info", methods=["GET"])
def info():
    my_output = "This server is for BME 547 at Duke University"
    return my_output


@app.route("/hdl/<hdl_value>", methods=["GET"])
def hdl_analysis_server(hdl_value):
    """
    Input should look like {"hdl": 50, "patient_id": 200}

    :return: 
    """
    #in_data = request.get_json()
    #hdl_value = in_data["hdl"]
    print("The hdl_value is {}".format(hdl_value))
    answer = hdl_analysis(int(hdl_value))
    return answer, 201 # return [whatever], [int response code (200 by default)]


@app.route("/say_hello/<input_name>", methods=["GET"])
def say_hello(input_name):
    return "Hello, {}".format(input_name)

if __name__ == '__main__':
    app.run()


"""
www.google.com/maps : host/route
http://127.0.0.1:5000/
default URL
"""