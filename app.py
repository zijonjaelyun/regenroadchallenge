"""REGEN ROAD CHALLENGE v14: fullscreen Streamlit launcher.
Gameplay scenery is rendered from 3D world coordinates with map-specific moving props; menu previews are embedded in game.html.
"""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="REGEN ROAD CHALLENGE", page_icon="🏎️", layout="wide", initial_sidebar_state="collapsed")
html = (Path(__file__).resolve().parent / "game.html").read_text(encoding="utf-8")
st.markdown("""
<style>
html,body,[data-testid="stAppViewContainer"],.stApp{
  background:#050b13!important; margin:0!important;padding:0!important;overflow:hidden!important
}
.block-container{padding:0!important;max-width:none!important;margin:0!important}
header[data-testid="stHeader"],footer,[data-testid="stToolbar"],#MainMenu{display:none!important}
iframe[title="streamlit.components.v1.html"]{display:block!important;width:100vw!important;height:100vh!important;border:0!important}
</style>
""",unsafe_allow_html=True)
components.html(html,height=1200,scrolling=False)
