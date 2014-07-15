#!/usr/bin/env python3

import threading
from gi.repository import Gdk
from gi.repository import ClutterGst
from gi.repository import Clutter
from gi.repository import GtkClutter
from gi.repository import Gst
from gi.repository import Gtk

ClutterGst.init([])

class EVP(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.window = Gtk.Window()
        self.texture = Clutter.Texture.new()
        self.sink = Gst.ElementFactory.make("cluttersink", None)
        self.sink.props.texture = self.texture
        self.src = Gst.ElementFactory.make ("videotestsrc", None)
        self.pipeline = Gst.Pipeline()
        self.pipeline.add(self.src)
        self.pipeline.add(self.sink)
        self.src.link(self.sink)

        self.embed = GtkClutter.Embed()
        self.embed.set_size_request(320, 240)

        self.stage = self.embed.get_stage()
        self.stage.add_child(self.texture)
        self.stage.set_size(320, 240)
        self.stage.show_all()

        self.window.add(self.embed)

        self.window.connect("delete-event", Gtk.main_quit)

    def run(self):
        self.window.show_all()
        self.pipeline.set_state(Gst.State.PLAYING)
        Gtk.main()

evp = EVP()
evp.start()
try:
    while True:
        pass
except KeyboardInturrupt:
    Gtk.main_quit()
