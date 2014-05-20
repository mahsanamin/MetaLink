### Game Data WebUI Converter

* Description  
Upload the excel file and download the python file.

* Installation Requirement for MacOS
  - pip install web.py
    http://webpy.org/
  - Download and Install Tk/Tcl for MacOS
    https://www.python.org/download/mac/tcltk
  - pip install matplotlib

* WebUI Server Start Up:
cd src/
python app.py

* Usage:
visit the http://localhost:9999/uploader


### Game Data Command-Line Converter

* Description
Convert the game data to CSV files from excel files in command-line.

* Installation Requirement for MacOS
  - pip install xlrd

* Usage:
cd converter
chmod u+x run_conv.py
./run_conv.py

