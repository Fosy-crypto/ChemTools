import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="ChemLab Mini Tools",
    layout="centered"
)

# =========================
# THEME: NAVY + MINERAL BLUE + FIX GARIS
# =========================
st.markdown(
    """
    <style>

    /* Background utama */
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

    /* Container glass effect */
    .block-container {
        padding: 2rem;
        border-radius: 16px;
        background-color: rgba(10, 25, 47, 0.75);
        box-shadow: 0px 8px 30px rgba(0,0,0,0.5);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(45, 156, 219, 0.2);
    }

    /* Text */
    h1, h2, h3, h4, p, label {
        color: #e6f1ff !important;
    }

    /* Button */
    button[kind="primary"] {
        border-radius: 10px !important;
        background-color: #2d9cdb !important;
        color: #0b1320 !important;
        font-weight: bold;
        border: none !important;
    }

    /* Input */
    input {
        background-color: #102a43 !important;
        color: #e6f1ff !important;
        border-radius: 8px !important;
        border: 1px solid #1f6f8b !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0b1320 !important;
    }

    /* =========================
       FIX GARIS / DIVIDER STREAMLIT
       ========================= */

    hr {
        display: none !important;
    }

    div[data-testid="stHeader"] {
        border-bottom: none !important;
        box-shadow: none !important;
    }

    div[data-testid="stToolbar"] {
        display: none !important;
    }

    h1, h2, h3 {
        border-bottom: none !important;
        box-shadow: none !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# TITLE
# =========================
st.markdown(
    "<h2 style='text-align:center;color:#2d9cdb;'>🧪 ChemLab Mini Tools</h2>",
    unsafe_allow_html=True
)

# =========================
# MENU
# =========================
menu = st.sidebar.selectbox(
    "Pilih Fitur",
    [
        "Kalkulator Pengenceran",
        "Tebak Warna Reaksi",
        "Kenapa Gagal?"
    ]
)

# =========================
# 1. KALKULATOR PENGENCERAN
# =========================
if menu == "Kalkulator Pengenceran":

    st.header("📊 Kalkulator Pengenceran")
    st.latex(r"C_1 \times V_1 = C_2 \times V_2")

    if "history" not in st.session_state:
        st.session_state.history = []

    satuan = st.selectbox("Satuan Volume", ["mL", "L"])
    satuan_konsentrasi = st.selectbox("Satuan Konsentrasi", ["M", "N"])

    cari = st.selectbox("Pilih variabel yang ingin dicari", ["V2", "C1", "C2", "V1"])

    # V2
    if cari == "V2":
        C1 = st.number_input(f"C1 ({satuan_konsentrasi})", value=None, placeholder="Masukkan C1")
        V1 = st.number_input(f"V1 ({satuan})", value=None, placeholder="Masukkan V1")
        C2 = st.number_input(f"C2 ({satuan_konsentrasi})", value=None, placeholder="Masukkan C2")

        if st.button("Hitung V2"):
            if None in (C1, V1, C2):
                st.error("Semua data harus diisi!")
            elif C2 == 0:
                st.error("C2 tidak boleh nol!")
            else:
                V2 = (C1 * V1) / C2
                hasil = f"V2 = {V2:.2f} {satuan}"
                st.session_state.history.append(hasil)
                st.success(hasil)

    # C1
    elif cari == "C1":
        V1 = st.number_input(f"V1 ({satuan})", value=None, placeholder="Masukkan V1")
        C2 = st.number_input(f"C2 ({satuan_konsentrasi})", value=None, placeholder="Masukkan C2")
        V2 = st.number_input(f"V2 ({satuan})", value=None, placeholder="Masukkan V2")

        if st.button("Hitung C1"):
            if None in (V1, C2, V2):
                st.error("Semua data harus diisi!")
            elif V1 == 0:
                st.error("V1 tidak boleh nol!")
            else:
                C1 = (C2 * V2) / V1
                hasil = f"C1 = {C1:.4f} {satuan_konsentrasi}"
                st.session_state.history.append(hasil)
                st.success(hasil)

    # C2
    elif cari == "C2":
        C1 = st.number_input(f"C1 ({satuan_konsentrasi})", value=None, placeholder="Masukkan C1")
        V1 = st.number_input(f"V1 ({satuan})", value=None, placeholder="Masukkan V1")
        V2 = st.number_input(f"V2 ({satuan})", value=None, placeholder="Masukkan V2")

        if st.button("Hitung C2"):
            if None in (C1, V1, V2):
                st.error("Semua data harus diisi!")
            elif V2 == 0:
                st.error("V2 tidak boleh nol!")
            else:
                C2 = (C1 * V1) / V2
                hasil = f"C2 = {C2:.4f} {satuan_konsentrasi}"
                st.session_state.history.append(hasil)
                st.success(hasil)

    # V1
    elif cari == "V1":
        C1 = st.number_input(f"C1 ({satuan_konsentrasi})", value=None, placeholder="Masukkan C1")
        C2 = st.number_input(f"C2 ({satuan_konsentrasi})", value=None, placeholder="Masukkan C2")
        V2 = st.number_input(f"V2 ({satuan})", value=None, placeholder="Masukkan V2")

        if st.button("Hitung V1"):
            if None in (C1, C2, V2):
                st.error("Semua data harus diisi!")
            elif C1 == 0:
                st.error("C1 tidak boleh nol!")
            else:
                V1 = (C2 * V2) / C1
                hasil = f"V1 = {V1:.2f} {satuan}"
                st.session_state.history.append(hasil)
                st.success(hasil)

    # RIWAYAT
    st.subheader("📜 Riwayat")

    if st.session_state.history:
        for item in reversed(st.session_state.history):
            st.write("•", item)
    else:
        st.info("Belum ada perhitungan")

    if st.button("🗑️ Hapus Riwayat"):
        st.session_state.history = []
        st.rerun()

# =========================
# 2. TEBAK WARNA REAKSI
# =========================
elif menu == "Tebak Warna Reaksi":

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
elif menu == "Kenapa Gagal?":

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
