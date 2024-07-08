
# main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
time_slots = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    tasks = request.form.getlist('task')
    time_slots = request.form.getlist('time_slot')

    return render_template('schedule.html', tasks=tasks, time_slots=time_slots)

@app.route('/edit')
def edit():
    return render_template('edit.html', tasks=tasks, time_slots=time_slots)

@app.route('/update', methods=['POST'])
def update():
    tasks = request.form.getlist('task')
    time_slots = request.form.getlist('time_slot')

    return render_template('schedule.html', tasks=tasks, time_slots=time_slots)

if __name__ == '__main__':
    app.run()
