## GEOG5990Assessment2
#### Repository of GEOG5990 Assessment 2 material

This application reads radar and lidar files in order to identify the location of icebergs within them, assess their tow-ability and display the outcomes, including the iceberg metadata (size and weight), on a GUI.

## Getting Started
This model was created in Spyder (Anaconda3). The version of python is version 3.7.

### Repository Contents
1. **LICENSE**: GNU General Public License v3.0
2. **README.md**: this file is the README.md file - it explains the contents of the GEOG5990Assessment2 repository
3. **icebergchecker.py**: working code that checks ocean for icebergs and displays all outputs to the console
4. **icebergchecker_gui.py**: MAIN working code that checks ocean for icebergs and displays outputs to the console and GUI
5. **white1.lidar**: lidar grid representing a 300 by 300 area of the sea with a single iceberg in
6. **white1.radar**: radar grid representing a 300 by 300 area of the sea with a single iceberg in
7. **whitelinesingle.jpg**: jpg version of white1.lidar
8. **whitelinesingle.png**: png version of white1.lidar
9. **white2.lidar**: lidar grid representing a 300 by 300 area of the sea with multiple icebergs in
10. **white2.radar**: radar grid representing a 300 by 300 area of the sea with multiple icebergs in
11. **whitelinemulti.jpg**: jpg version of white2.lidar
12. **whitelinemulti.gif**: gif version of white2.lidar
13. **GEOG5990_Assessment2.docx**: short document detatiling additional documentation about the repository - includes the intention of the software, designing the program, software development and resolved issues, general sources used and known errors and areas of improvement
14. **icebergmetadata.txt**: copy of the text document created in lines 289 - 303 of icebergchecker_gui.py
15. **UML_diagram.png**: UML activity diagram of icebergchecker_gui.py

### Prerequisites
Download the relevant files from this repository into your personal folder:
* icebergchecker_gui - main code which reads a lidar and radar file to identify if ice is present and return metadata about identified icebergs
* one radar and lidar files - these two files must be a corresponding pair of lidar and radar files. **If providing personal radar and lidar files, the user MUST change the name of the input file in iceberg.py. Change line 22 for the radar file and line 41 for the lidar file.**

If using Spyder, the backend may need to be change in order for matplotlib to render the graphics succesfully. For this application, "Inline" graphics are suitable. This can be set in Spyder by selecting 'Tools' > 'Preferences' > 'IPython console' > 'Graphics' > adjust the backend drop-down list to read Inline > Apply > OK > Restart Spyder

## Running the model
The model can be run from the command prompt by navigating to the current working directory and typing 'python icebergchecker_gui.py'.

Alternatively, the model can be run from within a programming software, such as Spyder.

Once the GUI is visible a figure displaying iceberg locations and their tow-ability will already be avaialble. To view the tow-ability values of each of the icebergs identified the user should choose 'Show tow-ability values' in the drop down menu or click the "Show tow-ability values" button.

### Expectations
Once the model is opened, a GUI will appear displaying a figure of iceberg locations and their tow-ability. Berg tow-ability is shown through colour where red is not towable, green is towable and blue is the 'ocean' background. (See GEOG5990_Assessment2.docx for further information on this figure.)

To view the tow-ability values of each of the icebergs identified the user should choose 'Show tow-ability values' in the drop down menu or click the "Show tow-ability values" button. Upon pressing this button, two lines will appear for each iceberg identified. The first line will show the iceberg number, size in meters cubed, and weight in kg. The second line will show the iceberg number and whether it "is towable" or "is NOT towable". The icebergs are numbered by the order in which the top left cell appears when reading the grid as one would read a 100 number square.

Upon running the program a text file called icebergmetadata.txt will be saved into the personal folder you are working in. This text file will contain the textual information about iceberg number, size, weight and tow-ability.

## Closing the model
To close the model, the user can choose 'Exit model' in the drop down menu or click the "Exit" button.

## Checks
A collection of checks have been commented into the model. To make checks, please uncomment them and re-run the model.

* lines 33 & 34: print number of rows and columns identified in .radar grid (and subsequently .lidar grid as they are the same size)
* lines 36 - 38: check the .radar data has correctly been read by displaying it as a figure in the console
* lines 50 - 52: check the .lidar data has correctly been read by displaying it as a figure in the console
* lines 90 & 99: check function is reading each cell of the .radar file
* line 125: check the berg_footprint function has successfully been called
* lines 145, 149 & 154: check the berg_footprint function is responding to each cell it is looking at as expected
* lines 164 - 166, 168, 173 & 176: check berg_footprint is sucessfully cumulatively adding to the iceberg's total height and looping correctly onto the next cell
* lines 250, 261, 264, 266, 270, 273, 276 & 279: check the berg tow-ability data grid is being assigned tow-ability values correctly and that each iceberg and the cells within are being looped through correctly

## Potential further development / areas for improvement
This model assumes the mass density of ice will always be exactly 900 kg/m3.

This model was designed under the assumption that icebergs are always regular cuboids. Future development would include the repeat of the ideas in lines 141 - 154 (of icebergchecker_gui.py) to calculate the dimension of the iceberg for number of rows instead of number of columns.

See GEOG5990_Assessment2.docx for more detailed information on future development and areas for improvement.

## Author
R Martin, gy19rgm, University of Leeds

## License
This project is licensed under the GNU General Public License v3.0 - see the [License.md](https://github.com/gy19rgm/GEOG5990Assessment2/blob/master/LICENSE) file for further details