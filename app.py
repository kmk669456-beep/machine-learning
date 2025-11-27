import streamlit as st
import pickle

# 모델 불러오기
model = pickle.load(open("model.pkl", "rb"))

st.title("날씨 기반 올림픽공원 주차 수요 예측 서비스")

temp = st.number_input("평균기온(℃)", 0, 40)
max_temp = st.number_input("평균최고기온(℃)", 0, 45)
min_temp = st.number_input("평균최저기온(℃)", -20, 30)
rain = st.number_input("강수량(mm)", 0, 300)
wind = st.number_input("평균풍속(m/s)", 0.0, 50.0)
month = st.number_input("월 (1~12)", 1, 12)

if st.button("예측하기"):
    features = [[temp, max_temp, min_temp, rain, wind, month]]
    result = model.predict(features)

    st.success(f"예측된 주차 수요: **{int(result[0]):,}대**")
