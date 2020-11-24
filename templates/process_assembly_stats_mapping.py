#!/usr/bin/env python3

"""
Purpose
-------
This module is intended parse the results of the process_assembly_stats_mapping.py for one or more
samples.

Expected input
--------------
The following variables are expected whether using NextFlow or the
:py:func:`main` executor.
- ``assembly_stats_global_file`` : Path to output file.
    - e.g.: ``'assembly_stats_global.tsv'``

Generated output
----------------
None
"""

import os
import json
try:
    import utils
except ImportError:
    from templates import utils

__version__ = "0.0.1"
__build__ = "24.11.2020"
__template__ = "PROCESS_ASSEMBLY_STATS_MAPPINGL-nf"

logger = utils.get_logger(__file__)

if __file__.endswith(".command.sh"):
    ASSEMBLY_STATS_GLOBAL_FILE_JSON = "$json_report".split()
    logger.debug("Running {} with parameters:".format(
        os.path.basename(__file__)))
    logger.debug("ASSEMBLY_STATS_GLOBAL_FILE_JSON: {}".format(ASSEMBLY_STATS_GLOBAL_FILE_JSON))


def main(stats_json):

    # Write JSON file report
    with open("global_assembly_mapping_stats.json", "w") as json_report:
        main_json = {}

        for data_report in stats_json:
            with open(data_report) as f:
                json_data = json.load(f)
                print(json_data)
                sample_id = json_data["sample_id"]
                reference_table_data = json_data["ReferenceTables"]

            if sample_id not in main_json.keys():
                main_json[sample_id] = {"ReferenceTable": [reference_table_data]}
            else:
                main_json[sample_id]["ReferenceTable"].append(reference_table_data)

        json_report.write(json.dumps(main_json, separators=(",", ":")))


if __name__ == '__main__':
    main(ASSEMBLY_STATS_GLOBAL_FILE_JSON)
