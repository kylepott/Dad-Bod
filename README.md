# Dad-Bod
Wrangle and clean MyFitnessPal exported data then analyze it using Prophet by Facebook to predict your future weight.  Or in my case, to predict when you will get an official Dad Bod.

# Dependencies
* Python 3
* Pandas
* Numpy
* Prophet
* Plotly
* Xlrd
* Xlwt

# How to
0. Personally, I think the easiest way to run this program is to install Jupyter and run it within a Jupyter notebook.  In this repository I have included an HTML export of the Jupyter notebook I used so you can follow my work in detail if you'd like. 
1. Export your weight data from MyFitnessPal.com
2. Rename your MyFitnessPal data mfp.xlsx
3. Run clean_mfp.py from the same directory as mfp.xlsx to clean up, organize, and sort your weight data. It should output a file titled "MFPClean.xlsx"
4. Run mfp_prophet.py from the same directory as MFPClean.xlsx.

# More information
I wrote a lengthy blog post about this which you can read at https://technicalagain.com.  I can be contacted at kylepott@gmail.com.
