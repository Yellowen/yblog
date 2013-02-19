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

from django.http import HttpResponse

from models import Tip


def tips(request):
    """
    Return a random tip.
    """
    from random import randrange

    count = Tip.objects.all().count()
    pk = 1
    if count == 0:
        return HttpResponse("")
    if count != 1:
        pk = randrange(1, count + 1)
    tip = Tip.objects.get(id=pk)
    return HttpResponse(tip.content)
