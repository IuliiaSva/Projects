from flask import Flask, render_template, request
app = Flask(__name__)
records={}
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Дневник_программиста', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        if title and text:
            records[title] = text
    return render_template('notes.html', records=records)
records ["Третья тема"]="Третья тема выполнена"
if __name__ == '__main__':
    app.run(debug=True)