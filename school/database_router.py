# school/database_router.py

# class SchoolDatabaseRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'student':
#             return 'default'  # Now points to SQLite
#         elif model._meta.app_label == 'subject':
#             return 'subjects_db'  # MySQL for subject
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'student':
#             return 'default'
#         elif model._meta.app_label == 'subject':
#             return 'subjects_db'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         if obj1._meta.app_label == 'student' and obj2._meta.app_label == 'subject':
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'student':
#             return db == 'default'
#         elif app_label == 'subject':
#             return db == 'subjects_db'
#         return None



# school/routers.py

# class SchoolDatabaseRouter:
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'student':
#             return 'default'  # SQLite
#         elif model._meta.app_label == 'subject':
#             return 'subjects_db'  # MySQL
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'student':
#             return 'default'  # SQLite
#         elif model._meta.app_label == 'subject':
#             return 'subjects_db'  # MySQL
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         if obj1._meta.app_label == 'student' and obj2._meta.app_label == 'subject':
#             return True
#         if obj1._meta.app_label == 'subject' and obj2._meta.app_label == 'student':
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label == 'student':
#             return db == 'default'
#         elif app_label == 'subject':
#             return db == 'subjects_db'
#         return None


# school/routers.py

class SchoolDatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'student':
            return 'default'  # SQLite for student
        elif model._meta.app_label == 'subject':
            return 'subjects_db'  # MySQL for subject
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'student':
            return 'default'  # SQLite for student
        elif model._meta.app_label == 'subject':
            return 'subjects_db'  # MySQL for subject
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'student' and obj2._meta.app_label == 'subject':
            return True
        if obj1._meta.app_label == 'subject' and obj2._meta.app_label == 'student':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'student':
            if model_name == 'enrollment':
                return db == 'default'  # Store enrollment in SQLite
            return db == 'default'  # Student in SQLite
        elif app_label == 'subject':
            return db == 'subjects_db'  # Subject in MySQL
        return None

