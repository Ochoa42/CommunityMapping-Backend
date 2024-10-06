from pydantic import BaseModel
from typing import List, Union


# Definir el esquema de los datos que se recibirán en el POST
class ItemIn(BaseModel):
    name: str

# Definir el esquema para los datos de un gráfico de barras
class BarData(BaseModel):
    title: str
    explanation: str
    labels: List[str]  # Ej: ['Category 1', 'Category 2']
    values: List[float]  # Ej: [10.0, 20.0]

# Definir el esquema para los datos de un gráfico de torta
class PieData(BaseModel):
    title: str
    explanation: str
    labels: List[str]  # Ej: ['Category 1', 'Category 2']
    percentages: List[float]  # Ej: [50.0, 50.0]

# Definir el esquema para el visual (puede ser un gráfico de barras o torta)
class Visual(BaseModel):
    char_type: str  # Puede ser "bar" o "pie"
    data: Union[BarData, PieData]  # Dependiendo del tipo de gráfico

# Definir el esquema para la respuesta de salida
class ResponseOut(BaseModel):
    message: str
    visual: List[Visual]