# Generated by Django 4.2 on 2023-04-09 15:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Listing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Jobs", "Jobs"),
                            ("Property", "Property"),
                            ("Books&Sports", "Books&Sports"),
                            ("Bikes", "Bikes"),
                            ("Cars", "Cars"),
                            ("Furniture", "Furniture"),
                            ("Electronics", "Electronics"),
                            ("Mobiles", "Mobiles"),
                            ("Fashion", "Fashion"),
                        ],
                        max_length=100,
                    ),
                ),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("MI", "Sikkim"),
                            ("GA", "Goa"),
                            ("ML", "Meghalaya"),
                            ("AS", "Assam"),
                            ("JH", "Jharkhand"),
                            ("AR", "Arunachal Pradesh"),
                            ("UK", "Uttarakhand"),
                            ("TN", "Tamil Nadu"),
                            ("MH", "Maharashtra"),
                            ("MN", "Manipur"),
                            ("TS", "Telegana"),
                            ("AP", "Andhra Pradesh"),
                            ("TR", "Tripura"),
                            ("OD", "Odisha"),
                            ("PB", "Punjab"),
                            ("BR", "Bihar"),
                            ("CG", "Chhattisgarh"),
                            ("HP", "Haryana"),
                            ("RJ", "Rajasthan"),
                            ("KA", "Karnataka"),
                            ("WB", "West Bengal"),
                            ("UP", "Uttar Pradesh"),
                            ("GJ", "Gujarat"),
                            ("MZ", "Mizoram"),
                            ("NL", "Nagaland"),
                            ("KL", "Kerala"),
                            ("MP", "Madhya Pradesh"),
                        ],
                        max_length=100,
                    ),
                ),
                ("zipcode", models.CharField(max_length=20)),
                ("description", models.TextField(blank=True)),
                ("price", models.IntegerField()),
                ("total_rating", models.IntegerField(null=True)),
                ("no_of_rating", models.IntegerField(null=True)),
                ("photo_main", models.ImageField(upload_to="photos/%Y/%m/%d/")),
                (
                    "photo_1",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_2",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_3",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_4",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_5",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_6",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                ("is_published", models.BooleanField(default=True)),
                ("list_date", models.DateField(default=datetime.datetime.now)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
