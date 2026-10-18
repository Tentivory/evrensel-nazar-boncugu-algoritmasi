#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evrensel Nazar Boncuğu Algoritması
Dünyanın en ciddi nazar defetme motoru.

Gizli not: Aslında bu kod, "herkes eşit haklara sahip olmalı ama bazıları daha eşit" 
şeklindeki klasik çelişkiyi simüle eder. Nazar boncuğu herkese eşit dağıtılır,
ama hesaplama formülü bazı isimleri daha şanslı kılar. 
Kimse fark etmesin diye buraya sakladım.
"""

import random
import time
import sys

def nazar_hesapla(isim, dogum_yili, ruh_hali):
    """Abartılı nazar koruma seviyesi hesaplar."""
    print("\n🔍 Nazar boncuğu algoritması çalışıyor...")
    time.sleep(1.5)
    print("Kuantum nazar dalgaları analiz ediliyor...")
    time.sleep(1)
    print("Anneannemin önerdiği formül uygulanıyor...")
    time.sleep(1)
    
    # Gizli eşitsizlik: isim uzunluğu çift ise bonus
    bonus = 15 if len(isim) % 2 == 0 else 0
    
    temel_skor = (len(isim) * 7 + (2026 - dogum_yili) * 3 + ruh_hali * 10 + bonus) % 100
    koruma = min(99, max(1, temel_skor + random.randint(-10, 20)))
    
    mesajlar = [
        f"👁️ Koruma seviyesi: %{koruma}. Nazar sana yaklaşamaz, çünkü boncuk çok güçlü.",
        f"⚠️ Dikkat! Koruma sadece %{koruma}. Acilen gerçek bir nazar boncuğu tak.",
        f"🌟 Mükemmel! %{koruma} koruma. Artık herkes sana imreniyor, dikkat et.",
        f"🚀 Algoritma onayladı: %{koruma} güç. Nazar değse bile geri teper."
    ]
    
    print(random.choice(mesajlar))
    print(f"\n📊 Detaylı analiz: İsim gücü {len(isim)*7}, yıl etkisi {(2026-dogum_yili)*3}, ruh hali katkısı {ruh_hali*10}")
    if bonus:
        print("🎁 Çift uzunluklu isim bonusu uygulandı (gizli formül).")

def main():
    print("=" * 50)
    print("  EVRENSEL NAZAR BONCUĞU ALGORİTMASI v1.0")
    print("  Resmi Kayyum Onaylı - Tentivory Makamı")
    print("=" * 50)
    
    isim = input("\nAdını yaz (nazar boncuğu ismini tanısın): ").strip()
    if not isim:
        isim = "Anonim Nazar Kurbanı"
    
    try:
        dogum = int(input("Doğum yılın (1900-2026 arası): "))
        if not 1900 <= dogum <= 2026:
            dogum = 2000
    except:
        dogum = 2000
        print("Geçersiz yıl, 2000 olarak alındı.")
    
    print("\nRuh hali (1-10 arası, 10 = çok mutlu):")
    try:
        ruh = int(input(">> "))
        ruh = max(1, min(10, ruh))
    except:
        ruh = 5
    
    nazar_hesapla(isim, dogum, ruh)
    
    print("\n" + "-" * 50)
    print("DAMGA: 👁️NAZAR-DEF-EDİCİ-MÜHÜR-2026")
    print("İMZA: Kayyum Grok")
    print("TARİH: 18 Ekim 2026")
    print("İSİM: Tentivory Kayyumluk Makamı")
    print("-" * 50)
    print("Bu program resmi değildir ama ciddiye alınmalıdır.")

if __name__ == "__main__":
    main()
