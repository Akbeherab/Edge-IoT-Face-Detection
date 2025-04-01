# Edge IoT Face Detection System


## Overview

The **Edge IoT Face Detection System** is an offline facial recognition-based attendance system designed for secure and efficient tracking in edge computing environments. Developed as a capstone project, this system leverages Raspberry Pi devices to process facial recognition locally, eliminating internet dependency. It features four interconnected nodes deployed across an IIT campus, using Wi-Fi or LoRa for data transfer, and a centralized dashboard for real-time monitoring. This project demonstrates expertise in IoT, computer vision, and secure communication, with potential applications in defense, education, and remote monitoring.

- **Duration**: February 2025 – Present  
- **Author**: Amit Kumar Behera ([GitHub link](https://github.com/Akbeherab))  
- **Institution**: Indian Institute of Technology (IIT) Patna

## Features

- **Offline Operation**: Processes facial recognition locally on Raspberry Pi, ensuring security and autonomy.
- **Multi-Node Deployment**: Four nodes (e.g., lecture hall, library, lab, hostel) capture and process attendance data.
- **Flexible Communication**: Supports Wi-Fi for high-speed areas and LoRa for long-range, low-bandwidth scenarios.
- **Real-Time Dashboard**: Aggregates attendance data and displays it on a web interface, accessible from any network-connected device.
- **Scalable Design**: Easily expandable to additional nodes or larger environments.

## Tools & Technologies

- **Hardware**: Raspberry Pi 4, Pi Camera Module v2, LoRa Module (SX1278)  
- **Software**:  
  - Python 3.9  
  - OpenCV 4.5 (Face Detection & Recognition)  
  - Flask 2.0 (Web Dashboard)  
  - PySerial (LoRa Communication)  
  - Edge AI Principles  
- **Communication Protocols**: TCP/IP (Wi-Fi), Point-to-Point (LoRa)  
- **Operating System**: Raspberry Pi OS (64-bit)  

## System Architecture

The system comprises three layers:
1. **Edge Layer**: Four Raspberry Pi nodes with Pi cameras perform local face detection and recognition.
2. **Communication Layer**: Nodes transfer data to a central server via Wi-Fi or LoRa.
3. **Presentation Layer**: A Flask-based dashboard on the central server visualizes attendance data.


## Installation & Setup

### Prerequisites
- Raspberry Pi 4 (5 units: 4 nodes + 1 server)
- Pi Camera Module v2 (4 units)
- LoRa Module (SX1278, optional for Node 4)
- Wi-Fi-enabled network

### Step 1: Install Dependencies
On each Raspberry Pi, run:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-dev python3-opencv libatlas-base-dev libjasper-dev libqtgui4 libqt4-test
pip3 install -r requirements.txt
