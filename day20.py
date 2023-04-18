from flask import Flask

#Creating obj var of flask import
app = Flask(__name__)

#Trying to decorate our custom hello world func(makes the func lang independent)
@app.route("/")
#Simple func isn't taking any input just gives some string as output
def hello_world():
    return "Hello, World!"

# We are trying to call our app & run make this thing as server
if __name__=="__main__":
    app.run(host="0.0.0.0")

'''* Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.43.33:5000
 -> The output. The small func we written is running in our server.
 '''