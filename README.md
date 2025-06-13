# LABU
A Nintendo Labo emulator.

## Supported kits:
- 03: Vehicle Kit (vehicle_*.py)

### Requirements:
1. python 3.11.9 (other versions might work but are untested)
2. a .venv enviroment in the this repositories folder with pygame-ce installed
3. yuzu/one of it's forks (Ryujinx doesn't have IR Camera emulation)
4. OBS with virtual camera
5. Your own copy of the labo kit ROM you wanna play
### Yuzu Setup:
1. Go to the settings and turn on `Controls -> advanced -> Infared Camera` 
2. Start vehicle_car.py (or any other kit py file thing)
3. Go into OBS and make a new source: window capture, select the Labu window and set it to only look for the window title and name the source something like LABU
4. turn on the virtual camera in OBS, go into it's settings and make it only look at the source just created
6. The py file can now be closed
5. Back in yuzu, select OBS Virtual Camera as the IR Camera
### Usage:
- Start one of the py files for the thing you want it to emulate
- You need to focus the small window that opens with the title Labu to input anything
- Don't have 2 open at the same time or it might not work
- ESC closes the program

### Keybinds:
#### Vehicle Car:
|Name|Key|
|-|-|
|Boost|W|
|Backwards|S|
|Left Stick|Q|
|Right Stick|E|
|Switch L. Stick Up/Down|1/2|
|Switch R. Stick Up/Down|3/4|
#### Vehicle Plane:
|Name|Key|
|-|-|
|Shoot|Space|
#### Vehicle Submarine:
|Name|Key|
|-|-|
|Shoot|Space|
|Left Turbine Up/Down|D/C|
|Right Turbine Up/Down|K/M|
