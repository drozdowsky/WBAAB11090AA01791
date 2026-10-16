# Electrical

## ECU
- RusEFI plug & play, built by KrycholRC: https://github.com/Krycholrc/rusEFI
- Alpha-N tune by SU2 Performance. MAP is still read for logs.
- Crank and cam sensors: hall type

## Sensors
- **TPS:** Variohm XPD-2832-812-214-911-00 (hall type, not a potentiometer). Gives a clean signal, which ITBs on Alpha-N need.
- **Oil temperature and pressure:** Bosch PST-F1 (one sensor for both)

## Wideband
- **Controller:** rusEFI wideband controller, in the glovebox. Talks to the ECU over CAN.
- **Sensor:** Bosch LSU 4.9
- **Relay:** HELLA 4RA 933 332-541 (40A), same part as the fan relay.

## Radiator fan

SPAL 12V VA08-AP71/LL-53A. The ECU switches it on at 92 °C.
Relay and 30A fuse are in the glovebox.
Relay: HELLA 4RA 933 332-541 (40A). The wideband control uses the same relay part.

```
                    30A fuse
BATTERY + ──┬───────[ ]────── thick red: +12V fused ─────┐
            │                                            │
       power supply                               ┌──────┴──────┐
            │                                     │ 30          │
         ┌──┴──┐ ── yellow: +12V ────────────────►│ 86   RELAY  │
         │ ECU │                                  │             │
         └──┬──┘ ── red: switched ground ────────►│ 85      87  │
            │                                     └──────┬──────┘
           GND                                           │
                                     BRW/BLK (relay) ──► RED (fan wire)
                                                         │
                                                  ┌──────┴──────┐
                                                  │  SPAL fan   │
                                                  │  +       -  │
                                                  └─────────┬───┘
                                                            │
                                                  GND (engine block)
BATTERY - ── GND
```

| RusEFI connector pin | Function |
|---|---|
| 11 | Fan output (switched ground → relay 85) |
| ? | +12V from BMW GY/VI wire |

The old drawing is in [images/fan-wiring.jpg](images/fan-wiring.jpg). Delete it once the text above is checked on the car.
