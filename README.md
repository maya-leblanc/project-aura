# Project AURA

## Overview
Project AURA is a non-invasive brain-computer interface (BCI) prosthetic that restores finger-level function for individuals with partial hand amputations. The system reads electroencephalography (EEG) signals in real time and maps them to individual finger movements, letting the user control the hand with trained mental commands instead of residual muscle activity.

## Problem
- Passive prosthetics offer psychological benefit but no active movement, grip modulation, or tactile feedback.
- Most prosthetic development targets full-hand replacement, leaving four-finger amputees who retain thumb function underserved.
- Extended socket wear causes heat buildup, skin irritation, and reduced stability during physical activity.

## Solution
- An Emotiv EPOC X headset detects motor intent and maps it to distinct motion profiles (grasping, pinching, full closure).
- High-torque servo motors, connected to tendon-like cables, drive finger articulation inside a lightweight 3D-printed frame.
- Two feedback loops run alongside the core control system:
  - **Haptic feedback** — force sensors at the fingertips measure grip strength and relay it as vibration in the arm socket.
  - **Environmental monitoring** — a BME680 sensor tracks internal socket temperature and flags conditions for adaptive cooling.

## Technical Stack
- **Hardware:** Arduino Uno R3, Emotiv EPOC X headset, BME680 environmental sensor, servo motors
- **Software:** Arduino IDE, Python (python-osc), Emotiv BCI / Launcher, Visual Studio Code
- **Fabrication:** 3D-printed ergonomic frame

## Results
- Trained EEG commands ("LIFT" / "DROP") reliably triggered hand opening and fist closure.
- Live temperature, humidity, and gas resistance readings were displayed on an onboard LCD to support user comfort.
- Responsiveness depended heavily on sensor placement and mental focus — both improved with iteration.

## Visuals

## Code
Includes a Python OSC dispatcher for processing classified mental commands, plus Arduino firmware for servo control and BME680/LCD sensor integration. Full codebase available on request for academic or professional review.
