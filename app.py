from flask import Flask, render_template

app = Flask(__name__)

@app.route('/url/task')
def task():
    @app.route('/url/task')
    dynamic_message = "This message is dynamic!"
    return render_template('task.html', dynamic_message=dynamic_message)

    

if __name__ == '__main__':
    app.run(port=8000)
