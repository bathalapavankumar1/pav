from django.contrib import admin
from .models import Complaint, Branch, Category, Feedback, Student, Hod

# Customize the Complaint Admin
from django.contrib import admin
from .models import Complaint, Branch, Category, Student, Hod

import matplotlib.pyplot as plt
import io
import base64
from django.db.models import Count, Avg, F
from django.utils.html import format_html
from django.contrib.admin.views.main import ChangeList

class ComplaintAdmin(admin.ModelAdmin):
    change_list_template = "admin/complaint_change_list.html"  # Custom template for Complaints section

    # Display fields
    fields = ['title', 'description', 'priority', 'branch', 'category', 'status']
    list_display = ['id', 'title', 'description', 'priority', 'branch', 'category', 'status']
    list_editable = ['status']

    def changelist_view(self, request, extra_context=None):
        # Existing data to show in complaint list view
        changelist = self.get_changelist_instance(request)

        # Add visualizations
        grievances_by_category = (
            Complaint.objects.values("category__category")
            .annotate(count=Count("id"))
            .order_by("-count")
        )
        avg_resolution_time = Complaint.objects.filter(
            status="SO"
        ).aggregate(avg_time=Avg(F("resolved_at") - F("c_date")))

        # Generate a pie chart
        fig, ax = plt.subplots(figsize=(3, 3))  # Adjust size of the pie chart
        categories = [item["category__category"] for item in grievances_by_category]
        counts = [item["count"] for item in grievances_by_category]

        # Define custom colors
        custom_colors = [ '#FFD700']

        ax.pie(
            counts,
            labels=categories,
            autopct="%1.1f%%",
            startangle=90,
            colors=custom_colors[:len(categories)],  # Use custom colors
        )
        ax.set_title("Grievances by Category")
        plt.tight_layout()

        # Convert chart to image URL
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graph_url = "data:image/png;base64," + base64.b64encode(image_png).decode()

        # Pass data to the template
        extra_context = extra_context or {}
        extra_context.update({
            "changelist": changelist,  # Keep previous list view data
            "grievances_by_category": grievances_by_category,
            "avg_resolution_time": avg_resolution_time["avg_time"],
            "graph_url": graph_url,
        })
        return super().changelist_view(request, extra_context=extra_context)

# Customize the Branch Admin
class BranchAdmin(admin.ModelAdmin):
    fields = []

# Customize the Category Admin
class CategoryAdmin(admin.ModelAdmin):
    fields = []


# Register all models in the admin
admin.site.register(Branch, BranchAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Student)
admin.site.register(Hod)
admin.site.register(Complaint, ComplaintAdmin)
