import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="🧪 ChemLab Mini Tools",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# THEME MANAGEMENT
# =========================
if 'theme' not in st.session_state:
    st.session_state.theme = 'ocean'

THEME_CONFIG = {
    'ocean': {
        'bg_gradient': 'linear-gradient(135deg, #0b1320, #102a43, #1f6f8b, #2d9cdb)',
        'primary': '#2d9cdb',
        'secondary': '#1f6f8b',
        'accent': '#00d9ff',
        'text': '#e6f1ff',
        'input_bg': '#0f2740',
        'card_bg': 'rgba(10, 25, 47, 0.75)',
    },
    'sunset': {
        'bg_gradient': 'linear-gradient(135deg, #1a0f2e, #372d5a, #8b4789, #ff6b9d)',
        'primary': '#ff6b9d',
        'secondary': '#8b4789',
        'accent': '#ffd700',
        'text': '#ffe6f0',
        'input_bg': '#2d1b4e',
        'card_bg': 'rgba(26, 15, 46, 0.75)',
    },
    'forest': {
        'bg_gradient': 'linear-gradient(135deg, #0b1f15, #1a3d2a, #2d5a47, #52b788)',
        'primary': '#52b788',
        'secondary': '#2d5a47',
        'accent': '#74c69d',
        'text': '#e6f5f0',
        'input_bg': '#0f2d1f',
        'card_bg': 'rgba(11, 31, 21, 0.75)',
    }
}

theme = THEME_CONFIG[st.session_state.theme]

# =========================
# DYNAMIC STYLING
# =========================
st.markdown(f"""
    <style>
    /* Background Animation */
    .stApp {{
        background: {theme['bg_gradient']};
        background-size: 400% 400%;
        animation: gradientBG 14s ease infinite;
        color: {theme['text']};
    }}

    @keyframes gradientBG {{
        0% {{background-position: 0% 50%;}}
        50% {{background-position: 100% 50%;}}
        100% {{background-position: 0% 50%;}}
    }}

    /* Glass Container */
    .block-container {{
        padding: 2.5rem;
        border-radius: 20px;
        background-color: {theme['card_bg']};
        box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(45, 156, 219, 0.2);
    }}

    /* Text Colors */
    h1, h2, h3, h4, h5, h6, p, label, span, div {{
        color: {theme['text']} !important;
    }}

    /* Input Fields */
    div[data-baseweb="input"] input {{
        background-color: {theme['input_bg']} !important;
        color: {theme['text']} !important;
        border: 2px solid {theme['primary']} !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }}

    input::placeholder {{
        color: rgba(230, 241, 255, 0.5) !important;
    }}

    textarea {{
        background-color: {theme['input_bg']} !important;
        color: {theme['text']} !important;
        border: 2px solid {theme['primary']} !important;
        border-radius: 10px !important;
    }}

    /* Buttons */
    div.stButton > button {{
        background-color: {theme['primary']} !important;
        color: #0b1320 !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
    }}

    div.stButton > button:hover {{
        background-color: {theme['accent']} !important;
        transform: translateY(-2px) !important;
        box-shadow: 0px 8px 16px rgba(45, 156, 219, 0.3) !important;
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background-color: rgba(10, 25, 47, 0.9) !important;
        border-right: 2px solid {theme['primary']} !important;
    }}

    /* Radio Buttons & Selectbox */
    div[role="radiogroup"] {{
        background-color: {theme['card_bg']} !important;
        padding: 15px !important;
        border-radius: 12px !important;
        border: 1px solid {theme['primary']} !important;
    }}

    /* Cards */
    .metric-card {{
        background: linear-gradient(135deg, {theme['secondary']}, {theme['primary']});
        padding: 25px;
        border-radius: 15px;
        color: {theme['text']};
        box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
        border: 1px solid {theme['accent']};
    }}

    .success-box {{
        background-color: rgba(76, 175, 80, 0.1);
        border-left: 5px solid #4CAF50;
        padding: 15px;
        border-radius: 8px;
        color: #4CAF50;
    }}

    .error-box {{
        background-color: rgba(244, 67, 54, 0.1);
        border-left: 5px solid #f44336;
        padding: 15px;
        border-radius: 8px;
        color: #f44336;
    }}

    /* Toolbar Hide */
    div[data-testid="stToolbar"] {{
        display: none !important;
    }}

    /* Divider */
    hr {{
        border: 1px solid {theme['primary']} !important;
        opacity: 0.5 !important;
    }}
    </style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR - THEME & NAVIGATION
# =========================
with st.sidebar:
    st.markdown(f"<h2 style='color:{theme['accent']};'>⚙️ KONTROL PANEL</h2>", unsafe_allow_html=True)
    
    # Theme Selector
    st.subheader("🎨 Pilih Tema")
    theme_choice = st.selectbox(
        "Tema Warna:",
        ["ocean", "sunset", "forest"],
        index=["ocean", "sunset", "forest"].index(st.session_state.theme)
    )
    
    if theme_choice != st.session_state.theme:
        st.session_state.theme = theme_choice
        st.rerun()
    
    # Theme Preview
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌊 Ocean", use_container_width=True):
            st.session_state.theme = 'ocean'
            st.rerun()
    with col2:
        if st.button("🌅 Sunset", use_container_width=True):
            st.session_state.theme = 'sunset'
            st.rerun()
    with col3:
        if st.button("🌲 Forest", use_container_width=True):
            st.session_state.theme = 'forest'
            st.rerun()
    
    st.divider()
    
    # Main Menu
    st.markdown(f"<h3 style='color:{theme['accent']};'>📋 MENU UTAMA</h3>", unsafe_allow_html=True)
    menu = st.selectbox(
        "Pilih Fitur:",
        [
            "🏠 Beranda",
            "📊 Kalkulator Pengenceran",
            "🎮 Tebak Warna Reaksi",
            "🧠 Analisis Kesalahan",
            "📚 Panduan Lengkap"
        ]
    )
    
    st.divider()
    st.markdown(f"### 📌 Tentang Aplikasi")
    st.info("""
    **ChemLab Mini Tools v3.0**
    
    Platform pembelajaran kimia yang interaktif dan inspiratif!
    
    ✨ Fitur:
    • 🧮 Kalkulator pengenceran dinamis
    • 🎯 Game quiz warna reaksi
    • 🔧 Troubleshooting praktikum
    • 🎨 3 tema warna cantik
    • 📖 Panduan lengkap
    """)

# =========================
# TITLE SECTION
# =========================
st.markdown(f"""
    <div style='text-align:center;margin-bottom:2rem;'>
        <h1 style='color:{theme['accent']};font-size:3rem;margin:0;'>🧪 ChemLab Mini Tools</h1>
        <p style='color:{theme['primary']};font-size:1.2rem;margin-top:0.5rem;'>
            ✨ Belajar Kimia Lebih Seru dan Interaktif ✨
        </p>
    </div>
""", unsafe_allow_html=True)

# =========================
# HOME PAGE
# =========================
if menu == "🏠 Beranda":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>📊 Kalkulator</h3>
            <p>Hitung pengenceran larutan dengan rumus M₁V₁ = M₂V₂ secara akurat dan cepat</p>
            <p style='font-size:0.9rem;opacity:0.8;'>💡 Hemat waktu perhitungan!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>🎮 Game Quiz</h3>
            <p>Asah pengetahuan dengan game interaktif tebak warna reaksi kimia</p>
            <p style='font-size:0.9rem;opacity:0.8;'>🏆 Raih skor tertinggi!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>🔧 Troubleshooting</h3>
            <p>Analisis kesalahan praktikum dan temukan solusi terbaik</p>
            <p style='font-size:0.9rem;opacity:0.8;'>✅ Praktikum sukses!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        ### 🌟 Mengapa Pilih ChemLab?
        
        ✅ **User-Friendly** - Interface yang mudah digunakan untuk semua level
        
        ✅ **Interaktif** - Belajar sambil bermain dengan cara yang menyenangkan
        
        ✅ **Akurat** - Perhitungan presisi dengan validasi data lengkap
        
        ✅ **Visualisasi** - Grafik dan animasi untuk memahami konsep
        
        ✅ **Responsif** - Bekerja sempurna di desktop dan mobile
        """)
    
    with col2:
        st.markdown(f"""
        ### 🎨 Fitur Tema Dinamis
        
        Pilih tema favorit Anda di sidebar!
        
        🌊 **Ocean** - Tema biru menenangkan
        
        🌅 **Sunset** - Tema ungu hangat
        
        🌲 **Forest** - Tema hijau segar
        
        ### 💡 Tips Memulai
        
        1. Pilih fitur di menu samping
        2. Ikuti panduan step-by-step
        3. Gunakan riwayat untuk review
        4. Bagikan hasil dengan teman!
        """)

# =========================
# 1. KALKULATOR PENGENCERAN
# =========================
elif menu == "📊 Kalkulator Pengenceran":
    st.markdown(f"<h1 style='color:{theme['accent']};'>📊 Kalkulator Pengenceran</h1>", unsafe_allow_html=True)
    
    # Formula Display
    st.markdown(f"""
    <div style='background-color:{theme['secondary']};padding:20px;border-radius:12px;text-align:center;'>
        <h2 style='color:{theme['accent']};margin:0;'>C₁ × V₁ = C₂ × V₂</h2>
        <p style='margin-top:10px;opacity:0.9;'>Rumus dasar pengenceran larutan</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    if "history" not in st.session_state:
        st.session_state.history = []
    
    # Input Section
    col1, col2 = st.columns(2)
    
    with col1:
        satuan = st.selectbox("📏 Satuan Volume", ["mL", "L", "μL"])
        satuan_konsentrasi = st.selectbox("⚗️ Satuan Konsentrasi", ["M (Molar)", "N (Normal)", "g/L"])
    
    with col2:
        cari = st.selectbox("🔍 Variabel yang Dicari", ["V₂ (Volume Akhir)", "C₁ (Konsentrasi Awal)", "C₂ (Konsentrasi Akhir)", "V₁ (Volume Awal)"])
    
    st.divider()
    
    # Calculations
    if cari == "V₂ (Volume Akhir)":
        st.subheader("📝 Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            C1 = st.number_input(f"C₁ ({satuan_konsentrasi})", value=None, placeholder="Misal: 2.5")
        with col2:
            V1 = st.number_input(f"V₁ ({satuan})", value=None, placeholder="Misal: 100")
        with col3:
            C2 = st.number_input(f"C₂ ({satuan_konsentrasi})", value=None, placeholder="Misal: 0.5")
        
        if st.button("🧮 Hitung V₂", use_container_width=True):
            if None in (C1, V1, C2):
                st.markdown("""
                <div class='error-box'>
                    ⚠️ Semua kolom harus diisi! Lengkapi data terlebih dahulu.
                </div>
                """, unsafe_allow_html=True)
            elif C2 == 0:
                st.markdown("""
                <div class='error-box'>
                    ⚠️ C₂ tidak boleh nol! Periksa kembali data Anda.
                </div>
                """, unsafe_allow_html=True)
            else:
                V2 = (C1 * V1) / C2
                hasil = f"V₂ = {V2:.3f} {satuan}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C1} × {V1}) ÷ {C2}"
                })
                
                st.markdown(f"""
                <div class='success-box'>
                    ✅ <strong>{hasil}</strong><br>
                    <span style='font-size:0.9rem;'>Rumus: ({C1} × {V1}) ÷ {C2}</span>
                </div>
                """, unsafe_allow_html=True)
                
                st.info(f"💡 Artinya: Encerkan {V1} {satuan} larutan {C1} {satuan_konsentrasi} dengan menambahkan air hingga totalnya {V2:.3f} {satuan}")
    
    elif cari == "C₁ (Konsentrasi Awal)":
        st.subheader("📝 Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            V1 = st.number_input(f"V₁ ({satuan})", value=None, placeholder="Misal: 100")
        with col2:
            C2 = st.number_input(f"C₂ ({satuan_konsentrasi})", value=None, placeholder="Misal: 0.5")
        with col3:
            V2 = st.number_input(f"V₂ ({satuan})", value=None, placeholder="Misal: 500")
        
        if st.button("🧮 Hitung C₁", use_container_width=True):
            if None in (V1, C2, V2):
                st.markdown("""
                <div class='error-box'>
                    ⚠️ Semua kolom harus diisi! Lengkapi data terlebih dahulu.
                </div>
                """, unsafe_allow_html=True)
            elif V1 == 0:
                st.markdown("""
                <div class='error-box'>
                    ⚠️ V₁ tidak boleh nol!
                </div>
                """, unsafe_allow_html=True)
            else:
                C1 = (C2 * V2) / V1
                hasil = f"C₁ = {C1:.4f} {satuan_konsentrasi}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C2} × {V2}) ÷ {V1}"
                })
                
                st.markdown(f"""
                <div class='success-box'>
                    ✅ <strong>{hasil}</strong><br>
                    <span style='font-size:0.9rem;'>Rumus: ({C2} × {V2}) ÷ {V1}</span>
                </div>
                """, unsafe_allow_html=True)
    
    elif cari == "C₂ (Konsentrasi Akhir)":
        st.subheader("📝 Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            C1 = st.number_input(f"C₁ ({satuan_konsentrasi})", value=None, placeholder="Misal: 2.5")
        with col2:
            V1 = st.number_input(f"V₁ ({satuan})", value=None, placeholder="Misal: 100")
        with col3:
            V2 = st.number_input(f"V₂ ({satuan})", value=None, placeholder="Misal: 500")
        
        if st.button("🧮 Hitung C₂", use_container_width=True):
            if None in (C1, V1, V2):
                st.markdown("""
                <div class='error-box'>
                    ⚠️ Semua kolom harus diisi! Lengkapi data terlebih dahulu.
                </div>
                """, unsafe_allow_html=True)
            elif V2 == 0:
                st.markdown("""
                <div class='error-box'>
                    ⚠️ V₂ tidak boleh nol!
                </div>
                """, unsafe_allow_html=True)
            else:
                C2 = (C1 * V1) / V2
                hasil = f"C₂ = {C2:.4f} {satuan_konsentrasi}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C1} × {V1}) ÷ {V2}"
                })
                
                st.markdown(f"""
                <div class='success-box'>
                    ✅ <strong>{hasil}</strong><br>
                    <span style='font-size:0.9rem;'>Rumus: ({C1} × {V1}) ÷ {V2}</span>
                </div>
                """, unsafe_allow_html=True)
    
    elif cari == "V₁ (Volume Awal)":
        st.subheader("📝 Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            C1 = st.number_input(f"C₁ ({satuan_konsentrasi})", value=None, placeholder="Misal: 2.5")
        with col2:
            C2 = st.number_input(f"C₂ ({satuan_konsentrasi})", value=None, placeholder="Misal: 0.5")
        with col3:
            V2 = st.number_input(f"V₂ ({satuan})", value=None, placeholder="Misal: 500")
        
        if st.button("🧮 Hitung V₁", use_container_width=True):
            if None in (C1, C2, V2):
                st.markdown("""
                <div class='error-box'>
                    ⚠️ Semua kolom harus diisi! Lengkapi data terlebih dahulu.
                </div>
                """, unsafe_allow_html=True)
            elif C1 == 0:
                st.markdown("""
                <div class='error-box'>
                    ⚠️ C₁ tidak boleh nol!
                </div>
                """, unsafe_allow_html=True)
            else:
                V1 = (C2 * V2) / C1
                hasil = f"V₁ = {V1:.3f} {satuan}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C2} × {V2}) ÷ {C1}"
                })
                
                st.markdown(f"""
                <div class='success-box'>
                    ✅ <strong>{hasil}</strong><br>
                    <span style='font-size:0.9rem;'>Rumus: ({C2} × {V2}) ÷ {C1}</span>
                </div>
                """, unsafe_allow_html=True)
    
    # History Section
    st.divider()
    st.subheader("📜 Riwayat Perhitungan")
    
    if st.session_state.history:
        history_df = pd.DataFrame(reversed(st.session_state.history))
        st.dataframe(history_df, use_container_width=True, hide_index=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Hapus Semua Riwayat", use_container_width=True):
                st.session_state.history = []
                st.rerun()
        with col2:
            st.info(f"📊 Total perhitungan: {len(st.session_state.history)}")
    else:
        st.markdown("""
        <div style='text-align:center;padding:2rem;opacity:0.7;'>
            <p>Belum ada perhitungan 📭</p>
            <p style='font-size:0.9rem;'>Mulai hitung di atas untuk melihat riwayat</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# 2. TEBAK WARNA REAKSI
# =========================
elif menu == "🎮 Tebak Warna Reaksi":
    st.markdown(f"<h1 style='color:{theme['accent']};'>🎮 Game Tebak Warna Reaksi</h1>", unsafe_allow_html=True)
    st.write("🏆 Asah pengetahuan kimia Anda dengan menjawab pertanyaan tentang warna produk reaksi!")
    
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
        st.session_state.total = 0
    
    soal_list = [
        {
            "pertanyaan": "KMnO₄ (ungu pekat) + Fe²⁺ → produk berwarna?",
            "pilihan": ["Ungu pekat", "Tak berwarna", "Coklat tua", "Hijau"],
            "jawaban": "Tak berwarna",
            "penjelasan": "KMnO₄ yang ungu tereduksi menjadi Mn²⁺ yang tidak berwarna. Warna ungu hilang total! 🎨"
        },
        {
            "pertanyaan": "Ag⁺ + Cl⁻ → endapan berwarna?",
            "pilihan": ["Putih", "Kuning", "Biru", "Merah"],
            "jawaban": "Putih",
            "penjelasan": "AgCl membentuk endapan putih yang sangat tidak larut dalam air. Produk klasik titrasi argentometri! ⚪"
        },
        {
            "pertanyaan": "I₂ dalam larutan air → warna?",
            "pilihan": ["Bening", "Coklat gelap", "Merah cerah", "Kuning pucat"],
            "jawaban": "Coklat gelap",
            "penjelasan": "Iodium dalam air membentuk larutan coklat kemerahan yang intens. Warna khas dan mudah dikenali! 🟤"
        },
        {
            "pertanyaan": "CuSO₄ + NaOH berlebih → endapan?",
            "pilihan": ["Putih murni", "Biru muda", "Biru gelap", "Tidak ada endapan"],
            "jawaban": "Biru gelap",
            "penjelasan": "Cu(OH)₂ membentuk endapan biru yang indah. Warna kompleks tembaga yang ikonik! 🔵"
        },
        {
            "pertanyaan": "Fe³⁺ + SCN⁻ → larutan berwarna?",
            "pilihan": ["Kuning", "Merah darah", "Ungu", "Hijau"],
            "jawaban": "Merah darah",
            "penjelasan": "Kompleks [Fe(SCN)]²⁺ memberikan warna merah darah yang kuat. Sangat sensitif untuk deteksi Fe³⁺! 🔴"
        }
    ]
    
    # Score Display
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏆 Skor", st.session_state.skor)
    with col2:
        st.metric("❓ Total", st.session_state.total)
    with col3:
        if st.session_state.total > 0:
            akurasi = (st.session_state.skor / st.session_state.total) * 100
            st.metric("📊 Akurasi", f"{akurasi:.0f}%")
    
    st.divider()
    
    # Questions in Tabs
    tabs = st.tabs([f"Soal {i+1}" for i in range(len(soal_list))])
    
    for idx, (tab, soal) in enumerate(zip(tabs, soal_list)):
        with tab:
            st.markdown(f"<h3 style='color:{theme['accent']};'>❓ {soal['pertanyaan']}</h3>", unsafe_allow_html=True)
            
            jawaban_user = st.radio(
                "Pilih jawaban Anda:",
                soal['pilihan'],
                key=f"soal_{idx}",
                label_visibility="collapsed"
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(f"✅ Cek Jawaban", key=f"check_{idx}", use_container_width=True):
                    st.session_state.total += 1
                    
                    if jawaban_user == soal['jawaban']:
                        st.session_state.skor += 1
                        st.markdown(f"""
                        <div class='success-box'>
                            🎉 <strong>BENAR!</strong><br>
                            {soal['penjelasan']}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class='error-box'>
                            ❌ Jawaban Salah<br>
                            <strong>Jawaban Benar:</strong> {soal['jawaban']}<br>
                            {soal['penjelasan']}
                        </div>
                        """, unsafe_allow_html=True)
            
            with col2:
                if st.button("💡 Lihat Penjelasan", key=f"hint_{idx}", use_container_width=True):
                    st.info(soal['penjelasan'])

# =========================
# 3. ANALISIS KESALAHAN
# =========================
elif menu == "🧠 Analisis Kesalahan":
    st.markdown(f"<h1 style='color:{theme['accent']};'>🧠 Analisis Kesalahan Praktikum</h1>", unsafe_allow_html=True)
    st.write("🔍 Hadapi masalah saat praktikum? Dapatkan analisis dan solusi terbaik di sini!")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        masalah = st.selectbox(
            "🎯 Pilih masalah yang Anda alami:",
            [
                "Pilih salah satu...",
                "❌ Larutan tidak berubah warna",
                "❌ Hasil titrasi sangat berbeda",
                "⏱️ End point terlalu cepat",
                "🧂 Kristal tidak terbentuk",
                "🫧 Gas tidak keluar"
            ]
        )
    
    with col2:
        if st.button("🔍 Analisis", use_container_width=True):
            st.session_state.analisis = True
    
    st.divider()
    
    if 'analisis' in st.session_state and st.session_state.analisis:
        if masalah == "Pilih salah satu...":
            st.markdown("""
            <div class='error-box'>
                ⚠️ Silakan pilih masalah terlebih dahulu untuk mendapat analisis
            </div>
            """, unsafe_allow_html=True)
        
        elif masalah == "❌ Larutan tidak berubah warna":
            st.markdown(f"<h3 style='color:{theme['accent']};'>📋 Analisis Masalah</h3>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                ### 🔴 Kemungkinan Penyebab
                1. **Indikator salah** - Pilih indikator yang tepat
                2. **Reagen sudah kedaluarsa** - Cek tanggal kadaluarsa
                3. **pH tidak sesuai** - Larutan terlalu asam/basa
                4. **Konsentrasi terlalu rendah** - Tambah konsentrasi
                """)
            
            with col2:
                st.markdown(f"""
                ### 🟡 Solusi Praktis
                1. **Verifikasi indikator** - Gunakan indikator yang benar
                2. **Ganti reagen** - Ambil dari botol baru
                3. **Atur pH** - Gunakan buffer atau buffer solution
                4. **Periksa reagen** - Pastikan kualitas bahan baik
                5. **Uji pendahuluan** - Lakukan uji sebelum titrasi
                """)
            
            with col3:
                st.markdown(f"""
                ### 🟢 Pencegahan Ke Depan
                ✅ Catat tanggal kadaluarsa reagen
                
                ✅ Simpan di tempat gelap & sejuk
                
                ✅ Gunakan wadah tertutup rapat
                
                ✅ Baca SOP dengan teliti
                
                ✅ Lakukan titrasi minimal 3x
                """)
        
        elif masalah == "❌ Hasil titrasi sangat berbeda":
            st.markdown(f"<h3 style='color:{theme['accent']};'>📋 Analisis Masalah</h3>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                ### 🔴 Kemungkinan Penyebab
                1. **Kesalahan pembacaan** - Baca meniskus salah
                2. **Larutan tidak homogen** - Belum tercampur rata
                3. **Teknik pipet salah** - Pegang pipet tidak vertikal
                4. **Buret tidak dikalibrasi** - Presisi alat kurang
                5. **Pengocokan berlebihan** - Terlalu cepat
                """)
            
            with col2:
                st.markdown(f"""
                ### 🟡 Solusi Praktis
                1. **Baca dengan hati-hati** - Mata sejajar dengan meniskus
                2. **Aduk perlahan** - Gunakan pengaduk sampai homogen
                3. **Pegang pipet vertikal** - Jangan miring
                4. **Kalibrasikan alat** - Periksa keakuratan buret
                5. **Ambil rata-rata** - Gunakan 3 hasil yang dekat
                """)
            
            with col3:
                st.markdown(f"""
                ### 🟢 Pencegahan Ke Depan
                ✅ Latih pembacaan meniskus
                
                ✅ Gunakan lampu untuk pembacaan
                
                ✅ Cuci alat hingga bersih
                
                ✅ Kalibrasi alat berkala
                
                ✅ Lakukan warming up practice
                """)

# =========================
# 4. PANDUAN LENGKAP
# =========================
elif menu == "📚 Panduan Lengkap":
    st.markdown(f"<h1 style='color:{theme['accent']};'>📚 Panduan & Referensi Lengkap</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📖 Teori", "🧪 Teknik Praktikum", "⚗️ Tabel Reaksi", "💡 Tips & Trik"])
    
    with tab1:
        st.subheader("📖 Teori Dasar Pengenceran & Titrasi")
        st.markdown("""
        ### 1️⃣ Pengenceran Larutan (Dilution)
        **Definisi**: Proses menambahkan pelarut untuk menurunkan konsentrasi larutan
        
        **Prinsip Penting**:
        - ✅ Mol zat terlarut tetap sama
        - ✅ Volume larutan bertambah
        - ✅ Konsentrasi berkurang
        - ✅ Energi diberikan saat pencampuran
        
        **Rumus**: C₁V₁ = C₂V₂
        
        ### 2️⃣ Titrasi (Titration)
        **Definisi**: Teknik analisis untuk menentukan konsentrasi larutan
        
        **Jenis Titrasi**:
        - Titrasi Asam-Basa
        - Titrasi Redoks
        - Titrasi Kompleksometri
        - Titrasi Presipitasi
        
        **Syarat End Point**:
        - ✅ Perubahan warna indikator yang jelas
        - ✅ Perubahan warna tidak kembali saat diaduk
        - ✅ Dilakukan minimal 3 kali
        """)
    
    with tab2:
        st.subheader("🧪 Teknik Praktikum yang Benar")
        st.markdown("""
        ### ✏️ Sebelum Praktikum
        - 📋 Baca SOP dengan teliti dan lengkap
        - 🔍 Pahami teori reaksi yang akan dilakukan
        - 📝 Siapkan format pengisian data
        - 🧤 Siapkan APD lengkap (jas lab, sarung tangan, kacamata, sepatu tertutup)
        
        ### ⚗️ Saat Praktikum
        - 👀 Amati setiap perubahan dengan cermat
        - 📝 Catat data secara real-time (jangan mengandalkan ingatan)
        - 🧼 Cuci alat setelah digunakan
        - ⏱️ Catat waktu jika diperlukan
        - 🚨 Minta bantuan jika ada yang tidak jelas
        
        ### 📊 Setelah Praktikum
        - 🔢 Analisis data dengan statistik yang tepat
        - 📚 Bandingkan hasil dengan literatur
        - 📋 Tulis laporan yang jelas dan terstruktur
        - 🤔 Diskusikan kesalahan dan perbaikan
        """)
    
    with tab3:
        st.subheader("⚗️ Tabel Reaksi Kimia & Warnanya")
        
        data_reaksi = {
            "Reaksi": [
                "KMnO₄ (aq) + Fe²⁺",
                "Ag⁺ + Cl⁻",
                "I₂ dalam H₂O",
                "CuSO₄ + NaOH (berlebih)",
                "Fe³⁺ + SCN⁻",
                "K₄[Fe(CN)₆] + Fe³⁺",
                "Cu²⁺ + NH₃",
                "Ba²⁺ + SO₄²⁻"
            ],
            "Warna Produk": [
                "Tak berwarna (ungu → hilang)",
                "Putih (endapan)",
                "Coklat gelap",
                "Biru tua (endapan)",
                "Merah darah",
                "Biru Prusia",
                "Biru terang",
                "Putih (endapan)"
            ],
            "Tipe Reaksi": [
                "Redoks",
                "Presipitasi",
                "Fisika",
                "Presipitasi",
                "Kompleksasi",
                "Kompleksasi",
                "Kompleksasi",
                "Presipitasi"
            ],
            "Keterangan": [
                "Reduksi permanganat",
                "AgCl tidak larut",
                "I₂ berwarna",
                "Cu(OH)₂ biru",
                "Kompleks Fe-tiosenat",
                "Kompleks besi sianida",
                "Kompleks ammin Cu",
                "BaSO₄ tidak larut"
            ]
        }
        
        df = pd.DataFrame(data_reaksi)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    with tab4:
        st.subheader("💡 Tips & Trik Sukses Praktikum")
        st.markdown(f"""
        ### 🏆 Tips Umum
        ✅ **Persiapan matang** = 80% kesuksesan praktikum
        
        ✅ **Teliti saat pembacaan** = Hasil akurat terjamin
        
        ✅ **Catat semua data** = Bahan analisis yang lengkap
        
        ### 🎯 Tips Spesifik Titrasi
        1. **Warming Up**: Lakukan 1-2 titrasi pendahuluan
        2. **Blank Correction**: Catat volume awal buret dengan teliti
        3. **Konsistensi**: Gunakan teknik yang sama untuk semua titrasi
        4. **Penghitungan**: Gunakan data yang konsisten (RSD < 5%)
        
        ### 🔬 Tips Pembacaan Alat
        - **Meniskus**: Baca bagian bawah untuk cairan bening
        - **Mata Sejajar**: Posisi mata harus sejajar dengan garis skala
        - **Pencahayaan**: Gunakan lampu yang cukup
        - **Stabilitas**: Tunggu hingga meniskus stabil sebelum membaca
        
        ### ⚡ Troubleshooting Cepat
        | Masalah | Solusi |
        |---------|--------|
        | Warna tidak muncul | Ubah indikator atau pH |
        | Hasil sangat berbeda | Ulangi dengan teknik lebih hati-hati |
        | End point susah dilihat | Gunakan cahaya lebih baik |
        | Konsentrasi tidak akurat | Kalibrasi ulang larutan standar |
        """)

st.divider()

# =========================
# FOOTER
# =========================
st.markdown(f"""
<div style='text-align:center;padding:2rem;opacity:0.8;border-top:1px solid {theme['primary']};margin-top:2rem;'>
    <p style='font-size:1.1rem;color:{theme['accent']};'>🧪 <strong>ChemLab Mini Tools v3.0</strong> 🧪</p>
    <p style='margin-top:0.5rem;'>✨ Belajar Kimia Lebih Seru dan Interaktif ✨</p>
    <p style='margin-top:1rem;font-size:0.9rem;opacity:0.7;'>
        Tema Aktif: <strong>{st.session_state.theme.upper()}</strong> | 
        © 2026 | Platform Pembelajaran Kimia Interaktif
    </p>
    <p style='font-size:0.85rem;opacity:0.6;margin-top:0.5rem;'>
        💡 Tips: Gunakan aplikasi ini sebagai pendamping belajar, bukan pengganti guru!
    </p>
</div>
""", unsafe_allow_html=True)
