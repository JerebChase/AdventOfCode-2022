def get_subroutine_marker(datastream):
    stream = datastream[0]
    for i in range(len(stream) - 13):
        marker = stream[i:i+14]
        if len(set(marker)) == len(marker):
            return i + 14