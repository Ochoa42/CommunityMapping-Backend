from pydantic import BaseModel
from typing import ClassVar, List, Union
from enum import Enum


# Definir el esquema de los datos de entrada
class ItemIn(BaseModel):
    name: str
    price: float
    tax: float = None
class ChartType(str, Enum):
    bar = "bar"
    pie = "pie"

# Definir el esquema para los datos de un gráfico de barras
class BarData(BaseModel):
    title_char: str
    explanation_char: str
    labels: List[str]  # Ej: ['Category 1', 'Category 2']
    values: List[float]  # Ej: [10.0, 20.0]

# Definir el esquema para los datos de un gráfico de torta
class PieData(BaseModel):
    title_char: str
    explanation_char: str
    labels: List[str]  # Ej: ['Category 1', 'Category 2']
    percentages: List[float]  # Ej: [50.0, 50.0]

# Definir el esquema para el visual con discriminador explícito en el nivel superior
class Visual(BaseModel):
    char_type: ChartType  # Tipo de gráfico: bar o pie
    bar_data: BarData = None  # Opcional, solo si el char_type es bar
    pie_data: PieData = None  # Opcional, solo si el char_type es pie

# Definir el esquema para la respuesta de salida
class RecomendationPlots(BaseModel):
    message: str
    visual: List[Visual]