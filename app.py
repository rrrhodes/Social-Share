# Import QR Code library
import qrcode.image.svg
import json, cgi

from flask import Flask, render_template
app = Flask(__name__)

form = cgi.FieldStorage()

#myFile = "myFile.txt"
#file = open(myFile)
@app.route('/')
def index():
    name = ""
    instagram = ""
    snapchat = ""
    twitter = ""
    return render_template("index.html", Name=name, insta=instagram, snap=snapchat, twitt=twitter)

# Create qr code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

hold = {}
name = ""
instagram = "" 
snapchat = "" 
twitter = ""
#tempDict = json.loads(file.read())

# def create(name, instagram, snapchat, twitter):
         # hold[name] = [instagram, snapchat, twitter]
        # display(name)

#def search(user):
 #   if(str(user) in tempDict):
  #      display(user)
   # else:
    #    print("User not found")

def display(name, instagram, snapchat, twitter):
    #tempDict = json.loads(file.read())
    data = name + "\nInstagram: " + instagram + "\nSnapchat: " + snapchat + "\nTwitter: " + twitter
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("image.jpeg")

if name == "main":
    app.run()
