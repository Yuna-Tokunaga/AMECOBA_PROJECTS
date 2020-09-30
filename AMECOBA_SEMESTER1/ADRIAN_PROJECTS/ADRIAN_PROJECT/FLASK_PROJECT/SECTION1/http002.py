from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return '''
        <form action="#" method="post">
        	<p>ユーザー名:　<input type="text" name="nm" />
            <input type="submit" value="check"/>
            </p>
        </form>
        '''
    elif request.method == 'POST':
        user = request.form["nm"]
        return "<h2>ユーザー名： " + user + "</h2>"