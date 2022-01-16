# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains two helper functions for loading and saving CSV files,
and one helper function to create a directory in case it doesn't exist.

"""
import csv
from pathlib import Path
import os


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        1. A list of lists that contains the rows of data from the CSV file.
        2. The header of the csv input file in csvpath

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Read the CSV data
        for row in csvreader:
            data.append(row)

        header=data[0]
        n=len(data)
        data=data[1:n]
    return data, header


def save_csv(csvpath, data, header):
    """Save data & header as a csv output file in the path provided.

    Args:
        csvpath (Path): The csv file-path where the output data will be saved
        data (list of list): list of list with the same number of elements that can be strings and/or numeric values
        header: a proper header for the 'data' argument
    
    Additional outputs:
        It indicates whether the file will be override or created

    Returns:
         The absolute csvpath to the file with the data output
    """

    #Verify that path exist, and inform user
    if csvpath.exists():
        print("This file currently exist, and it will be overwritted.")
    else:
        print(f"\n This file does not exist currently, so it will be created. \n\n")
        csvpath=Path(create_path(csvpath))

    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Export the header
        csvwriter.writerow(header)

        # Write the CSV data in the csvfile
        for row in data:
            csvwriter.writerow(row)
        print(f"\n Data has been exported to the following path:\n {csvpath} \n\n")
    return(csvpath)


def create_path(path):
    """
    This function receives a path and creates the directory in the case it doesn't exist
    
    Arg:
        csvfile (Path): path to a file
    
    Return: 
        created_path: absolute Path to a created file
    """  
    # Split the path in 
    # dir and csvfile pair
    abs_path=os.path.abspath(path)
    dir_file = os.path.split(abs_path)

    dir_alone=dir_file[0]
    file_alone=dir_file[1]

    if not os.path.exists(dir_alone):
        os.makedirs(dir_alone)

    created_path=os.path.join(dir_alone, file_alone)

    return(created_path)




