from questionary import Separator, prompt, Choice
from click import clear as click_clear
from posixpath import join
import os
from pprint import pprint
from pdpp.styles.prompt_style import custom_style_fancy
from pdpp.pdpp_class_base import BasePDPPClass
from pdpp.utils.ignorelist import ignorelist
from typing import Tuple, List, Dict
from os import DirEntry
from collections import defaultdict



def q2(selected_dep_tasks: List[BasePDPPClass], task: BasePDPPClass):
    """
    A question which asks users to indicate which individual files 
    (drawn from a list of those contained in the output directories of the steps indicated in question #1) 
    are required as dependencies for the current step.
    """

    click_clear()

    q2input: Dict[BasePDPPClass, List[DirEntry[str]]] = {}
    import_input = []

    for selected_task in selected_dep_tasks:

        search_dir = join(selected_task.target_dir, selected_task.OUT_DIR)

        results = [r for r in os.scandir(search_dir) if r.name not in ignorelist]

        if results:
            q2input[selected_task] = results


    choice_list = []

    for key, values in q2input.items():

        choice_list.append(Separator('\n= ' + key.target_dir + ' ='))

        for value in values:
            try:
                checked = value.name in task.dep_files[key.target_dir]
            except KeyError:
                checked = False
            except TypeError:
                checked = False 

            title = value.name 

            if value.is_dir():
                title += " (This is a directory)"

            choice_list.append(
                Choice(
                    title = title,
                    value = (key, value),
                    checked= checked,
                )
            )

    questions_2 =[
        {
            'type': 'checkbox',
            'message': 'Select the dependency files for "{}"'.format(task.target_dir),
            'name': 'dependencies',
            'choices': choice_list,
        }
    ]
    
    response_dict = {}

    responses: List[Tuple[BasePDPPClass, DirEntry[str]]]

    if questions_2[0]['choices']:
        responses = prompt(questions_2, style=custom_style_fancy)['dependencies']
    else:
        return {}

    dep_task_set = set([t for t, f in responses])

    for dep_task in dep_task_set:
        task_out = dep_task.OUT_DIR
        file_list = [f.name for t, f in responses if t == dep_task and f.is_file()]
        dir_list = [d.name for t, d in responses if t == dep_task and d.is_dir()]

        response_dict[dep_task.target_dir] = {
            "task_out": task_out,
            "file_list": file_list,
            "dir_list": dir_list,
        }
    
    return response_dict