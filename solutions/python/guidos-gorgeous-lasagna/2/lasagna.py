EXPECTED_BAKE_TIME = 40

def bake_time_remaining(minutes_in_oven):
    """Calculate how much time remainig to finish
    :param minutes_in_oven: int - the actual time that the lasagna is in the oven

    :return: int - the remaining time
    
    """
    return EXPECTED_BAKE_TIME - minutes_in_oven

def preparation_time_in_minutes(number_of_layers):
    """ Elapsed time in the kitchen, from preparation to remainig time to finish the baking

    :param number_of_layers: int - the number of layers the lasagna will have

    :return: int - the total time will take to finish
    """ 
    return (number_of_layers * 2)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time    