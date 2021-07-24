get_data = session.query(myclass).all()
for i in get_data:
    print('我的名字是：' + i.name)
    print('我的班级是：' + i.class_name)
session.close()
