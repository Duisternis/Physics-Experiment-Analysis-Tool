
![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

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
```
git clone https://github.com/Duisternis/Physics-Experiment-Analysis-Tool.git
```
Install the dependencies: 
```
pip install -r requirements.txt
```
Run the application: 
```
python main.py
``` 

### Note :
- Information regarding the different csv files can be accessed using csv_info.
- PDF files are provided for the different experiments featured in this application.
- CSV files with sample readings are provided in csv_files folder.
- `content_1.csv` - here '1' shows which experiment csv file belongs to. _(compare it with dropdown choices - shown in screenshots)_

**WARNING -** Choose the designated csv files for a perticular experiment. Choosing any other file will result in unwanted outputs.


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)
![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Authors

The Physics Experiment Analysis Tool was created by [@Duisternis](https://www.github.com/Duisternis) as a project for [Engineering Physics Lab -II | [Jaypee University of Information Technology](https://www.juit.ac.in)].

## License

[MIT](https://choosealicense.com/licenses/mit/)