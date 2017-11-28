# Copyright (c) 2010, Evil Airborn- http://www.theairborn.com
#
# This file is a Dos Attack Tools Named Airlated.
#
# This Tool is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# Airlated is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Airlated.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup
import py2exe

setup(
    name = 'Airlated',
    description = 'Airlated By The EvilAirborn',
    version = 1.0',

    windows = [
      {
        'script': 'gui.py',
      }
      ],

    options = {
      'py2exe': {
        'packages': 'encodings',
        'includes': 'cairo, pango, pangocairo, atk, gobject, gio',
        }
      },

    data_files=[
      'interface.glade',
      '../build/src/http_dos_cli.exe',
      '../license.txt',
      'VERSION'
      ]
    )
