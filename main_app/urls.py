from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories, name='categories'),

    # path('posting/<int:subcategory_id>/', views.job_subcategory, name='subcategory'),

    path('graphic_design/', views.graphic_design_index, name='graphic_design'),
    path('graphic_design/logo_design_jobs/', views.logo_design_jobs, name='logo_design_jobs'),
    path('graphic_design/web_ui_jobs/', views.web_ui_jobs, name='web_ui_jobs'),
    path('graphic_design/mobile_ui_design_jobs/', views.mobile_ui_design_jobs, name='mobile_ui_design_jobs'),
    path('graphic_design/illustration_jobs/', views.illustration_jobs, name='illustration_jobs'),
    path('graphic_design/email_design_jobs/', views.email_design_jobs, name='email_design_jobs'),
    path('graphic_design/infographics_design_jobs/', views.infographics_design_jobs, name='infographics_design_jobs'),
    path('graphic_design/branding_and_identity_design_jobs/', views.branding_and_identity_design_jobs, name='branding_and_identity_design_jobs'),

    path('web_dev/', views.web_dev_index, name='web_dev'),
    path('web_dev/front_end_development_jobs/', views.front_end_development_jobs, name='front_end_development_jobs'),
    path('web_dev/back_end_development_jobs/', views.back_end_development_jobs, name='back_end_development_jobs'),
    path('web_dev/full_stack_development_jobs/', views.full_stack_development_jobs, name='full_stack_development_jobs'),
    path('web_dev/e_commerce_development_jobs/', views.e_commerce_development_jobs, name='e_commerce_development_jobs'),
    path('web_dev/web_application_development_jobs/', views.web_application_development_jobs, name='web_application_development_jobs'),
    path('web_dev/responsive_web_design_jobs/', views.responsive_web_design_jobs, name='responsive_web_design_jobs'),

    path('digital_marketing/', views.digital_marketing_index, name='digital_marketing'),
    path('digital_marketing/search_engine_optimization_jobs/', views.search_engine_optimization_jobs, name='search_engine_optimization_jobs'),
    path('digital_marketing/social_media_marketing_jobs/', views.social_media_marketing_jobs, name='social_media_marketing_jobs'),
    path('digital_marketing/pay_per_click_advertising_jobs/', views.pay_per_click_advertising_jobs, name='pay_per_click_advertising_jobs'),
    path('digital_marketing/content_marketing_jobs/', views.content_marketing_jobs, name='content_marketing_jobs'),
    path('digital_marketing/email_marketing_jobs/', views.email_marketing_jobs, name='email_marketing_jobs'),
    path('digital_marketing/influencer_marketing_jobs/', views.influencer_marketing_jobs, name='influencer_marketing_jobs'),
    path('digital_marketing/online_reputation_management_jobs/', views.online_reputation_management_jobs, name='online_reputation_management_jobs'),
    
    path('mobile_app_dev/', views.mobile_app_dev_index, name='mobile_app_dev'),
    path('mobile_app_dev/ios_app_development_jobs/', views.ios_app_development_jobs, name='ios_app_development_jobs'),
    path('mobile_app_dev/andriod_app_development_jobs/', views.andriod_app_development_jobs, name='andriod_app_development_jobs'),
    path('mobile_app_dev/cross_platform_app_development_jobs/', views.cross_platform_app_development_jobs, name='cross_platform_app_development_jobs'),
    path('mobile_app_dev/mobile_game_development_jobs/', views.mobile_game_development_jobs, name='mobile_game_development_jobs'),
    path('mobile_app_dev/app_testing_and_quality_assurance_jobs/', views.app_testing_and_quality_assurance_jobs, name='app_testing_and_quality_assurance_jobs'),
    path('mobile_app_dev/app_maintenance_and_updates_jobs/', views.app_maintenance_and_updates_jobs, name='app_maintenance_and_updates_jobs'),
    
    path('cybersecurity/', views.cybersecurity_index, name='cybersecurity'),
    path('cybersecurity/network_security_jobs/', views.network_security_jobs, name='network_security_jobs'),
    path('cybersecurity/ethical_hacking_jobs/', views.ethical_hacking_jobs, name='ethical_hacking_jobs'),
    path('cybersecurity/penetration_testing_jobs/', views.penetration_testing_jobs, name='penetration_testing_jobs'),
    path('cybersecurity/security_auditing_jobs/', views.security_auditing_jobs, name='security_auditing_jobs'),
    path('cybersecurity/data_encription_jobs/', views.data_encription_jobs, name='data_encription_jobs'),
    path('cybersecurity/incident_response_jobs/', views.incident_response_jobs, name='incident_response_jobs'),
    path('cybersecurity/security_compliance_jobs/', views.security_compliance_jobs, name='security_compliance_jobs'),

    path('register/', views.register, name='register'),
    path('register/client/', views.reg_client, name='reg_client'),
    path('register/freelancer/', views.reg_freelancer, name='reg_freelancer'),
    path('client_signup/', views.client_signup, name='client_signup'),
    path('freelancer_signup/', views.freelancer_signup, name='freelancer_signup'),
    path('posting/create/', views.JobCreate.as_view(), name='posting_create'),
    path('posting/<int:pk>/update/', views.JobUpdate.as_view(), name='posting_update'),
    path('posting/<int:pk>/delete/', views.JobDelete.as_view(), name='posting_delete'),
    path('posting/<int:job_id>/', views.job_detail, name='posting_detail'),
    path('profile/client/<int:client_id>', views.profile_client, name='prof_client'),
    path('profile/client/<int:pk>/update', views.ClientUpdate.as_view(), name='client_update'),
    path('profile/client/<int:pk>/delete', views.ClientDelete.as_view(), name='client_delete'),
    path('profile/freelancer/<int:freelancer_id>', views.profile_freelancer, name='prof_freelancer'),
    path('profile/freelancer/<int:pk>/update', views.FreelancerUpdate.as_view(), name='freelancer_update'),
    path('profile/freelancer/<int:pk>/delete', views.FreelancerDelete.as_view(), name='freelancer_delete'),

]