def which_prize(number_of_point):
    if number_of_point >= 0 and number_of_point <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif number_of_point >= 51 and number_of_point <= 150:
        return "Oh dear, no prize this time."
    elif number_of_point >= 151 and number_of_point <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    elif number_of_point >= 181 and number_of_point <= 200:
        return "Congratulations! You have won a penguim!"
