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
import itertools
import operator
import pprint


stock_data = []
monthly_averages = []
date_details = []
#places a tuple for each entry

def read_stock_data(stock_name, stock_file_name):
    file_data = read_json_from_file(stock_file_name)
    """
   reads stock data from json file
    <<<<<<< HEAD
    :param stock_name
    :param stock_file_name: The name of a JSON formatted file that contains monthly stock data
    :return: List of strings. it returns stock data
    """
    #iterates over data in the given json file
    for data in file_data:
<<<<<<< Updated upstream
        stock_date = datetime.datetime.strptime(data["Date"], "%Y-%m-%d").strftime("%Y/%m")
        data['Date'] = stock_date
=======
        stock_date = datetime.datetime.strptime(data['Date'], '%Y-%m-%d').strftime('%Y/%m')
        data['Date'] = stock_date

        print(stock_date)

>>>>>>> Stashed changes
        sorted_data = []
        total_sales_list = []
        total_volume_list = []
        file_data.sort(key=operator.itemgetter('Date'))

        for key, items in itertools.groupby(file_data, operator.itemgetter('Date')):
<<<<<<< Updated upstream
            sorted_data.append(list(items))
<<<<<<< HEAD
=======
            sorted_data.append(items)
>>>>>>> Stashed changes

        date_list = []
        for item in sorted_data:
            month = item[0]['Date']
            size = len(item)
        total = 0
        for k in range(size):
            total += int((item[k]['Volume'])*(item[k]['Close']))
<<<<<<< Updated upstream
            total_sales_list.append((month, total))
        print(total_sales_list)
=======
        for monthly_data in sorted_data:
            monthly_close = []
            monthly_volume = []
            monthly_close.append(monthly_data['close'])
            monthly_volume.append(monthly_data['volume'])
          
>>>>>>> origin/master
    return stock_data
=======
            total_sales_list.append(month, total)
        print(total_sales_list)

        for monthly_data in sorted_data:
            monthly_close = []
            monthly_volume = []
            monthly_close.append(monthly_data['Close'])
            monthly_volume.append(monthly_data['Volume'])
>>>>>>> Stashed changes

    return stock_data


def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)


<<<<<<< Updated upstream
x = read_stock_data("GOOG", "data/GOOG.json")
print(x)
=======
#keeping this line to see what the function eventually displays (as a test)
x = read_stock_data("GOOG", "data/GOOG.json")
print(x)
>>>>>>> Stashed changes
