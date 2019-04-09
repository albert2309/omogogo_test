from django.db import models
import datetime

class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Tag(models.Model):
    tag = models.CharField(blank=False,max_length=50)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.tag)

class Member(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    title = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "%s %s" %(self.name, self.title)


class PostActivity(models.Model):
    ROLE_TYPE = (
        ('O', 'Owner'),
        ('C', 'Contributor'),
        ('R', 'Reader'),
    )
    members = models.ForeignKey(Member,null=True, on_delete=models.CASCADE)
    # todoList = models.ForeignKey(TodoList, on_delete=models.CASCADE),
    status = models.CharField(max_length=1, blank=False, choices=ROLE_TYPE, default='O')

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "%s/%s" %(self.members, self.status)

class Todo(models.Model):
    STATUS = (
        ('1', 'Todo'),
        ('2', 'Doing'),
        ('3', 'Done'),
    )
    #The title has 200 char max length to prevent lengthy title and encourage readers to write on description instead
    title = models.CharField(default="Sample Title2", unique=True, null=False,max_length=200)
    description = models.CharField(default="insert description in here",max_length=3000)
    due_date = models.DateTimeField(blank=True, default=datetime.datetime.now() +datetime.timedelta(days=1, hours=3))
    status = models.CharField(max_length=1,choices=STATUS, default='1')
    date_created = models.DateTimeField(default=datetime.datetime.now())
    date_modified = models.DateTimeField(default=datetime.datetime.now())
    tag_list = models.ManyToManyField(Tag)
    member_list = models.ManyToManyField(PostActivity)

#
# class ChildList(models.Model):
#     parent_post_id = models.ForeignKey(TodoList, on_delete=models.CASCADE)
#     content = models.CharField(max_length=3000)
#     due_date = models.DateTimeField(blank=True)
#     status = models.CharField(max_length=1,choices=TodoList.STATUS, default=1)
#     date_created = models.DateTimeField(blank=False,auto_now_add=True)
#     date_modified = models.DateTimeField(blank=False,auto_now_add=True)

