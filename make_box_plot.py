# creates a box plot for a sample of results from both the congruent and
# incongruent Stroop test.  Starting point for the code was
# blog.bharatbhole.com/creating-boxplots-with-matplotlib/

import csv
import matplotlib as mpl

## for creating plot as png file
mpl.use('agg')

import matplotlib.pyplot as plt

congruent = []
incongruent = []
skipline = True
with open('stroopdata.csv') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=',')
    for row in rowreader:
        if skipline:
            skipline = False
        else:
            congruent.append(float(row[0]))
            incongruent.append(float(row[1]))

data_to_plot = [congruent[1:], incongruent[1:]]

# create a figure instance
fig = plt.figure(1, figsize=(9,6))

# create an axis instance
ax = fig.add_subplot(111)

# create the boxplot
bp = ax.boxplot(data_to_plot)

# save the figure
fig.savefig('boxplot.png', bbox_inches='tight')
