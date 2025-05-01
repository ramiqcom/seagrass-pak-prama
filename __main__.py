import json
import subprocess
from shutil import copyfile
from tempfile import TemporaryDirectory

temp_folder = TemporaryDirectory(delete=False)

source = "Stack_AGC_2016-2024_v2/2016-2024_stack_rrs_AGC_PPI_ntr300_alignedGEE"
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

mean = f"{temp_folder.name}/mean_seagrass.tif"
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

std = f"{temp_folder.name}/std_seagrass.tif"
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

cv = f"{temp_folder.name}/cv_seagrass.tif"
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

copyfile(mean, "output/mean_seagrass.tif")
copyfile(std, "output/std_seagrass.tif")
copyfile(cv, "output/cv_seagrass.tif")
