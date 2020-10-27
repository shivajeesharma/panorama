# import lms.urls
# def show_urls(urllist):
#     result = []
#     for entry in urllist:
#         # if entry.regex.pattern:
#         if hasattr(entry, 'url_patterns'):
#             if not entry.regex.pattern:
#                 show_urls(entry.url_patterns)
#                 continue
#             else:
#                 name = entry.urlconf_name.__name__ if hasattr(entry.urlconf_name, '__name__') else entry.regex.pattern
#         else:
#             name = entry.name if entry.name else entry.regex.pattern
#         result.append([entry.regex.pattern, name])
#         print("['{}','{}'],".format(entry.regex.pattern, name))
#     return result
#
# show_urls(lms.urls.urlpatterns)


urlpatterns = [
    ['^$', 'root'],
    ['^email_confirm/(?P<key>[^/]*)$', 'confirm_email_change'],
    ['^activate/(?P<key>[^/]*)$', 'activate'],
    ['^accounts/disable_account_ajax$', 'disable_account_ajax'],
    ['^accounts/manage_user_standing', 'manage_user_standing'],
    ['^change_setting$', 'change_setting'],
    ['^change_email_settings$', 'change_email_settings'],
    ['^account/password$', 'password_change_request'],
    ['^account/account_recovery', 'account_recovery'],
    ['^password_reset/$', 'password_reset'],
    ['^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm'],
    ['^account_recovery_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'account_recovery_confirm'],
    ['^course_run/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/refund_status$', 'course_run_refund_status'],
    ['^activate_secondary_email/(?P<key>[^/]*)$', 'activate_secondary_email'],
    ['^password_reset_complete/$', 'password_reset_complete'],
    ['^dashboard/?$', 'dashboard'],
    ['^change_enrollment$', 'change_enrollment'],
    ['^event$', '^event$'],
    ['^segmentio/event$', '^segmentio/event$'],
    ['^404$', '404'],
    ['^404$', 'static_template_view.views.render_404'],
    ['^500$', 'static_template_view.views.render_500'],
    ['^blog$', 'blog'],
    ['^contact$', 'contact'],
    ['^donate$', 'donate'],
    ['^faq$', 'faq'],
    ['^help$', 'help_edx'],
    ['^jobs$', 'jobs'],
    ['^news$', 'news'],
    ['^press$', 'press'],
    ['^media-kit$', 'media-kit'],
    ['^copyright$', 'copyright'],
    ['^press/([_a-zA-Z0-9-]+)$', 'press_release'],
    ['^privacy$', 'privacy'],
    ['^tos$', 'tos'],
    ['^contact$', 'contact'],
    ['^honor$', 'honor'],
    ['^what_is_verified_cert$', 'verified-certificate'],
    ['^faq$', 'help'],
    ['^tos_and_honor$', '#'],
    ['^press$', 'press'],
    ['^sitemap.xml$', 'sitemap_xml'],
    ['^heartbeat', 'openedx.core.djangoapps.heartbeat.urls'],
    ['^user_api/', 'openedx.core.djangoapps.user_api.legacy_urls'],
    ['^notifier_api/', 'notifier_api.urls'],
    ['^i18n/', 'django.conf.urls.i18n'],
    ['^submit_feedback$', '^submit_feedback$'],
    ['^api/enrollment/v1/', 'enrollment.urls'],
    ['^api/entitlements/', 'entitlements.api.urls'],
    ['^search/', 'search.urls'],
    ['^api/courses/', 'course_api.urls'],
    ['^api/completion/', 'completion.api.urls'],
    ['^api/user/', 'openedx.core.djangoapps.user_api.urls'],
    ['^api/profile_images/', 'openedx.core.djangoapps.profile_images.urls'],
    ['^api/val/v0/', 'edxval.urls'],
    ['^api/commerce/', 'commerce.api.urls'],
    ['^api/credit/', 'openedx.core.djangoapps.credit.urls'],
    ['^rss_proxy/', 'rss_proxy.urls'],
    ['^api/organizations/', 'organizations.urls'],
    ['^catalog/', 'openedx.core.djangoapps.catalog.urls'],
    ['^lang_pref/session_language', 'session_language'],
    ['^course_modes/', 'course_modes.urls'],
    ['^verify_student/', 'verify_student.urls'],
    ['^update_lang/', 'openedx.core.djangoapps.dark_lang.urls'],
    ['^help_token/', 'help_tokens.urls'],
    ['^api-admin/', 'openedx.core.djangoapps.api_admin.urls'],
    ['^dashboard/', 'learner_dashboard.urls'],
    ['^api/experiments/', 'experiments.urls'],
    ['^openassessment/fileupload/', 'openassessment.fileupload.urls'],
    ['^sysadmin/', 'dashboard.sysadmin_urls'],
    ['^support/', 'support.urls'],
    ['^favicon\.ico$', '^favicon\.ico$'],
    ['^wiki/create-root/$', 'root_create'],
    ['^wiki/', '^wiki/'],
    ['^notify/', '^notify/'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/course_wiki/?$', 'course_wiki'],
    ['^courses/(?:[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/wiki/',
     # '^courses/(?:[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/wiki/'],
     '^courses/wiki/'],
['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/jump_to/(?P<location>.*)$', 'jump_to'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/jump_to_id/(?P<module_id>.*)$', 'jump_to_id'],
    [
        '^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/xblock/(?P<usage_id>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))/handler/(?P<handler>[^/]*)(?:/(?P<suffix>.*))?$',
        'xblock_handler'],
    [
        '^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/xblock/(?P<usage_id>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))/handler_noauth/(?P<handler>[^/]*)(?:/(?P<suffix>.*))?$',
        'xblock_handler_noauth'],
    [
        '^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/xblock/(?P<usage_id>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))/view/(?P<view_name>[^/]*)$',
        'xblock_view'],
    ['^xblock/(?P<usage_key_string>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))$', 'render_xblock'],
    ['xblock/resource/(?P<block_type>[^/]+)/(?P<uri>.*)$', 'xblock_resource_url'],
    [
        '^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/xqueue/(?P<userid>[^/]*)/(?P<mod_id>.*?)/(?P<dispatch>[^/]*)$',
        'xqueue_callback'],
    ['^calculate$', '^calculate$'],
    ['^courses/?$', 'courses'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/about$', 'about_course'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/enroll_staff$', 'enroll_staff'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/$', 'course_root'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/info$', 'info'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/syllabus$', 'syllabus'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/survey$', 'course_survey'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/book/(?P<book_index>\d+)/$', 'book'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/book/(?P<book_index>\d+)/(?P<page>\d+)$', 'book'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/pdfbook/(?P<book_index>\d+)/$', 'pdf_book'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/pdfbook/(?P<book_index>\d+)/(?P<page>\d+)$', 'pdf_book'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/pdfbook/(?P<book_index>\d+)/chapter/(?P<chapter>\d+)/$',
     'pdf_book'],
    [
        '^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/pdfbook/(?P<book_index>\d+)/chapter/(?P<chapter>\d+)/(?P<page>\d+)$',
        'pdf_book'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/htmlbook/(?P<book_index>\d+)/$', 'html_book'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/htmlbook/(?P<book_index>\d+)/chapter/(?P<chapter>\d+)/$',
     'html_book'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/courseware/?$', 'courseware'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/courseware/(?P<chapter>[^/]*)/$', 'courseware_chapter'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/courseware/(?P<chapter>[^/]*)/(?P<section>[^/]*)/$',
     'courseware_section'],
    [
        '^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/courseware/(?P<chapter>[^/]*)/(?P<section>[^/]*)/(?P<position>[^/]*)/?$',
        'courseware_position'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/progress$', 'progress'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/progress/(?P<student_id>[^/]*)/$', 'student_progress'],
    ['^programs/(?P<program_uuid>[0-9a-f-]+)/about', 'program_marketing_view'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/instructor$', 'instructor_dashboard'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/set_course_mode_price$', 'set_course_mode_price'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/remove_coupon$', 'remove_coupon'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/add_coupon$', 'add_coupon'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/update_coupon$', 'update_coupon'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/get_coupon_info$', 'get_coupon_info'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/',
     # '^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/'],
     'courses_root'],
     ['^courses/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/discussions/settings$',
     'course_discussions_settings'],
    ['^api/cohorts/', 'openedx.core.djangoapps.course_groups.urls'],
    ['^courses/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/cohorts/settings$', 'course_cohort_settings'],
    ['^courses/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/cohorts/(?P<cohort_id>[0-9]+)?$', 'cohorts'],
    ['^courses/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/cohorts/(?P<cohort_id>[0-9]+)$', 'list_cohort'],
    ['^courses/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/cohorts/(?P<cohort_id>[0-9]+)/add$',
     'add_to_cohort'],
    ['^courses/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/cohorts/(?P<cohort_id>[0-9]+)/delete$',
     'remove_from_cohort'],
    ['^courses/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/cohorts/debug$', 'debug_cohort_mgmt'],
    ['^courses/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/discussion/topics$', 'discussion_topics'],
    ['^courses/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/verified_track_content/settings',
     'verified_track_cohorting'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/notes$', 'notes'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/notes/', 'notes.urls'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/lti_rest_endpoints/', 'lti_rest_endpoints'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/edxnotes/', 'edxnotes.urls'],
    ['^api/edxnotes/v1/', 'edxnotes.api_urls'],
    ['^api/branding/v1/', 'branding.api_urls'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/course/', 'openedx.features.course_experience.urls'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/bookmarks/', 'openedx.features.course_bookmarks.urls'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/search/', 'openedx.features.course_search.urls'],
    ['^u/', 'openedx.features.learner_profile.urls'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/learner_analytics/',
     'openedx.features.learner_analytics.urls'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/xfeature/portfolio/',
     'openedx.features.portfolio_project.urls'],
    ['^api/team/', 'lms.djangoapps.teams.api_urls'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/teams/', 'lms.djangoapps.teams.urls'],
    ['^courses/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/masquerade$', 'masquerade_update'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/generate_user_cert', 'generate_user_cert'],
    ['^api/discussion/', 'discussion_api.urls'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/discussion/', 'django_comment_client.urls'],
    ['^notification_prefs/enable/', '^notification_prefs/enable/'],
    ['^notification_prefs/disable/', '^notification_prefs/disable/'],
    ['^notification_prefs/status/', '^notification_prefs/status/'],
    ['^notification_prefs/unsubscribe/(?P<token>[a-zA-Z0-9-_=]+)/', 'unsubscribe_forum_update'],
    ['^notification_prefs/resubscribe/(?P<token>[a-zA-Z0-9-_=]+)/', 'resubscribe_forum_update'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/tab/(?P<tab_type>[^/]+)/$', 'course_tab_view'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/(?P<tab_slug>[^/]+)/$', 'static_tab'],
    [
        '^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/submission_history/(?P<student_username>[^/]*)/(?P<location>.*?)$',
        'submission_history'],
    ['^admin/password_change/$', '^admin/password_change/$'],
    ['^admin/auth/user/\d+/password/$', '^admin/auth/user/\d+/password/$'],
    ['^admin/', '^admin/'],
    ['^shoppingcart/', 'shoppingcart.urls'],
    ['^commerce/', 'lms.djangoapps.commerce.urls'],
    ['^api/course_goals/', 'lms.djangoapps.course_goals.urls'],
    ['^survey/', 'survey.urls'],
    ['^openid/provider/login/$', 'openid-provider-login'],
    ['^openid/provider/login/(?:.+)$', 'openid-provider-login-identity'],
    ['^openid/provider/identity/$', 'openid-provider-identity'],
    ['^openid/provider/xrds/$', 'openid-provider-xrds'],
    ['^oauth2/', 'openedx.core.djangoapps.oauth_dispatch.urls'],
    ['^oauth2/', 'edx_oauth2_provider.urls'],
    ['^_o/', 'oauth2_provider.urls'],
    ['^instructor_task_status/$', 'instructor_task_status'],
    ['^debug/show_parameters$', '^debug/show_parameters$'],
    ['^auth/inactive', 'third_party_inactive_redirect'],
    ['^auth/custom_auth_entry', 'tpa_post_to_custom_auth_form'],
    ['^auth/saml/metadata.xml', '^auth/saml/metadata.xml'],
    ['^auth/login/(?P<backend>lti)/$', '^auth/login/(?P<backend>lti)/$'],
    ['^auth/', 'social_django.urls'],
    ['api/third_party_auth/', 'third_party_auth.api.urls'],
    ['^oauth2/login/$', 'login_with_access_token'],
    ['^certificates/', 'certificates.urls'],
    ['^update_certificate$', 'update_certificate'],
    ['^update_example_certificate$', 'update_example_certificate'],
    ['^request_certificate$', 'request_certificate'],
    ['^api/certificates/', 'lms.djangoapps.certificates.apis.urls'],
    ['^xdomain_proxy.html$', 'xdomain_proxy'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/', 'ccx.urls'],
    ['^api/ccx/', 'lms.djangoapps.ccx.api.urls'],
    ['config/self_paced', 'config/self_paced'],
    ['config/programs', 'config/programs'],
    ['config/catalog', 'config/catalog'],
    ['config/forums', 'config/forums'],
    ['^template/(?P<template>.+)$', '^template/(?P<template>.+)$'],
    ['^csrf/api/', 'csrf.api.urls'],
    ['^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/discussion/forum/', 'lms.djangoapps.discussion.urls'],
    ['api/grades/', 'lms.djangoapps.grades.api.urls'],
    ['^account/settings$', 'account_settings'],
    ['^create_account$', 'create_account'],
    ['^login_post$', 'login_post'],
    ['^login_ajax$', 'login'],
    ['^login_ajax/(?P<error>[^/]*)$', '^login_ajax/(?P<error>[^/]*)$'],
    ['^login_refresh$', 'login_refresh'],
    ['^logout$', 'logout'],
    ['^account/finish_auth$', 'finish_auth'],
    ['^login$', 'signin_user'],
    ['^register$', 'register_user'],
    ['^zendesk_proxy/', 'openedx.core.djangoapps.zendesk_proxy.urls'],
    ['api/bookmarks/', 'openedx.core.djangoapps.bookmarks.urls'],
    ['courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/instructor/api/',
     'lms.djangoapps.instructor.views.api_urls'],
    ['^journals/', 'openedx.features.journals.urls'],
    ['theming/', 'openedx.core.djangoapps.theming.urls'],
    ['^api/', 'edx_proctoring.urls'],
    ['^api/completion/', 'completion.api.urls'],
]

# CMS urls
urlpatterns += [
    ['^create_account$', 'create_account'],
    ['^login_post$', 'login_post'],
    ['^login_ajax$', 'login'],
    ['^login_ajax/(?P<error>[^/]*)$', '^login_ajax/(?P<error>[^/]*)$'],
    ['^login_refresh$', 'login_refresh'],
    ['^logout$', 'logout'],
    ['^email_confirm/(?P<key>[^/]*)$', 'confirm_email_change'],
    ['^activate/(?P<key>[^/]*)$', 'activate'],
    ['^accounts/disable_account_ajax$', 'disable_account_ajax'],
    ['^accounts/manage_user_standing', 'manage_user_standing'],
    ['^change_setting$', 'change_setting'],
    ['^change_email_settings$', 'change_email_settings'],
    ['^account/password$', 'password_change_request'],
    ['^account/account_recovery', 'account_recovery'],
    ['^password_reset/$', 'password_reset'],
    ['^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm'],
    ['^account_recovery_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'account_recovery_confirm'],
    ['^course_run/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/refund_status$', 'course_run_refund_status'],
    ['^activate_secondary_email/(?P<key>[^/]*)$', 'activate_secondary_email'],
    ['^password_reset_complete/$', 'password_reset_complete'],
    ['^transcripts/upload$', 'upload_transcripts'],
    ['^transcripts/download$', 'download_transcripts'],
    ['^transcripts/check$', 'check_transcripts'],
    ['^transcripts/choose$', 'choose_transcripts'],
    ['^transcripts/replace$', 'replace_transcripts'],
    ['^transcripts/rename$', 'rename_transcripts'],
    ['^preview/xblock/(?P<usage_key_string>.*?)/handler/(?P<handler>[^/]*)(?:/(?P<suffix>.*))?$', 'preview_handler'],
    ['^xblock/(?P<usage_key_string>.*?)/handler/(?P<handler>[^/]*)(?:/(?P<suffix>.*))?$', 'component_handler'],
    ['^xblock/resource/(?P<block_type>[^/]*)/(?P<uri>.*)$', 'xblock_resource_url'],
    ['^not_found$', 'not_found'],
    ['^server_error$', 'server_error'],
    ['^organizations$', 'organizations'],
    ['^event$', 'event'],
    ['^heartbeat', 'openedx.core.djangoapps.heartbeat.urls'],
    ['^user_api/', 'openedx.core.djangoapps.user_api.legacy_urls'],
    ['^i18n/', 'django.conf.urls.i18n'],
    ['^api/user/', 'openedx.core.djangoapps.user_api.urls'],
    ['^lang_pref/session_language', 'session_language'],
    ['^update_lang/', 'openedx.core.djangoapps.dark_lang.urls'],
    ['^help_token/', 'help_tokens.urls'],
    ['^api/', 'cms.djangoapps.api.urls'],
    ['^$', 'homepage'],
    ['^howitworks$', 'howitworks'],
    ['^signup$', 'signup'],
    ['^signin$', 'login'],
    ['^signin_redirect_to_lms$', 'login_redirect_to_lms'],
    ['^request_course_creator$', 'request_course_creator'],
    ['^course_team/(?P<course_key_string>([^/]+/[^/]+/[^/]+|[^/:]+:[^/+]+\+[^/+]+(\+[^/]+)?))(?:/(?P<email>.+))?$',
     'course_team_handler'],
    ['^course_info/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$', 'course_info_handler'],
    ['^course_info_update/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/(?P<provided_id>\d+)?$',
     'course_info_update_handler'],
    ['^home/?$', 'home'],
    ['^course/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/search_reindex?$', 'course_search_index_handler'],
    ['^course/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)?$', 'course_handler'],
    ['^checklists/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)?$', 'checklists_handler'],
    ['^course_notifications/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/(?P<action_state_id>\d+)?$',
     'course_notifications_handler'],
    ['^course_rerun/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$', 'course_rerun_handler'],
    ['^container/(?P<usage_key_string>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))$', 'container_handler'],
    ['^orphan/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$', 'orphan_handler'],
    [
        '^assets/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/(?P<asset_key_string>(?:/?c4x(:/)?/[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))?$',
        'assets_handler'],
    ['^import/(?P<course_key_string>([^/]+/[^/]+/[^/]+|[^/:]+:[^/+]+\+[^/+]+(\+[^/]+)?))$', 'import_handler'],
    ['^import_status/(?P<course_key_string>([^/]+/[^/]+/[^/]+|[^/:]+:[^/+]+\+[^/+]+(\+[^/]+)?))/(?P<filename>.+)$',
     'import_status_handler'],
    ['^api/courses/', 'cms.djangoapps.contentstore.api.urls'],
    ['^export/(?P<course_key_string>([^/]+/[^/]+/[^/]+|[^/:]+:[^/+]+\+[^/+]+(\+[^/]+)?))$', 'export_handler'],
    ['^export_output/(?P<course_key_string>([^/]+/[^/]+/[^/]+|[^/:]+:[^/+]+\+[^/+]+(\+[^/]+)?))$',
     'export_output_handler'],
    ['^export_status/(?P<course_key_string>([^/]+/[^/]+/[^/]+|[^/:]+:[^/+]+\+[^/+]+(\+[^/]+)?))$',
     'export_status_handler'],
    ['^xblock/outline/(?P<usage_key_string>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))$',
     'xblock_outline_handler'],
    ['^xblock/container/(?P<usage_key_string>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))$',
     'xblock_container_handler'],
    ['^xblock/(?P<usage_key_string>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))/(?P<view_name>[^/]+)$',
     'xblock_view_handler'],
    ['^xblock/(?P<usage_key_string>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))?$', 'xblock_handler'],
    ['^tabs/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$', 'tabs_handler'],
    ['^settings/details/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$', 'settings_handler'],
    ['^settings/grading/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)(/)?(?P<grader_index>\d+)?$',
     'grading_handler'],
    ['^settings/advanced/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$', 'advanced_settings_handler'],
    ['^textbooks/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$', 'textbooks_list_handler'],
    ['^textbooks/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/(?P<textbook_id>\d[^/]*)$',
     'textbooks_detail_handler'],
    ['^videos/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)(?:/(?P<edx_video_id>[-\w]+))?$', 'videos_handler'],
    ['^video_images/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)(?:/(?P<edx_video_id>[-\w]+))?$',
     'video_images_handler'],
    ['^transcript_preferences/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$',
     'transcript_preferences_handler'],
    ['^transcript_credentials/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$',
     'transcript_credentials_handler'],
    ['^transcript_download/$', 'transcript_download_handler'],
    ['^transcript_upload/$', 'transcript_upload_handler'],
    [
        '^transcript_delete/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)(?:/(?P<edx_video_id>[-\w]+))?(?:/(?P<language_code>[^/]*))?$',
        'transcript_delete_handler'],
    ['^video_encodings_download/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$', 'video_encodings_download'],
    ['^group_configurations/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$',
     'group_configurations_list_handler'],
    [
        '^group_configurations/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/(?P<group_configuration_id>\d+)(/)?(?P<group_id>\d+)?$',
        'group_configurations_detail_handler'],
    ['^api/val/v0/', 'edxval.urls'],
    ['^api/tasks/v0/', 'user_tasks.urls'],
    ['^accessibility$', 'accessibility'],
    ['^library/(?P<library_key_string>library-v1:[^/+]+\+[^/+]+)?$', 'library_handler'],
    ['^library/(?P<library_key_string>library-v1:[^/+]+\+[^/+]+)/team/$', 'manage_library_users'],
    ['^admin/password_change/$', '^admin/password_change/$'],
    ['^admin/auth/user/\d+/password/$', '^admin/auth/user/\d+/password/$'],
    ['^admin/', '^admin/'],
    ['^course/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/entrance_exam/?$',
     # '^course/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/entrance_exam/?$'],
     'course/entrance_exam'],
    ['^certificates/activation/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/',
     'certificate_activation_handler'],
    [
        '^certificates/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/(?P<certificate_id>\d+)/signatories/(?P<signatory_id>\d+)?$',
        'signatory_detail_handler'],
    ['^certificates/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/(?P<certificate_id>\d+)?$',
     'certificates_detail_handler'],
    ['^certificates/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$', 'certificates_list_handler'],
    ['^maintenance/', 'maintenance.urls'],
    ['^template/(?P<template>.+)$', 'openedx.core.djangoapps.debug.views.show_reference_template'],
    ['^404$', '^404$'],
    ['^500$', '^500$'],
    ['^zendesk_proxy/', 'openedx.core.djangoapps.zendesk_proxy.urls'],
    ['theming/', 'openedx.core.djangoapps.theming.urls'],
    ['^api/', 'edx_proctoring.instructor_dashboard_exam_urls'],

]