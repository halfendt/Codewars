def which_note(key_press_count):
    """
    Piano Kata, Part 2
    https://www.codewars.com/kata/589631d24a7323d18d00016f
    """
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    return notes[(key_press_count - 1) % 88 % 12]