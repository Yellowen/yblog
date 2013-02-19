# -----------------------------------------------------------------------------
#    YBlog
#    Copyright (C) 2011-2013 Yellown Inc
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# -----------------------------------------------------------------------------

import os

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from ultra_blog import typediscover

typediscover()


urlpatterns = patterns('',

    (r"^", include("ultra_blog.blogs_urls")),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^socket/$', 'yblog.views.socket'),
    (r'^search/', include('haystack.urls')),
    (r'^notify/', include('notify.urls')),
    (r'^robots\.txt$', include('robots.urls')),
)

urlpatterns += patterns('',
        (r'^statics/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(os.path.dirname(__file__),\
                                        '../media/statics').replace('\\', '/')}),
)
