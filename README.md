<p align="center"><img src="images/logo.png" width="260" height="220"></p>

# Pluto Polygraph
Pluto Polygraph is a web-based lie detector application that uses a brainwave headset to pick up EEG (Electroencephalography) signals in the brain. Pluto Polygraph uses Deep Learning technology to perform the detection process with the Long-Short Term Memory (LSTM) algorithm. The model on the Pluto Polygraph knows with a dataset the human brain's EEG signals.

Pluto Polygraph was built for the purposes of scientific investigation and research. This website is built with Python's Flask technology and Mysql database. With a dynamic and attractive appearance, it can simplify the analysis of lie detection on the web.

[![instagram](https://img.shields.io/badge/CONTACT-TELEGRAM-blue)](https://t.me/shivayadavv)
[![instagram](https://img.shields.io/badge/CONTACT-INSTAGRAM-red)](https://instagram.com/shivaya.dav)

# Requirements
1. Software :
- OS (Windows/Linux/Mac).
- Python (2.x/3.x).
- XAMPP (Any Version).
- Visual Studio Code or others.
- Web Browser (Chrome, Firefox, MS Edge).
2. Hardware :
- Device Laptop or Personal Computer.
- Neurosky Mindwave Headset.
- I/O (Mouse, Monitor, Keyboard).
3. Skills :
- Have an understanding of **computer and web interfaces, polygraph process or lie detector in general, and interview or interrogation process**

# Installation
1. Python <br />
Decide which version of python to use. Python can be downloaded at the following link: [Download Python](Python.org) <br />
After the download is complete, you can follow the following instructions:
  ## Windows
    - Open python installer file.
    - Select "install for all users" so that it can be used by all users on the computer.
    - Configure python to be recognized by the operating system by clicking the Add Python 3.7 to PATH checklist or according to the installed version.
    - Click "Install now".
    - If the installation is successful, the words "Setup was Successful" will appear.
    - To do a test (optional), run Command Prompt (CMD) and write 'python' to enter python mode.
  ## MacOS
    - Open python installer file.
    - Click Continue at the next stage starting from Introduction to Installation Type.
    - Enter the computer user password if prompted at the installation stage.
    - If the installation is successful it will appear "Installation was successful".
    - Python testing can be done using the Command Prompt (CMD) the same as in the Windows version.
  ## Linux
    - Download the development package needed to build python.
    - Download the latest python installer file on the official website and there will be a file with the format .tar.xz (tarball) containing the python source code.
    - If a dialog box appears, select Save.
    - Double click on the downloaded file.
    - Extract files.
    - Configure the script and run the following command in the terminal:
      $ cd Python-3.*
      ./configure
    - Wait until the installation is complete.
    - Do a test by writing 'python3 -version' in the terminal.
2. Database / Using XAMPP <br />
XAMPP is used for databases which can be downloaded via the following link: [Download XAMPP](https://www.apachefriends.org/download.html) <br />
After the download is complete, you can install it by following these instructions:
  ## Windows
    - Open the downloaded folder then open the installer file (.exe) by right-clicking and selecting Run as Administrator.
    - The initial installation process will usually display the Bitnami icon, click OK on the warning that appears.
    - Click Next when the initial XAMPP Setup window appears.
    - Make sure all components (Apache, MySQL, FileZilla, Phpmyadmin) and others must be checked, then click Next.
    - Click Next at each subsequent stage, then wait until the installation process is complete.
  ## MacOS
    - Open the downloaded installer file then click the XAMPP file to start the installation.
    - Enter the password of the computer user if prompted.
    - Just like windows, an initial window will appear with a bitnami writing logo, then click Next in the XAMPP Setup window.
    - Centang komponen instalasi XAMPP, lalu klik Next pada setiap tahap selanjutnya.
    - When the installation is complete, go to the Application directory and select the XAMPP folder.
    - Control Panel XAMPP on MacOS named Manager OSX, open the file to run XAMPP.
  ## Linux
    - After the installer file has been downloaded, open a terminal on linux then change to the download directory using the command:
      $ cd Downloads/
    - Then change the executable file using the command:
      $ sudo chmod +x xampp-linux-x64-7.2.3-0-installer.run
      or according to the file name of the downloaded version.
    - Install the XAMPP file using the command:
      $ sudo ./xampp-linux-x64-7.2.3-0-installer.run
    - Once the XAMPP Setup window opens, follow the install prompts as on Windows or MacOS.
    - Click finish after the installation process is complete.
3. Cloning Project <br />
For use without installation, please visit the [following link](https://pluto-polygraph.havefun-ktrnxx.my.id/) <br />
And if you want to install on a local system, clone the project from the [following github link](https://github.com/zal-ghiffari/Pluto-Polygraph.git) <br />
4. Module <br />
Install the python module by opening the Command Prompt (CMD) or terminal and then executing the command: <br /> <br />
  ## Windows 
    python -m pip install -r requirements.txt
  ## Linux
    pip install -r requirements.txt
  ## MacOS
    pip install -r requirements.txt

5. Database Congiguration <br />
Run XAMPP then open localhost phpmyadmin, after that create a database then import the **pluto_polygraph.sql** file in the database. Next, open the project folder, then edit the **app.py** file and then adjust the following parameters: <br /> <br />
  ## Parameters
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'pluto_polygraph'
In **MYSQL_HOST** adjust to the mysql server host, in **MYSQL_USER** adjust to the mysql user name, in **MYSQL_PASSWORD** adjust to the mysql password, and finally **MYSQL_DB** is adjusted to the database name created earlier.

6. Flask Configuration <br />
In this configuration just adjust the app.py file on the following parameters: 
  ## Parameters
    app.secret_key = "S3cr3t0VickingLovelySt4aar1!"
Please adjust it with your favorite secret_key <br /> <br />

7. Running Flask <br />
Run the flask app with the following command in CMD: 
  ## Command Line 
    python app.py
The flask contains the following parameters: 
  ## Parameters
    app.run(debug=True, host='0.0.0.0', port=9000)
You can use the port as desired, and if you use host 0.0.0.0 it will use the local IP on the network, while if you use host 127.0.0.1 it will use localhost. In the debug parameter, if it is enabled it will display an error that occurs when running the flask app and when there is a change in the source code it will be restarted immediately, and vice versa if the debug parameter is not enabled.
