from subprocess import check_call
from tempfile import TemporaryDirectory

temp_folder = TemporaryDirectory(delete=False)

data_prefix = "data/KMZ/*.kmz"
output = "output/seagrass_plot.fgb"

tmp_merge = f"{temp_folder.name}/merged.fgb"
check_call(
    f"""ogrmerge \
      -single \
      -nln seagrass_plot \
      -f "FlatGeobuf" \
      -o {tmp_merge} \
      {data_prefix}
  """,
    shell=True,
)

check_call(
    f"""ogr2ogr \
      -makevalid \
      -nln seagrass_plot \
      -f "FlatGeobuf" \
      -lco SPATIAL_INDEX=YES \
      {output} \
      {tmp_merge}
  """,
    shell=True,
)
