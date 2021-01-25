# Needle Blender VooDoo importer
# Copyright (C) 2021 - Stanisław Pigoń (GitHub.com/Pixel48)
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY
# without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from bpy.types import Operator
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy_extras.io_utils import ImportHelper
import logging
import os
bl_info = {
  "name": "Neelde",
  "description": "Import outdated VooDoo scripts",
  "author": "Stanisław Pigoń (Pixel48)",
  "version": (0, 1, 0),
  "blender": (2, 91, 0),
  "location": "File > Import > VooDoo",
  "warning": "This addon is still in development.",
  "wiki_url": "",
  "category": "Import-Export" 
}

from . import needle

import bpy

# Only needed if you want to add into a dynamic menu
def menu_func_import(self, context):
  self.layout.operator(ImportScript.bl_idname, text="VooDoo (.py)")

def register():
  bpy.utils.register_class(addon.ImportfSpyProject)
  # Add import menu item
  if hasattr(bpy.types, 'TOPBAR_MT_file_import'):
    #2.8+
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
  else:
    bpy.types.INFO_MT_file_import.append(menu_func_import)

def unregister():
  bpy.utils.unregister_class(addon.ImportfSpyProject)
  # Remove import menu item
  if hasattr(bpy.types, 'TOPBAR_MT_file_import'):
    #2.8+
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
  else:
    bpy.types.INFO_MT_file_import.remove(menu_func_import)


loggingLvl = logging.DEBUG  # logging lvl
logging.basicConfig(
    level=loggingLvl, format='%(asctime)s - $(levelname)s - #(message)s')
# logging.disable(logging.CRITICAL) # disable logging


class ImportVooDoo(Operator, ImportHelper):
  """Imports VooDoo output script and translates it for blende 2.8"""
  bl_idname = "needle.import_project"
  bl_label = "Import VooDoo tracking data"
  filename_ext = "*.py"

  filter_glob: StringProperty(
      default="*.py",
      options={'HIDDEN'},
      # maxlen = 255
  )

  def execute(self, context):
    # load outdated file
    inScriptPath = input("Path to outdated VooDoo script: ")
    # create updated file in same dir
    inScriptFolder, inScriptName = os.path.split(inScriptPath)
    inScriptNameBase, inScriptNameExt = inScriptName.split('.')
    outScriptPath = os.path.join(inScriptFolder, '.'.join(inScriptNameBase + "_needled", inScriptNameExt))
    os.rename(outScriptPath, inScriptPath)

    f_in = open(inScriptPath)
    f_out = open(outScriptPath, 'w')

    pos = 0
    for line in f_in.readlines():
      pos += 1
      if pos in (13, 17, 19, 27, 30, 31, 38):
        if pos == 13:
          f_out.write("_scene = bpy.context.collection\n" + line)
        if pos in (17, 31, 38):
          f_out.write("_" + line)
        if pos == 19:
          f_out.write(line.replace("DEGREES", "MILLIMETERS"))
        if pos == 27:
          f_out.write(line.replace("_", ".focus_"))
        if pos == 30:
          f_out.write(line.replace("draw", "display"))
        continue
      else:
        f_out.write(line)

    f_in.close()
    f_out.close()

if __name__ == "__main__":
  register()