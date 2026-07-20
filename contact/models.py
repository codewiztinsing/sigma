from django.db import models


class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('partnership', 'Partnership Inquiry'),
        ('project', 'Project Proposal'),
        ('training', 'Training Inquiry'),
        ('media', 'Media & Press'),
        ('general', 'General Inquiry'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.get_subject_display()}"
