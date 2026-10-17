# WBAAB11090AA01791

BMW E30 coupe (2-door saloon) from 1989. This repo documents all modifications and service done to the car.

Contact info is on my GitHub profile.

## The car today

| Area | Summary |
|---|---|
| Engine | M42B18.5 (85 mm bore), forged pistons, GT-R cams, 42 mm ITBs. **200 BHP** on the dyno ([details](engine/README.md)) |
| ECU | RusEFI, Alpha-N tune by SU2 Performance ([details](electrical/README.md)) |
| Drivetrain | Getrag 240, 168 diff 4.27 with 25% LSD ([details](drivetrain/README.md)) |
| Suspension | H&R -35 mm, Bilstein B8, poly bushings, E46 quick rack (no power assist) ([details](suspension/README.md)) |
| Brakes | E30 325i OEM, HEL braided lines ([details](brakes/README.md)) |
| Fuel | 98 RON. Bosch OEM pump, new in 2026-05 ([details](fuel/README.md)) |
| Wheels | Stock 14" bottlecaps, Vredestein Sportrac 195/65 ([details](wheels/README.md)) |
| Interior | E30 sport seats, M-Tech 1 wheel, 8k rpm cluster, OBC 1, Blaupunkt Bremen SQR 46 ([details](interior/README.md)) |
| Weight | About 1100 kg with fluids (not weighed in years). About 182 BHP per tonne |
| Paint | Malachitgrün metallic |
| Factory options | No power steering, no AC |

## Files

- [CHANGELOG.md](CHANGELOG.md): what was done to the car and when
- [ROADMAP.md](ROADMAP.md): ideas and planned work
- [MAINTENANCE.md](MAINTENANCE.md): fluids, parts numbers, yearly mileage
- [electrical/tunes/](electrical/tunes/README.md): TunerStudio projects for Stage 1 (Speeduino) and Stage 2 (RusEFI)
- [tools/acceleration.html](tools/acceleration.html): 0–100 km/h simulator (open in a browser)
- `tools/build_pdf.py`: builds one PDF from all `.md` files
- `engine/`, `fuel/`, `drivetrain/`, `suspension/`, `brakes/`, `wheels/`, `electrical/`, `interior/`: current spec of each area

## PDF

```
uv run tools/build_pdf.py
```

Writes `build/WBAAB11090AA01791.pdf` (the `build/` folder is not in git). Needs [uv](https://docs.astral.sh/uv/) and Google Chrome.

- First page is a contents page. Tap a file or a section to jump there. Each file starts with "↑ Contents" at the top to go back.
- Links between `.md` files work inside the PDF. Linked images (dyno sheets, wiring) are on their own pages at the end. Wide images are turned sideways.
