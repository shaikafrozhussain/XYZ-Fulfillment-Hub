import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import text

from database.db import engine
from ui.downloads import excel_download_button
from ui.theme import style_dataframe


# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="XYZ Fulfillment Hub",
    page_icon=":material/inventory_2:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Keep the appearance choice in Streamlit's session state so it survives reruns.
with st.sidebar:
    st.title("Fulfillment Hub", icon=":material/inventory_2:")
    st.caption("XYZ Operations Dashboard")
    st.divider()
    dark_mode = st.toggle("Dark theme", key="dark_theme", value=False)

px.defaults.template = "plotly_dark" if dark_mode else "plotly_white"


# ============================================================
# CUSTOM CSS - DARK + WHITE PROFESSIONAL THEME
# ============================================================
# ============================================================
# CUSTOM CSS - PREMIUM FULFILLMENT HUB THEME
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       PREMIUM DESIGN SYSTEM
       ======================================================== */

    @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap'
    );

    :root {

        /* ----------------------------------------------------
           CORE COLORS
           ---------------------------------------------------- */

        --bg-main: #F5F7FB;
        --bg-white: #FFFFFF;
        --bg-soft: #F8FAFC;

        --dark: #080D1A;
        --dark-2: #0D1424;
        --dark-3: #151E31;
        --dark-4: #1E293B;

        /* ----------------------------------------------------
           BRAND COLORS
           ---------------------------------------------------- */

        --primary: #6366F1;
        --primary-dark: #4F46E5;
        --primary-deep: #4338CA;

        --blue: #3B82F6;
        --cyan: #06B6D4;
        --violet: #8B5CF6;

        /* ----------------------------------------------------
           STATUS COLORS
           ---------------------------------------------------- */

        --green: #10B981;
        --green-dark: #059669;
        --green-bg: #ECFDF5;

        --yellow: #F59E0B;
        --yellow-dark: #D97706;
        --yellow-bg: #FFFBEB;

        --red: #EF4444;
        --red-dark: #DC2626;
        --red-bg: #FEF2F2;

        --orange: #F97316;
        --orange-bg: #FFF7ED;

        --cyan-bg: #ECFEFF;

        /* ----------------------------------------------------
           TEXT
           ---------------------------------------------------- */

        --text-main: #0F172A;
        --text-dark: #1E293B;
        --text-body: #475569;
        --text-muted: #64748B;
        --text-light: #94A3B8;

        /* ----------------------------------------------------
           BORDERS
           ---------------------------------------------------- */

        --border: #E2E8F0;
        --border-light: #EDF2F7;
        --border-dark: #CBD5E1;

        /* ----------------------------------------------------
           SHADOWS
           ---------------------------------------------------- */

        --shadow-xs:
            0 1px 2px rgba(15, 23, 42, 0.04);

        --shadow-sm:
            0 2px 5px rgba(15, 23, 42, 0.04),
            0 8px 20px rgba(15, 23, 42, 0.035);

        --shadow-md:
            0 5px 12px rgba(15, 23, 42, 0.06),
            0 14px 30px rgba(15, 23, 42, 0.06);

        --shadow-lg:
            0 10px 25px rgba(15, 23, 42, 0.08),
            0 25px 55px rgba(15, 23, 42, 0.08);

        --shadow-blue:
            0 8px 25px rgba(99, 102, 241, 0.20);

        /* ----------------------------------------------------
           RADIUS
           ---------------------------------------------------- */

        --radius-sm: 8px;
        --radius-md: 12px;
        --radius-lg: 16px;
        --radius-xl: 20px;
        --radius-pill: 999px;

        /* ----------------------------------------------------
           GRADIENTS
           ---------------------------------------------------- */

        --gradient-brand:
            linear-gradient(
                135deg,
                #6366F1 0%,
                #3B82F6 50%,
                #06B6D4 100%
            );

        --gradient-purple:
            linear-gradient(
                135deg,
                #4F46E5 0%,
                #7C3AED 100%
            );

        --gradient-sidebar:
            linear-gradient(
                180deg,
                #0B1020 0%,
                #080D1A 45%,
                #050812 100%
            );

        --gradient-dark-card:
            linear-gradient(
                145deg,
                #111827 0%,
                #0B1120 100%
            );

        /* ----------------------------------------------------
           FONTS
           ---------------------------------------------------- */

        --font-main:
            'Inter',
            -apple-system,
            BlinkMacSystemFont,
            'Segoe UI',
            sans-serif;

        --font-mono:
            'JetBrains Mono',
            monospace;
    }


    /* ========================================================
       ANIMATIONS
       ======================================================== */

    @keyframes fadeUp {

        0% {
            opacity: 0;
            transform: translateY(14px);
        }

        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }


    @keyframes fadeIn {

        0% {
            opacity: 0;
        }

        100% {
            opacity: 1;
        }
    }


    @keyframes slideRight {

        0% {
            opacity: 0;
            transform: translateX(-12px);
        }

        100% {
            opacity: 1;
            transform: translateX(0);
        }
    }


    @keyframes pulse {

        0%,
        100% {
            opacity: 1;
            transform: scale(1);
        }

        50% {
            opacity: 0.72;
            transform: scale(1.08);
        }
    }


    @keyframes glow {

        0%,
        100% {
            box-shadow:
                0 0 0 rgba(99, 102, 241, 0);
        }

        50% {
            box-shadow:
                0 0 24px rgba(99, 102, 241, 0.25);
        }
    }


    @keyframes shimmer {

        0% {
            background-position: -200% 0;
        }

        100% {
            background-position: 200% 0;
        }
    }


    @keyframes gradientMove {

        0% {
            background-position: 0% 50%;
        }

        50% {
            background-position: 100% 50%;
        }

        100% {
            background-position: 0% 50%;
        }
    }


    @keyframes cardAppear {

        0% {
            opacity: 0;
            transform: translateY(20px) scale(0.985);
        }

        100% {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }


    /* ========================================================
       GLOBAL
       ======================================================== */

    html,
    body,
    [class*="css"] {

        font-family: var(--font-main) !important;

        -webkit-font-smoothing: antialiased;

        -moz-osx-font-smoothing: grayscale;
    }


    .stApp {

        background:
            radial-gradient(
                circle at 5% 5%,
                rgba(99, 102, 241, 0.055),
                transparent 28%
            ),
            radial-gradient(
                circle at 95% 90%,
                rgba(6, 182, 212, 0.045),
                transparent 30%
            ),
            var(--bg-main);

        background-attachment: fixed;
    }


    .main {

        background: transparent !important;
    }


    .block-container {

        max-width: 1500px !important;

        padding-top: 2.1rem !important;

        padding-bottom: 4rem !important;

        animation:
            fadeUp 0.45s ease-out;
    }


    /* ========================================================
       STREAMLIT HEADER
       ======================================================== */

    header[data-testid="stHeader"] {

        background:
            rgba(245, 247, 251, 0.82) !important;

        backdrop-filter:
            blur(18px) saturate(150%) !important;

        -webkit-backdrop-filter:
            blur(18px) saturate(150%);

        border-bottom:
            1px solid rgba(226, 232, 240, 0.75);
    }


    /* ========================================================
       TYPOGRAPHY
       ======================================================== */

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {

        font-family: var(--font-main) !important;

        color: var(--text-main) !important;

        letter-spacing: -0.035em !important;

        font-weight: 700 !important;
    }


    h1 {

        font-size: 2.05rem !important;

        line-height: 1.2 !important;

        font-weight: 800 !important;

        margin-bottom: 0.25rem !important;

        background:
            linear-gradient(
                135deg,
                #0F172A 0%,
                #334155 45%,
                #4F46E5 100%
            );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;
    }


    h2 {

        font-size: 1.45rem !important;

        margin-top: 1.5rem !important;
    }


    h3 {

        font-size: 1.15rem !important;
    }


    p {

        color: var(--text-muted);

        line-height: 1.6;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {

        background:
            var(--gradient-sidebar) !important;

        border-right:
            1px solid rgba(51, 65, 85, 0.35) !important;

        box-shadow:
            8px 0 35px rgba(0, 0, 0, 0.18);

        animation:
            slideRight 0.4s ease-out;
    }


    section[data-testid="stSidebar"] > div {

        background: transparent !important;

        padding-top: 1.65rem;
    }


    section[data-testid="stSidebar"] * {

        color: #CBD5E1;
    }


    section[data-testid="stSidebar"] h1 {

        color: #FFFFFF !important;

        font-size: 1.35rem !important;

        font-weight: 800 !important;

        letter-spacing: -0.025em !important;
    }


    section[data-testid="stSidebar"] h1:first-letter {

        filter:
            drop-shadow(
                0 0 8px rgba(99, 102, 241, 0.75)
            );
    }


    section[data-testid="stSidebar"] p {

        color: #94A3B8 !important;

        font-size: 0.82rem;
    }


    section[data-testid="stSidebar"] hr {

        border: none !important;

        border-top:
            1px solid rgba(71, 85, 105, 0.35) !important;

        margin:
            1.3rem 0 !important;
    }


    /* ========================================================
       SIDEBAR NAVIGATION
       ======================================================== */

    section[data-testid="stSidebar"]
    div[role="radiogroup"] {

        gap: 5px;

        padding-top: 5px;
    }


    section[data-testid="stSidebar"]
    div[role="radiogroup"]
    label {

        position: relative;

        border-radius:
            var(--radius-md) !important;

        padding:
            10px 13px !important;

        border:
            1px solid transparent !important;

        background:
            transparent !important;

        cursor: pointer;

        transition:
            all 0.22s
            cubic-bezier(0.16, 1, 0.3, 1) !important;
    }


    section[data-testid="stSidebar"]
    div[role="radiogroup"]
    label:hover {

        background:
            rgba(51, 65, 85, 0.42) !important;

        border-color:
            rgba(100, 116, 139, 0.28) !important;

        transform:
            translateX(4px);
    }


    section[data-testid="stSidebar"]
    div[role="radiogroup"]
    label:hover p {

        color: #FFFFFF !important;
    }


    /* ACTIVE NAVIGATION */

    section[data-testid="stSidebar"]
    div[role="radiogroup"]
    label[data-checked="true"],
    section[data-testid="stSidebar"]
    div[role="radiogroup"]
    label:has(input:checked) {

        background:
            linear-gradient(
                135deg,
                rgba(99, 102, 241, 0.95),
                rgba(59, 130, 246, 0.9)
            ) !important;

        border-color:
            rgba(165, 180, 252, 0.3) !important;

        box-shadow:
            0 7px 20px
            rgba(79, 70, 229, 0.32);

        animation:
            glow 3s ease-in-out infinite;
    }


    section[data-testid="stSidebar"]
    div[role="radiogroup"]
    label[data-checked="true"] p,
    section[data-testid="stSidebar"]
    div[role="radiogroup"]
    label:has(input:checked) p {

        color: #FFFFFF !important;

        font-weight: 650 !important;
    }


    /* Active indicator */

    section[data-testid="stSidebar"]
    div[role="radiogroup"]
    label[data-checked="true"]::before,
    section[data-testid="stSidebar"]
    div[role="radiogroup"]
    label:has(input:checked)::before {

        content: "";

        position: absolute;

        left: -1px;

        top: 25%;

        width: 3px;

        height: 50%;

        border-radius: 999px;

        background: #FFFFFF;

        box-shadow:
            0 0 10px
            rgba(255, 255, 255, 0.75);
    }


    /* ========================================================
       SECTION TITLES
       ======================================================== */

    .section-title {

        position: relative;

        display: flex;

        align-items: center;

        gap: 12px;

        margin:
            2rem 0 1rem 0;

        color:
            #64748B !important;

        font-size:
            0.78rem !important;

        font-weight:
            800 !important;

        text-transform:
            uppercase;

        letter-spacing:
            0.11em;
    }


    .section-title::before {

        content: "";

        width: 4px;

        height: 18px;

        border-radius: 999px;

        background:
            var(--gradient-brand);

        box-shadow:
            0 0 10px
            rgba(99, 102, 241, 0.35);
    }


    .section-title::after {

        content: "";

        height: 1px;

        flex: 1;

        background:
            linear-gradient(
                90deg,
                #E2E8F0,
                transparent
            );
    }


    /* ========================================================
       KPI METRIC CARDS
       ======================================================== */

    div[data-testid="stMetric"] {

        position: relative;

        overflow: hidden;

        min-height: 112px;

        padding:
            1.25rem 1.35rem !important;

        background:
            rgba(255, 255, 255, 0.96) !important;

        border:
            1px solid var(--border) !important;

        border-radius:
            var(--radius-lg) !important;

        box-shadow:
            var(--shadow-sm) !important;

        transition:
            transform 0.28s
                cubic-bezier(0.16, 1, 0.3, 1),
            box-shadow 0.28s
                cubic-bezier(0.16, 1, 0.3, 1),
            border-color 0.2s ease;

        animation:
            cardAppear 0.5s ease-out both;
    }


    /* Stagger KPI animation */

    div[data-testid="stMetric"]:nth-child(1) {
        animation-delay: 0.05s;
    }

    div[data-testid="stMetric"]:nth-child(2) {
        animation-delay: 0.10s;
    }

    div[data-testid="stMetric"]:nth-child(3) {
        animation-delay: 0.15s;
    }

    div[data-testid="stMetric"]:nth-child(4) {
        animation-delay: 0.20s;
    }

    div[data-testid="stMetric"]:nth-child(5) {
        animation-delay: 0.25s;
    }


    /* Top gradient line */

    div[data-testid="stMetric"]::before {

        content: "";

        position: absolute;

        left: 0;

        right: 0;

        top: 0;

        height: 3px;

        background:
            var(--gradient-brand);

        background-size:
            200% 200%;

        animation:
            gradientMove 6s ease infinite;
    }


    /* Soft corner glow */

    div[data-testid="stMetric"]::after {

        content: "";

        position: absolute;

        width: 90px;

        height: 90px;

        right: -40px;

        top: -40px;

        border-radius: 50%;

        background:
            rgba(99, 102, 241, 0.06);

        filter:
            blur(2px);

        transition:
            transform 0.35s ease;
    }


    div[data-testid="stMetric"]:hover {

        transform:
            translateY(-6px);

        border-color:
            rgba(99, 102, 241, 0.28) !important;

        box-shadow:
            var(--shadow-blue),
            var(--shadow-md) !important;
    }


    div[data-testid="stMetric"]:hover::after {

        transform:
            scale(1.6);
    }


    div[data-testid="stMetricLabel"] {

        color:
            var(--text-muted) !important;

        font-size:
            0.73rem !important;

        font-weight:
            700 !important;

        text-transform:
            uppercase;

        letter-spacing:
            0.075em;

        margin-bottom:
            0.35rem;
    }


    div[data-testid="stMetricValue"] {

        color:
            var(--text-main) !important;

        font-size:
            2rem !important;

        font-weight:
            800 !important;

        letter-spacing:
            -0.045em !important;

        line-height:
            1.15 !important;

        font-variant-numeric:
            tabular-nums;
    }


    div[data-testid="stMetricDelta"] {

        display:
            inline-flex !important;

        align-items:
            center;

        margin-top:
            7px !important;

        padding:
            3px 8px !important;

        border-radius:
            var(--radius-pill) !important;

        font-size:
            0.72rem !important;

        font-weight:
            700 !important;
    }


    /* ========================================================
       ALERTS
       ======================================================== */

    div[data-testid="stAlert"] {

        border-radius:
            var(--radius-md) !important;

        border:
            1px solid transparent !important;

        padding:
            0.85rem 1rem !important;

        margin-bottom:
            0.75rem !important;

        box-shadow:
            var(--shadow-xs) !important;

        backdrop-filter:
            blur(8px);

        animation:
            fadeUp 0.35s ease-out;

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }


    div[data-testid="stAlert"]:hover {

        transform:
            translateX(3px);

        box-shadow:
            var(--shadow-sm) !important;
    }


    div[data-testid="stAlert"] p {

        font-size:
            0.86rem !important;

        font-weight:
            500;
    }


    /* WARNING */

    div[data-testid="stAlert"][kind="warning"] {

        background:
            linear-gradient(
                135deg,
                #FFFBEB,
                #FFF7E6
            ) !important;

        border-color:
            #FDE68A !important;

        border-left:
            4px solid #F59E0B !important;
    }


    /* ERROR */

    div[data-testid="stAlert"][kind="error"] {

        background:
            linear-gradient(
                135deg,
                #FEF2F2,
                #FFF5F5
            ) !important;

        border-color:
            #FECACA !important;

        border-left:
            4px solid #EF4444 !important;
    }


    /* SUCCESS */

    div[data-testid="stAlert"][kind="success"] {

        background:
            linear-gradient(
                135deg,
                #ECFDF5,
                #F0FDFA
            ) !important;

        border-color:
            #A7F3D0 !important;

        border-left:
            4px solid #10B981 !important;
    }


    /* INFO */

    div[data-testid="stAlert"][kind="info"] {

        background:
            linear-gradient(
                135deg,
                #EFF6FF,
                #F0F9FF
            ) !important;

        border-color:
            #BFDBFE !important;

        border-left:
            4px solid #3B82F6 !important;
    }


    /* ========================================================
       CUSTOM ALERT BOX
       ======================================================== */

    .alert-box {

        background:
            #FFFFFF;

        border:
            1px solid var(--border);

        border-left:
            4px solid var(--yellow);

        border-radius:
            var(--radius-md);

        padding:
            15px 18px;

        margin-bottom:
            10px;

        box-shadow:
            var(--shadow-sm);

        animation:
            fadeUp 0.4s ease-out;

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }


    .alert-box:hover {

        transform:
            translateX(4px);

        box-shadow:
            var(--shadow-md);
    }


    /* ========================================================
       CHART CONTAINERS
       ======================================================== */

    div[data-testid="stPlotlyChart"] {

        background:
            rgba(255, 255, 255, 0.98) !important;

        border:
            1px solid var(--border) !important;

        border-radius:
            var(--radius-lg) !important;

        padding:
            8px !important;

        box-shadow:
            var(--shadow-sm) !important;

        overflow:
            hidden;

        transition:
            transform 0.28s
                cubic-bezier(0.16, 1, 0.3, 1),
            box-shadow 0.28s ease,
            border-color 0.2s ease;

        animation:
            fadeUp 0.5s ease-out;
    }


    div[data-testid="stPlotlyChart"]:hover {

        transform:
            translateY(-3px);

        border-color:
            #CBD5E1 !important;

        box-shadow:
            var(--shadow-md) !important;
    }


    div[data-testid="stVegaLiteChart"],
    div[data-testid="stPyplot"] {

        background:
            #FFFFFF !important;

        border:
            1px solid var(--border) !important;

        border-radius:
            var(--radius-lg) !important;

        box-shadow:
            var(--shadow-sm) !important;

        padding:
            8px !important;
    }


    /* ========================================================
       DATA TABLE
       ======================================================== */

    div[data-testid="stDataFrame"] {

        background:
            #FFFFFF !important;

        border:
            1px solid var(--border) !important;

        border-radius:
            var(--radius-lg) !important;

        overflow:
            hidden !important;

        box-shadow:
            var(--shadow-sm) !important;

        transition:
            box-shadow 0.25s ease,
            transform 0.25s ease;

        animation:
            fadeUp 0.5s ease-out;
    }


    div[data-testid="stDataFrame"]:hover {

        transform:
            translateY(-2px);

        box-shadow:
            var(--shadow-md) !important;
    }


    div[data-testid="stDataFrame"] div[role="grid"] {

        font-family:
            var(--font-main) !important;

        font-size:
            0.84rem !important;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {

        position:
            relative;

        overflow:
            hidden;

        background:
            var(--gradient-brand) !important;

        background-size:
            200% 200% !important;

        color:
            #FFFFFF !important;

        border:
            none !important;

        border-radius:
            var(--radius-sm) !important;

        padding:
            0.58rem 1.3rem !important;

        font-family:
            var(--font-main) !important;

        font-size:
            0.85rem !important;

        font-weight:
            700 !important;

        box-shadow:
            0 5px 15px
            rgba(79, 70, 229, 0.22) !important;

        transition:
            all 0.22s
            cubic-bezier(0.16, 1, 0.3, 1) !important;
    }


    .stButton > button::before {

        content: "";

        position:
            absolute;

        top: 0;

        left: -100%;

        width: 70%;

        height: 100%;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(255,255,255,0.25),
                transparent
            );

        transition:
            left 0.5s ease;
    }


    .stButton > button:hover {

        background-position:
            100% 50% !important;

        transform:
            translateY(-2px);

        box-shadow:
            0 9px 24px
            rgba(79, 70, 229, 0.32) !important;
    }


    .stButton > button:hover::before {

        left:
            130%;
    }


    .stButton > button:active {

        transform:
            translateY(0) scale(0.97);
    }


    /* ========================================================
       INPUTS
       ======================================================== */

    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {

        background:
            #FFFFFF !important;

        border:
            1px solid var(--border) !important;

        border-radius:
            var(--radius-sm) !important;

        font-family:
            var(--font-main) !important;

        color:
            var(--text-main) !important;

        box-shadow:
            var(--shadow-xs);

        transition:
            border-color 0.18s ease,
            box-shadow 0.18s ease,
            transform 0.18s ease;
    }


    div[data-baseweb="select"] > div:hover,
    div[data-baseweb="input"] > div:hover,
    div[data-testid="stTextInput"] input:hover {

        border-color:
            #A5B4FC !important;
    }


    div[data-baseweb="select"] > div:focus-within,
    div[data-baseweb="input"] > div:focus-within,
    div[data-testid="stTextInput"] input:focus {

        border-color:
            var(--primary) !important;

        box-shadow:
            0 0 0 3px
            rgba(99, 102, 241, 0.13) !important;

        outline:
            none !important;
    }


    /* ========================================================
       INPUT LABELS
       ======================================================== */

    label[data-testid="stWidgetLabel"] p {

        color:
            var(--text-dark) !important;

        font-size:
            0.8rem !important;

        font-weight:
            650 !important;
    }


    /* ========================================================
       DIVIDERS
       ======================================================== */

    hr {

        border:
            none !important;

        border-top:
            1px solid var(--border) !important;

        margin:
            22px 0 !important;
    }


    /* ========================================================
       SIDEBAR CAPTION
       ======================================================== */

    section[data-testid="stSidebar"]
    [data-testid="stCaptionContainer"] {

        color:
            #64748B !important;
    }


    /* ========================================================
       CUSTOM LIVE STATUS
       ======================================================== */

    .live-badge {

        display:
            inline-flex;

        align-items:
            center;

        gap:
            7px;

        padding:
            5px 10px;

        background:
            rgba(16, 185, 129, 0.09);

        color:
            #059669;

        border:
            1px solid rgba(16, 185, 129, 0.22);

        border-radius:
            var(--radius-pill);

        font-size:
            0.72rem;

        font-weight:
            750;

        text-transform:
            uppercase;

        letter-spacing:
            0.06em;
    }


    .live-dot {

        width:
            7px;

        height:
            7px;

        background:
            var(--green);

        border-radius:
            50%;

        box-shadow:
            0 0 0
            rgba(16, 185, 129, 0.5);

        animation:
            pulse 1.8s infinite;
    }


    /* ========================================================
       SCROLLBAR
       ======================================================== */

    ::-webkit-scrollbar {

        width:
            7px;

        height:
            7px;
    }


    ::-webkit-scrollbar-track {

        background:
            transparent;
    }


    ::-webkit-scrollbar-thumb {

        background:
            linear-gradient(
                180deg,
                #CBD5E1,
                #94A3B8
            );

        border-radius:
            999px;
    }


    ::-webkit-scrollbar-thumb:hover {

        background:
            linear-gradient(
                180deg,
                #94A3B8,
                #64748B
            );
    }


    /* ========================================================
       COLUMN SPACING
       ======================================================== */

    [data-testid="column"] {

        padding-left:
            5px;

        padding-right:
            5px;
    }


    /* ========================================================
       EXPANDERS
       ======================================================== */

    div[data-testid="stExpander"] {

        background:
            #FFFFFF !important;

        border:
            1px solid var(--border) !important;

        border-radius:
            var(--radius-md) !important;

        box-shadow:
            var(--shadow-xs);

        transition:
            all 0.2s ease;
    }


    div[data-testid="stExpander"]:hover {

        border-color:
            #C7D2FE !important;

        box-shadow:
            var(--shadow-sm);
    }


    /* ========================================================
       CHECKBOXES / RADIO
       ======================================================== */

    div[data-testid="stCheckbox"] label,
    div[data-testid="stRadio"] label {

        transition:
            color 0.18s ease;
    }


    div[data-testid="stCheckbox"] label:hover,
    div[data-testid="stRadio"] label:hover {

        color:
            var(--primary) !important;
    }


    /* ========================================================
       TOOLTIPS / POPOVERS
       ======================================================== */

    div[data-baseweb="popover"] {

        border-radius:
            var(--radius-md) !important;

        box-shadow:
            var(--shadow-lg) !important;

        border:
            1px solid var(--border) !important;
    }


    /* ========================================================
       RESPONSIVE
       ======================================================== */

    @media (max-width: 1100px) {

        .block-container {

            padding-left:
                1.2rem !important;

            padding-right:
                1.2rem !important;
        }

        div[data-testid="stMetricValue"] {

            font-size:
                1.7rem !important;
        }
    }


    @media (max-width: 768px) {

        .block-container {

            padding-top:
                1.25rem !important;

            padding-left:
                0.9rem !important;

            padding-right:
                0.9rem !important;
        }


        h1 {

            font-size:
                1.55rem !important;
        }


        h2 {

            font-size:
                1.25rem !important;
        }


        div[data-testid="stMetric"] {

            min-height:
                95px;

            padding:
                1rem !important;
        }


        div[data-testid="stMetricValue"] {

            font-size:
                1.55rem !important;
        }


        .section-title {

            font-size:
                0.72rem !important;
        }
    }


    /* ========================================================
       REDUCE MOTION FOR ACCESSIBILITY
       ======================================================== */

    @media (prefers-reduced-motion: reduce) {

        *,
        *::before,
        *::after {

            animation-duration:
                0.01ms !important;

            animation-iteration-count:
                1 !important;

            transition-duration:
                0.01ms !important;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# The base design above is tuned for the light theme. These overrides keep the
# same layout and accent colors while adapting every major surface for dark mode.
if dark_mode:
    st.markdown(
        """
        <style>
        :root {
            color-scheme: dark;
            --bg-main: #0b1120; --bg-white: #111a2c; --bg-soft: #151f33;
            --text-main: #eef2ff; --text-dark: #dbe4f4; --text-body: #c2ccdc;
            --text-muted: #94a3b8; --text-light: #718096;
            --border: #273449; --border-light: #202c40; --border-dark: #3b4b63;
            --shadow-xs: 0 1px 2px rgba(0,0,0,.2);
            --shadow-sm: 0 4px 14px rgba(0,0,0,.22);
            --shadow-md: 0 10px 28px rgba(0,0,0,.28);
        }
        .stApp { background: radial-gradient(ellipse at 5% 0%, rgba(99,102,241,.13), transparent 34%), radial-gradient(ellipse at 95% 95%, rgba(6,182,212,.08), transparent 32%), #0b1120 !important; color: #dbe4f4; }
        .main, [data-testid="stMain"] { background: transparent !important; }
        header[data-testid="stHeader"] { background: rgba(11,17,32,.86) !important; border-bottom-color: #273449 !important; }
        h1 { background-image: linear-gradient(135deg,#f8fafc 0%,#cbd5e1 48%,#a5b4fc 100%) !important; }
        h2,h3,h4,h5,h6 { color: #e2e8f0 !important; }
        p, [data-testid="stCaptionContainer"] { color: #9aa9bf; }
        section[data-testid="stSidebar"] { background: linear-gradient(180deg,#111a2c,#0b1120) !important; border-right-color: #273449 !important; }
        div[data-testid="stMetric"], div[data-testid="stPlotlyChart"], div[data-testid="stVegaLiteChart"], div[data-testid="stPyplot"], div[data-testid="stDataFrame"], div[data-testid="stExpander"] {
            background: #111a2c !important; border-color: #273449 !important; color: #dbe4f4 !important;
        }
        div[data-testid="stMetric"] { box-shadow: 0 8px 24px rgba(0,0,0,.2) !important; }
        div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"], [data-testid="stWidgetLabel"] p { color: #dbe4f4 !important; }
        div[data-testid="stDataFrame"] [role="grid"] { color: #dbe4f4 !important; }
        div[data-baseweb="select"] > div, div[data-baseweb="input"] > div,
        div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input {
            background: #111a2c !important; border-color: #34445c !important; color: #e2e8f0 !important;
        }
        div[data-baseweb="popover"], ul[role="listbox"] { background: #111a2c !important; border-color: #34445c !important; color: #e2e8f0 !important; }
        div[data-baseweb="popover"] *, ul[role="listbox"] * { color: #e2e8f0 !important; }
        div[data-testid="stAlert"] { background: #172338 !important; border-color: #34445c !important; }
        div[data-testid="stAlert"] p, div[data-testid="stAlert"] span { color: #e2e8f0 !important; }
        div[data-testid="stAlert"][kind="warning"] { border-left-color: #f59e0b !important; }
        div[data-testid="stAlert"][kind="error"] { border-left-color: #f87171 !important; }
        div[data-testid="stAlert"][kind="success"] { border-left-color: #34d399 !important; }
        div[data-testid="stAlert"][kind="info"] { border-left-color: #60a5fa !important; }
        div[data-testid="stCodeBlock"], pre, code { background: #111a2c !important; color: #dbe4f4 !important; }
        [data-testid="stMarkdownContainer"] a { color: #a5b4fc !important; }
        [data-testid="stTabs"] button { color: #aab7cb !important; }
        [data-testid="stTabs"] button[aria-selected="true"] { color: #c7d2fe !important; border-bottom-color: #818cf8 !important; }
        [data-testid="stProgress"] > div > div { background: #818cf8 !important; }
        input, textarea { caret-color: #a5b4fc; }
        .section-title { color: #a8b5ca !important; }
        .section-title::after, hr { border-color: #273449 !important; background-image: linear-gradient(90deg,#273449,transparent); }
        .alert-box { background: #111a2c; border-color: #34445c; color: #dbe4f4; }
        ::-webkit-scrollbar-thumb { background: linear-gradient(180deg,#475569,#334155); }
        @media (prefers-reduced-motion: reduce) { *,*::before,*::after { animation-duration:.01ms !important; animation-iteration-count:1 !important; transition-duration:.01ms !important; } }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        :root { color-scheme: light; }
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg,#ffffff 0%,#f7f9fd 100%) !important;
            border-right: 1px solid #e2e8f0 !important;
            box-shadow: 8px 0 30px rgba(15,23,42,.045) !important;
        }
        section[data-testid="stSidebar"] * { color: #334155 !important; }
        section[data-testid="stSidebar"] h1 { color: #0f172a !important; }
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] { color: #64748b !important; }
        section[data-testid="stSidebar"] hr { border-top-color: #e2e8f0 !important; }
        section[data-testid="stSidebar"] div[role="radiogroup"] label { background: transparent !important; }
        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background: #eef2ff !important; border-color: #c7d2fe !important;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover p { color: #3730a3 !important; }
        section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"],
        section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
            background: linear-gradient(135deg,#4f46e5,#6366f1) !important;
            border-color: #6366f1 !important; box-shadow: 0 7px 18px rgba(79,70,229,.2) !important;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] p,
        section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p { color: #fff !important; }
        [data-testid="stMarkdownContainer"] a { color: #4f46e5; }
        [data-testid="stTabs"] button { color: #475569; }
        [data-testid="stTabs"] button[aria-selected="true"] { color: #4338ca; border-bottom-color: #6366f1; }
        div[data-testid="stCodeBlock"], pre, code { background: #f1f5f9; color: #1e293b; }
        div[data-testid="stAlert"] { box-shadow: 0 3px 12px rgba(15,23,42,.04) !important; }
        @media (prefers-reduced-motion: reduce) {
            *,*::before,*::after { animation-duration:.01ms !important; animation-iteration-count:1 !important; transition-duration:.01ms !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Cap navigation labels consistently and give the appearance switch a compact,
# clear place above the page links.
st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] div[role="radiogroup"] label p { text-transform: capitalize; }
    section[data-testid="stSidebar"] div[role="radiogroup"] label { min-height: 44px; }
    section[data-testid="stSidebar"] [data-testid="stToggle"] { padding: 0 .15rem .25rem; }
    section[data-testid="stSidebar"] [data-testid="stSidebarNav"] { display: none !important; }
    .stButton > button, .stDownloadButton > button, [data-testid="stFormSubmitButton"] > button {
        color: #ffffff !important; text-shadow: 0 1px 2px rgba(15,23,42,.35) !important;
        font-weight: 700 !important;
    }
    .stButton > button *, .stDownloadButton > button *, [data-testid="stFormSubmitButton"] > button * {
        color: #ffffff !important; fill: #ffffff !important;
    }
    .stDownloadButton > button {
        background: linear-gradient(135deg, #059669, #10b981) !important;
        border: 1px solid #047857 !important;
    }
    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #047857, #059669) !important;
        border-color: #065f46 !important;
    }
    [data-testid="stMainBlockContainer"] { max-width: 1500px; padding-top: 2rem; }
    div[data-testid="stMetric"] { padding: 1rem 1.1rem; transition: transform .18s ease, box-shadow .18s ease; }
    div[data-testid="stMetric"]:hover { transform: translateY(-2px); }
    div[data-testid="stMetric"], div[data-testid="stPlotlyChart"], div[data-testid="stDataFrame"], div[data-testid="stExpander"] {
        border-radius: 15px !important; overflow: hidden;
    }
    h1 { letter-spacing: -.04em !important; }
    @media (max-width: 700px) {
        [data-testid="stMainBlockContainer"] { padding: 1rem .8rem 2rem; }
        div[data-testid="stMetric"] { padding: .8rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# DATABASE HELPERS
# ============================================================

def get_scalar(query, params=None):
    with engine.connect() as connection:
        result = connection.execute(
            text(query),
            params or {},
        )
        return result.scalar()


def get_dataframe(query, params=None):
    with engine.connect() as connection:
        return pd.read_sql(
            text(query),
            connection,
            params=params or {},
        )


# ============================================================
# METRICS
# ============================================================

def get_dashboard_metrics():

    total_orders = get_scalar(
        "SELECT COUNT(*) FROM orders"
    )

    priority_orders = get_scalar(
        """
        SELECT COUNT(*)
        FROM orders
        WHERE priority IN ('HIGH', 'URGENT')
        AND status NOT IN ('SHIPPED', 'DELIVERED')
        """
    )

    delayed_orders = get_scalar(
        """
        SELECT COUNT(*)
        FROM orders
        WHERE deadline < CURRENT_TIMESTAMP
        AND status NOT IN ('SHIPPED', 'DELIVERED')
        """
    )

    open_issues = get_scalar(
        """
        SELECT COUNT(*)
        FROM issues
        WHERE status != 'RESOLVED'
        """
    )

    inventory_mismatches = get_scalar(
        """
        SELECT COUNT(*)
        FROM inventory
        WHERE system_stock != physical_stock
        """
    )

    product_mismatches = get_scalar(
        """
        SELECT COUNT(*)
        FROM order_items
        WHERE product_id != picked_product_id
        """
    )

    return {
        "total_orders": total_orders,
        "priority_orders": priority_orders,
        "delayed_orders": delayed_orders,
        "open_issues": open_issues,
        "inventory_mismatches": inventory_mismatches,
        "product_mismatches": product_mismatches,
    }


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Orders",
            "Inventory",
            "Picking",
            "Shipping",
            "Issues",
        ],
    )

    st.divider()

    st.caption("Operations")
    st.caption("Order → Pick → Pack → Stage → Ship")


# ============================================================
# HEADER
# ============================================================

st.title("XYZ Fulfillment Hub")

st.caption(
    "Operational control center for order fulfillment, "
    "inventory and shipping."
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    metrics = get_dashboard_metrics()

    # --------------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Today\'s Overview</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Total Orders",
            f"{metrics['total_orders']:,}",
        )

    with col2:
        st.metric(
            "Priority Orders",
            f"{metrics['priority_orders']:,}",
        )

    with col3:
        st.metric(
            "Delayed Orders",
            f"{metrics['delayed_orders']:,}",
        )

    with col4:
        st.metric(
            "Open Issues",
            f"{metrics['open_issues']:,}",
        )

    with col5:
        st.metric(
            "Mismatches",
            f"{metrics['product_mismatches'] + metrics['inventory_mismatches']:,}",
        )

    st.divider()

    # --------------------------------------------------------
    # ACTION REQUIRED
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title"> Action Required</div>',
        unsafe_allow_html=True,
    )

    urgent_count = get_scalar(
        """
        SELECT COUNT(*)
        FROM orders
        WHERE priority = 'URGENT'
        AND status NOT IN ('SHIPPED', 'DELIVERED')
        AND deadline <= datetime('now', '+2 hours')
        """
    )

    shortage_count = get_scalar(
        """
        SELECT COUNT(*)
        FROM order_items oi
        JOIN inventory i
            ON oi.product_id = i.product_id
        WHERE i.warehouse_id = 1
        AND (i.system_stock - i.reserved_stock) < oi.quantity
        """
    )

    open_mismatches = metrics["product_mismatches"]

    pickup_delays = get_scalar(
        """
        SELECT COUNT(*)
        FROM shipments
        WHERE status = 'PICKUP_MISSED'
        """
    )

    action_col1, action_col2 = st.columns(2)

    with action_col1:

        if urgent_count > 0:
            st.warning(
                f" **{urgent_count:,}** urgent orders "
                f"are approaching their deadline."
            )

        if shortage_count > 0:
            st.warning(
                f" **{shortage_count:,}** order items "
                f"may have insufficient stock."
            )

    with action_col2:

        if open_mismatches > 0:
            st.warning(
                f" **{open_mismatches:,}** picking mismatches "
                f"need verification."
            )

        if pickup_delays > 0:
            st.error(
                f" **{pickup_delays:,}** courier pickups "
                f"were missed."
            )

    st.divider()

    # --------------------------------------------------------
    # ORDER PIPELINE
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Fulfillment Pipeline</div>',
        unsafe_allow_html=True,
    )

    pipeline = get_dataframe(
        """
        SELECT
            status,
            COUNT(*) AS orders
        FROM orders
        GROUP BY status
        ORDER BY orders DESC
        """
    )

    if not pipeline.empty:

        fig = px.bar(
            pipeline,
            x="status",
            y="orders",
            text="orders",
            title="Orders by Fulfillment Stage",
        )

        fig.update_layout(
            xaxis_title="Status",
            yaxis_title="Orders",
            showlegend=False,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    # --------------------------------------------------------
    # TWO CHARTS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        channel_data = get_dataframe(
            """
            SELECT
                channel,
                COUNT(*) AS orders
            FROM orders
            GROUP BY channel
            ORDER BY orders DESC
            """
        )

        fig = px.pie(
            channel_data,
            names="channel",
            values="orders",
            title="Orders by Channel",
        )

        fig.update_traces(
            textposition="inside",
            textinfo="label+percent",
            insidetextorientation="radial",
            textfont=dict(color="#ffffff", size=13),
            marker=dict(line=dict(color="#ffffff" if not dark_mode else "#111a2c", width=2)),
        )
        fig.update_layout(
            uniformtext_minsize=11,
            uniformtext_mode="hide",
            legend=dict(font=dict(color="#dbe4f4" if dark_mode else "#1e293b", size=12)),
            margin=dict(l=20, r=20, t=60, b=35),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    with col2:

        issue_data = get_dataframe(
            """
            SELECT
                type,
                COUNT(*) AS issues
            FROM issues
            GROUP BY type
            ORDER BY issues DESC
            """
        )

        fig = px.bar(
            issue_data,
            x="type",
            y="issues",
            title="Operational Issues",
        )

        fig.update_layout(
            xaxis_title="Issue Type",
            yaxis_title="Count",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    # --------------------------------------------------------
    # PRIORITY ORDERS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-title">Priority Orders</div>',
        unsafe_allow_html=True,
    )

    priority_orders = get_dataframe(
        """
        SELECT
            id AS order_id,
            channel,
            priority,
            status,
            deadline
        FROM orders
        WHERE priority IN ('HIGH', 'URGENT')
        AND status NOT IN ('SHIPPED', 'DELIVERED')
        ORDER BY deadline
        LIMIT 15
        """
    )

    if not priority_orders.empty:

        excel_download_button(priority_orders, "priority_orders.xlsx", "download_priority_orders")

        st.dataframe(
            style_dataframe(priority_orders),
            use_container_width=True,
            hide_index=True,
        )

elif page == "Orders":

    exec(
        open(
            "pages/orders.py",
            encoding="utf-8",
        ).read()
    )
elif page == "Inventory":
    exec(open("pages/inventory.py", encoding="utf-8").read())


elif page == "Picking":
    exec(open("pages/picking.py", encoding="utf-8").read())

elif page == "Shipping":
    exec(open("pages/shipping.py", encoding="utf-8").read())
    
elif page == "Issues":
    exec(open("pages/issues.py", encoding="utf-8").read())
