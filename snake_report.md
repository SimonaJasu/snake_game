# Kursinis darbas: Objektiškai orientuotas žaidimas „Snake“

---

## 1. Įžanga

Šis kursinis darbas yra klasikinio žaidimo „Snake“ atkartojimas naudojant Python programavimo kalbą ir `pygame` biblioteką. Žaidimas buvo sukurtas siekiant įgyvendinti visus keturis objektiškai orientuoto programavimo (OOP) principus, įtraukti bent vieną dizaino šabloną, realizuoti kompoziciją tarp objektų, įgyvendinti testavimą, bei įrašyti ir išsaugoti žaidėjų rezultatus.

**Tikslas** – sukurti išplečiamą, tvarią, gerai struktūruotą programą, kuri veiktų kaip pavyzdys taikant OOP principus praktikoje.

**Tikslinė auditorija** – vartotojai, norintys žaisti paprastą bet vizualiai patrauklų žaidimą, bei programuotojai, besimokantys OOP pagrindų.

---

## 2. Kaip paleisti žaidimą

1. Įdiekite `pygame` biblioteką komanda:
   ```
   pip install pygame
   ```
2. Paleiskite `main.py` failą:
   ```
   python main.py
   ```

3. Įveskite savo vardą registracijos lange.
4. Naudokite rodyklių klavišus gyvatei valdyti.

---

## 3. Projekto struktūra

```
snake_game/
├── main.py                # Paleidžia žaidimą, valdo ciklą
├── game.py                # Singleton klasė, kurioje vyksta žaidimo logika
├── snake.py               # Gyvatės klasė
├── apple.py               # Obuolio klasė
├── settings.py            # Ekrano matmenys ir ląstelių dydis
├── ui/
│   ├── input_box.py       # Tekstinio įvesties lauko UI klasė
│   └── registration.py    # Registracijos logika
├── utils/
│   └── file_io.py         # Rezultatų saugojimas ir nuskaitymas
├── tests/
│   └── test_snake.py      # Vienetiniai testai
├── scores.json            # JSON failas rezultatams saugoti
```

---

## 4. OOP principų įgyvendinimas

### 4.1. Kapsuliacija *(Encapsulation)*

Kiekviena klasė slepia savo logiką ir turi tik jai priklausančius metodus bei atributus.

```python
# snake.py
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (CELL_SIZE, 0)
        self.grow_snake = False
```

### 4.2. Abstrakcija *(Abstraction)*

Sukurta abstrakti bazinė klasė `GameObject`, kurioje apibrėžtas bendras metodas `draw()`:

```python
# base/game_object.py
from abc import ABC, abstractmethod

class GameObject(ABC):
    @abstractmethod
    def draw(self, surface):
        pass
```

### 4.3. Paveldėjimas *(Inheritance)*

```python
# apple.py
from base.game_object import GameObject

class Apple(GameObject):
    def draw(self, surface):
        ...
```

### 4.4. Polimorfizmas *(Polymorphism)*

```python
# game.py
for obj in [self.snake, self.apple]:
    obj.draw(surface)
```

---

## 5. Naudotas dizaino šablonas: Singleton

```python
class Game:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Game, cls).__new__(cls)
        return cls._instance
```

---

## 6. Kompozicija

```python
self.snake = Snake()
self.apple = Apple()
```

---

## 7. Failų skaitymas ir rašymas

```python
def save_scores(scores):
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=4)
```

---

## 8. Vienetiniai testai

```python
def test_move_forward(self):
    original_head = self.snake.body[0]
    self.snake.move()
    expected = (original_head[0] + CELL_SIZE, original_head[1])
    self.assertEqual(self.snake.body[0], expected)
```

---

## 9. Rezultatai ir iššūkiai

- Sukurta veikianti sistema
- Visi OOP principai įgyvendinti
- Failų įrašymas, registracija ir testai

---

## 10. Išvados

Projektas patvirtino OOP principų naudą – geresnis kodo struktūravimas, aiški atsakomybė, testuojamumas. Šį žaidimą galima nesunkiai tobulinti ir pritaikyti platesniems projektams.

---

## 11. Galimos plėtros kryptys

- Kliūtys ir lygiai
- Multiplayer režimas
- Online rezultatų lentelė

---

## 12. Šaltiniai

- https://www.pygame.org/docs/
- https://docs.python.org/3/library/unittest.html
- https://refactoring.guru/design-patterns/singleton
- https://realpython.com/python-application-layouts/
