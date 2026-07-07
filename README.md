# project-aura

## Overview
Project AURA is a non-invasive, brain-computer interface (BCI) prosthetic designed to restore autonomy and finger-level function for individuals with partial hand amputations. By interpreting electroencephalography (EEG) signals in real-time, the system allows users to control individual finger articulations through mental commands, bypassing the need for residual muscle movement.

## Problem
- Traditional passive prosthetics offer psychological benefits but lack active movement, grip modulation, or tactile feedback.
- Many prosthetic solutions focus on full-hand replacement, often overlooking the specific needs of four-finger amputees who retain thumb function.
- Extended wear of prosthetic sockets often leads to heat buildup, skin irritation, and reduced stability in physically demanding conditions

## Solution
- Utilizes a non-invasive Emotiv EPOC X headset to detect motor intentions and map them to distinct motion profiles like grasping and pinching.
- Employs high-torque servo motors connected to tendon-like cables to mimic natural finger articulation in a lightweight 3D-printed frame.
- Integrated Feedback Systems:
1. Haptic Feedback. Embedded force sensors measure grip strength and relay tactile data via vibration motors in the arm socket.
2. Environmental Monitoring. Integrates a BME680 sensor to monitor internal socket temperature and provide adaptive cooling alerts.

## Technical Stack
- Hardware: Arduino Uno R3, Emotiv EPOC X Brainwear, BME680 Environmental Sensor, Servo Motors.
- Software: Arduino IDE, Python (python-osc), Emotiv BCI/Launcher, Visual Studio Code.
- Fabrication: 3D Printing (lightweight ergonomic frame).

## Results
- Achieved functional hand opening ("LIFT") and fist closure ("DROP") through trained EEG commands.
- Successfully displayed live temperature, humidity, and gas resistance data on an integrated LCD screen to enhance user comfort.
- Demonstrated that responsiveness significantly improves with precise sensor placement and consistent mental focus.

## Visuals

## Full Code Access
The implementation includes Python-based OSC dispatchers for mental command processing and Arduino firmware for servo control and sensor integration.

Full codebase available upon request for academic or professional review.
