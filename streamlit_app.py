import streamlit as st

st.title("🧪 ChemLab Mini Tools")

menu = st.sidebar.selectbox("Pilih Fitur", [
    "Kalkulator Pengenceran",
    "Tebak Warna Reaksi",
    "Kenapa Gagal?"
])

# =========================
# 1. Kalkulator Pengenceran
# =========================
if menu == "Kalkulator Pengenceran":
    st.header("📊 Kalkulator Pengenceran")

    cari = st.selectbox(
        "Pilih variabel yang ingin dicari",
        ["V2", "C1", "C2", "V1"]
    )

    if cari == "V2":
        C1 = st.number_input("Konsentrasi Awal (C1)", min_value=0.0)
        V1 = st.number_input("Volume Awal (V1)", min_value=0.0)
        C2 = st.number_input("Konsentrasi Akhir (C2)", min_value=0.0)

        if st.button("Hitung V2"):
            if C2 != 0:
                V2 = (C1 * V1) / C2
                st.success(f"Volume Akhir (V2) = {V2:.2f} mL")
            else:
                st.error("C2 tidak boleh nol!")

    elif cari == "C1":
        V1 = st.number_input("Volume Awal (V1)", min_value=0.0)
        C2 = st.number_input("Konsentrasi Akhir (C2)", min_value=0.0)
        V2 = st.number_input("Volume Akhir (V2)", min_value=0.0)

        if st.button("Hitung C1"):
            if V1 != 0:
                C1 = (C2 * V2) / V1
                st.success(f"Konsentrasi Awal (C1) = {C1:.4f}")
            else:
                st.error("V1 tidak boleh nol!")

    elif cari == "C2":
        C1 = st.number_input("Konsentrasi Awal (C1)", min_value=0.0)
        V1 = st.number_input("Volume Awal (V1)", min_value=0.0)
        V2 = st.number_input("Volume Akhir (V2)", min_value=0.0)

        if st.button("Hitung C2"):
            if V2 != 0:
                C2 = (C1 * V1) / V2
                st.success(f"Konsentrasi Akhir (C2) = {C2:.4f}")
            else:
                st.error("V2 tidak boleh nol!")

    elif cari == "V1":
        C1 = st.number_input("Konsentrasi Awal (C1)", min_value=0.0)
        C2 = st.number_input("Konsentrasi Akhir (C2)", min_value=0.0)
        V2 = st.number_input("Volume Akhir (V2)", min_value=0.0)

        if st.button("Hitung V1"):
            if C1 != 0:
                V1 = (C2 * V2) / C1
                st.success(f"Volume Awal (V1) = {V1:.2f} mL")
            else:
                st.error("C1 tidak boleh nol!")
   
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
        if jawaban == "Tak Berwarna":
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

