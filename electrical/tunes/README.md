# ECU tunes

TunerStudio project folders. To open one: TunerStudio → File → Open Project → pick the folder.

| Folder | Stage | ECU | Firmware | Tune type | Last saved |
|---|---|---|---|---|---|
| [stage-1-speeduino](stage-1-speeduino/) | 1 | Speeduino on STM32 | Speeduino 2023.05 | MAP (VE) | 2026-08-31 |
| [stage-2-rusefi](stage-2-rusefi/) | 2 (current) | RusEFI by KrycholRC (KRC_ECU_V3) | rusEFI 2026-08-24, build master.2026.09.19 | Alpha-N | 2026-10-12 |

Dyno results for each stage: [engine/README.md](../../engine/README.md#dyno).

## What is in each folder
- `CurrentTune.msq`: the tune to load into the ECU
- `restorePoints/`: older saved tunes, named by date
- `projectCfg/`: TunerStudio project settings and the ECU definition (`mainController.ini`)
- `dashboard/`, `TuneView/`: TunerStudio screen layouts
- `DataLogs/`: logs from the car
