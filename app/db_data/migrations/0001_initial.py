# Generated by Django 4.1 on 2022-11-20 20:51

import uuid

import db_data.uploadpaths
import db_data.validations
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="BaseUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    "email",
                    models.CharField(max_length=255, unique=True, validators=[db_data.validations.email_validation]),
                ),
                ("full_name", models.CharField(blank=True, max_length=255)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=17, validators=[db_data.validations.phone_validation]),
                ),
                (
                    "timezone_name",
                    models.CharField(
                        default="UTC", max_length=50, validators=[db_data.validations.timezone_validation]
                    ),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "role",
                    models.CharField(
                        choices=[("admin", "admin"), ("member", "member"), ("owner", "owner")], max_length=25
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Assignment",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("total_marks", models.IntegerField(default=10)),
                ("due_date", models.DateTimeField()),
            ],
            options={
                "db_table": "assignment",
            },
        ),
        migrations.CreateModel(
            name="AssignmentFile",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    "file",
                    models.FileField(
                        upload_to=db_data.uploadpaths.upload_assignment_file,
                        validators=[db_data.validations.file_validation],
                    ),
                ),
                ("file_type", models.CharField(max_length=255)),
                ("file_name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "assignmentfile",
            },
        ),
        migrations.CreateModel(
            name="Material",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    "file",
                    models.FileField(
                        upload_to=db_data.uploadpaths.upload_material_file,
                        validators=[db_data.validations.file_validation],
                    ),
                ),
                ("file_type", models.CharField(max_length=255)),
                ("file_name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "material",
            },
        ),
        migrations.CreateModel(
            name="Workshop",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "level",
                    models.CharField(
                        choices=[("one", "one"), ("two", "two"), ("three", "three"), ("four", "four")], max_length=25
                    ),
                ),
                ("mode", models.CharField(choices=[("online", "online"), ("onsite", "onsite")], max_length=25)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "workshop",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                (
                    "workshop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="%(class)s", to="db_data.workshop"
                    ),
                ),
            ],
            options={
                "db_table": "student",
            },
        ),
        migrations.CreateModel(
            name="Score",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("score", models.IntegerField(default=None)),
                (
                    "assignment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="%(class)s", to="db_data.assignment"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="%(class)s", to="db_data.student"
                    ),
                ),
            ],
            options={
                "db_table": "score",
            },
        ),
        migrations.CreateModel(
            name="Lecture",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("url", models.URLField(blank=True)),
                (
                    "material",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, related_name="%(class)s", to="db_data.material"
                    ),
                ),
                (
                    "workshop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="%(class)s", to="db_data.workshop"
                    ),
                ),
            ],
            options={
                "db_table": "lecture",
            },
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("present", models.BooleanField(default=False)),
                (
                    "lecture",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="%(class)s", to="db_data.lecture"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="%(class)s", to="db_data.student"
                    ),
                ),
            ],
            options={
                "db_table": "attendance",
            },
        ),
        migrations.AddField(
            model_name="assignment",
            name="assignment_file",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, related_name="%(class)s", to="db_data.assignmentfile"
            ),
        ),
        migrations.AddField(
            model_name="assignment",
            name="workshop",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="%(class)s", to="db_data.workshop"
            ),
        ),
    ]
