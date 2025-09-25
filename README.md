# Alehundred-Depot (English Version)

A Text-based User Interface (TUI) tool to facilitate the installation and management of a Perforce Helix Core server on low-cost hardware like a Raspberry Pi.

# 1. Installation
Connect to your Raspberry Pi via SSH

- Replace with your actual user and hostname/IP
ssh YourUserName@RaspberryName.local 

# 2. Copy, paste, and run this entire block

- This will update, install dependencies, install the toolkit, and set up the PATH all in one go.

sudo apt update && sudo apt upgrade -y && sudo apt install python3-pip -y
pip install --break-system-packages alehundred-depot-en
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
echo "¡Setup complete! Run 'alehundred-depot-en' to start."

# 3. Run the program

alehundred-depot-en

## 4. Updating the Toolkit

To ensure you have the latest features and fixes, update the toolkit regularly with the following command:

pip install --upgrade --break-system-packages alehundred-depot-en

If the command above doesn't install the latest version (especially on a Raspberry Pi), it may be due to a cache in the `piwheels` repository. To force the update directly from PyPI, use this command:

pip install --upgrade --index-url https://pypi.org/simple/ --break-system-packages alehundred-depot-en