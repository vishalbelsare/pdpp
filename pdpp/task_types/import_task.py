from pdpp.pdpp_class_base import BasePDPPClass
from typing import List, Dict
from os import mkdir, chdir
from pdpp.utils.yaml_task import dump_self
from pdpp.utils.execute_at_target import execute_at_target
from pdpp.templates.dep_dataclass import dep_dataclass


class ImportTask(BasePDPPClass):
    """
    This is the class documentation
    """

    def __init__(
            self
            ):

        self.target_dir = "_import_"
        self.dep_files = {}
        self.enabled = True


    FILENAME = ".pdpp_import.yaml"
    RIG_VALID = False # Can be rigged
    TRG_VALID = True # Can have targets 
    DEP_VALID = True # Can contain dependencies for other tasks
    SRC_VALID = False # Can have source code
    RUN_VALID = True # Has actions that should be executed at runtime
    IN_DIR = "./"
    OUT_DIR = "./"
    SRC_DIR = False

    def rig_task(self):
        raise NotImplementedError

    def initialize_task(self):
        mkdir(self.target_dir)
        execute_at_target(dump_self, self)

    def provide_dependencies(self, other_task) -> List[str]:
        return []
