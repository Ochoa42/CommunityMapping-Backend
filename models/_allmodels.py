from pydantic import BaseModel
from typing import List, Union

# Definir el esquema para los datos de una problemática
class Problematic(BaseModel):
    date: str
    quantity: float
    locality: str

# Definir el esquema de los datos que se recibirán en el POST
class ItemIn(BaseModel):
    name: str

# Definir el esquema para los datos de un gráfico de barras
class BarData(BaseModel):
    title: str
    explanation: str
    labels = List[str]
    values = List[float] # Ej: ['Category 1', 'Category 2']

# Definir el esquema para los datos de un gráfico de torta
class PieData(BaseModel):
    title: str
    explanation: str
    labels = List[str]
    percentages = List[float]

# Definir el esquema para el visual (puede ser un gráfico de barras o torta)
class Visual(BaseModel):
    char_type: str  # Puede ser "bar" o "pie"
    data: Union[BarData, PieData]  # Dependiendo del tipo de gráfico

# Definir el esquema para la respuesta de salida
class ResponseOut(BaseModel):
    message: str
    visual: List[Visual]
    