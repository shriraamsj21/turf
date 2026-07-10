from django.db import models


# =========================
# STUDENT (Internal Login)
# =========================
class Student(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email


# =========================
# EXTERNAL BOOKING
# =========================
class ExternalBooking(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ("pending", "Pending Verification"),
        ("verified", "Verified"),
        ("rejected", "Rejected"),
    )

    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    persons = models.PositiveIntegerField()
    date = models.DateField()
    slot = models.CharField(max_length=50)

    receipt = models.ImageField(upload_to="receipts/", null=True, blank=True)
    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["date", "slot"],
                name="unique_external_slot_per_day"
            )
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.date} | {self.slot} | {self.payment_status}"


# =========================
# INTERNAL BOOKING
# =========================
class InternalBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    persons = models.PositiveIntegerField()
    date = models.DateField()
    slot = models.CharField(max_length=50)
    excel_file = models.FileField(upload_to="internal_excel/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["date"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.date} - {self.slot}"


# =========================
# INTERNAL PLAYERS
# =========================
class InternalPlayer(models.Model):
    booking = models.ForeignKey(
        InternalBooking,
        related_name="players",
        on_delete=models.CASCADE
    )
    player_name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=16)

    class Meta:
        indexes = [
            models.Index(fields=["register_number"]),
        ]

    def __str__(self):
        return f"{self.player_name} ({self.register_number})"

class RegisterOverride(models.Model):
    register_number = models.CharField(max_length=16, unique=True)
    allow_more_than_two = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.register_number

# =========================
# PENDING STUDENT SIGNUP (OTP)
# =========================
class PendingStudent(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email