#!/usr/bin/env python3
# modules

# imports
import json
import os

# modules update
def modules_update(self, modules):
    new_config = self.CONFIG
    new_config["report_elements"] = modules

    try:
        with open(self.CONFIG["config_path"], 'w') as fp:
            json.dump(new_config, fp, indent=4)
    except Exception as e:
        print(e)

# remove modules that do not exists
def get_report_modules(self):
    return list( set(self.CONFIG["report_elements"]) & set(list(self.CONFIG["plateform"].keys())) )