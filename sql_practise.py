from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Float, Column, ForeignKey, DATETIME
import sqlalchemy
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(70))
    Age = Column(Integer)
    Class = Column(String(20))


class Subjects(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50))


class Marks(Base):
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Student_id = Column(Integer, ForeignKey('students.id'))
    Subject_id = Column(Integer, ForeignKey('subjects.id'))
    Mark = Column(Integer)
    Date = Column(DATETIME)


import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///D:/Proj/pythonProject/blogsite/db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()


def student_list() -> list:
    students = session.query(Students).all()
    return [[student.id, student.Name] for student in students]


def db_delete_student(student_id: int) -> int:
    student = session.query(Students).filter(Students.id == student_id).first()
    if student is None:
        return 0
    else:
        session.query(Marks).filter(Marks.Student_id == student_id).delete()
        session.delete(student)
        session.commit()
        return 1


def db_get_student_marks(student_id: int) -> [list, int]:
    student = session.query(Students).filter(Students.id == student_id).first()
    if student is None:
        return [], 0
    else:
        marks = session.query(Marks.Mark, Subjects.Name).join(Subjects, Marks.Subject_id == Subjects.id).filter(
            Marks.Student_id == student_id).order_by(Subjects.Name).all()
        grouped_mask = []
        subj_id = -1
        last_subj = ""
        for mark, subject in marks:
            if subject != last_subj:
                subj_id += 1
                grouped_mask.append([subject, []])
                last_subj = subject
            grouped_mask[subj_id][1].append(mark)
        return grouped_mask, 1


