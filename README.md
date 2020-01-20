## GEOG5990Assessment2
#### Repository of GEOG5990 Assessment 2 material

This application reads .radar and .lidar files in order to identify the location of icebergs within them, assess their towability and display the outcomes, including the iceberg metadata (size and weight), on a GUI.

## Getting Started
This model was created in Spyder (Anaconda3). The version of python is version 3.7.

### Repository Contents
1. **LICENSE**: GNU General Public License v3.0
2. **icebergchecker_gui.py**: Main code
3. **test.lidar**: lidar grid created with one known iceberg for test purposes
4. **test.radar**: radar grid created with one known iceberg for test purposes
5. **white1.lidar**: lidar grid representing a 300 by 300 area of the sea with a single iceberg in
6. **white1.radar**: radar grid representing a 300 by 300 area of the sea with a single iceberg in
7. **white2.lidar**: lidar grid representing a 300 by 300 area of the sea with multiple icebergs in
8. **white2.radar**: radar grid representing a 300 by 300 area of the sea with multiple icebergs in
9. ________ SHORT DOCUMENT ________
10. **README.md**: this file is the README.md file - it explains the contents of the GEOG5990Assessment2 repository


### Prerequisites
Download the relevant files from this repository into your personal folder:
* icebergchecker_gui - main code which reads a lidar and radar file to identify if ice is present and return metadata about identified icebergs
* one .lidar and one .radar tile - a corresponding pair of lidar and radar files

If using Spyder, the backend may need to be change in order for matplotlib to render the graphics succesfully. For this application, "Inline" graphics are suitable. This can be set in Spyder by selecting 'Tools' > 'Preferences' > 'IPython console' > 'Graphics' > adjust the backend drop-down list to read Inline > Apply > OK > Restart Spyder

## Running the model
The model can be run from the command prompt by navigating to the current working directory and typing 'python icebergchecker_gui.py'.

Alternatively, the model can be run from within a programming software, such as Spyder.

Once the GUI is visible a figure displaying iceberg locations and their tow-ability will already be avaialble. To view the tow-ability values of each of the icebergs identified the user should choose 'Show tow-ability values' in the drop down menu or click the "Show tow-ability values" button.

### Expectations
Once the model is opened, a GUI will appear displaying a figure of iceberg locations and their tow-ability (as shown by colours where red is not towable and green is towable on a blue 'ocean' background). 

To view the tow-ability values of each of the icebergs identified the user should choose 'Show tow-ability values' in the drop down menu or click the "Show tow-ability values" button. Upon pressing this button, two lines will appear for each iceberg identified. The first line will show the iceberg number, size in meters cubed, and weight in kg. The second line will the iceberg number and whether it "is towable" or "is NOT towable".

## Closing the model
To close the model, the user can choose 'Exit model' in the drop down menu or click the "Exit" button.

## Checks
A collection of checks have been commented into the model. To make checks, please uncomment them and re-run the model.

* lines 33 & 34: print number of rows and columns identified in .radar grid (and subsequently .lidar grid as they are the same size)
* lines 36 - 38: check the .radar data has correctly been read by displaying it as a figure in the console
* lines 49 - 51: check the .lidar data has correctly been read by displaying it as a figure in the console
* line 82: check function is reading each cell of the .radar file
* line 105: check the berg_footprint function has successfully been called
* lines 125, 129 & 134: check the berg_footprint function is responding to each cell it is looking at as expected
* lines 144 - 146, 148, 153 & 156: check berg_footprint is sucessfully cumulatively adding to the iceberg's total height and looping correctly onto the next cell
* lines 226, 239, 243, 245, 249, 252, 255 & 258: check the berg towability data grid is being assigned tow-ability values correctly and that each iceberg and the cells within are being looped through correctly

## Potential further development / areas of improvement
This model assumes the mass density of ice will always be 900 kg/m3.

This model was designed under the assumption that icebergs are always regular cuboids. Future development would include the repeat of the ideas in lines 121 - 134 (of icebergchecker_gui.py) to calculate the dimension of the iceberg for number of rows instead of number of columns.

## Author
R Martin, gy19rgm, University of Leeds


## License
This project is licensed under the GNU General Public License v3.0 - see the [License.md](https://github.com/gy19rgm/GEOG5990Assessment1/blob/master/LICENSE) file for further details