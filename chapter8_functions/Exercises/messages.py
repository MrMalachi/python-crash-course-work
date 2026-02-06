# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed.
# After calling the function,
# print both of your lists to make sure the messages were moved correctly.
messages = ["on my way", "be right back", "hello", "oh my god"]
sent_messages = []

def show_messages(message):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """
    When called, this function prints every text message in the list 'messages'
    and moves each message to a new list called sent_messages as it’s printed.
    """
    print("\nSending all messages:")
    while messages:
        current_messages = messages.pop()
        print(current_messages)
        sent_messages.append(current_messages)

show_messages(messages)
send_messages(messages[:], sent_messages)

print("\nFinal messages lists:")
print(messages)
print(sent_messages)






