import datetime


user_status_type = ["Offline", "Away", "Idle", "Available", "Busy"]
request_status = ["Unread", "Read", "Accepted", "Rejected"]


class Message:
    """
    Message
    """
    def __init__(self, content, create_date):
        self.content = content
        self.create_date = create_date

    def get_content(self):
        return self.content

    def get_date(self):
        return self.create_date


class Chat:
    """
    Chat
    """
    def __init__(self):
        self.chat_id = 0
        self.participants = []
        self.messages = []

    def get_chat_id(self):
        return self.chat_id

    def get_messages(self):
        return self.messages

    def add_message(self, message):
        self.messages.add(message)
        return True


class PrivateChat(Chat):
    """
    Private Chat
    """
    def __init__(self, user1, user2):
        super(PrivateChat, self).__init__()
        self.participants.add(user1)
        self.participants.add(user2)

    def get_other_participant(self, primary):
        if self.participants.get(0) == primary:
            return self.participants.get(1)
        elif self.participants.get(1) == primary:
            return self.participants.get(0)
        else:
            return None


class GroupChat(Chat):
    """
    Group Chat
    """
    def remove_participant(self, user):
        self.participants.remove(user)

    def add_participant(self, user):
        self.participants.add(user)


class AddRequest:
    """
    Add Request
    """
    def __init__(self, from_user, to_user, create_date):
        self.from_user = from_user
        self.to_user = to_user
        self.date = create_date
        self.status = request_status[0]  # Unread

    def get_status(self):
        return self.status

    def get_from_user(self):
        return self.from_user

    def get_to_user(self):
        return self.to_user

    def get_date(self):
        return datetime.date


class UserStatus:
    """
    User Status
    """
    def __init__(self, status_type, message):
        self.status_type = status_type
        self.message = message

    def get_status_type(self):
        return self.status_type

    def get_message(self):
        return self.message


class UserManager:
    """
    UserManager serves as the central place for the core user actions
    """
    instance = None

    def __init__(self):
        self.users_by_id = {}
        self.users_by_account_name = {}
        self.online_users = {}

    @staticmethod
    def get_instance():
        if not UserManager.instance:
            UserManager.instance = UserManager()

        return UserManager.instance

    def add_user(self, from_user, to_account_name):
        to_user = self.users_by_account_name[to_account_name]
        add_req = AddRequest(from_user, to_user, datetime.date)
        to_user.received_add_request(add_req)
        from_user.sent_add_request(add_req)

    def approve_add_request(self, req):
        req.status = request_status[2]  # Accepted
        from_user = req.get_from_user()
        to_user = req.get_to_user()
        from_user.add_contact(to_user)
        to_user.add_contact(from_user)

    def reject_add_request(self, req):
        req.status = request_status[3]  # Rejected
        from_user = req.get_from_user()
        to_user = req.get_to_user()
        from_user.remove_add_request(req)
        to_user.remove_add_request(req)

    def user_signed_on(self, account_name):
        user = self.users_by_account_name[account_name]
        if user:
            user.set_status(UserStatus(user_status_type[3], ""))  # Available
            self.online_users[user.get_id()] = user

    def user_signed_off(self, account_name):
        user = self.users_by_account_name[account_name]
        if user:
            user.set_status(UserStatus(user_status_type[0], ""))  # Offline
            del self.online_users[user.get_id()]


class User:
    """
    User
    """
    def __init__(self, user_id, account_name, full_name):
        self.user_id = user_id
        self.account_name = account_name
        self.full_name = full_name
        self.private_chats = {}
        self.group_chats = []
        self.received_add_requests = {}
        self.sent_add_requests = {}
        self.contacts = {}
        self.status = user_status_type[0]  # Offline

    def send_message_to_user(self, to_user, content):
        chat = self.private_chats.get(to_user.get_id())
        if not chat:
            chat = PrivateChat(self, to_user)
            self.private_chats.put(to_user.get_id(), chat)

        message = Message(content, datetime.date)
        return chat.add_message(message)

    def send_message_to_group_chat(self, group_id, content):
        chat = self.group_chats.get(group_id)
        if not chat:
            message = Message(content, datetime.date)
            return chat.add_message(message)

        return False

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def add_contact(self, user):
        if user.get_id() in self.contacts:
            return False
        else:
            self.contacts[user.get_id()] = user
            return True

    def received_add_request(self, req):
        sender_id = req.get_from_user().get_id()
        if sender_id not in self.received_add_requests:
            self.received_add_requests[sender_id] = req

    def sent_add_request(self, req):
        receiver_id = req.get_from_user().get_id()
        if receiver_id not in self.sent_add_requests:
            self.sent_add_requests[receiver_id] = req

    def remove_add_request(self, req):
        if req.get_to_user() == self:
            self.received_add_requests.remove(req)
        elif req.get_from_user() == self:
            self.sent_add_requests.remove(req)

    def request_add_user(self, account_name):
        UserManager.get_instance().add_user(self, account_name)

    def add_private_conversation(self, conversation):
        other_user = conversation.get_other_participant(self)
        self.private_chats[other_user.get_id()] = conversation

    def add_group_conversation(self, conversation):
        self.group_chats.add(conversation)

    def get_id(self):
        return self.user_id

    def get_account_name(self):
        return self.account_name

    def get_full_name(self):
        return self.full_name

