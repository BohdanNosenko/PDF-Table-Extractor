# PDF Table Extractor

PDF Table Extractor is a Python program that allows users to extract tables from PDF files and export them to XLSX file. This program uses the [**customtkinter**](https://pypi.org/project/customtkinter/) library to provide a modern Graphical User Interface (GUI) and uses the [**tabula-py**](https://pypi.org/project/tabula-py/) library to read PDF files and extract tables, and the [**pandas**](https://pypi.org/project/pandas2/) library to create Excel documents.

![img](/images/GUI.png)

## Installation

Before running the program, make sure you have Python 3.x installed on your computer. Clone this repository and install the required dependencies using the following command:

```python
pip install -r requirements.txt
```

## How to Use
Once you have installed the required dependencies, you can run the program by running the following command:

```python
python main.py
```

This will open up the PDF Table Extractor GUI. To extract tables from a PDF file, follow these steps:

1. Click on the "Select PDF File" button to select the PDF file you want to extract tables from.
2. Click on the "Convert" button to extract the tables from the selected pages.
3. New XLSX file containing all tables from selected PDF file will be saved in the same directory as the original file.

## Contributing
If you want to contribute to this project, feel free to create a pull request or submit an issue. I welcome contributions from anyone who wants to improve the program or add new features.

## License
This program is licensed under the MIT License. See the [LICENSE](/LICENCE) file for more details.
