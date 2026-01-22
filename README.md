# 16762
# Stretch Robot Setup Guide

This repository contains instructions for setting up the development environment and running the Hello Robot Stretch platform.

---

## Setup

Create a working directory:

```bash
cd 16762/
mkdir your_name
cd your_name


python3 -m venv env
source env/bin/activate
pip3 install --upgrade pip
pip3 install hello-robot-stretch-body
pip3 install numpy==1.26.4 opencv-contrib-python==4.10.0.84 opencv-python==4.11.0.86

git clone https://github.com/SoiNew-SamYu/16762.git
```

To Run Rviz
```bash
ros2 launch stretch_core stretch_driver.launch.py
ros2 run rviz2 rviz2 -d `ros2 pkg prefix --share stretch_calibration`/rviz/stretch_simple_test.rviz

```
