#先删除myclass，后删除mytable
myclass.drop(bind=engine)
Base.metadata.drop_all(engine)
