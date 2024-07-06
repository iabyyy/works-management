from django.urls import path

from new_app import views, manager_views, customer_views, admin_views

urlpatterns = [
    path('',views.test,name='home'),
    path('user',views.login_view,name='user'),
    path('dash',views.dash,name='dash'),
    path('customer_reg',views.customer_reg,name='customer_reg'),
    path('manager',views.manager_reg,name='manager'),
    path('managerpage',views.managerpage,name='managerpage'),
    path('customerpage',views.customerpage,name='customerpage'),
    path('adminpage',views.staffpage,name='adminpage'),
    path('managertable',views.managertable,name='managertable'),
    path('managerdelete<int:id>/',views.managerdelete,name='managerdelete'),
    path('managerupdate<int:id>/',views.managerupdate,name='managerupdate'),
    path('customertable',views.customertable,name='customertable'),
    path('customerdelete<int:id>/',views.customerdelete,name='customerdelete'),
    path('profile_view',manager_views.profile_view,name='profile_view'),
    path('customer_profile',customer_views.customer_profile,name='customer_profile'),
    path('customer_feed',customer_views.customer_feed,name='customer_feed'),
    path('customer_feedview',customer_views.customer_feedview,name='customer_feedview'),
    path('adminfeedbackview',admin_views.adminfeedbackview,name='adminfeedbackview'),
    path('feedupdate<int:id>/',admin_views.feedupdate,name='feedupdate'),
    path('schedule',admin_views.schedule,name='schedule'),
    path('schedule_table',admin_views.schedule_table,name='schedule_table'),
    path('disable<int:id>/',admin_views.disable,name='disable'),
    path('customer_schedule',customer_views.customer_schedule,name='customer_schedule'),
    path('customer_booking<int:id>/',customer_views.customer_booking,name='customer_booking'),
    path('bookingview',customer_views.bookingview,name='bookingview'),
    path('manager_booking_approve',manager_views.manager_booking_approve,name='manager_booking_approve'),
    path('manager_approval<int:id>/',manager_views.approval,name='manager_approval'),
    path('manager_rejection<int:id>/',manager_views.rejection,name='manager_rejection'),
    path('work_assaign',admin_views.work_assaign,name='work_assaign'),
    path('admin_work_create/<int:id>/',admin_views.admin_work_create,name='admin_work_create'),
    path('managerworkassign',manager_views.managerwork,name='managerworkassign'),
    path('managerworkupdate<int:id>/',manager_views.managerworkupdate,name='managerworkupdate'),
    path('vehiclestatus',customer_views.vehiclestatus,name='vehiclestatus'),
    path('payment<int:id>/',customer_views.payment,name='payment')


]
