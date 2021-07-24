# TODO: 添加数据  <13-05-21, Redari-Es> #
from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind=engine)
session = DBSession()

#
new_data = mytable(name='Li Lei',
                   age=10,
                   birth='2017-10-01',
                   class_name='一年级一班')
session.add(new_data)
session.commit()
session.close()
