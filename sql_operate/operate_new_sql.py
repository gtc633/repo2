from learn_sql import Student, db, Grade

# 增

# db.session.add(s1)
# db.session.commit()

# db.session.add_all([s1, s2, s3, s4])
# db.session.commit()

# 查

# get(id)
# stu = Student.query.get(1)
# print(stu.name)
# print(stu.gender)
# print(stu.phone)

# all() 查全部
# for i in stu:
#   print(i.name, i.id)

# filter_by()
# stu = Student.query.filter_by(name="张三").all()
# for i in stu:
#   print(i.name)

# 改

# 第一种
# stu = Student.query.filter(Student.id == 1).update({"name": "张一"})
# db.session.commit()

# 第二种
# stu = Student.query.filter(Student.gender == "女").all()
# for i in stu:
#   i.gender = "男"
#  db.session.add(i)
# db.session.commit()

# 删
# stu = Student.query.filter(Student.id == 1).delete()
# db.session.commit()


# grade1 = Grade(grade=100,student_id=1)
# grade2 = Grade(grade=95,student_id=1)

# db.session.add_all([grade1,grade2])
# db.session.commit()

# 通过一访问多
# stu = Student.query.get(1)
# for i in stu.grades:
#   print(stu.name, i.grade)

# 通过多访问一
grade = Grade.query.filter(Grade.grade == "100").all()
for i in grade:
    print(i.student.name, i.student.gender)
