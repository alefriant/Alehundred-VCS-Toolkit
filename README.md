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

*(Note: The toolkit is currently in early development. These instructions are the target goal.)*

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/alefriant/Alehundred-VCS-Toolkit.git](https://github.com/alefriant/Alehundred-VCS-Toolkit.git)
    cd Alehundred-VCS-Toolkit
    ```
2.  **Run the automated setup script:**
    ```sh
    python setup.py
    ```
3.  Follow the on-screen prompts to configure your server, create your first user, and set up your main depot.

## 🗺️ Roadmap

This project is just getting started! Here are some of the features planned for future releases:

* [ ] **Automated Installer:** Core script to set up Helix Core on a fresh Raspberry Pi OS.
* [ ] **Terminal-based UI (TUI):** A lightweight, Xtree-style management dashboard for users, depots, and server monitoring, designed to run directly in the terminal on Raspberry Pi OS Lite.
* [ ] **Automated Backups:** A simple utility to schedule and manage backups of your server data to an external drive.
* [ ] **Performance Monitoring:** Scripts to check server health, disk space, and memory usage.
* [ ] **Detailed Documentation:** Step-by-step guides for advanced configurations.

See the [open issues](https://github.com/alefriant/Alehundred-VCS-Toolkit/issues) for a full list of proposed features (and known issues).

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📬 Contact

Alejandro Friant - (https://www.linkedin.com/in/alejandrofriant/)

Project Link: [https://github.com/alefriant/Alehundred-VCS-Toolkit](https://github.com/alefriant/Alehundred-VCS-Toolkit)
