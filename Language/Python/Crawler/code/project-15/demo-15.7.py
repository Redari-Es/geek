# TODO: 更新数据  <13-05-21, Redari-Es> #
session.query(mytable).filter_by(id=1).update({mytable.age: 12})
session.commit()
session.close()

get_data = session.query(mytable).filter_by(id=1).first()
get_data.class_name = '三年级三班'
session.commit()
session.close()
