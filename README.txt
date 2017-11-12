Michael Bido-Chavez (euid: mb0501)
CSCE 4444 - Fall 2017
Homework 1 - Program
Due Nov 4 by Midnight

______________________________
Files/Directories

setup.sh
runPython.sh
scraper.py
chromedriver
cnn-instance (this directory contains the webpage and example results)

______________________________
Description

This program creates an instance of Chrome to load the dynamic elements
of CNN's webpage. Then, using selenium's webdriver, finds instances of divs
of class zn_containers. Then, for each of the divs inside them, select 
the text nested inside that falls under the category of Tech, Entertainment or
Travel. From the script that runs this, the data is fowarded into an ouput file.
______________________________

EXAMPLE DEMONSTRATION: (sorry about it being so quiet)
https://youtu.be/DyHRaus0rpE

______________________________
Setting up the enviorment

This Python file was tested under a virtual enviorment to isolate installs. 
The appropriate packages were also installed to work with this project. Ensure 
that Python and Chrome are installed in your local machine, this was tested 
within an OSX/Linux machine. 

To create an enviorment suitable for virtualenv, enter the attached folder in
the terminal and then run the following lines in the terminal (sudo pip install
virtualenv is a part of the script, so it will prompt you for a password):

./setup.sh
source new_app/bin/activate
pip install selenium

This will set up a local enviornment with virtualenv and then install the correct
package. Since it is a virtual enviorment, these install will not affect the global
bin. This will also activate it. This can be deactivated with 'deactivate', which will 
be done later.
______________________________
______________________________
Running the code

To run the python script, run the following line in terminal (it will take a moment 
as all of the javascript must finish running on the webpage):

./runPython.sh

After this is done running, the results of the program will be located inside 'results.txt'
To exit the virtual enviroment, type:

deactivate

You now have your data outside and you are done with the enviorment!
______________________________
______________________________
Useful documentation:

http://sourabhbajaj.com/mac-setup/Python/virtualenv.html
http://selenium-python.readthedocs.io/installation.html

______________________________