from django.contrib import admin
from website.models import Course,CouponCode,Tag,Prerequisite,Learning,Video,Payment,UserCourse
from django.utils.html import format_html
# Register your models here.

class VideoAdmin(admin.TabularInline):
    model=Video

class TagAdmin(admin.TabularInline):
    model=Learning



class LearningAdmin(admin.TabularInline):
    model=Tag


class PrerequisiteAdmin(admin.TabularInline):
    model=Prerequisite

class CourseAdmin(admin.ModelAdmin):
    inlines=[TagAdmin,LearningAdmin,PrerequisiteAdmin,VideoAdmin]
    list_display=["name","get_price",'get_discount',"active"]
    list_filter=("discount","active")
    def get_discount(self,course):
        return f'{course.discount}%'

    def get_price(self,course):
        return f'₹{course.price}'

    get_discount.short_description="Discount"
    get_price.short_description="Price"


class PaymentAdmin(admin.ModelAdmin):
    model=UserCourse
    list_display=["order_id","user","course","status"]
    list_filter=("status","course")


class UserCourseAdminModel(admin.ModelAdmin):
    model=Payment
    list_display=["user","course",]
    list_filter=["course"]


    



admin.site.register(Course,CourseAdmin)
admin.site.register(Video)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(UserCourse,UserCourseAdminModel)
admin.site.register(CouponCode)