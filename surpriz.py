import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Sitenin sekme adı ve ikonu
st.set_page_config(page_title="Sürpriz Oyun", page_icon="❤️")

# Sitenin hafızası (Soruları sırayla sormak ve skoru tutmak için)
if 'adim' not in st.session_state:
    st.session_state.adim = 1
if 'skor' not in st.session_state:
    st.session_state.skor = 0

# BAŞLANGIÇ
st.title("Hoşgeldin minik kuşum ❤️")
st.write("Seninle bir oyun oynayacağız oyunumuz boyunca ingilizce karakter kullanmayı ve seni çok sevdiğimi unutma")
st.write("İlk sorumuzla başlayalım!")
st.write("---")

# --- 1. SORU ---
if st.session_state.adim == 1:
    cevap1 = st.text_input("İlk öpüsmemiz neredeydi?")
    if st.button("Cevapla"):
        if cevap1.lower() == "bahce":
            st.success("Tebrikler!")
            st.session_state.skor += 1
            st.session_state.adim = 2
            st.rerun()
        else:
            st.error("Cevabınız yanlış")

# --- 2. SORU ---
elif st.session_state.adim == 2:
    cevap2 = st.text_input("2. sorumuza geçelim bizim şarkımız nedir?")
    if st.button("Cevapla"):
        if cevap2.lower() == "ısıkları sondurseler bıle" or cevap2.lower() == "isiklari sondurseler bile":
            st.success("Tebrikler!")
            st.session_state.skor += 1
            st.session_state.adim = 3
            st.rerun()
        else:
            st.error("Noktasız harfler kullanarak tekrar deneyiniz")

# --- 3. SORU ---
elif st.session_state.adim == 3:
    cevap3 = st.text_input("Seninle bizim evde ne icerek lego yapmıştık?")
    if st.button("Cevapla"):
        if cevap3.lower() == "sarap":
            st.success("Tebrikler!")
            st.session_state.skor += 1
            st.session_state.adim = 4
            st.rerun()
        else:
            st.error("Tekrar deneyiniz")

# --- 4. SORU ---
elif st.session_state.adim == 4:
    st.write("**a:** ıslak kek   |   **b:** crumble   |   **c:** puding   |   **d:** sufle")
    cevap4 = st.text_input("Sana hangi tatlıyı yapmadım?")
    if st.button("Cevapla"):
        if cevap4.lower() == "c":
            st.success("Tebrikler!")
            st.session_state.skor += 1
            st.session_state.adim = 5
            st.rerun()
        else:
            st.error("Tekrar deneyiniz")

# --- 5. SORU ---
elif st.session_state.adim == 5:
    st.write("**A:** ozi seni çok özledim")
    st.write("**B:** sen beni sevmiyorsun")
    st.write("**C:** sevgim kalbime sığmıyor")
    st.write("**D:** beni neden aramıyorsun?")
    cevap5 = st.text_input("Seni bazen çok aşırı sevdiğimde arayıp ne diye ağlıyorum?")
    if st.button("Cevapla"):
        if cevap5.lower() == "c":
            st.success("Tebrikler!")
            st.session_state.skor += 1
            st.session_state.adim = 6
            st.rerun()
        else:
            st.error("Tekrar deneyiniz")

# --- FİNAL VE KALP GRAFİĞİ ---
elif st.session_state.adim == 6:
    st.balloons() # Sürpriz balonlar uçar
    st.write("---")
    st.subheader(f"🎉 Oyun bitti tebrik ederim minik kuşum, skorun: {st.session_state.skor} / 5")
    
    # Kalp Grafiği Çizimi
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(x, y, color='red', linewidth=3)
    ax.fill_between(x, y, color='red', alpha=0.5)
    ax.axis('off')

    ax.set_title(f"Tebrikler Minik Kuşum! Toplam Skorun: {st.session_state.skor}\nSeni Çok Seviyorum! ❤️", 
                 fontsize=14, color='darkred', fontweight='bold')

    st.pyplot(fig)
