# Engine

Original engine: M40B16. Since 2023: fully rebuilt M42B18, bored to 85 mm (M42B18.5).

## Bottom end
- Forged pistons from [CPS Pistoni Stampati](https://www.pistonistampati.it/) (ring gap: Sport N/A)
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
- K&N cone filter (RE-0950), 90 mm plastic pipe tapered to 80 mm

## Fuel and ignition
- Bosch "green giant" injectors 440cc (0280155968)
- BMW M52 coil-on-plug, NGK BKR7E plugs

## Exhaust
- Custom downpipe: 2x 45 mm, 35 cm long
- 2.25" exhaust by Kowalsky Custom (Wrocław): custom 100one.pl mid muffler + Scorpion 318iS DTM mufflers

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
