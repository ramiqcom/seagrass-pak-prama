import json
import subprocess
from shutil import copyfile
from tempfile import TemporaryDirectory

temp_folder = TemporaryDirectory(delete=False)

output_name = "CS"
source = "Stack_2016_to_2024/Stack_CS_2016_2024_aligned"
band_info = json.loads(
    subprocess.check_output(
        [
            "gdalinfo",
            "-json",
            source,
        ],
        text=True,
    )
)["bands"]

for x in range(len(band_info)):
    subprocess.run(
        [
            "gdalwarp",
            "-of",
            "GTiff",
            "-ot",
            "Float32",
            "-t_srs",
            "EPSG:4326",
            "-srcnodata",
            "-999",
            "-dstnodata",
            "NaN",
            "-b",
            f"{x + 1}",
            "-co",
            "COMPRESS=LZW",
            "-overwrite",
            source,
            f"{temp_folder.name}/image_no_{x + 1}.tif",
        ],
        check=True,
        text=True,
    )

mean = f"{temp_folder.name}/mean_{output_name}.tif"
subprocess.run(
    f"""gdal_calc \
        -A {temp_folder.name}/image_no_*.tif \
        --outfile={mean} \
        --calc=nanmean(A,axis=0) \
        --NoDataValue=0 \
        --overwrite \
        --co="COMPRESS=LZW" \
        --co="TILED=YES" \
    """,
    check=True,
    text=True,
    shell=True,
)

std = f"{temp_folder.name}/std_{output_name}.tif"
subprocess.run(
    f"""gdal_calc \
        -A {temp_folder.name}/image_no_*.tif \
        --outfile={std} \
        --calc=nanstd(A,axis=0) \
        --NoDataValue=0 \
        --overwrite \
        --co="COMPRESS=LZW" \
        --co="TILED=YES" \
    """,
    check=True,
    text=True,
    shell=True,
)

cv = f"{temp_folder.name}/cv_{output_name}.tif"
subprocess.run(
    f"""gdal_calc \
        -A {mean} \
        -B {std} \
        --outfile={cv} \
        --calc="B/A" \
        --NoDataValue=0 \
        --overwrite \
        --co="COMPRESS=LZW" \
        --co="TILED=YES" \
    """,
    check=True,
    text=True,
    shell=True,
)

copyfile(mean, f"output/mean_{output_name}.tif")
copyfile(std, f"output/std_{output_name}.tif")
copyfile(cv, f"output/cv_{output_name}.tif")
