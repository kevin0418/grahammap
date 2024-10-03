import streamlit as st
from streamlit_folium import folium_static
import folium

# 기본 지도 생성
m = folium.Map(location=[-27.35614, 153.01403], zoom_start=12)

# 마커 추가 (optional)
folium.Marker(location=[-27.35614, 153.01403], popup='Yong Sale').add_to(m)

# Streamlit에서 Folium 지도를 표시
folium_static(m)
