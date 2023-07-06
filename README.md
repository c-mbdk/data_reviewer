# data_reviewer

## About this project
This project checks a source (csv) file for missing values in important columns and checks the source file against another lookup (csv) file. All negative observations are detailed in a timestamped log file e.g., "Null value present in this column in this row", "No match found for this value". The main application requires some user input to determine which columns in the main source file should be checked for missing values and which column should match with the lookup file.

## Background
The inspiration for this tool came from the manual task of reviewing rejections from another ETL using multiple files. It was originally meant to be more customised towards the logic in the transformation part of the ETL. However, during development, it became clear that a more generic template would be more valuable. It is still possible to customise this further. But this is a good base.

The main application executes a couple of clean-up functions, which include moving the files in the source_file, lookup_files event_logs directories into the archive folder.

## Future enhancements
At the moment, the check of the source file against the lookup file assumes the values should be integers. This needs to be updated.

The check against the lookup file also assumes the 'matching' column is the first column of the lookup csv file. This isn't an unrealistic assumption, but it should be more flexible.

Although Pandas is excellent for data analysis with smaller datasets, the slow performance and long runtime experienced with larger datasets means there is a limit to how useful this tool can be. 

Originally, the tool was developed using Dask, a parallel computing library which is perfect for large datasets. But there were difficulties when trying to implement one of the key features of the tool. Instaed of scrapping the project, the approach was changed to stick with NumPy and Pandas. There are still improvements that can be with the current approach e.g., reading the csv file in chunks and filtering out unnecessary columns.

But the original vision is still important. The manual task that inspired the tool's creation involved reviewing csv files with hundreds of thousands of rows. The goal was to make it as quick as possible. So, in the future, redesigning the tool with Dask will be explored.

## How to Run

1. Install virtualenv:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```