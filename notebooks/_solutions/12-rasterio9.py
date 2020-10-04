# Apply function to all files in the directory
from pathlib import Path
for file in Path("./data/gent/raster").glob("*.tiff"):
    print(f"Converting {file.name}...")
    resample_raster_file(file, Path(f"./{file.name}_resampled.tiff"), Resampling.bilinear, scaling_factor=2)    