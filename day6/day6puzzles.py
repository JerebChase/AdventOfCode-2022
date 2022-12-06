def get_subroutine_marker(datastream):
    stream = datastream[0]
    for i in range(len(stream) - 3):
        marker = stream[i:i+4]
        if len(set(marker)) == len(marker):
            return i + 4

def get_message_marker(datastream):
    stream = datastream[0]
    for i in range(len(stream) - 13):
        marker = stream[i:i + 14]
        if len(set(marker)) == len(marker):
            return i + 14