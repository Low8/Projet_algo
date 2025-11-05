import vrplib
import os

def get_vrptw_instance(file_name):
    """
    This function return a dataset of the intance
    in the good format and his solution.

    EXECUTE ONLY IN THE scripts FOLDER ! with from functions import get_vrptw_instance
    
    Args:
        file_name (str): the name of the instance file that we want to use
    
    Return:
        tuple: (dataset, solution) where:
            - dataset (dict): Instance data (node_coord, capacity, etc.)
            - solution (dict): Solution with 'routes' and 'cost'
    """

    instance_path = os.path.join("..", "instances", file_name)
    data = vrplib.read_instance(instance_path, instance_format="solomon")

    solution_path = os.path.join("..", "instances", file_name.replace(".txt", ".sol"))
    solution = vrplib.read_solution(solution_path)

    return data, solution
    
    