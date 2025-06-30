import json

data_list = [
    dict(
        region="Pari Island",
        dates=[
            dict(
                year=2022,
                month="09-10",
                start="2022-09-01",
                end="2022-10-30",
            ),
            dict(
                year=2022,
                month="03-04",
                start="2022-03-01",
                end="2022-04-31",
            ),
        ],
    ),
    dict(
        region="Banyak Island",
        dates=[
            dict(
                year=2024,
                month="09-10",
                start="2024-09-01",
                end="2024-10-30",
            ),
        ],
    ),
    dict(
        region="Bontang",
        dates=[
            dict(
                year=2024,
                month="07-08",
                start="2024-07-01",
                end="2024-08-31",
            ),
        ],
    ),
    dict(
        region="Kangean Island",
        dates=[
            dict(
                year=2024,
                month="09-10",
                start="2024-09-01",
                end="2024-10-30",
            ),
        ],
    ),
    dict(
        region="Osi Island",
        dates=[
            dict(
                year=2024,
                month="07-08",
                start="2024-07-01",
                end="2024-08-31",
            ),
        ],
    ),
    dict(
        region="Banggai Island",
        dates=[
            dict(
                year=2024,
                month="09-10",
                start="2024-09-01",
                end="2024-10-30",
            ),
        ],
    ),
    dict(
        region="Kwandang Island",
        dates=[
            dict(
                year=2024,
                month="07-08",
                start="2024-07-01",
                end="2024-08-31",
            ),
        ],
    ),
    dict(
        region="Belitung Island",
        dates=[
            dict(
                year=2024,
                month="05-06",
                start="2024-05-01",
                end="2024-06-31",
            ),
        ],
    ),
    dict(
        region="Labuan Bajo",
        dates=[
            dict(
                year=2024,
                month="05-06",
                start="2024-05-01",
                end="2024-06-31",
            ),
        ],
    ),
    dict(
        region="Oeseli",
        dates=[
            dict(
                year=2021,
                month="09-10",
                start="2024-09-01",
                end="2024-10-30",
            ),
        ],
    ),
    dict(
        region="Gili Lawang Island",
        dates=[
            dict(
                year=2023,
                month="07-08",
                start="2024-07-01",
                end="2024-08-31",
            ),
        ],
    ),
    dict(
        region="Menjangan Besar Island",
        dates=[
            dict(
                year=2024,
                month="03-04",
                start="2024-03-01",
                end="2024-04-31",
            ),
        ],
    ),
    dict(
        region="Sanur",
        dates=[
            dict(
                year=2024,
                month="07-08",
                start="2024-07-01",
                end="2024-08-31",
            ),
            dict(
                year=2024,
                month="09-10",
                start="2024-09-01",
                end="2024-10-30",
            ),
            dict(
                year=2024,
                month="11-12",
                start="2024-01-01",
                end="2024-12-31",
            ),
        ],
    ),
]

with open("output/region_list.json", "w") as file:
    json.dump(data_list, file)
