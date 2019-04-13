# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:08:54 2018

@author: bxu601
"""

import wx
class Frame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title = "Hello World in wxPython")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1= wx.TextCtrl(panel, value = "Hello, World!", size = (200,180), style = wx.TE_MULTILINE)
        sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)
        button = wx.Button(panel, label = "Click Me")
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)        
        panel.Layout()
        self.Bind(wx.EVT_BUTTON,self.OnClick,button)
    def OnClick(self, text):
        self.text1.AppendText("\nHello, World!")

if __name__ == '__main__': 
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()