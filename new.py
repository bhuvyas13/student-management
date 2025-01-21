#create a flask app for the crud operations of a student. 
#student details : name, email-id, class, batch,register number that will be created randomly

from flask import Flask, request
import random

app = Flask(__name__)

students = []
def generate_register_number():
    return random.randint(23112000, 23114000)

@app.route('/create/', methods = ['POST'])
def create_students():
    data = request.json
    student = {
        'name': data['name'],
        'email': data['email'],
        'class':data['class'],
        'batch':data['batch'],
        'register_number': generate_register_number()
    }
    students.append(student)
    return student

@app.route('/read/',methods = ['GET'])
def show_students():
    return(students)

@app.route('/update/<int:register_number>',methods = ['PUT'])
def update_students(register_number):
    data = request.json
    for student in students:
        if student['register_number'] == register_number:
            student['name'] = data['name']
            student['email'] = data['email']
            student['class'] = data['class']
            student['batch'] = data['batch']
            return student
    return {'msg':'student not found'}

@app.route('/delete/<int:register_number>',methods = ['DELETE'])
def delete_student(register_number):
    global students
    students = [s for s in students if s['register_number'] != register_number]
    return {'msg': 'Student deleted'}

@app.route('/count/', methods=['GET'])
def count_students():
    return ({'count': len(students)})

@app.route('/<string:class_name>', methods=['GET'])
def get_students_by_class(class_name):
    filtered_students = [s for s in students if s['class'] == class_name]
    return (filtered_students)

if __name__ == '__main__':
    app.run(debug=True)