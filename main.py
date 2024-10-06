""" This is the main app"""

from typing import ClassVar, Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from models._allmodels import ItemIn, RecomendationPlots, Visual, BarData, PieData
import openai
from openai import OpenAI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


# Crear el endpoint POST
@app.post("/ia-process/", response_model=RecomendationPlots)
async def create_item(item: ItemIn):
    # Mensaje de salida
    message = f"Texto de analisis generado por openai de ejemplo .. y este texto: {item.name} fue pasado desde el cliente"

    # problematic = Problematic(
    #     date= 'Enero',
    #     quantity= 234,
    #     locality= 'Santa Cruz'
    # )
    # Ejemplo de visualización para gráfico de barras
    bar_data = BarData(
        title='Titulo de Bar char generado por ia',
        explanation='Explicacion del grafico generado por ia',
        labels = ["label1", "label2", "label3"],
        values= [104, 200, 103]
    )

    # Ejemplo de visualización para gráfico de torta
    pie_data = PieData(
        title='Titulo de Pie  char generado por ia',
        explanation='Explicacion del grafico generado por ia',
        labels = ["label1", "label2", "label3"],
        percentages = [50.3, 20.3, 29.4]
    )

    # Crear la lista de visuales (gráfico de barras y gráfico de torta)
    visuals = [
        Visual(char_type="bar", data=bar_data),
        Visual(char_type="pie", data=pie_data)
    ]

    stats_text = """
        Focos de calor bolivia 
        # 1) Focos de Calor

        Year,City,Heat_Spots_Count
        2022,La Paz,705
        2016,La Paz,824
        2022,Tarija,675
        2021,Tarija,395
        2023,Tarija,686
        2019,La Paz,254
        2023,Trinidad,219
        2023,La Paz,955
        2021,La Paz,315
        2015,Cochabamba,831
        2017,La Paz,382
        2020,Trinidad,344
        2017,Sucre,39
        2016,Santa Cruz,815
        2023,Cochabamba,970
        2020,Sucre,555
        2019,Sucre,938
        2020,La Paz,367
        2018,Tarija,472
        2015,Cochabamba,998
        2020,Sucre,986
        2016,Cochabamba,557
        2023,Cochabamba,377
        2015,Cochabamba,446
        2018,Trinidad,582
        2019,La Paz,97
        2015,La Paz,725
        2016,La Paz,422
        2015,Tarija,381
        2021,Santa Cruz,690
        2015,Sucre,509
        2015,Cochabamba,371
        2021,Tarija,706
        2018,Cochabamba,370
        2018,Trinidad,607
        2018,La Paz,783
        2019,Trinidad,334
        2019,La Paz,372
        2015,Cochabamba,22
        2018,La Paz,729
        2020,Sucre,946
        2018,Trinidad,960
        2020,Cochabamba,725
        2018,Trinidad,419
        2021,Sucre,484
        2023,La Paz,779
        2022,La Paz,487
        2019,Sucre,947
        2020,La Paz,720
        2017,La Paz,705

        # 2) Incendio por regiones

        Year,Region,Area_Affected_Ha
        2022,Amazonas,8825
        2015,Chiquitania,25727
        2022,Gran Chaco,2182
        2016,Amazonas,1267
        2015,Chiquitania,40783
        2023,Chiquitania,45481
        2018,Chiquitania,8491
        2017,Chiquitania,26125
        2015,Chiquitania,32799
        2022,Andes,10854
        2019,Valle Central,31625
        2021,Chiquitania,48597
        2022,Chiquitania,6404
        2023,Chiquitania,9909
        2021,Amazonas,47310
        2020,Amazonas,27174
        2020,Valle Central,36528
        2018,Amazonas,48053
        2016,Gran Chaco,7995
        2016,Valle Central,5781
        2015,Andes,3724
        2021,Valle Central,3684
        2018,Amazonas,12210
        2023,Gran Chaco,8708
        2021,Valle Central,27498
        2019,Valle Central,685
        2021,Amazonas,8234
        2020,Valle Central,26981
        2018,Amazonas,10360
        2018,Valle Central,33040
        2021,Andes,43048
        2022,Valle Central,18065
        2021,Andes,30680
        2023,Gran Chaco,11961
        2021,Chiquitania,44439
        2015,Valle Central,29798
        2022,Valle Central,13318
        2020,Valle Central,15647
        2015,Amazonas,10626
        2020,Valle Central,28292
        2022,Andes,46705
        2020,Andes,9795
        2015,Andes,49404
        2023,Valle Central,21476
        2021,Gran Chaco,30828
        2017,Valle Central,40606
        2021,Valle Central,1155
        2021,Gran Chaco,45905
        2016,Gran Chaco,21797
        2022,Andes,28938
        """
    client = OpenAI(api_key="")

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente muy util, ayudas a dar recomendaciones de grafica basado en estadisticas que recibes, como tambien dando un analisis desde tu perspectiva generando mucha informacion para graficar y visualizar los datos como tambien un mensaje que ayuda a interpretar los datos recibidos, aqui tienes los datos recibidos del usuario. Estas limitado a solo sugerir 2 graficas",
            },
            {
                "role": "user",
                "content": f"tengo este analisis de 2 variables que son problematica de mi pais Bolivia :  {stats_text}",
            },
        ],
        
        response_format=RecomendationPlots,
        # tools=[
        #     openai.pydantic_function_tool(ResponseOut),
        # ],
    )

    # Retornar la respuesta con el mensaje y los gráficos
    return completion.choices[0].message.parsed
    # return RecomendationPlots(message=message, visual=visuals)
