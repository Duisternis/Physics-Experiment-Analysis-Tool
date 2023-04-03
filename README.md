
![Logo](/screenshots/header.png)

[![Python Version](https://img.shields.io/pypi/pyversions/matplotlib?color=lightblue&label=Python&logo=python&logoColor=lightblue&style=for-the-badge)](https://python.org/)

# Physics Experiment Analysis Tool

The Physics Experiment Analysis Tool is a Python application that simplifies the process of analyzing and plotting the results of physics experiments. The application reads observation tables from a CSV file and generates a graph based on the data.
## Features

- Read observation tables from a CSV file and parse the data
- Calculate the result of the experiment based on the observation data
- Plot the graph of the data using Matplotlib
- Save the graph to a PNG file
- Provide a graphical user interface built using Tkinter for ease of use
## Usage

To use the application, simply open the GUI by running the main.py file, select the CSV file containing your observation table, and choose the type of experiment you conducted. The application will calculate the result and plot the graph for you automatically.


## Installation

Clone the repository: 
```console
git clone https://github.com/Duisternis/Physics-Experiment-Analysis-Tool.git
```
Install the dependencies: 
```console
pip install -r requirements.txt
```
Run the application: 
```console
python main.py
``` 

### Note :
- Information regarding the different csv files can be accessed using [csv_info](/csv_files/csv_files.md).
- PDF files are provided for the different experiments featured in this application.
- CSV files with sample readings are provided in [csv_files](/csv_files/) folder.
- `content_1.csv` - here '1' shows which experiment csv file belongs to. _(compare it with dropdown choices - shown in screenshots)_

**WARNING -** Choose the designated csv files for a perticular experiment. Choosing any other file will result in unwanted outputs.


## Screenshots (how to use the application)

**STEP - 1:** Choose an experiment from the drop down, and browse the corresponding csv file.

  ![App Screenshot](/screenshots/tut_1.png)

**STEP - 2:** Click on submit button.

  ![App Screenshot](/screenshots/tut_2.png)
  
**STEP - 3:** Navigate between different graphs and tables through navigation pane.

  ![App Screenshot](/screenshots/tut_3.png)
  ![App Screenshot](/screenshots/tut_4.png)


## Authors

The Physics Experiment Analysis Tool was created by [@Duisternis](https://www.github.com/Duisternis) as a project for [Engineering Physics Lab -II | [Jaypee University of Information Technology](https://www.juit.ac.in)].

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the [LICENSE](/LICENSE.md) file for details. You are free to use, modify, and distribute this software for any purpose, as long as you include the original copyright and license notices in any copy of the software. This software is provided "as is," without warranty of any kind, express or implied.
