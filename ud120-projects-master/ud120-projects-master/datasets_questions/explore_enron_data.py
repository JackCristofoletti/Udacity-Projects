#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import numpy as np
import pandas

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
names = pandas.read_csv( "../final_project/poi_names.txt" )
#pois
print names.shape
df = pandas.DataFrame( enron_data )
#size and features
poi_count = 0
salary_nan_count = 0
email_nan_count = 0
for person in enron_data:
	if df[person]["poi"]:
		poi_count = poi_count + 1
	if df[person]["salary"] != np.nan:
		salary_nan_count = salary_nan_count + 1
	if df[person]["email_address"] !="":
		email_nan_count = email_nan_count + 1
		
print salary_nan_count
print email_nan_count
		
#print df["PRENTICE JAMES"]
#print df["COLWELL WESLEY"]
#print df["SKILLING JEFFREY K"]