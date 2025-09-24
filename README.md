# Alehundred-VCS-Toolkit
A powerful, open-source toolkit to simplify the setup and management of a professional, self-hosted version control system on low-cost ARM hardware.

<div align="center">

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-3.9+-yellow.svg)](https://www.python.org/)
[![Perforce Helix Core](https://img.shields.io/badge/Supports-Perforce%20Helix%20Core-purple.svg)](https://www.perforce.com/products/helix-core)
[![Raspberry Pi](https://img.shields.io/badge/Runs%20on-Raspberry%20Pi-red.svg)](https://www.raspberrypi.org/)
[![Unreal Engine](https://img.shields.io/badge/For-Unreal%20Engine-blueviolet.svg)](https://www.unrealengine.com/)

A powerful, open-source toolkit designed to simplify the setup and management of a professional, self-hosted version control system on low-cost **ARM hardware** like the Raspberry Pi.

**This is the open-source engine that will power Alehundred Depot.**

</div>

---

## 📖 About The Project

Indie developers for games and complex software often face a significant challenge: professional-grade version control systems (VCS) are either too expensive or not suited for large binary files.

* **The Problem:** Commercial solutions like Perforce Helix Core are the industry standard for handling large assets, but the cost of cloud hosting is a major barrier for small teams and solo developers. On the other hand, free platforms like GitHub are inefficient with the massive binary files (3D models, textures, audio) common in game development, leading teams to rely on messy, non-integrated solutions like Dropbox or Google Drive.

* **The Solution:** The Alehundred VCS Toolkit bridges this gap. It provides a set of scripts and tools to seamlessly install, configure, and manage a Perforce Helix Core server on a Raspberry Pi (or other **ARM-based** single-board computers). This approach transforms a small, one-time hardware purchase into a robust, enterprise-level VCS, effectively democratizing professional workflows for everyone.

This toolkit aims to empower indie creators to use the same tools as AAA studios with a fraction of the cost and full control over their own data.

## 🚀 Getting Started

This section will guide you through setting up your own self-hosted VCS server using the toolkit.

### Prerequisites

* A Raspberry Pi (Model 3B+ or newer recommended) or other ARM-based board.
* Python 3.9 or higher installed.
* An external hard drive or high-capacity SD card for storage.
* For external access, you will need to configure Port Forwarding on your router and consider using a Dynamic DNS (DDNS) service.

### Installation

1.  **Connect to your Raspberry Pi via SSH**

    ```bash
    # Replace with your actual user and hostname/IP
    ssh YourUserName@RaspberryName.local 
    ```
    
2.  **Copy, paste, and run this entire block**

    This will update, install dependencies, install the toolkit, and set up the PATH all in one go.

    ```bash
    sudo apt update && sudo apt upgrade -y && sudo apt install python3-pip -y
    pip install --break-system-packages alehundred-depot-en
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    echo "¡Setup complete! Run 'alehundred-depot-en' to start."
    ```

3.  **Run the program**

    ```bash
    alehundred-depot-en
    ```

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📬 Contact

Alejandro Friant - (https://www.linkedin.com/in/alejandrofriant/)

Project Link: [https://github.com/alefriant/Alehundred-VCS-Toolkit](https://github.com/alefriant/Alehundred-VCS-Toolkit)
