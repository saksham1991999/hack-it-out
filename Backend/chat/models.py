import uuid

from django.db import models


class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey("accounts.User", related_name='author_room', on_delete=models.CASCADE)
    friend = models.ForeignKey("accounts.User", related_name='friend_room', on_delete=models.CASCADE)


class Message(models.Model):
    author = models.ForeignKey("accounts.User", related_name='author_messages', on_delete=models.CASCADE)
    friend = models.ForeignKey("accounts.User", related_name='friend_messages', on_delete=models.CASCADE)
    chat = models.ForeignKey("chat.Chat", related_name='messages', on_delete=models.DO_NOTHING)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message + " " + str(self.timestamp)


class Room(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='rooms')
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    users = models.ManyToManyField("accounts.User", through="chat.RoomUser")
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.name


user_role_choices = (
    ("A", "Admin"),
    ("U", "User"),
)


class RoomUser(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    room = models.ForeignKey("chat.Room", on_delete=models.CASCADE, related_name='room_users')
    role = models.CharField(max_length=2, choices=user_role_choices)
    viewed_at = models.DateTimeField(auto_now=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    left_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'room')

    def __str__(self):
        return self.room.name


class Message(models.Model):
    room = models.ForeignKey('chat.Room', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    file_field = models.FileField(upload_to='messages', blank=True, null=True)
    message_text = models.CharField(max_length=1000, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.__str__() + " : " + self.message_text


class ReportGroup(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    room = models.ForeignKey('chat.Room', on_delete = models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)