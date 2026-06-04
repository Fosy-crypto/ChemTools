import streamlit as st
import pandas as pd
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="ChemLab Mini Tools",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# SAFE THEME (NAVY + MINERAL BLUE)
# =========================
st.markdown(
    """
    <style>

    /* =========================
       BACKGROUND
       ========================= */
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

    /* =========================
       GLASS CONTAINER
       ========================= */
    .block-container {
        padding: 2rem;
        border-radius: 16px;
        background-color: rgba(10, 25, 47, 0.75);
        box-shadow: 0px 8px 30px rgba(0,0,0,0.5);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(45, 156, 219, 0.2);
    }

    /* =========================
       TEXT FIX
       ========================= */
    h1, h2, h3, h4, h5, p, label, span {
        color: #e6f1ff !important;
    }

    /* =========================
       INPUT FIX (STREAMLIT SAFE)
       ========================= */
    div[data-baseweb="input"] input {
        background-color: #0f2740 !important;
        color: #ffffff !important;
        border: 1px solid #2d9cdb !important;
        caret-color: #2d9cdb !important;
    }

    textarea {
        background-color: #0f2740 !important;
        color: #ffffff !important;
        border: 1px solid #2d9cdb !important;
    }

    input::placeholder, textarea::placeholder {
        color: #a9c7e6 !important;
        opacity: 1 !important;
    }

    /* =========================
       BUTTON FIX
       ========================= */
    div.stButton > button {
        background-color: #2d9cdb !important;
        color: #0b1320 !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 10px 20px !important;
        transition: all 0.3s ease !important;
    }

    div.stButton > button:hover {
        background-color: #1f6f8b !important;
        transform: translateY(-2px) !important;
    }

    /* =========================
       SIDEBAR
       ========================= */
    section[data-testid="stSidebar"] {
        background-color: rgba(11, 19, 32, 0.95) !important;
        border-right: 2px solid rgba(45, 156, 219, 0.3) !important;
    }

    /* =========================
       SELECTBOX & RADIO
       ========================= */
    div[data-baseweb="select"] {
        background-color: #0f2740 !important;
    }

    div[data-baseweb="radio"] label {
        color: #e6f1ff !important;
    }

    /* =========================
       CARDS/COLUMNS
       ========================= */
    .metric-card {
        background-color: rgba(45, 156, 219, 0.1);
        border: 2px solid rgba(45, 156, 219, 0.3);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }

    /* =========================
       TOOLBAR HIDE
       ========================= */
    div[data-testid="stToolbar"] {
        display: none !important;
    }

    /* =========================
       CUSTOM MENU BUTTONS
       ========================= */
    .menu-button {
        background: linear-gradient(135deg, #2d9cdb, #1f6f8b);
        border: 2px solid #2d9cdb;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        color: #e6f1ff;
        font-weight: bold;
        font-size: 18px;
    }

    .menu-button:hover {
        background: linear-gradient(135deg, #1f6f8b, #102a43);
        box-shadow: 0px 8px 20px rgba(45, 156, 219, 0.4);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# SESSION STATE INITIALIZATION
# =========================
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "history" not in st.session_state:
    st.session_state.history = []
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_attempts" not in st.session_state:
    st.session_state.quiz_attempts = 0

# =========================
# NAVIGATION FUNCTIONS
# =========================
def set_page(page_name):
    st.session_state.page = page_name

# =========================
# HOME PAGE
# =========================
def page_home():
    st.markdown(
        "<h1 style='text-align:center;color:#2d9cdb;margin-bottom:2rem;'>🧪 ChemLab Mini Tools</h1>",
        unsafe_allow_html=True
    )
    
    st.markdown(
        "<p style='text-align:center;font-size:18px;color:#a9c7e6;margin-bottom:3rem;'>Selamat datang di platform pembelajaran kimia interaktif</p>",
        unsafe_allow_html=True
    )

    # Statistics Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📊 Perhitungan", len(st.session_state.history), "histori")
    with col2:
        st.metric("🎮 Kuis", st.session_state.quiz_attempts, "percobaan")
    with col3:
        st.metric("✅ Jawaban Benar", st.session_state.quiz_score, "poin")
    with col4:
        if st.session_state.quiz_attempts > 0:
            akurasi = (st.session_state.quiz_score / st.session_state.quiz_attempts) * 100
            st.metric("🎯 Akurasi", f"{akurasi:.1f}%", "tepat sasaran")
        else:
            st.metric("🎯 Akurasi", "0%", "belum ada")

    st.divider()

    # Main Features
    st.markdown("<h2 style='color:#2d9cdb;text-align:center;'>📚 Pilih Fitur Favorit Anda</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(45, 156, 219, 0.2), rgba(31, 111, 139, 0.2)); 
                        border: 2px solid rgba(45, 156, 219, 0.5); border-radius: 15px; padding: 2rem; 
                        text-align: center; cursor: pointer;'>
                <h3 style='color:#2d9cdb;font-size:32px;'>📊</h3>
                <h3 style='color:#e6f1ff;'>Kalkulator Pengenceran</h3>
                <p style='color:#a9c7e6;'>Hitung volume & konsentrasi dengan rumus C₁V₁ = C₂V₂</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Buka Kalkulator", key="btn_calculator", use_container_width=True):
            set_page("Kalkulator Pengenceran")
            st.rerun()

    with col2:
        st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(45, 156, 219, 0.2), rgba(31, 111, 139, 0.2)); 
                        border: 2px solid rgba(45, 156, 219, 0.5); border-radius: 15px; padding: 2rem; 
                        text-align: center; cursor: pointer;'>
                <h3 style='color:#2d9cdb;font-size:32px;'>🎮</h3>
                <h3 style='color:#e6f1ff;'>Tebak Warna Reaksi</h3>
                <p style='color:#a9c7e6;'>Kuis interaktif tentang warna reaksi kimia</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Mainkan Kuis", key="btn_quiz", use_container_width=True):
            set_page("Tebak Warna Reaksi")
            st.rerun()

    with col3:
        st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(45, 156, 219, 0.2), rgba(31, 111, 139, 0.2)); 
                        border: 2px solid rgba(45, 156, 219, 0.5); border-radius: 15px; padding: 2rem; 
                        text-align: center; cursor: pointer;'>
                <h3 style='color:#2d9cdb;font-size:32px;'>🧠</h3>
                <h3 style='color:#e6f1ff;'>Kenapa Gagal?</h3>
                <p style='color:#a9c7e6;'>Analisis kesalahan percobaan kimia</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Lihat Analisis", key="btn_analysis", use_container_width=True):
            set_page("Kenapa Gagal?")
            st.rerun()

    st.divider()

    # Info Section
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            ### ⚡ Fitur Unggulan
            - ✨ Antarmuka interaktif & responsif
            - 📊 Riwayat lengkap semua perhitungan
            - 🎮 Kuis edukatif dengan scoring
            - 🧠 Analisis detail setiap kesalahan
            - 🎨 Desain modern dengan tema gelap
        """)
    with col2:
        st.markdown("""
            ### 💡 Tips Penggunaan
            - Masukkan nilai dengan cermat
            - Periksa satuan sebelum menghitung
            - Pelajari setiap analisis kesalahan
            - Catat hasil di riwayat Anda
            - Berlatih kuis secara berkala
        """)

# =========================
# KALKULATOR PENGENCERAN
# =========================
def page_kalkulator():
    st.markdown(
        "<h2 style='text-align:center;color:#2d9cdb;'>📊 Kalkulator Pengenceran</h2>",
        unsafe_allow_html=True
    )
    
    st.latex(r"C_1 \times V_1 = C_2 \times V_2")
    
    st.markdown("""
    **Penjelasan Rumus:**
    - **C₁** = Konsentrasi awal
    - **V₁** = Volume awal
    - **C₂** = Konsentrasi akhir
    - **V₂** = Volume akhir
    """)
    
    st.divider()

    # Settings
    col1, col2, col3 = st.columns(3)
    with col1:
        satuan = st.selectbox("Satuan Volume", ["mL", "L"], key="volume_unit")
    with col2:
        satuan_konsentrasi = st.selectbox("Satuan Konsentrasi", ["M", "N", "mol/L"], key="conc_unit")
    with col3:
        cari = st.selectbox("Cari Variabel", ["V2", "C1", "C2", "V1"], key="variable")

    st.markdown("### 📝 Masukkan Data")

    # V2 Calculation
    if cari == "V2":
        col1, col2, col3 = st.columns(3)
        with col1:
            C1 = st.number_input(f"C1 ({satuan_konsentrasi})", value=0.0, step=0.01, format="%.2f")
        with col2:
            V1 = st.number_input(f"V1 ({satuan})", value=0.0, step=0.1, format="%.1f")
        with col3:
            C2 = st.number_input(f"C2 ({satuan_konsentrasi})", value=0.0, step=0.01, format="%.2f")

        if st.button("🔢 Hitung V2", use_container_width=True, key="calc_v2"):
            if C1 <= 0 or V1 <= 0 or C2 <= 0:
                st.error("❌ Semua nilai harus lebih besar dari 0!")
            else:
                V2 = (C1 * V1) / C2
                hasil = f"V2 = {V2:.2f} {satuan}"
                st.session_state.history.append({
                    "waktu": datetime.now().strftime("%H:%M:%S"),
                    "tipe": "V2",
                    "hasil": hasil,
                    "data": f"C1={C1}, V1={V1}, C2={C2}"
                })
                
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.success(f"✅ {hasil}")
                with col2:
                    st.balloons()

    # C1 Calculation
    elif cari == "C1":
        col1, col2, col3 = st.columns(3)
        with col1:
            V1 = st.number_input(f"V1 ({satuan})", value=0.0, step=0.1, format="%.1f", key="c1_v1")
        with col2:
            C2 = st.number_input(f"C2 ({satuan_konsentrasi})", value=0.0, step=0.01, format="%.2f", key="c1_c2")
        with col3:
            V2 = st.number_input(f"V2 ({satuan})", value=0.0, step=0.1, format="%.1f", key="c1_v2")

        if st.button("🔢 Hitung C1", use_container_width=True, key="calc_c1"):
            if V1 <= 0 or C2 <= 0 or V2 <= 0:
                st.error("❌ Semua nilai harus lebih besar dari 0!")
            else:
                C1 = (C2 * V2) / V1
                hasil = f"C1 = {C1:.4f} {satuan_konsentrasi}"
                st.session_state.history.append({
                    "waktu": datetime.now().strftime("%H:%M:%S"),
                    "tipe": "C1",
                    "hasil": hasil,
                    "data": f"V1={V1}, C2={C2}, V2={V2}"
                })
                
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.success(f"✅ {hasil}")
                with col2:
                    st.balloons()

    # C2 Calculation
    elif cari == "C2":
        col1, col2, col3 = st.columns(3)
        with col1:
            C1 = st.number_input(f"C1 ({satuan_konsentrasi})", value=0.0, step=0.01, format="%.2f", key="c2_c1")
        with col2:
            V1 = st.number_input(f"V1 ({satuan})", value=0.0, step=0.1, format="%.1f", key="c2_v1")
        with col3:
            V2 = st.number_input(f"V2 ({satuan})", value=0.0, step=0.1, format="%.1f", key="c2_v2")

        if st.button("🔢 Hitung C2", use_container_width=True, key="calc_c2"):
            if C1 <= 0 or V1 <= 0 or V2 <= 0:
                st.error("❌ Semua nilai harus lebih besar dari 0!")
            else:
                C2 = (C1 * V1) / V2
                hasil = f"C2 = {C2:.4f} {satuan_konsentrasi}"
                st.session_state.history.append({
                    "waktu": datetime.now().strftime("%H:%M:%S"),
                    "tipe": "C2",
                    "hasil": hasil,
                    "data": f"C1={C1}, V1={V1}, V2={V2}"
                })
                
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.success(f"✅ {hasil}")
                with col2:
                    st.balloons()

    # V1 Calculation
    elif cari == "V1":
        col1, col2, col3 = st.columns(3)
        with col1:
            C1 = st.number_input(f"C1 ({satuan_konsentrasi})", value=0.0, step=0.01, format="%.2f", key="v1_c1")
        with col2:
            C2 = st.number_input(f"C2 ({satuan_konsentrasi})", value=0.0, step=0.01, format="%.2f", key="v1_c2")
        with col3:
            V2 = st.number_input(f"V2 ({satuan})", value=0.0, step=0.1, format="%.1f", key="v1_v2")

        if st.button("🔢 Hitung V1", use_container_width=True, key="calc_v1"):
            if C1 <= 0 or C2 <= 0 or V2 <= 0:
                st.error("❌ Semua nilai harus lebih besar dari 0!")
            else:
                V1 = (C2 * V2) / C1
                hasil = f"V1 = {V1:.2f} {satuan}"
                st.session_state.history.append({
                    "waktu": datetime.now().strftime("%H:%M:%S"),
                    "tipe": "V1",
                    "hasil": hasil,
                    "data": f"C1={C1}, C2={C2}, V2={V2}"
                })
                
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.success(f"✅ {hasil}")
                with col2:
                    st.balloons()

    st.divider()

    # History
    st.markdown("### 📜 Riwayat Perhitungan")
    
    if st.session_state.history:
        history_df = pd.DataFrame(st.session_state.history)
        st.dataframe(history_df, use_container_width=True, hide_index=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🗑️ Hapus Riwayat", use_container_width=True, key="clear_history"):
                st.session_state.history = []
                st.rerun()
        with col2:
            if st.button("📥 Export CSV", use_container_width=True, key="export_csv"):
                csv = history_df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="riwayat_perhitungan.csv",
                    mime="text/csv"
                )
        with col3:
            if st.button("← Kembali ke Menu", use_container_width=True, key="back_calc"):
                set_page("Home")
                st.rerun()
    else:
        st.info("📭 Belum ada perhitungan. Mulai hitung sekarang!")
        if st.button("← Kembali ke Menu", use_container_width=True, key="back_calc_empty"):
            set_page("Home")
            st.rerun()

# =========================
# TEBAK WARNA REAKSI
# =========================
def page_quiz():
    st.markdown(
        "<h2 style='text-align:center;color:#2d9cdb;'>🎮 Tebak Warna Reaksi</h2>",
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div style='text-align:center; background: rgba(45, 156, 219, 0.1); padding: 1rem; border-radius: 10px; margin-bottom: 2rem;'>
        <h3>📊 Skor Anda: {st.session_state.quiz_score}/{st.session_state.quiz_attempts if st.session_state.quiz_attempts > 0 else '0'}</h3>
    </div>
    """, unsafe_allow_html=True)

    quiz_data = [
        {
            "soal": "KMnO₄ + Fe²⁺ → warna apa?",
            "jawaban_benar": "Tak Berwarna",
            "penjelasan": "MnO₄⁻ (ungu) akan tereduksi menjadi Mn²⁺ (tidak berwarna) oleh Fe²⁺",
            "opsi": ["Ungu", "Tak Berwarna", "Coklat"]
        },
        {
            "soal": "Larutan CuSO₄ berwarna?",
            "jawaban_benar": "Biru",
            "penjelasan": "Ion Cu²⁺ dalam air menghasilkan warna biru yang khas",
            "opsi": ["Biru", "Hijau", "Kuning"]
        },
        {
            "soal": "Reaksi antara AgNO₃ + NaCl menghasilkan endapan?",
            "jawaban_benar": "Putih",
            "penjelasan": "AgCl adalah endapan putih yang tidak larut dalam air",
            "opsi": ["Putih", "Hitam", "Merah"]
        },
        {
            "soal": "Larutan FeCl₃ berwarna?",
            "jawaban_benar": "Kuning-coklat",
            "penjelasan": "Ion Fe³⁺ memberikan warna kuning-coklat dalam larutan",
            "opsi": ["Biru", "Kuning-coklat", "Ungu"]
        },
        {
            "soal": "Reaksi Na₂CO₃ + CaCl₂ menghasilkan endapan?",
            "jawaban_benar": "Putih",
            "penjelasan": "CaCO₃ adalah endapan putih yang tidak larut dalam air",
            "opsi": ["Putih", "Biru", "Hitam"]
        }
    ]

    col1, col2 = st.columns([3, 1])
    with col1:
        pilihan_soal = st.selectbox("Pilih Soal:", [f"Soal {i+1}" for i in range(len(quiz_data))], key="quiz_select")
    with col2:
        if st.button("🔀 Acak", use_container_width=True, key="randomize"):
            st.session_state.random_order = True

    soal_index = int(pilihan_soal.split()[-1]) - 1
    soal = quiz_data[soal_index]

    st.markdown(f"### {soal['soal']}")

    jawaban = st.radio(
        "Pilihan Anda:",
        soal["opsi"],
        key=f"quiz_answer_{soal_index}"
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✅ Cek Jawaban", use_container_width=True, key=f"check_{soal_index}"):
            st.session_state.quiz_attempts += 1
            if jawaban == soal["jawaban_benar"]:
                st.success(f"🎉 Benar! \n\n{soal['penjelasan']}")
                st.session_state.quiz_score += 1
                st.balloons()
            else:
                st.error(f"❌ Salah! \n\n**Jawaban yang benar:** {soal['jawaban_benar']} \n\n**Penjelasan:** {soal['penjelasan']}")

    with col2:
        if st.button("📚 Lihat Penjelasan", use_container_width=True, key=f"info_{soal_index}"):
            st.info(f"💡 **Penjelasan:** {soal['penjelasan']}")

    with col3:
        if st.button("← Kembali ke Menu", use_container_width=True, key="back_quiz"):
            set_page("Home")
            st.rerun()

    st.divider()
    st.markdown("### 📝 Semua Soal")
    for i, q in enumerate(quiz_data):
        st.write(f"**Soal {i+1}:** {q['soal']}")

# =========================
# KENAPA GAGAL?
# =========================
def page_analisis():
    st.markdown(
        "<h2 style='text-align:center;color:#2d9cdb;'>🧠 Analisis Kesalahan</h2>",
        unsafe_allow_html=True
    )

    analisis_data = {
        "Larutan tidak berubah warna": {
            "penyebab": [
                "🔴 Indikator salah - gunakan indikator yang sesuai dengan pH reaksi",
                "🔴 Reagen tidak aktif - periksa tanggal kadaluarsa",
                "🔴 Konsentrasi terlalu rendah - tambah jumlah reagen",
                "🔴 Kondisi pH tidak tepat - sesuaikan pH larutan"
            ],
            "solusi": [
                "✅ Pilih indikator dengan range pH yang sesuai",
                "✅ Gunakan reagen baru yang belum kadaluarsa",
                "✅ Tingkatkan konsentrasi atau volume reagen",
                "✅ Gunakan buffer untuk menyesuaikan pH"
            ],
            "tips": "Selalu lakukan uji coba dengan standar sebelum eksperimen sesungguhnya"
        },
        "Hasil titrasi berbeda jauh": {
            "penyebab": [
                "🔴 Kesalahan pembacaan buret - baca dari bawah meniscus",
                "🔴 Larutan tidak homogen - aduk perlahan sebelum titrasi",
                "🔴 Cuaca mempengaruhi - lakukan titrasi pada suhu yang sama",
                "🔴 Teknik poor - hati-hati dengan kecepatan penambahan"
            ],
            "solusi": [
                "✅ Baca skala buret dengan benar, catat pembacaan awal dan akhir",
                "✅ Aduk larutan dengan baik, pastikan homogen",
                "✅ Lakukan titrasi dalam kondisi suhu terkontrol",
                "✅ Latih teknik titrasi yang tepat"
            ],
            "tips": "Lakukan titrasi minimal 3 kali dan ambil rata-rata yang reasonable"
        },
        "End point terlalu cepat": {
            "penyebab": [
                "🔴 Titrasi terlalu cepat - kurangi kecepatan penambahan",
                "🔴 Konsentrasi terlalu tinggi - lakukan pengenceran",
                "🔴 Suhu larutan tinggi - dinginkan sebelum titrasi",
                "🔴 Sensitivitas indikator berlebih - gunakan indikator lain"
            ],
            "solusi": [
                "✅ Tambahkan zat titran perlahan-lahan, terutama saat mendekati akhir",
                "✅ Encerkan larutan dengan air suling",
                "✅ Biarkan larutan mencapai suhu ruangan",
                "✅ Coba indikator dengan sensitivitas lebih rendah"
            ],
            "tips": "Gunakan pipet atau buret dengan akurasi tinggi"
        },
        "Warna tidak hilang sama sekali": {
            "penyebab": [
                "🔴 Volume zat titran tidak cukup - tambah lebih banyak",
                "🔴 Reaksi reversible - gunakan zat lain",
                "🔴 Ada pengotor - saring atau distilasi larutan"
            ],
            "solusi": [
                "✅ Terus tambahkan zat titran hingga warna hilang",
                "✅ Gunakan reaksi yang lebih irreversible",
                "✅ Purifikasi larutan dengan cara yang sesuai"
            ],
            "tips": "Pastikan reaksi yang dipilih adalah reaksi yang sesuai untuk tujuan titrasi"
        }
    }

    masalah = st.selectbox(
        "🔍 Pilih masalah yang dialami:",
        list(analisis_data.keys()),
        key="analisis_select"
    )

    if st.button("📋 Analisis Masalah", use_container_width=True, key="analyze"):
        data = analisis_data[masalah]

        st.markdown("### 🔴 Penyebab Kemungkinan")
        for penyebab in data["penyebab"]:
            st.write(penyebab)

        st.markdown("### ✅ Solusi")
        for solusi in data["solusi"]:
            st.write(solusi)

        st.markdown("### 💡 Tips Tambahan")
        st.info(data["tips"])

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Kembali ke Menu", use_container_width=True, key="back_analisis"):
            set_page("Home")
            st.rerun()
    with col2:
        if st.button("🔄 Reset Skor", use_container_width=True, key="reset_score"):
            st.session_state.quiz_score = 0
            st.session_state.quiz_attempts = 0
            st.rerun()

# =========================
# MAIN APP LOGIC
# =========================
def main():
    # Sidebar Navigation
    with st.sidebar:
        st.markdown("<h3 style='text-align:center;color:#2d9cdb;'>🧪 MENU UTAMA</h3>", unsafe_allow_html=True)
        
        st.divider()

        # Navigation Buttons
        if st.button("🏠 Beranda", use_container_width=True, key="nav_home"):
            set_page("Home")
            st.rerun()

        if st.button("📊 Kalkulator Pengenceran", use_container_width=True, key="nav_calc"):
            set_page("Kalkulator Pengenceran")
            st.rerun()

        if st.button("🎮 Tebak Warna Reaksi", use_container_width=True, key="nav_quiz"):
            set_page("Tebak Warna Reaksi")
            st.rerun()

        if st.button("🧠 Kenapa Gagal?", use_container_width=True, key="nav_analisis"):
            set_page("Kenapa Gagal?")
            st.rerun()

        st.divider()

        # Statistics in Sidebar
        st.markdown("### 📈 Statistik")
        st.write(f"📊 Perhitungan: **{len(st.session_state.history)}**")
        st.write(f"🎮 Kuis: **{st.session_state.quiz_attempts}**")
        st.write(f"✅ Benar: **{st.session_state.quiz_score}**")

        st.divider()

        st.markdown("""
        ### 📚 Tentang App
        **ChemLab Mini Tools** adalah aplikasi pembelajaran kimia interaktif yang dirancang untuk membantu pelajar memahami:
        
        - Perhitungan konsentrasi & volume
        - Identifikasi warna reaksi
        - Analisis kesalahan praktikum
        
        **Versi:** 2.0  
        **Tema:** Modern Dark Mode
        """)

    # Main Content Area
    if st.session_state.page == "Home":
        page_home()
    elif st.session_state.page == "Kalkulator Pengenceran":
        page_kalkulator()
    elif st.session_state.page == "Tebak Warna Reaksi":
        page_quiz()
    elif st.session_state.page == "Kenapa Gagal?":
        page_analisis()

if __name__ == "__main__":
    main()
