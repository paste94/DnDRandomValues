from random import randint

from Model import get_tuple
import Constants


def calculate_coins(cr):
    tuple = get_tuple(cr)

    number_of_dices = tuple[Constants.NUMBER_OF_DICES]
    dice_type = tuple[Constants.DICE_TYPE]
    multiplier = tuple[Constants.MULTIPLIER]
    coin_type = tuple[Constants.POUND_TYPE]

    return_string = 'Calcolo: ' + str(number_of_dices) + 'd' + str(dice_type) + 'x' + str(multiplier) + '\n'
    result = 0
    i = 0

    while i < number_of_dices:
        thrown = randint(1, dice_type)
        return_string += '\t' + 'Dado ' + str(i + 1) + ': ' + str(thrown) + '\n'
        result += thrown
        i += 1

    return_string += 'Risultato: ' + str(result) + ' x ' + str(multiplier) + ' = ' + str(result * multiplier) + \
                     coin_type

    return return_string
