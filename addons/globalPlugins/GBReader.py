# -*- coding: UTF-8 -*-
# Simplified Chinese (gb2312) reader for NVDA by Coscell Kao <coscell@gmail.com>
import os
import globalPluginHandler
import globalVars
import speechDictHandler
import ui

dic = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gb.dic")
sD = speechDictHandler.SpeechDict()
gb = False

def gbon():
  global gb
  speechDictHandler.dictionaries["temp"].extend(sD)
  gb = True

def gboff():
  global gb
  for entry in sD:
    if entry in speechDictHandler.dictionaries["temp"]:
      speechDictHandler.dictionaries["temp"].remove(entry)
  gb = False

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
  def __init__(self):
    super(globalPluginHandler.GlobalPlugin, self).__init__()
    global sD, dic
    sD.load(dic)

  def terminate(self):
    gboff()
    global sD 
    sD = None

  def script_toggle(self, gesture):
    if not globalVars.speechDictionaryProcessing:
      return
    if gb:
      gboff()
      ui.message(_(u"簡體中文報讀關"))
    else:
      ui.message(_(u"簡體中文報讀開"))
      gbon()
  script_toggle.__doc__ = _(u"簡體中文報讀開關")

  __gestures = {"kb:NVDA+g":"toggle"}
