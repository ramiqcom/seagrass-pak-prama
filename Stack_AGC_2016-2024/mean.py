import json
import subprocess

image_info = "image.json"

source = "2016-2024_stack_rrs_AGC_PPI_ntr300_alignedGEE"
check = subprocess.run(
    [
        "gdalinfo",
        "-json",
        source,
    ],
    check=True,
    text=True,
    capture_output=True,
)

# band_info = json.loads(check.stdout)["bands"]
# for x in range(len(band_info)):
#     subprocess.run(
#         [
#             "gdalwarp",
#             "-of",
#             "GTiff",
#             "-ot",
#             "Float32",
#             "-t_srs",
#             "EPSG:4326",
#             "-srcnodata",
#             "-999",
#             "-dstnodata",
#             "NaN",
#             "-b",
#             f"{x + 1}",
#             "-co",
#             "COMPRESS=LZW",
#             "-overwrite",
#             source,
#             f"images/image_no_{x + 1}.tif",
#         ],
#         check=True,
#         text=True,
#     )

mean = "mean_seagrass.tif"
subprocess.run(
    f"""gdal_calc \
        -A images/*.tif \
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

std = "std_seagrass.tif"
subprocess.run(
    f"""gdal_calc \
        -A images/*.tif \
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

cv = "cv_seagrass.tif"
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
