import cairo

class TShirtLogo(object):
    def __init__(self, filename, size):
	super(TShirtLogo, self).__init__()
	self.size = size
	self.filename = filename
	self.ext = filename.split('.')[-1]
	if self.ext == 'svg':
	    self.ps = cairo.SVGSurface(filename, *self.size)
	elif self.ext == 'png':
	    self.ps = cairo.ImageSurface(cairo.FORMAT_ARGB32, *self.size)
	self.cr = cairo.Context(self.ps)
	self.phrases = ["Trust happens", "Samba / MIT Kerberos / FreeIPA"]

    def logo(self, color, fontface, size):
	self.cr.set_source_rgb(*color)
	self.cr.select_font_face(fontface, 
			        cairo.FONT_SLANT_NORMAL,
				cairo.FONT_WEIGHT_BOLD)
	self.cr.set_font_size(size)
	xbearing, ybearing, width, height, xadvance, yadvance = self.cr.text_extents(self.phrases[0])
	x = self.size[0]/2.0-(width/2 + xbearing);
	y = self.size[1]/2.0-(height/2 + ybearing);
	self.cr.move_to(x, y)
	self.cr.show_text(self.phrases[0])
	y = y - yadvance - ybearing
	x = x + xadvance
	self.cr.select_font_face(fontface, 
			        cairo.FONT_SLANT_NORMAL,
				cairo.FONT_WEIGHT_NORMAL)
	self.cr.set_font_size(size*0.3334)
	xbearing, ybearing, width, height, xadvance, yadvance = self.cr.text_extents(self.phrases[1])
	x = x - width;
	y = y - height
	self.cr.move_to(x, y)
	self.cr.show_text(self.phrases[1])

    def done(self):
	if self.ext == 'svg':
            self.cr.show_page()
	elif self.ext == 'png':
	    self.ps.write_to_png(self.filename)


colors = {'red' : (255,0,0), 'green' : (0,255,0), 'blue' : (0,0,255), 'black' : (0,0,0), 'white' : (255,255,255)}

formats = ['png', 'svg']

for format in formats:
    for color in colors.keys():
        logo = TShirtLogo("trust-happens-%s.%s" % (color, format), [1600, 400])
        logo.logo(colors[color], "Comfortaa", 150)
        logo.done()

