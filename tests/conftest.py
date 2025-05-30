import pytest
from pathlib import Path
from typing import Dict, Any

from edgar.xbrl import XBRL

# Base paths
FIXTURE_DIR = Path("tests/fixtures/xbrl2")
DATA_DIR = Path("data/xbrl/datafiles")