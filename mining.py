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
import math

stock_data = []
monthly_averages = []
date_details = []
six_best_months = []
six_worst_months = []
# places a tuple for each entry


def read_stock_data(stock_name, stock_file_name):
    """
   reads stock data from json file
    :param stock_name
    :param stock_file_name: The name of a JSON formatted file that contains monthly stock data
    :return: lists of tuples contain month and monthly average
    """
    # Reads data from the given json file
    stock_file = read_json_from_file(stock_file_name)
    total_sales_list = []
    total_volume_list = []
    month_groups = list()

    #loops to group the data in this list by month and year
    for key, items in itertools.groupby(stock_file,
                                        lambda p: datetime.datetime.strptime(p['Date'], "%Y-%m-%d").strftime("%Y/%m")):
        month_groups.append(list(items))

<<<<<<< HEAD
        #inner-loop to go through each month list and calculate total sales and volume
=======
>>>>>>> origin/master
        for value in items:
            total = sum([int(value["Volume"])*float(value["Close"])])
            total_sales_list.append((key, total))
            total_volume = sum([int(value["Volume"])])
            total_volume_list.append((key, total_volume))
        size = len(total_sales_list)

        index = 0
        # iterates through total sales_length  and divide each item in this list by items in total volume list
        for index in range(size):
            if total_sales_list[index][0] == total_volume_list[index][0]:
                monthly_averages.append((total_sales_list[index][0], total_sales_list[index][1] /
                                         total_volume_list[index][1]))
                index += 1

    return monthly_averages


def six_best_months():
    """
    sorts monthly averages according to highest six months averages
    :return: list of tuples contains six months with six dates
    """
<<<<<<< HEAD
    # sorting data in monthly averages from best to worst months
    sorted_list = sorted(monthly_averages, key=operator.itemgetter('Date'))

    # slicing sorted list to get the best six monthly averages
    best_months = sorted_list[:6]
    
    # adding best_months into a list of tuples which include date and month
=======
    sorted_list = sorted(monthly_averages, key=operator.itemgetter('Date'))
    best_months = sorted_list[:6]
>>>>>>> origin/master
    six_best_months.append(monthly_averages['Date'], best_months)
    return six_best_months


def six_worst_months():
    """
    sorts monthly averages according to lowest six months averages
    :return: list of tuples contains six months with six dates
    """
<<<<<<< HEAD
    # sorting data in monthly averages from worst to best months
    sorted_list = sorted(monthly_averages, key=operator.itemgetter('Date'))
    worst_months = sorted(sorted_list[6:], key=operator.itemgetter('Date'))

    # slicing sorted list to get the worst six monthly averages
=======
    sorted_list = sorted(monthly_averages, key=operator.itemgetter('Date'))
    worst_months = sorted(sorted_list[6:], key=operator.itemgetter('key'))
>>>>>>> origin/master
    six_worst_months.append(monthly_averages['Date'], worst_months)
    return six_best_months


def read_json_from_file(file_name):
    """
    :param file_name:
    :return:
    """
    with open(file_name) as file_handle:
        file_contents = file_handle.read()
<<<<<<< HEAD
=======
        #Reads the file into a dictionary

>>>>>>> origin/master
    return json.loads(file_contents)

# keeping this line to see what the function eventually displays (as a test)
x = read_stock_data("GOOG", "data/GOOG.json")
print(x)

