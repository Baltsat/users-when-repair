import time

import catboost
from catboost import CatBoostRegressor
import numpy as np
import plotly.graph_objects as go
import streamlit as st
import json


def predict(data):
    gb_model = catboost.CatBoostRegressor()
    gb_model.load_model('model.cbm')

    return round(gb_model.predict(data) * 100, 3)


st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; background-color: #001111; color: #ece5f6'> Mr.Sister</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; background-color: #001111; color: #ece5f6'>Кейс 2. Когда ремонт?</h4>", unsafe_allow_html=True)



col1, col2, col3, col4 = st.columns(4)

with col1:
    Qp = st.text_input("Qп")
    T_average_first = st.text_input("Tср. начальная точка")
    p_input = st.text_input("Давление входа")

with col2:
    Vj = st.text_input("Vj")
    T_average_second = st.text_input("Tср. конечная точка")
    p_output = st.text_input("Давление выхода")

with col3:
    W = st.text_input("W")
    p_average_first = st.text_input("Pср. начальная точка")
    ingib = st.toggle("Ингибируемый трубопровод НГЖС")

with col4:
    Qg = st.text_input("Qg")
    p_average = st.text_input("Pср. конечная точка")
    long_ingib = st.text_input("Протяженность ингибитора")

with open('coord.json', 'r') as json_file:
    data = json.load(json_file)

data1 = [Qp, T_average_first, p_input, Vj, T_average_second, p_output, W, p_average_first, ingib, Qg, p_average, long_ingib]

flag = False
if st.button('% Износа данного участка трубопровода'):
    flag = True
print(flag)

if flag:
    st.write(predict(data1))
    flag = False



lat = []

lon = []

x, y = 44.19761932975591, 17.66469586172627

for key, val in data.items():
    lat.append(x - val[0])
    lon.append(y - val[1])

lat.sort()
lon.sort()

lat_nsk = [54.859249, 54.858190, 54.849264, 54.844629, 54.844280]
lon_nsk = [83.086347, 83.083929, 83.084680, 83.088186, 83.092101]

# fill data
mean_pres, std = 600, 350
pressures = np.random.normal(mean_pres, std, len(lat)).round(4)
pressures1 = np.random.normal(20, std, len(lat_nsk)).round(4)

st.title("Интерактивная карта возможных отказов трубопроводов от команды \"Mr.Sister\"")

# st.markdown(
#     "Разработанная система использует датчики с передачей данных с помощью акустического модема и обычной сети, "
#     "которые поступают на сервер, где происходит анализ и визуализация. "
#     "Разработанное решение позволит быстро и эффективно диагностировать трубы и обнаруживать утечки, "
#     "что также предотвратит негативное влияние на окружающую среду.")

# st.markdown("<b><h3>Состояние системы обновляется раз в 5 секунд</b></h3>", unsafe_allow_html=True)

# st.subheader("Интерактивная карта состояния Северного потока 2")
st_sever = st.empty()
st_text = st.empty()
st_nsk = st.empty()

while True:
    pressures = np.random.normal(mean_pres, std, len(lat)).round(4)
    pressures1 = np.random.normal(20, std, len(lat_nsk)).round(4)
    fig = go.Figure(
        go.Scattermapbox(
            name="<b>Северный поток - 2</b>",
            lat=lat,
            lon=lon,
            mode='lines+markers',
            line=dict(width=1, color='black'),
            marker=dict(
                color=["red" if abs(temp - pressures.mean()) > std else "green" for temp in pressures],
                size=10,
                symbol='circle'
            ),
            text=[f'Датчик {i}\nДавление p = {pressures[i]}' for i in range(len(pressures))]
        )
    )
    fig.update_layout(
        mapbox_style="open-street-map",
        title='Россия',
        autosize=True,
        mapbox=dict(
            bearing=0,
            center=dict(
                lat=np.mean(lat),
                lon=np.mean(lon)
            ),
            pitch=0,
            zoom=6.5
        ),
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    st_sever.plotly_chart(fig, use_container_width=True)
    time.sleep(300)


