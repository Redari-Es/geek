from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:110@localhost:3306/test",
                       echo=True,
                       pool_size=5,
                       max_overflow=4,
                       pool_recycle=7200,
                       pool_timeout=30)
