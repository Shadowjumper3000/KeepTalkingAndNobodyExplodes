# Keep Talking and Nobody Explodes - Module Solvers

Custom solving programs for KTANE Puzzle Modules to assist defusers during gameplay.
This was one of my favourite Games while I was initially learning Python, and I wanted to create a few tools to help with the modules. As such this was a passion project, I will not be adding any new modules or features, but I will be happy to accept pull requests for any bugs or issues you may find.

## Overview

This repository contains Python command-line tools to help solve various modules from the game "Keep Talking and Nobody Explodes". These tools guide the defuser through the solving process by asking relevant questions and providing instructions.

## Modules Included

- **Button** - Solver for the Button module
- **Complicated Wires** - Solver for the Complicated Wires module
- **Memory** - Solver for the Memory module
- **Passwords** - Solver for the Password module
- **Simple Wires** - Solver for the Simple Wires module

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Shadowjumper3000/KeepTalkingAndNobodyExplodes.git
   cd KeepTalkingAndNobodyExplodes
   ```

2. No additional packages are required as these scripts only use the Python standard library

### Usage

#### Using the main launcher

Run the main launcher to select which module to solve:

```bash
python main.py
```

This will display a menu where you can select which module solver to use.

#### Running individual modules

Alternatively, you can run any of the solver scripts directly:

```bash
python KTANE-Button.py
```

## Module Instructions

### Simple Wires
Helps solve the Simple Wires module by analyzing wire colors and positions based on the bomb's serial number.

### Button
Determines whether to press and immediately release the button or hold it based on the button's color and label.

### Complicated Wires
Analyzes color, LED status, and star symbol to determine whether to cut wires based on serial number, batteries, and parallel ports.

### Memory
Guides you through the 5 stages of the Memory module, tracking positions and values across stages.

### Passwords
Helps solve the Password module by finding valid passwords from a collection of letters.

## License

This project is available under the MIT License.