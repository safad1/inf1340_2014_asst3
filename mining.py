#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime

stock_data = []
monthly_averages = []
date_details = []

def read_stock_data(stock_name, stock_file_name):
    """
   reads stock data from json file
    <<<<<<< HEAD
    :param stock_name
    :param stock_file_name: The name of a JSON formatted file that contains monthly stock data
    :return: List of strings. it returns stock data
    """
    file_data = read_json_from_file(stock_file_name)

    for data in file_data:
        date = data['date']
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        date_month = date.month
        date_year = date.year
        date_details.append(date_month, date_year)
        close = data['close']
        volume = data['volume']
        stock_data.append(date, close, volume)

    return stock_data


def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)

