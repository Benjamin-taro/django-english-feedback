from django.db import models

# Create your models here.


class Conversation(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PronunciationFeedback(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='pronunciation_feedback')
    word = models.CharField(max_length=100)
    phoneme = models.CharField(max_length=10)
    issue = models.TextField()
    description = models.TextField()
    video_link = models.URLField()
    
class UserProgress(models.Model):
    user = models.CharField(max_length=100)
    total_conversations = models.IntegerField(default=0)
    total_grammar_issues = models.IntegerField(default=0)
    total_vocabulary_issues = models.IntegerField(default=0)
    total_pronunciation_issues = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def update_progress(self, grammar_count, vocabulary_count, pronunciation_count):
        self.total_conversations += 1
        self.total_grammar_issues += grammar_count
        self.total_vocabulary_issues += vocabulary_count
        self.total_pronunciation_issues += pronunciation_count
        self.save()
