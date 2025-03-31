class PostOffice:
    def __init__(self):
        # Inbox will be a dictionary where key is the username and value is a list of message dicts.
        self.inboxes = {}

    def send_message(self, username, subject, body):
        """Send a message to the user's inbox."""
        if username not in self.inboxes:
            self.inboxes[username] = []
        message = {"subject": subject, "body": body, "read": False}
        self.inboxes[username].append(message)

    def read_inbox(self, username, num_messages=None):
        """
        Returns the first 'num_messages' unread messages from the user's inbox.
        Marks them as read.
        If 'num_messages' is None, return all unread messages.
        """
        if username not in self.inboxes:
            return []  # No inbox for this user

        inbox = self.inboxes[username]
        unread_messages = [msg for msg in inbox if not msg["read"]]  # Filter unread messages

        if num_messages is None:
            num_messages = len(unread_messages)  # If no number of messages is provided, return all unread messages

        # Get the specified number of unread messages and mark them as read
        messages_to_return = unread_messages[:num_messages]
        for message in messages_to_return:
            message["read"] = True  # Mark the message as read

        return messages_to_return

    def search_inbox(self, username, search_string):
        """
        Search for messages that contain 'search_string' in either their subject or body.
        Returns a list of messages that match the search.
        """
        if username not in self.inboxes:
            return []  # No inbox for this user

        inbox = self.inboxes[username]
        matching_messages = []

        for message in inbox:
            if (search_string.lower() in message["subject"].lower()) or (search_string.lower() in message["body"].lower()):
                matching_messages.append(message)

        return matching_messages


# This block will only run when the script is executed directly, not when imported
if __name__ == '__main__':
    # Testing the PostOffice class
    post_office = PostOffice()

    # Send some messages
    post_office.send_message("john_doe", "Meeting Tomorrow", "Let's meet tomorrow at 10 AM.")
    post_office.send_message("john_doe", "Lunch Plans", "Do you want to grab lunch today?")
    post_office.send_message("alice_smith", "Hello", "Hi Alice, how are you?")

    # Read the inbox for john_doe
    print("John Doe's inbox:")
    print(post_office.read_inbox("john_doe", 1))  # Read the first unread message

    # Search for messages in john_doe's inbox containing "meeting"
    print("\nMessages containing 'meeting':")
    print(post_office.search_inbox("john_doe", "meeting"))

    # Read all unread messages for alice_smith
    print("\nAlice Smith's inbox:")
    print(post_office.read_inbox("alice_smith"))
