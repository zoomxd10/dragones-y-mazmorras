# Dragones y Mazmorras 🐉🎲

A short text-based role-playing adventure for the terminal, written in **Python** and inspired by the dice mechanics of *Dungeons & Dragons*.

You play a young adventurer (random race: human, dwarf, elf or halfling) who must carry sacred amulets across the Forgotten Realms. Along the way you decide whether to fight or flee, and every combat is resolved with dice rolls.

## Mechanics

- **Attack roll:** d20 + attack modifier against the enemy's armour class
  - a natural **1** is a fumble (automatic miss)
  - a natural **20** is a critical hit (automatic hit)
- **Damage roll** depending on the weapon: dagger (d4), short sword (d6), long sword (d8), greatsword (d12), flail (2d4), plus a damage modifier
- Modifiers change with the story (rested +2, tired −1)

## Running it

Requires Python 3 (no external libraries).

```bash
python dragones_y_mazmorras.py
```

Single-player mode is playable; two-player mode is planned for the future.

---

## 🇪🇸 En español

Aventura de rol por texto para la terminal, hecha en **Python** e inspirada en las tiradas de dados de *Dragones y Mazmorras*. Eres un joven aventurero (de raza aleatoria) que debe llevar unos amuletos sagrados a Calimshan. Por el camino decides si luchar o huir, y cada combate se resuelve con tiradas: d20 para impactar (con pifia y crítico) y un dado de daño según el arma.

**Cómo ejecutarlo:** `python dragones_y_mazmorras.py` (solo necesita Python 3).

Autor: **Antonio Galván Gerona**
