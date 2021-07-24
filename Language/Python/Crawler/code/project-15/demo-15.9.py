#方法一
#get_data=session.query(myclass).filter(myclass.id==1).all()
#方法二
get_data = session.query(myclass).filter_by(id=1).all()
print('数据类型是：' + str(type(get_data)))
for i in get_data:
    print('我的名字是：' + i.name)
    print('我的班级是：' + i.class_name)
