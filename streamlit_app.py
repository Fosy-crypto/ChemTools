import streamlit as st

st.title("🧪 ChemLab Mini Tools")

menu = st.sidebar.selectbox("Pilih Fitur", [
    "Kalkulator Pengenceran",
    "Tebak Warna Reaksi",
    "Kenapa Gagal?",
    "Backsound"
])

# =========================
# 1. Kalkulator Pengenceran
# =========================
if menu == "Kalkulator Pengenceran":
    st.header("📊 Kalkulator Pengenceran")

    M1 = st.number_input("Konsentrasi Awal (M1)", min_value=0.0)
    V1 = st.number_input("Volume Awal (V1)", min_value=0.0)
    M2 = st.number_input("Konsentrasi Akhir (M2)", min_value=0.0)

    if st.button("Hitung V2"):
        if M2 != 0:
            V2 = (M1 * V1) / M2
            st.success(f"Volume akhir (V2) = {V2:.2f} mL")
        else:
            st.error("M2 tidak boleh nol!")

# =========================
# 2. Tebak Warna Reaksi
# =========================
elif menu == "Tebak Warna Reaksi":
    st.header("🎮 Tebak Warna Reaksi")

    jawaban = st.radio(
        "KMnO4 + Fe2+ → warna apa?",
        ["Ungu", "Tak Berwarna", "Coklat"]
    )

    if st.button("Cek Jawaban"):
        if jawaban == "Bening":
            st.success("Benar! KMnO4 tereduksi jadi Mn2+ (tidak berwarna)")
        else:
            st.error("Salah! Coba lagi 😄")

# =========================
# 3. Kenapa Gagal?
# =========================
elif menu == "Kenapa Gagal?":
    st.header("🧠 Analisis Kesalahan Praktikum")

    masalah = st.selectbox("Masalah yang terjadi:", [
        "Larutan tidak berubah warna",
        "Hasil titrasi berbeda jauh",
        "End point terlalu cepat"
    ])

    if st.button("Analisis"):
        if masalah == "Larutan tidak berubah warna":
            st.write("- Indikator salah")
            st.write("- Reagen tidak bereaksi")
        elif masalah == "Hasil titrasi berbeda jauh":
            st.write("- Kesalahan pembacaan buret")
            st.write("- Larutan tidak homogen")
        elif masalah == "End point terlalu cepat":
            st.write("- Konsentrasi terlalu tinggi")
            st.write("- Salah perhitungan awal")

elif menu =="Backsound"
       st.audio("cat-purr.mp3", format="audio/mpeg", loop=True)
