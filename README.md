# Snake Game – Kursinis OOP projektas

Tai klasikinis „Snake“ žaidimas, sukurtas naudojant **Python** ir **Pygame**. Projektas realizuoja visus keturis OOP principus, naudoja Singleton dizaino šabloną, turi rezultatų saugojimo sistemą bei vienetinius testus.

## Paleidimas

### 1. Įdiegti priklausomybes
Prieš paleidžiant, įsitikinkite, kad turite įdiegtą `pygame`:

```
pip install pygame
```

### 2. Paleisti žaidimą

```
python main.py
```

## Projekto struktūra

```
├── main.py             # Pagrindinis paleidimo failas
├── game.py             # Singleton žaidimo valdymas
├── snake.py            # Gyvatės logika
├── apple.py            # Obuolio logika
├── settings.py         # Ekrano parametrai
├── game_object.py      # Bazinė abstrakti klasė
├── input_box.py        # Įvesties langas (registracija)
├── registration.py     # Vartotojo registracijos scenarijus
├── file_io.py          # Rezultatų saugojimas JSON
├── test_snake.py       # Vienetiniai testai su unittest
├── scores.json         # Rezultatų failas (sukuriamas automatiškai)
├── snake_report.md     # Markdown kursinio darbo ataskaita
```

## Įgyvendinti OOP reikalavimai

- Kapsuliacija
- Abstrakcija (GameObject)
- Paveldėjimas (Snake, Apple)
- Polimorfizmas (draw metodas)
- Singleton dizaino šablonas (`Game`)
- Kompozicija (`Game` turi `Snake`, `Apple`)
- Failų įrašymas JSON formatu
- Vienetiniai testai su `unittest`

## Kursinio darbo ataskaita

Ataskaita pateikta faile [`snake_report.md`](snake_report.md) pagal kursinio darbo reikalavimus (Markdown formatu).

---

Sėkmės žaidžiant!
