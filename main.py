import random

def main():
    pemain = input("Kertas (k), Gunting (g), Batu (b)?")
    musuh = random.choice(['k', 'g', 'b'])

    if pemain == musuh:
        return 'Seri!'

    if menang(pemain, musuh):
        return 'Selamat, kamu menang!'

    return 'Maaf, kamu kalah!'

def menang(pemain, musuh):
    # return true if player wins
    # r > s, s > p, p > r
    if (pemain == 'b' and musuh == 'g') or (pemain == 'g' and musuh == 'k') \
        or (pemain == 'k' and musuh == 'b'):
        return True

print(main())