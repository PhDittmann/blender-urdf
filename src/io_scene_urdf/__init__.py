############################################################################
#    Copyright (C) 2014 by Ralf Kaestner                                   #
#    ralf.kaestner@gmail.com                                               #
#                                                                          #
#    This program is free software; you can redistribute it and#or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
############################################################################

bl_info = {
  "name": "Unified Robot Description Format (URDF)",
  "author": "Ralf Kaestner",
  "version": (0, 0, 1),
  "blender": (2, 81, 6),
  "location": "File > Import-Export",
  "description": "Import-Export Unified Robot Description Format (URDF)",
  "warning": "",
  "doc_url": "http://github.com/kralf/blender-urdf",
  "tracker_url": "http://github.com/kralf/blender-urdf",
  "support": "COMMUNITY",
  "category": "Import-Export"
}


if "bpy" in locals():
  #import imp # Blender 2.8
  import importlib
  if "import_urdf" in locals():
    importlib.reload(import_urdf)
  if "import_urdf_xacro" in locals():
    importlib.reload(import_urdf_xacro)
  #if "export_urdf" in locals():
    #imp.reload(export_urdf) # Blender 2.8
  #  importlib.reload(export_urdf)
  #if "export_urdf_xacro" in locals():
    #imp.reload(export_urdf_xacro) # Blender 2.8
  #  importlib.reload(export_urdf_xacro)


import os
import bpy
from bpy.props import CollectionProperty, StringProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper, ExportHelper


class ImportURDF(bpy.types.Operator, ImportHelper):
  bl_idname = "import_scene.urdf"
  bl_label = "Import URDF"
  bl_options = {"PRESET", "UNDO"}

  filename_ext = ".urdf"
  filter_glob = StringProperty(default="*.urdf", options = {"HIDDEN"})

  def execute(self, context):
    keywords = self.as_keywords()
    
    from . import import_urdf
    return import_urdf.load(context, **keywords)

  def draw(self, context):
    pass

class ImportURDFXacro(bpy.types.Operator, ImportHelper):
  bl_idname = "import_scene_urdf.xacro"
  bl_label = "Import URDF/Xacro"
  bl_options = {"PRESET", "UNDO"}

  filename_ext = ".urdf.xacro"
  filter_glob = StringProperty(default="*.urdf.xacro", options = {"HIDDEN"})
 
  def execute(self, context):
    keywords = self.as_keywords()
     
    from . import import_urdf_xacro
    return import_urdf_xacro.load(self, context, **keywords)

  def draw(self, context):
    pass
  
def menu_func_import(self, context):
  self.layout.operator(ImportURDF.bl_idname, text="Unified Robot Description Format (.urdf)")
  self.layout.operator(ImportURDFXacro.bl_idname, text="Unified Robot Description Format/Xacro (.urdf.xacro)")


def menu_func_export(self, context):
  #self.layout.operator(ExportURDF.bl_idname, text="Unified Robot Description Format (.urdf)")
  #self.layout.operator(ExportURDFXacro.bl_idname, text="Unified Robot Description Format/Xacro (.urdf.xacro)")
  pass

classes = (
    ImportURDF,
    ImportURDFXacro,
    #ExportURDF,
    #ExportURDFXacro
)

def register():
  #bpy.utils.register_module(__name__)
  for cls in classes:
    bpy.utils.register_class(cls)

  #bpy.types.INFO_MT_file_import.append(menu_func_import)
  #bpy.types.INFO_MT_file_export.append(menu_func_export)
  bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
  bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
  #bpy.utils.unregister_module(__name__)

  #bpy.types.INFO_MT_file_import.remove(menu_func_import)
  #bpy.types.INFO_MT_file_export.remove(menu_func_export)
  bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
  bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

  for cls in classes:
    bpy.utils.unregister_class(cls)


if __name__ == "__main__":
  register()
