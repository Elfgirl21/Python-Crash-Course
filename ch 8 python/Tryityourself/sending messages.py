def sent_messages(message,sent_msgs):
    while messages:
        current_msg = messages.pop()
        print(current_msg)
        sent_msgs.append(current_msg)

def show_messages(sent_msgs):
    print("\nFollowing messages have been sent: ")
    for sent_msg in sent_msgs:
        print(sent_msg)

messages = ['Hi', 'lol', 'rn', 'brb']
sent_msgs = []
sent_messages(messages, sent_msgs)
show_messages(sent_msgs)