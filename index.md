# Python for GIS and Geoscience

## Introduction

An important aspect of daily work in geographic information science and earth sciences is the handling of potentially large amounts of data. Reading in spatial data, exploring the data, creating visualisations and preparing the data for further analysis may become tedious tasks. Hence, increasing efficiency and reproducibility in this process without the need of a GUI interface is beneficial for many scientists. The usage of high-level scripting languages such as R and Python are increasingly popular for these tasks thanks to the development of GIS oriented packages.

This course trains students to use Python effectively to do these tasks, with a focus on geospatial data. It covers both vector and raster data. The course focuses on introducing the main Python packages for handling such data (GeoPandas, Xarray, Rasterio) and how to use those packages for importing, exploring, visualizing and manipulating geospatial data. It is the aim to give the students an understanding of the data structures used in Python to represent geospatial data (geospatial dataframes, (multi-dimensional) arrays and composite netCDF-like multi-dimensional datasets), while also providing pointers to the broader ecosystem of Python packages for GIS and geosciences.

The course has been developed as a specialist course for the Doctoral schools of Ghent University, but can be taught to others upon request.

## Course info

### Aim & scope

This course targets researchers that want to enhance their general data manipulation and analysis skills in Python specifically for handling geospatial data.

The course does not aim to provide a course in specific spatial analysis and statistics, cartography, remote sensing, OGC web services, ... or general Geographical Information Management (GIS). It aims to provide researchers the means to effectively tackle commonly encountered spatial data handling tasks in order to increase the overall efficiency of the research. The course does not tackle desktop GIS Python extensions such as arcpy or pyqgis.

### Program

The course is organized as a three day course with following program:

- **Day 1** - Setting up the programming environment with the required packages using the conda package manager and introduction to GeoPandas and related packages to work with geospatial vector data.
- **Day 2** - More advanced features of GeoPandas for spatial joins and overlays. An introduction to xarray for working with raster data. Combining raster and vector data and more advanced plotting. The acquired skills will immediately be brought into practice to handle real-world data sets.
- **Day 3** - The use of xarray for spatial data cubes (netcdf-like) and out-of-memory raster data. Case studies to apply the learned skills of the full workshop. Interactive visualisation of spatial data. The day will end with an overview of other packages that are being used in the geospatial Python ecosystem (other visualization frameworks, specialized GIS oriented packages).

## Getting started

The course uses Python 3, data analysis packages such as Pandas, Numpy and Matplotlib and geospatial packages such as GeoPandas, Rasterio and Xarray. To install the required libraries, we highly recommend Anaconda or miniconda (<https://www.anaconda.com/download/>) or another Python distribution that includes the scientific libraries (this recommendation applies to all platforms, so for both Window, Linux and Mac).

For detailed instructions to get started on your local machine , see the [setup instructions](./setup.md).

In case you do not want to install everything and just want to try out the course material, use the environment setup by Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jorisvandenbossche/DS-python-geospatial/master) and open de notebooks rightaway.

## Slides

For the course slides, click [here](https://jorisvandenbossche.github.io/DS-python-geospatial/slides.html).


## Contributing

Found any typo or have a suggestion, see [how to contribute](./CONTRIBUTING.html).


## Meta
Authors: Joris Van den Bossche, Stijn Van Hoey

<img src="img/logo_flanders+richtingmorgen.png" width="79%">
<img src="img/doctoralschoolsprofiel_hq_rgb_web.png" width="20%">



