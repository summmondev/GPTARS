# Assembly Guide for GPTARS

Follow these step-by-step instructions to build your own GPTARS robot:

---

## Materials Needed  
- 3D-printed parts (files in `3D_models/`)  
- Laser-cut chassis parts (files in `laser_cut_files/`)  
- Raspberry Pi 4 (or equivalent)  
- Adafruit PCA9685 Servo Controller  
- 6 x Servo Motors  
- Rechargeable Battery Pack  
- Wiring (refer to `wiring_diagrams/`)  

---

## Assembly Steps  

### 1️⃣ Assemble the Frame  
1. Print the parts from `3D_models/` or use `laser_cut_files/`.  
2. Attach the chassis components to form the main robot body.  

### 2️⃣ Attach the Servos  
1. Install servo motors for:
   - Center lift.
   - Port and starboard drive.  
2. Connect to the Adafruit PCA9685 board.  

### 3️⃣ Mount the Raspberry Pi  
1. Attach the Raspberry Pi securely to the robot's main frame.  
2. Connect the GPIO pins to the PCA9685 board.  

### 4️⃣ Wire Everything  
1. Refer to `wiring_diagrams/` for servo and power connections.  
2. Ensure the rechargeable battery pack is properly connected to the system.

---

## Testing  
1. Run `software/app.py` to initialize the robot.  
2. Use `hardware_control/movement.py` to test the servo motors.  

Congratulations! Your GPTARS is ready to go!

