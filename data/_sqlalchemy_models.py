from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped, sessionmaker
from sqlalchemy import String, Integer, Text, ForeignKey, DateTime, create_engine
import datetime
import os
from dotenv import load_dotenv

class Base(DeclarativeBase):
    pass

class Problematic(Base):
    __tablename__ = 'problematic'
    id:  Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)

class ProblematicInput(Base):
    __tablename__ = 'problematic_input'
    id:  Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    problematic_id: Mapped[int] = mapped_column(ForeignKey("problematic.id"))
    dataJson: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime)

load_dotenv()

# Obtener las variables del entorno
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}')

Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)

# Cerrar la sesión
session.close()
