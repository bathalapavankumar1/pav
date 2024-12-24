from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Branch Model
class Branch(models.Model):
    branch = models.TextField(default='')
    
    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.branch

# Category Model
class Category(models.Model):
    category = models.TextField(default='')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category

# Student Model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE, default='')
    is_student = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.user.username

# HOD Model
class Hod(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE, default='')
    is_hod = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'HOD'
        verbose_name_plural = 'HODs'

    def __str__(self):
        return self.user.username

# Complaint Model
class Complaint(models.Model):
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE, related_name='compbranch')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name='compcategory')
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    c_date = models.DateField(auto_now=True)

    title = models.CharField(max_length=255, default=" ")
    description = models.TextField(default=" ")
    priority = models.CharField(
        max_length=6,
        choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')],
        default='Low',
    )

    class Status(models.TextChoices):
        PENDING = 'PN', _('Pending')
        SOLVED = 'SO', _('Solved')
        REJECTED = 'RJ', _('Rejected')

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PENDING,
    )
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    resolved_at = models.DateTimeField(blank=True, null=True)  # New field for resolution date

    @property
    def resolution_time(self):
        if self.resolved_at:
            return (self.resolved_at - self.c_date).days
        return None

    class Meta:
        verbose_name = 'Complaint'
        verbose_name_plural = 'Complaints'

# Feedback Model
class Feedback(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, default=1)
    feedback = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)  # New field for feedback rating
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for Complaint {self.complaint.id}"
