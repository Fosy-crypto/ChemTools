import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="ChemLab Mini Tools",
    layout="centered"
)

# =========================
# SAFE THEME (NAVY + MINERAL BLUE)
# =========================
st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #0b1320,
            #102a43,
            #1f6f8b,
            #2d9cdb
        );
        background-size: 400% 400%;
        animation: gradientBG 14s ease infinite;
        color: #e6f1ff;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .block-container {
        padding: 2rem;
        border-radius: 16px;
        background-color: rgba(10, 25, 47, 0.75);
        box-shadow: 0px 8px 30px rgba(0,0,0,0.5);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(45, 156, 219, 0.2);
    }

    h1, h2, h3, h4, h5, p, label, span {
        color: #e6f1ff !important;
    }

    div[data-baseweb="input"] input {
        background-color: #0f2740 !important;
        color: #ffffff !important;
        border: 1px solid #2d9cdb !important;
        caret-color: #2d9cdb !important;
    }

    textarea {
        background-color: #0f2740 !important;
        color: #ffffff !important;
    }

    input::placeholder, textarea::placeholder {
        color: #a9c7e6 !important;
        opacity: 1 !important;
    }

    div.stButton > button {
        background-color: #2d9cdb !important;
        color: #0b1320 !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: none !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #0b1320 !important;
    }

    div[data-testid="stToolbar"] {
        display: none !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# TITLE
# =========================
st.markdown(
    """
    <h1 style='text-align:center;color:#2d9cdb;'>
        🧪 ChemLab Mini Tools
    </h1>
    <p style='text-align:center;color:#e6f1ff;'>
        📊 Kalkulator • 🎮 Quiz Reaksi • 🧠 Analisis Praktikum
    </p>
    """,
    unsafe_allow_html=True
)

# =========================
# MENU
# =========================
st.sidebar.markdown("## ⚙️ Menu Utama")
st.sidebar.markdown("---")

menu = st.sidebar.selectbox(
    "🧪 Pilih Fitur",
    [
        "📊 Kalkulator Pengenceran",
        "🎮 Tebak Warna Reaksi",
        "🧠 Kenapa Gagal?"
    ]
)

# =========================
# 1. KALKULATOR PENGENCERAN
# =========================
if menu == "📊 Kalkulator Pengenceran":

    st.header("📊 Kalkulator Pengenceran")
    st.latex(r"C_1 \times V_1 = C_2 \times V_2")

    # lanjutkan seluruh kode kalkulator Anda di sini tanpa perubahan

# =========================
# 2. TEBAK WARNA REAKSI
# =========================
elif menu == "🎮 Tebak Warna Reaksi":

    st.header("🎮 Tebak Warna Reaksi")

    jawaban = st.radio(
        "KMnO₄ + Fe²⁺ → warna apa?",
        ["Ungu", "Tak Berwarna", "Coklat"]
    )

    if st.button("Cek Jawaban"):
        if jawaban == "Tak Berwarna":
            st.success("Benar! MnO₄⁻ → Mn²⁺ (tidak berwarna)")
        else:
            st.error("Salah! Coba lagi 😄")

# =========================
# 3. KENAPA GAGAL
# =========================
elif menu == "🧠 Kenapa Gagal?":

    st.header("🧠 Analisis Kesalahan")

    masalah = st.selectbox(
        "Masalah:",
        [
            "Larutan tidak berubah warna",
            "Hasil titrasi berbeda jauh",
            "End point terlalu cepat"
        ]
    )

    if st.button("Analisis"):
        if masalah == "Larutan tidak berubah warna":
            st.write("- Indikator salah")
            st.write("- Reagen tidak aktif")

        elif masalah == "Hasil titrasi berbeda jauh":
            st.write("- Kesalahan pembacaan buret")
            st.write("- Larutan tidak homogen")

        elif masalah == "End point terlalu cepat":
            st.write("- Titrasi terlalu cepat")
            st.write("- Konsentrasi terlalu tinggi")
