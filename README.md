	
	## Users Guide

	### Import Data

	* You can simply drag and drop a file on the *Drag and Drop or Select Files* area.
	* You can browse to the file by clicking on the *Drag and Drop or Select Files* area.

	### Supported Extensions

	* xls, xlsx, csv, txt, tsv etc.
	* UTF-8 supported

	### Interactive Chart

	#### Legend

	* You can toggle chart elements by clicking on the legend.

	#### Chart Tools (from left to right)

	* SaveTool - The save tool pops up a modal dialog that allows the user to save a PNG image of the plot.
	* BoxZoomTool - The box zoom tool allows the user to define a rectangular region to zoom the plot bounds too, by left-dragging a mouse, or dragging a finger across the plot area.
	* PanTool - The pan tool allows the user to pan the plot by left-dragging a mouse or dragging a finger across the plot region.
	* BoxSelectTool - The box selection tool allows the user to define a rectangular selection region by left-dragging a mouse, or dragging a finger across the plot area.
	* LassoSelectTool - The lasso selection tool allows the user to define an arbitrary region for selection by left-dragging a mouse, or dragging a finger across the plot area.
	* ZoomInTool - The zoom-in tool will increase the zoom of the plot.
	* ZoomOutTool - The zoom-out tool will decrease the zoom level of the plot.
	* AutoscaleTool - The autoscale tool will fit the plot to screen.
	* ResetAxesTool - The reset axes tool (home) will restore the plot ranges to their original values.
	* ToggleSpikeLinesTool - The toggle spike lines tool will specify the points location on both axes.
	* ShowClosestTool - The show closest tool will show the closest datapoint on hover
	* CompareTool - The compare tool will compare data on hover.

	### Data Format

	* The data must be represented in a tabular format.
	* The target variable should be in a single column. It should be the first or second column.
	* The data can have header.
	* The first column can contain the indices of  measurement/statistic (e.g. order, timestamp)

	## About Control Chart

	Control charts, also known as Shewhart charts or process-behavior charts, are a statistical process control tool used to determine if a manufacturing or business process is in a state of control. It is more appropriate to say that the control charts are the graphical device for Statistical Process Monitoring (SPM).
	A control chart consists of: 
	* Points representing a statistic (e.g., a mean, range, proportion) of measurements of a quality characteristic in samples taken from the process at different times (i.e., the data)
	* The mean of this statistic using all the samples is calculated (e.g., the mean of the means, mean of the ranges, mean of the proportions)
	* A center line is drawn at the value of the mean of the statistic
	* The standard deviation of the statistic is also calculated using all the samples
	Upper and lower control limits (sometimes called "natural process limits") that indicate the threshold at which the process output is considered statistically 'unlikely' and are drawn typically at 3 standard deviations (*3xSigma*) from the center line (*Mean*). 
	Sometimes a business process requires a measurement to lie between predetermined bounds, hence "artificial process limits" are also useful such as *User Specified Upper Limit* and *User Specified Lower Limit*.

	Developped in 
	![Python](https://img.shields.io/badge/Python-v3.6-blue.svg?logo=python&longCache=true&logoColor=white&style=flat-square&colorA=4c566a&colorB=5e81ac)
	![Plotly](https://img.shields.io/badge/Plotly-v4.13.0-blue.svg?logo=python&longCache=true&logoColor=white&style=flat-square&colorA=4c566a&colorB=5e81ac)
	![Pandas](https://img.shields.io/badge/Pandas-v1.1.4-blue.svg?logo=pandas&longCache=true&logoColor=white&style=flat-square&colorA=4c566a&colorB=B48EAD)
	by *Robert Vizi*
