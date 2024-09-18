# from django.db import models
# from subject.models import Subject

# class Student(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     age = models.PositiveIntegerField()

#     class Meta:
#         db_table = 'students'
#         verbose_name = 'Student'
#         verbose_name_plural = 'Students'

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# # Custom relationship table
# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     subject_id = models.IntegerField()  # Store subject ID manually (since Subject is on a different DB)

#     class Meta:
#         db_table = 'enrollment'
#         verbose_name = 'Enrollment'
#         verbose_name_plural = 'Enrollments'

#     def get_subject(self):
#         # Custom method to fetch subject from MySQL DB
#         try:
#             return Subject.objects.using('subjects_db').get(id=self.subject_id)
#         except Subject.DoesNotExist:
#             return None



from django.db import models
from subject.models import Subject
from django.db.models import UniqueConstraint

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Custom relationship table
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.IntegerField()  # Store subject ID manually (since Subject is on a different DB)

    class Meta:
        db_table = 'enrollment'
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollments'
        # Ensure that each student can only be enrolled in a specific subject once
        constraints = [
            UniqueConstraint(fields=['student', 'subject_id'], name='unique_student_subject')
        ]

    def get_subject(self):
        # Custom method to fetch subject from MySQL DB
        try:
            return Subject.objects.using('subjects_db').get(id=self.subject_id)
        except Subject.DoesNotExist:
            return None

