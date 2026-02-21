import random

high_score = 0

while True:
    print("\n=== Game Tebak Angka ===")
    print("High Score:", high_score)
    print("Pilih tingkat kesulitan:")
    print("1. Mudah (1 - 10 | 5 kesempatan)")
    print("2. Sedang (1 - 50 | 7 kesempatan)")
    print("3. Sulit (1 - 100 | 10 kesempatan)")

    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1":
        max_angka = 10
        kesempatan = 5
    elif pilihan == "2":
        max_angka = 50
        kesempatan = 7
    elif pilihan == "3":
        max_angka = 100
        kesempatan = 10
    else:
        print("Pilihan tidak valid.")
        continue

    angka_rahasia = random.randint(1, max_angka)
    kesempatan_awal = kesempatan

    print(f"\nTebak angka dari 1 sampai {max_angka}\n")

    while kesempatan > 0:
        print("Sisa kesempatan:", kesempatan)
        tebakan = int(input("Masukkan tebakan: "))

        if tebakan < angka_rahasia:
            print("Terlalu kecil\n")
        elif tebakan > angka_rahasia:
            print("Terlalu besar\n")
        else:
            score = kesempatan * 10
            print("Benar! Kamu menang 🎉")
            print("Score kamu:", score)

            if score > high_score:
                high_score = score
                print("🔥 High Score baru!")

            break

        kesempatan -= 1

    if kesempatan == 0:
        print("Kamu kalah.")
        print("Angka yang benar:", angka_rahasia)

    main_lagi = input("\nMain lagi? (ya/tidak): ")
    if main_lagi.lower() != "ya":
        print("Game selesai.")
        break
