def check_answer(old, resp):
    print(f"The original message sent was: {old}")
    print(f"The translated message sent was: {resp['message']}")
    print(f"Program detects the message to be {(old == resp['message'])}")

    if (old == resp['message']) ==  resp["state"]:
        print("Result: Code is Correct, Success!")
    else:
        print("Result: Code is Wrong.")
