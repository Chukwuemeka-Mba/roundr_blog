from django.db import models
from django.contrib.auth.models import User
# Question Model

class Question(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=300)
	details=models.TextField()
	tags=models.TextField(default='')
	add_time=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

#Anwer Model
class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    details=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
    	return self.title

#Comment Model
class Comment(models.Model):
	answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_user')
	add_time=models.DateTimeField(auto_now_add=True)

#	UpVotes
class UpVote(models.Model):
	answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='upvote_user')
	
#	DownVotes
class DownVote(models.Model):
	answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='downvote_user')
	