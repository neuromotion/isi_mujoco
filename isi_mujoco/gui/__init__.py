"""Viewer's windowing systems."""

from dm_control import _render

# pylint: disable=g-import-not-at-top
# pylint: disable=invalid-name

RenderWindow = None

try:
  from dm_control.viewer.gui import glfw_gui
  RenderWindow = glfw_gui.GlfwWindow
except ImportError:
  pass

if RenderWindow is None:

  def ErrorRenderWindow(*args, **kwargs):
    del args, kwargs
    raise ImportError(
        'Cannot create a window because no windowing system could be imported')
  RenderWindow = ErrorRenderWindow

del _render