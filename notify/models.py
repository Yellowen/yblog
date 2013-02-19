# -----------------------------------------------------------------------------
#    lxsameer.com
#    Copyright (C) 2011-2012 Sameer Rahmani <lxsameer@gnu.org>
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

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site


class Tip(models.Model):
    """
    This model holds the tips.
    """
    content = models.CharField(_("Tip"), max_length=256)
    site = models.ForeignKey(Site, verbose_name=_("Site"),
                             null=True, blank=True)

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name = _("Tip")
        verbose_name_plural = _("Tips")

