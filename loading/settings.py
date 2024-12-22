"""Load generator settings from file"""

import os

from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    print("Error loading PyYAML, using built-in YAML module")
    from yaml import Loader


folder = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(folder, "../config.yaml")
with open(config_path, encoding="utf-8") as config_file:
    config = load(config_file, Loader=Loader)
if isinstance(config["dictionary"], str):
    config["dictionary"] = [config["dictionary"]]
