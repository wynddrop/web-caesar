from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
        
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/" method="post">
        <label for="rot">Rotate by:</label>
        <input id="rot" type="text" name="rot" value="0"/>
        <textarea type="text" name="text">{0}</textarea>
        <input type="submit" />
      </form>
    </body>
</html>
"""

@app.route('/')
def index():
    return form.format('')
 

@app.route('/', methods=['POST'])
def encrypt():
    rot_in = request.form['rot']
    rot_in = int(rot_in)
    text_in = request.form['text']
    display = rotate_string(text_in, rot_in)
    return form.format(display)
 
if __name__ == "__main__":
    app.run(debug=True)
