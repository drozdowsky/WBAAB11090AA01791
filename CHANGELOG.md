# Changelog

Newest first. Add cost only when it's worth noting.

Dates before 2026-10 come from git history: they show when the work was written down, not always the exact day it was done.

## 2026-07-01: Stage 2 dyno (engine)
- ITBs tuned by SU2 Performance.
- Result: **200.0 BHP @ 7379 rpm, 208.4 Nm @ 6233 rpm** (30.8 °C, 99.7 kPa). About 203 BHP if corrected to 20 °C.
- Proof: [engine/images/dyno-stage-2.jpg](engine/images/dyno-stage-2.jpg)
- What changed since Stage 1:
  - Individual throttle bodies (42 mm) + carbon plenum
  - Electric fan (Stage 1 was measured with the viscous fan)
  - Speeduino → RusEFI
  - Crank + cam sensors: VR → hall
  - Tune: MAP (VE) → Alpha-N. ECU still reads MAP for logs.
  - TPS: potentiometer → hall sensor (Variohm XPD-2832-812-214-911-00). Much better behaviour, because ITBs on Alpha-N need a clean signal.

## 2026-06: ITBs and RusEFI (engine, electrical)
- Race Head Engineering 42 mm ITBs + carbon plenum.
- K&N cone intake (RE-0950), 90 mm plastic pipe tapered to 80 mm. Replaced the custom 70 mm aluminium intake.
- RusEFI plug & play ECU built by KrycholRC.
- Fan switch-on temperature 95 °C → 92 °C.

## 2026-06: Oil temperature and pressure sensors (electrical)

## 2026-06: Door seals (body)

## 2025: Speeduino update (electrical)
- Arduino → [STM32](https://github.com/pazi88/STM32_mega). Added SD card logging and CAN.

## 2025-05: LSD (drivetrain)
- Small case 168, 4.27, 25% lock, billet steel cap.
- Bolts: M12x1.5x55 (8.8) + washers + nut, 12x M10x50 Torx or Allen (10.9).

## 2025-05: Mid muffler (exhaust)
- Custom from 100one.pl. Replaced the Magnaflow.

## 2025-04: New starter (engine)

## 2025-04: SPAL fan connector (electrical)

## 2025-04: Front valance (body)

## 2025-03: Side window gaskets (body)

## 2024: Driveshaft (drivetrain)
- New giubo and center support bearing.

## 2023, after Stage 1: Electric fan (engine)
- SPAL VA08-AP71/LL-53A replaced the viscous fan. Switched on by the ECU at 95 °C.

## 2023, around Stage 1: E46 steering rack (suspension)
- E46 "purple tag" rack, about 3 turns lock to lock. Used without power assist.

## 2023-06: Stage 1 dyno (engine)
- Result: **175.4 BHP @ 6223 rpm, 210.9 Nm @ 5581 rpm** (21.6 °C, 98.4 kPa).
- Speeduino, MAP (VE) tune, viscous fan.
- Proof: [engine/images/dyno-stage-1.jpg](engine/images/dyno-stage-1.jpg)

## 2023: Engine swap (engine)
- M40B16 → fully rebuilt M42B18, bored to 85 mm. Almost all parts new. Full spec in [engine/README.md](engine/README.md).
- Custom Speeduino ECU.
- Custom downpipe and 2.25" exhaust by Kowalsky Custom (Wrocław).

## 2022: Suspension refresh (suspension)
- Poly bushings (80A), all parts blasted and painted, new hubs and links.
- H&R -35 mm springs, Bilstein B8, rear sway bar added.
