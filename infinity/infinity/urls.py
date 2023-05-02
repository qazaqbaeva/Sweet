from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path


from hadipage.views import *
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hadipage.urls')),
    # path('api/v1/womenlist/',ZavedeniyaAPIView.as_view())


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ]+urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound404
handler403 = forbiddenError403
handler400 = badRequest400
handler500 = serverError500