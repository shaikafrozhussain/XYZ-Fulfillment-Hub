"""Theme setup for pages launched outside the main dashboard script."""

import plotly.express as px
import streamlit as st


def style_dataframe(dataframe):
    """Apply the selected palette using pandas Styler for older Streamlit APIs."""
    dark_mode = bool(st.session_state.get("dark_theme", False))
    background = "#111a2c" if dark_mode else "#ffffff"
    foreground = "#dbe4f4" if dark_mode else "#334155"
    header_background = "#18243a" if dark_mode else "#eef2f8"
    header_foreground = "#f1f5f9" if dark_mode else "#1e293b"
    border = "#273449" if dark_mode else "#e2e8f0"

    return (
        dataframe.style
        .set_properties(**{
            "background-color": background,
            "color": foreground,
            "border-color": border,
            "font-size": "13px",
        })
        .set_table_styles([
            {
                "selector": "th",
                "props": [
                    ("background-color", header_background),
                    ("color", header_foreground),
                    ("font-weight", "700"),
                    ("border-color", border),
                ],
            },
        ])
    )


def configure_page_theme():
    """Add the standalone light/dark switch and return the table theme."""
    with st.sidebar:
        dark_mode = st.toggle("Dark theme", key="dark_theme", value=False)

    px.defaults.template = "plotly_dark" if dark_mode else "plotly_white"
    st.markdown(
        """
        <style>
        :root { color-scheme: __COLOR_SCHEME__; }
        * { box-sizing: border-box; }
        .stApp {
            background: __APP_BACKGROUND__ !important;
            color: __TEXT__;
        }
        [data-testid="stMain"] { background: transparent !important; }
        header[data-testid="stHeader"] {
            background: __HEADER_BACKGROUND__ !important;
            border-bottom: 1px solid __BORDER__;
        }
        h1,h2,h3,h4,h5,h6 { color: __HEADING__ !important; letter-spacing: -.025em; }
        h1 { font-weight: 800 !important; }
        p, [data-testid="stCaptionContainer"] { color: __MUTED__; }
        section[data-testid="stSidebar"] {
            background: __SIDEBAR_BACKGROUND__ !important;
            border-right: 1px solid __BORDER__ !important;
            box-shadow: 8px 0 30px rgba(15,23,42,.05);
        }
        /* The app-level radio menu is the single navigation control. */
        section[data-testid="stSidebar"] [data-testid="stSidebarNav"] { display: none !important; }
        section[data-testid="stSidebar"] div[role="radiogroup"] label {
            min-height: 44px; border: 1px solid transparent; border-radius: 11px;
            padding: .35rem .65rem; transition: background .18s ease, transform .18s ease;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover { transform: translateX(2px); }
        .stButton > button, .stDownloadButton > button,
        [data-testid="stFormSubmitButton"] > button {
            color: #ffffff !important; font-weight: 700 !important;
            background: linear-gradient(135deg,#4338ca,#4f46e5) !important;
            border: 1px solid #4338ca !important;
            text-shadow: 0 1px 2px rgba(15,23,42,.35) !important;
        }
        .stButton > button *, .stDownloadButton > button *,
        [data-testid="stFormSubmitButton"] > button * { color: #ffffff !important; fill: #ffffff !important; }
        section[data-testid="stSidebar"] * { color: __SIDEBAR_TEXT__ !important; }
        section[data-testid="stSidebar"] p { color: __MUTED__ !important; }
        section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"] {
            min-height: 42px; border-radius: 11px; text-transform: capitalize;
            transition: background .2s ease, transform .2s ease;
        }
        section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"]:hover {
            background: __NAV_HOVER__ !important; transform: translateX(3px);
        }
        div[data-testid="stMetric"], div[data-testid="stDataFrame"],
        div[data-testid="stPlotlyChart"], div[data-testid="stExpander"] {
            background: __SURFACE__ !important; border: 1px solid __BORDER__ !important;
            border-radius: 15px !important; box-shadow: 0 5px 18px rgba(15,23,42,.06);
        }
        div[data-testid="stMetric"] { padding: 1rem 1.1rem; transition: transform .18s ease, box-shadow .18s ease; }
        div[data-testid="stMetric"]:hover { transform: translateY(-2px); box-shadow: 0 10px 26px rgba(15,23,42,.1); }
        div[data-testid="stPlotlyChart"], div[data-testid="stDataFrame"], div[data-testid="stExpander"] { overflow: hidden; }
        [data-testid="stMainBlockContainer"] { max-width: 1500px; padding-top: 2rem; }
        h1 { letter-spacing: -.04em !important; }
        hr { opacity: .65; }
        div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"],
        [data-testid="stWidgetLabel"] p { color: __TEXT__ !important; }
        div[data-baseweb="select"] > div, div[data-baseweb="input"] > div,
        input, textarea { background: __SURFACE__ !important; color: __TEXT__ !important; }
        div[data-testid="stAlert"] { border-radius: 12px; }
        [data-testid="stMarkdownContainer"] a { color: __LINK__; }
        @media (prefers-reduced-motion: reduce) {
            *,*::before,*::after { animation-duration:.01ms !important; transition-duration:.01ms !important; }
        }
        @media (max-width: 700px) {
            [data-testid="stMainBlockContainer"] { padding: 1rem .8rem 2rem; }
            div[data-testid="stMetric"] { padding: .8rem; }
        }
        </style>
        """
        .replace("__COLOR_SCHEME__", "dark" if dark_mode else "light")
        .replace("__APP_BACKGROUND__", "#0b1120" if dark_mode else "#f5f7fb")
        .replace("__HEADER_BACKGROUND__", "rgba(11,17,32,.88)" if dark_mode else "rgba(255,255,255,.88)")
        .replace("__BORDER__", "#273449" if dark_mode else "#e2e8f0")
        .replace("__TEXT__", "#dbe4f4" if dark_mode else "#1e293b")
        .replace("__HEADING__", "#eef2ff" if dark_mode else "#0f172a")
        .replace("__MUTED__", "#94a3b8" if dark_mode else "#64748b")
        .replace("__SIDEBAR_BACKGROUND__", "linear-gradient(180deg,#111a2c,#0b1120)" if dark_mode else "linear-gradient(180deg,#fff,#f7f9fd)")
        .replace("__SIDEBAR_TEXT__", "#dbe4f4" if dark_mode else "#334155")
        .replace("__NAV_HOVER__", "#202c40" if dark_mode else "#eef2ff")
        .replace("__SURFACE__", "#111a2c" if dark_mode else "#fff")
        .replace("__LINK__", "#a5b4fc" if dark_mode else "#4f46e5"),
        unsafe_allow_html=True,
    )
