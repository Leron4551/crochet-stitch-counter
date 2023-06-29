# CONSTANTS to identify stitch type
SC = 1  # single crochet
INC = 2  # increase stitch (counts as two stitches)
DEC = 1  # decrease stitch


class Round:

    def __init__(self, round_number, first_stitch_count, first_stitch_type, second_stitch_count, second_stitch_type,
                 repetitions):
        self.roundNumber = round_number
        self.firstStitchCount = first_stitch_count
        self.firstStitchType = first_stitch_type.upper()
        self.secondStitchCount = second_stitch_count
        self.secondStitchType = second_stitch_type.upper()
        self.repetitions = repetitions
        self.totalCount = eval("((" + str(first_stitch_count) + "*" + first_stitch_type.upper() + ") + (" + str(
            second_stitch_count) + "*" + second_stitch_type.upper() + ")) *" + str(repetitions))

    def get_round_number(self):
        return self.roundNumber

    def get_first_stitch_count(self):
        return self.firstStitchCount

    def get_first_stitch_type(self):
        return self.firstStitchType

    def get_second_stitch_count(self):
        return self.secondStitchCount

    def get_second_stitch_type(self):
        return self.secondStitchType

    def get_repetitions(self):
        return self.repetitions

    def get_total_count(self):
        return self.totalCount


def main():
    current_round_number = get_round_number()
    current_pattern = get_pattern(current_round_number)
    current_round = make_round(current_round_number, current_pattern)
    count = 1

    # Print round header
    print_header(current_round_number, current_pattern)

    # Loop through pattern sequence to track stitch count on Enter press.
    for i in range(current_round.get_repetitions()):
        for j in range(eval(str(current_round.get_first_stitch_count()))):
            print("Stitch " + str(count) + "/" + str(
                current_round.get_total_count()) + " (" + current_round.get_first_stitch_type() + " +" + str(eval(current_round.get_first_stitch_type())) + ")")
            count += eval(current_round.get_first_stitch_type())
            input()
        for k in range(eval(str(current_round.get_second_stitch_count()))):
            print("Stitch " + str(count) + "/" + str(
                current_round.get_total_count()) + " (" + current_round.get_second_stitch_type() + " +" + str(eval(current_round.get_second_stitch_type())) + ")")
            count += eval(current_round.get_second_stitch_type())
            input()

    # Prompt user to run again
    print("\nRound " + current_round_number + " is done!\n")
    repeat = input("Do another round? (y/N) ")

    if repeat.lower() == "y" or repeat.lower() == "yes":
        main()


# Prompt user for round number
def get_round_number():
    return input("What round are you starting on? ")


# Prompt user for pattern (in the Woobles format (e.g., "[5 sc, inc] x 4" or "28 sc" or "[dec, 2 sc] x 3"
def get_pattern(round_number):
    return input("What's the pattern for round " + round_number + "? ")


# Parse pattern into component pieces stored in a Round class
def make_round(round_number, full_pattern_string):
    first_stitch_count = 1
    first_stitch_type = "0"
    second_stitch_count = 1
    second_stitch_type = "0"
    repetitions = 1

    if full_pattern_string.find("x") >= 0:
        full_pattern = full_pattern_string.split("x")
        repetitions = int(full_pattern[1].strip())
        full_pattern_string = full_pattern[0][1:full_pattern[0].find("]")].strip()

    stitch_pattern = full_pattern_string.split(",")

    if len(stitch_pattern) > 1:
        second_stitch = stitch_pattern[1].strip().split(" ")
        if len(second_stitch) > 1:
            second_stitch_type = str(second_stitch[1].strip())
            second_stitch_count = int(second_stitch[0].strip())
        else:
            second_stitch_type = str(second_stitch[0].strip())

    first_stitch = stitch_pattern[0].strip().split(" ")

    if len(first_stitch) > 1:
        first_stitch_type = str(first_stitch[1].strip())
        first_stitch_count = int(first_stitch[0].strip())
    else:
        first_stitch_type = str(first_stitch[0].strip())

    return Round(round_number, first_stitch_count, first_stitch_type, second_stitch_count, second_stitch_type, repetitions)


# Print a header at the start of the round
def print_header(round_number, pattern_string):
    padding = 45 - (len(round_number) + len(pattern_string) + 22)
    print("_" * 45)
    print("| Beginning round " + round_number + " " + ("." * padding) + " " + pattern_string + " |")
    print("| Press ENTER to advance to the next stitch |")
    print("-" * 45)


main()
