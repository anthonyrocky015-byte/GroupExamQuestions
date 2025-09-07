from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# =====================
# USERS TABLE
# =====================
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(100), unique=True, nullable=False)

    # Relationships
    teachers = db.relationship('Teacher', backref='user', lazy=True)
    students = db.relationship('StudentAnswer', backref='user', lazy=True)
    test_infos = db.relationship('StudentTestInfo', backref='user', lazy=True)


# =====================
# TEACHERS TABLE
# =====================
class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), db.ForeignKey('users.username'), nullable=False)
    test_id = db.Column(db.String(50), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    password = db.Column(db.String(6), nullable=False)
    subject = db.Column(db.String(100))
    topic = db.Column(db.String(100))
    email = db.Column(db.String(500))


# =====================
# QUESTIONS TABLE
# =====================
class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.String(50), nullable=False)
    qid = db.Column(db.String(20), nullable=False)
    q = db.Column(db.Text, nullable=False)
    a = db.Column(db.Text, nullable=False)
    b = db.Column(db.Text, nullable=False)
    c = db.Column(db.Text, nullable=False)
    d = db.Column(db.Text, nullable=False)
    ans = db.Column(db.String(10), nullable=False)
    marks = db.Column(db.Integer, nullable=False)


# =====================
# STUDENTS TABLE (answers per question)
# =====================
class StudentAnswer(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), db.ForeignKey('users.username'), nullable=False)
    test_id = db.Column(db.String(50), nullable=False)
    qid = db.Column(db.String(20), nullable=False)
    ans = db.Column(db.String(10))
    date_taken = db.Column(db.DateTime, default=datetime.utcnow)


# =====================
# STUDENT TEST INFO TABLE
# =====================
class StudentTestInfo(db.Model):
    __tablename__ = 'studentTestInfo'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), db.ForeignKey('users.username'), nullable=False)
    test_id = db.Column(db.String(50), nullable=False)
    completed = db.Column(db.Boolean, default=False)
