from middleman import *
from receiver import *
from check import *

def send(message=None):
    if message is None:
        message = " ".join([get_random_word() for _ in range(5)])

    """===================="""
    """ YOUR CODE HERE """
    # You can write code to encode / encrypt the message

    """ END OF YOUR CODE """
    """===================="""

    received_bits = send_to_receiver(message)
    receiver_response = receive(received_bits)


    check_answer(message, receiver_response)


