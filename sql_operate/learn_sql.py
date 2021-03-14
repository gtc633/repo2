import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@127.0.0.1:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123456'

db = SQLAlchemy(app)  # 实例化的数据库


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.Enum("男", "女"), nullable=False)
    phone = db.Column(db.String(11))
    grades = db.relationship("Grade", backref="student")
    courses = db.relationship("Course", secondary="student_to_course", backref="students")


class StudentToCourse(db.Model):
    __tablename__ = 'student_to_course'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, ForeignKey('student.id'))
    course_id = db.Column(db.Integer, ForeignKey('course.id'))


class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    grades = db.relationship("Grade", backref="course")
    teacher_id = db.Column(db.Integer, ForeignKey('teacher.id'))


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    gender = db.Column(db.Enum("男", "女"), nullable=False)
    phone = db.Column(db.String(11))
    course = db.relationship("Grade", backref="teacher")


class Grade(db.Model):
    __tablename__ = 'grade'
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(3), nullable=False)
    student_id = db.Column(db.Integer, ForeignKey('student.id'))
    course_id = db.Column(db.Integer, ForeignKey('course.id'))


if __name__ == '__main__':
    #db.drop_all()
    db.create_all()
