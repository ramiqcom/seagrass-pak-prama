from subprocess import check_call
from tempfile import TemporaryDirectory

temp_folder = TemporaryDirectory(delete=False)

data_prefix = "data/KMZ/*.kmz"
output = "output/seagrass_plot"

check_call(
    f"""ogrmerge \
      -single \
      -nln seagrass_plot \
      -f "ESRI Shapefile" \
      -lco SPATIAL_INDEX=YES \
      -o {output} \
      {data_prefix}
  """,
    shell=True,
)
