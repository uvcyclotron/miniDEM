Hypsomteric tint Topographic map to 3D model generator
===========================================


Generates topographic 3D model of land using a hypsometric map (a contour map with differently tinted land areas). Inspired from the [original Paper](http://www.researchgate.net/publication/27646342_VRML_generator_of_land_features_3D_representation_based_on_a_hypsometric_map) by W. Pasternak and Z. Latala.

###Tools used:
+ Python 2.7
+ Maya 2013

###Python dependencies:
+ numpy 1.8.1
+ openCV 2.4.8
+ matplotlib 1.3.0
+ colorama 0.2.7
+ json

####Module1:

**Input:** 

Any hypsometric contour map using the standard color ramp, ranging from 
`dark blue>blue >cyan>green>yellow>orange>red` , would be suitable for use in this program. The color ramp data can be easily modified to accommodate maps using a different color ramp.
Currently the standard color ramp is being used. 


![Sample input](https://dl.dropboxusercontent.com/u/10667631/Work/f4.png "Sample Input")
Sample input map


![Overlaid with 4x4 mesh](https://dl.dropboxusercontent.com/u/10667631/Work/f4_2.png "Overlaid with 4x4 mesh")
Sample input map overlaid with 4x4 mesh


**Output:**

The mapped color ramp index for each vertex pixel’s color is written to the output file 'meshdata.txt'.

And terminal output: 
The output is colored with similar colours to mimic the input map. Sample 50x50 output included in repository.

	yellow	yellow	green	cyan	skblue
	yellow	yellow	green	cyan	skblue
	orange	orange	yellow	green	cyan
	dkorng	dkorng	yellow	green	cyan
	dkorng	red		orange	yellow	cyan


####Module2:

**Input:**
The text output from module1 : *meshdata.txt*

**Output:**
a 3D polygonal mesh model of the topographic land map.

The below sample output is for the 4x4 mesh data. 
![Sample mesh output](https://dl.dropboxusercontent.com/u/10667631/Work/sample_out.jpg "Sample 4x4 mesh output")

The below sample output is for the 50x50 mesh data, for the same input map.
![Output for 50x50 mesh](https://dl.dropboxusercontent.com/u/10667631/Work/out50x50.png "Output for 50x50 mesh")


###How to Run:

1.	Install all the python dependencies mentioned above for the respective modules.
2.	Run the module1 python script, obtain the meshdata.txt
3.	Ensure that path for meshdata.txt in module 2 is correct, if not so correct it.
4.	Open Maya 2013, and go to the Script Editor
5.	Copy the module2 program to the script editor and run it.
6.	The final model will be generated on screen
7.	Go to Shading submenu and apply Smooth shading/flat shading if desired.

The actual sample input and output model is also included in the repository.


###Possible future improvements:

+	Add support for maps with black contour lines. Currently only borderless contour maps work.
+	A small module to automatically get the color palettle for any custom colour ramps used.
