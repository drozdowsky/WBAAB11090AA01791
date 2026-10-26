# Engine

Original engine: M40B16. Since 2023: fully rebuilt M42B18, bored to 85 mm (M42B18.5).

## Bottom end
- Forged pistons from [CPS Pistoni Stampati](https://www.pistonistampati.it/) (ring gap: Sport N/A)
- Compression ratio: 10.5:1
- Crank, rods and flywheel fully balanced
- Main and rod bearings: standard size, ACL Race Bearings

## Head and cams
- Ported a bit to match the inlet and outlet gaskets ([sheet](https://docs.google.com/spreadsheets/d/1PFJInhn7sOsHwqv-euhsF417-aVGpTfvuwedF-gkzFo/edit#gid=0))
- GT-R camshafts from [Świątek](http://swiatek.com.pl), same spec for intake and exhaust:

  | | GT-R | Stock |
  |---|---|---|
  | Lift | 10.60 mm | 9.70 mm |
  | Duration | 262° | 238° |
  | Duration @ 1.0 mm | 226° | 205° |
  | Duration @ 2.0 mm | 209° | 189° |
  | Buckets | hydraulic | |

  Timing: [sheet](https://docs.google.com/spreadsheets/d/1PFJInhn7sOsHwqv-euhsF417-aVGpTfvuwedF-gkzFo/edit#gid=1037211742)

## Intake
- Individual throttle bodies 42 mm + carbon plenum, by Race Head Engineering

Air path, from the filter to the head:

| # | Part | Notes |
|---|---|---|
| 1 | K&N cone filter (RE-0950) | 90 mm neck |
| 2 | ABS plastic pipe | tapers from 90 mm to 80 mm, about 20 cm long. Goes through an aluminium heat shield wall, so the filter sits on the cold side, away from engine heat |
| 3 | Flexible hose | ribbed inside (wire coil), not smooth. About 10 cm long |
| 4 | Plenum adapter | about 5 cm long. The plenum inlet is 90 mm OD / 80 mm ID. The adapter makes the hose easy to fit and gives a smoother step |
| 5 | Carbon plenum | open type (no back wall). Big enough for a 2.0 l engine. Volume: to be measured |
| 6 | Stainless plenum wall | the plenum bolts to it. Holds 4 stainless trumpets with a bell-mouth radius |
| 7 | Trumpets | taper from about 48 mm to 42 mm |
| 8 | Throttle bodies | 4x 42 mm |
| 9 | Head adapter | throttle bodies to the cylinder head. Has the injector bosses |

Runner length (bell mouth to head): about 30 cm, to be measured.

## Fuel and ignition
- Bosch "green giant" injectors 440cc (0280155968)
- BMW M52 coil-on-plug (BREMI 1748017), NGK BKR7E plugs

## Exhaust
- Custom downpipe and 2.25" (57 mm) system by Kowalsky Custom (Wrocław). Mid muffler from 100one.pl (2025-05), rear muffler 318iS DTM from Scorpion.

Gas path, from the head to the tips:

| # | Part | Notes |
|---|---|---|
| 1 | OEM M42 manifold, 4-2 | Ported: the inside weld is ground away on both the head side and the outlet side. Weld notes in `private/exhaust/manifold-weld.md` |
| 2 | Downpipe | 2x 45 mm OD / 42 mm ID, about 35 cm long, then merges into one 2.25" pipe |
| 3 | Flex pipe | 2.25" |
| 4 | Mid muffler, 100one.pl | Straight-through, perforated tube. Elliptical case 175 x 105 mm, 550 mm long. Packed with a lot of steel wool and ceramic wool |
| 5 | Pipe | 2.25" |
| 6 | Rear muffler, Scorpion 318iS DTM | 2.25" inlet, twin DTM-style tips. Details below |

### Rear muffler (Scorpion)

Technical drawing: `private/RearMufflerScorpionExhaust.pdf`

- Overall length about 1040 mm. Inlet pipe about 430 mm, case about 430 mm, tips about 155 mm.
- Inside the case: an empty chamber at the inlet end, then perforated tubes through packing (absorptive section, about 410 mm), then a second chamber at the outlet end that feeds both tips.
- Tips: 76 mm, perforated inside (also absorptive).

## Cooling
- SPAL electric fan, switched on by the ECU at 92 °C. Wiring: [electrical/README.md](../electrical/README.md#radiator-fan)

## Dyno

All runs at SU2 Performance.

| Stage | Date | Power | Torque | Conditions | Sheet |
|---|---|---|---|---|---|
| 1 | 2023-06 | 175.4 BHP @ 6223 | 210.9 Nm @ 5581 | 21.6 °C, 98.4 kPa | [image](images/dyno-stage-1.jpg) |
| 2 | 2026-07 | 200.0 BHP @ 7379 | 208.4 Nm @ 6233 | 30.8 °C, 99.7 kPa | [image](images/dyno-stage-2.jpg) |

Stage 2 is about 203 BHP when corrected to 20 °C.

### Curves every 500 rpm

Read by hand from the dyno sheets, so values are ±3. Stage 1 hits the limiter at about 7050 rpm.

| rpm | Stage 1 BHP | Stage 1 Nm | Stage 2 BHP | Stage 2 Nm | Δ BHP |
|---|---|---|---|---|---|
| 1600 | 27 | 117 | 30 | 132 | +3 |
| 2000 | 37 | 129 | 44 | 153 | +7 |
| 2500 | 56 | 157 | 56 | 158 | 0 |
| 3000 | 66 | 154 | 73 | 170 | +7 |
| 3500 | 87 | 174 | 90 | 181 | +3 |
| 4000 | 97 | 171 | 100 | 175 | +3 |
| 4500 | 122 | 191 | 120 | 187 | -2 |
| 5000 | 143 | 201 | 143 | 201 | 0 |
| 5500 | 164 | 210 | 162 | 207 | -2 |
| 6000 | 174 | 204 | 175 | 205 | +1 |
| 6500 | 174 | 188 | 190 | 205 | +16 |
| 7000 | limiter | | 198 | 199 | |
| 7500 | | | 199 | 186 | |

What it shows:
- Stage 2 gains are mostly at the top. Torque stays at about 205 Nm up to 6500 rpm, where Stage 1 was already falling off, and the engine now pulls to about 7600 rpm.
- Low end (2000 to 3000 rpm) is a bit stronger.
- 4500 to 5500 rpm is about the same. The small minus is within reading error, and the Stage 2 day was 9 °C hotter. What changed between stages: see [CHANGELOG.md](../CHANGELOG.md).
