from pdpp.pdpp_class_base import BasePDPPClass
from os import makedirs
from posixpath import join

def create_in_out_src(task: BasePDPPClass):

    """
    Creates the input, output, and src directories, as well as a source file and .gitkeep files, in the new step.
    Only applicable to pdpp_step (pdpp new) and pdpp_custom (pdpp custom) steps.

    """

    makedirs("input")
    makedirs("output")
    makedirs("src")
    
    open(join("input", ".gitkeep"), "a").close()
    open(join("output", ".gitkeep"), "a").close()
    open(join("src", ".gitkeep"), "a").close()
    open(join("src", (task.target_dir + ".py")), "a").close()