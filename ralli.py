import pygame
import random

# Mängu alustamine
pygame.init()

# Ekraani suurus
ekraani_laius = 640
ekraani_korgus = 480

# Loome ekraani objekti
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))

# Taustapildi failinimi
bg_failinimi = "bg_rally.jpg"

# Punase auto failinimi ja alguskoht
punane_auto_failinimi = "f1_red.png"
punane_auto_suurus = 100
punane_auto_x = (ekraani_laius - punane_auto_suurus) // 2
punane_auto_y = ekraani_korgus - punane_auto_suurus - 20

# Sinise auto failinimi ja suurus
sinine_auto_failinimi = "f1_blue.png"
sinine_auto_suurus = 100

# Siniste autode alguspositsioonid
sinised_autod = [
    ((ekraani_laius // 3.2) - (sinine_auto_suurus // 2), -sinine_auto_suurus - 80),  # Vasakpoolne auto
    ((ekraani_laius // 3 * 2.05) - (sinine_auto_suurus // 2), -sinine_auto_suurus)   # Parem auto
]


# Siniste autode kiirus
sinine_auto_kiirus = 2

# Skoori muutuja
skoor = 0

# Mänguakna sulgemise funktsioon
def sulge_mang():
    pygame.quit()

# Teksti renderdamise funktsioon
def kuvage_skoor(ekraan, skoor):
    font = pygame.font.SysFont(None, 36)
    tekst = font.render("Skoor: " + str(skoor), True, (0, 0, 0))
    ekraan.blit(tekst, (10, 10))
    
pygame.display.set_caption("F1 ralli")


# Mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sulge_mang()
            running = False

    # Autode animatsiooni liikumine ja skoori värskendamine
    for i, (auto_x, auto_y) in enumerate(sinised_autod):
        auto_y += sinine_auto_kiirus
        if auto_y > ekraani_korgus:
            auto_y = -sinine_auto_suurus
            # Suurendame skoori, kui sinine auto jõuab alla
            skoor += 1
        sinised_autod[i] = (auto_x, auto_y)

       
    # Taustapildi kuvamine
    bg_pilt = pygame.image.load(bg_failinimi)
    bg_pilt = pygame.transform.scale(bg_pilt, (ekraani_laius, ekraani_korgus))
    ekraan.blit(bg_pilt, (0, 0))

    # Punase auto kuvamine
    punane_auto_pilt = pygame.image.load(punane_auto_failinimi)
    punane_auto_pilt = pygame.transform.scale(punane_auto_pilt, (punane_auto_suurus, punane_auto_suurus))
    ekraan.blit(punane_auto_pilt, (punane_auto_x, punane_auto_y))

    # Siniste autode kuvamine
    sinine_auto_pilt = pygame.image.load(sinine_auto_failinimi)
    sinine_auto_pilt = pygame.transform.scale(sinine_auto_pilt, (sinine_auto_suurus, sinine_auto_suurus))
    for auto_x, auto_y in sinised_autod:
        ekraan.blit(sinine_auto_pilt, (auto_x, auto_y))

    # Kuvame skoori
    kuvage_skoor(ekraan, skoor)

    # Ekraani värskendamine
    pygame.display.flip()

# Pygame'i sulgemine
pygame.quit()


