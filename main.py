""" This is the main app"""

from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from models._allmodels import ItemIn, ResponseOut, Visual, BarData, PieData, Problematic


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


# Crear el endpoint POST
@app.post("/ia-process/", response_model=ResponseOut)
async def create_item(item: ItemIn):
    # Mensaje de salida
    message = f"Texto de analisis generado por openai de ejemplo .. y este texto: {item.name} fue pasado desde el cliente"

    problematic = Problematic(
        date= 'Enero',
        quantity= 234,
        locality= 'Santa Cruz'
    )
    # Ejemplo de visualización para gráfico de barras
    bar_data = BarData(
        title='Titulo de Bar char generado por ia',
        explanation='Explicacion del grafico generado por ia',
        labels = ["label1", "label2", "label3"],
        values= ["val1", "val2", "val3"]
    )

    # Ejemplo de visualización para gráfico de torta
    pie_data = PieData(
        title='Titulo de Pie  char generado por ia',
        explanation='Explicacion del grafico generado por ia',
        labels = ["label1", "label2", "label3"],
        percentages = ["per1", "per2", "per3"]
    )

    # Crear la lista de visuales (gráfico de barras y gráfico de torta)
    visuals = [
        Visual(char_type="bar", data=bar_data),
        Visual(char_type="pie", data=pie_data)
    ]

    # Retornar la respuesta con el mensaje y los gráficos
    return ResponseOut(message=message, visual=visuals)
