from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from website.models import Course,Video,Payment,UserCourse,CouponCode
from time import time
from django.contrib.auth.decorators import login_required
from course.settings import *
import razorpay





client=razorpay.Client(auth=(KEY_ID,KEY_SECRET))




@login_required(login_url='/login')
def checkout(request,slug):
    
    
    course=Course.objects.get(slug=slug)
    
    
    user=request.user
    action=request.GET.get('action')
    couponcode=request.GET.get('couponcode')
    coupon_code_message=None
    coupon=None
    order=None
    payment=None
    error=None
    if action=='create_payment':
        try:
            user_course=UserCourse.objects.get(user=user,course=course)
            error="You are already Enrolled in this course"
        except:
            pass
        if error is None:
            amount=int((course.price-(course.price*course.discount*0.01))*100)
            currency="INR"
            notes={
                "email":user.email,
                "name":f'{user.first_name} {user.last_name}"'

            }
            receipt=f"Order-{int(time())}"
            order=client.order.create({"receipt":receipt,
            "notes":notes,
            "amount":amount,
            "currency":currency})
            payment=Payment()
            payment.user=user
            payment.course=course
            payment.order_id=order.get("id")
            payment.save()

    

        
    context={"course":course,
    "order":order,
    "payment":payment,
    "user":user,
    "error":error,
    "coupon_code_message":coupon_code_message,
    "coupon":coupon
    }
   

    return render(request, template_name='courses/check_out.html',context=context)
    

@csrf_exempt
def verifyPayment(request):
    if request.method=="POST":
        data=request.POST
        context={}
        print(data)
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id=data['razorpay_order_id']
            razorpay_payment_id=data['razorpay_payment_id']
            payment=Payment.objects.get(order_id=razorpay_order_id)    
            payment.payment_id=razorpay_payment_id
            payment.status=True

            userCourse=UserCourse(user=payment.user,course=payment.course)
            userCourse.save()

            payment.user_course=userCourse
            payment.save()


            return redirect ("my-courses")
        except:
            return HttpResponse("invalid payment details")
           
        