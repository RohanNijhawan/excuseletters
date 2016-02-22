excuseletters.py is the script I use to create correctly formatted tables for use by UC Berkeley's ASUC. 

There is some basic error handling and some fault tolerance. However, the code is by no means bulletproofed. 

Features:
	.> Automatically builds dictionary from a pickled (serialized) file; if none is found a new one is created based on user input
	.> Optionally generates data for the entire week, or just Mondays/Fridays
	.> Provides informative command line readouts

Future additions:
	.> Allow for modification of the pickled dictionary; for example to correct spelling errors
	.> Add image parsing capabilities - currently only works with plaintext
