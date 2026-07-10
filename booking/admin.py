from django.contrib import admin
from django.utils.html import format_html
from .models import ExternalBooking, InternalBooking, InternalPlayer, RegisterOverride, Student, PendingStudent

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    search_fields = ("username", "email")

@admin.register(PendingStudent)
class PendingStudentAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "otp", "created_at")
    search_fields = ("username", "email")


@admin.register(ExternalBooking)
class ExternalBookingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "mobile",
        "date",
        "slot",
        "persons",
        "created_at",
        "receipt_preview",
        "payment_status",
    )

    list_editable = ("payment_status",)
    list_filter = ("date", "payment_status")
    search_fields = ("name", "mobile", "slot")

    readonly_fields = ("receipt_preview",)

    def receipt_preview(self, obj):
        if obj.receipt:
            return format_html(
                '<a href="{}" target="_blank">View Receipt</a>',
                obj.receipt.url
            )
        return "No Receipt"

    receipt_preview.short_description = "Receipt"



class InternalPlayerInline(admin.TabularInline):
    model = InternalPlayer
    extra = 0
    readonly_fields = ("player_name", "register_number")


@admin.register(InternalBooking)
class InternalBookingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "mobile",
        "persons",
        "date",
        "slot",
        "created_at",
        "excel_preview",
    )
    list_filter = ("date", "slot")
    search_fields = ("name", "mobile")
    ordering = ("-created_at",)
    inlines = [InternalPlayerInline]
    readonly_fields = ("excel_preview",)

    def excel_preview(self, obj):
        if obj.excel_file:
            return format_html(
                '<a href="{}" target="_blank" download>Download Excel</a>',
                obj.excel_file.url
            )
        return "No File"
    
    excel_preview.short_description = "Excel File"


@admin.register(RegisterOverride)
class RegisterOverrideAdmin(admin.ModelAdmin):
    list_display = (
        "register_number",
        "allow_more_than_two",
    )
