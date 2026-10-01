"""Download helpers shared by the dashboard and its pages."""

from io import BytesIO

import streamlit as st


def excel_download_button(dataframe, filename, key):
    """Render a button that downloads the displayed dataframe as an Excel file."""
    output = BytesIO()
    dataframe.to_excel(output, index=False, engine="openpyxl")
    st.download_button(
        "Download Excel",
        data=output.getvalue(),
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key=key,
    )
