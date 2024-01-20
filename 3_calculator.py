import streamlit as streamlit
from app_pages.multi_page import MultiPage

from app_pages.page_calculator import calculator_body

app = MultiPage(app_name = "Calculator App")

app.add_page("Calculator", calculator_body)

app.run()
