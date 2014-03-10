from tools import check_param_in_list, swapdict, check_range


__all__ = ["Color"]

"""

RGB: 3-tuple of red/green/blue between 0.0 and 1.0
HSV: 3-tuple of Hue, saturation and value between 0.0 and 1.0
HEX: a string to encode RGB in hexadecimal format. Strings start with" : "# sign

"""
import colorsys




def hex2web(hexa):
    raise NotImplementedError

def web2hex(web):
    raise NotImplementedError

def hex2rgb(hexcolor, normalise=False):
    """This function converts a hex color triplet into RGB
    
    The like those found in HTML or CSS, and converts it to a Python 3-integer tuple. 
    
    0000FF
    #0000FF
    0x0000FF
    """
    hexcolor = get_standard_hex_color(hexcolor)
    hexcolor = hexcolor[1:]
    r, g, b =  int(hexcolor[0:2], 16), int(hexcolor[2:4], 16), int(hexcolor[4:6], 16)
    if normalise:
        r, g, b = _normalise(r,g,b)
    return r, g, b


def color_range(color1, color2, n=10):
    """Returns a list of nb color HSL tuples between begin_hsl and end_hsl

    >>> from colour import color_scale

    >>> [rgb2hex(hsl2rgb(hsl)) for hsl in color_scale((0, 1, 0.5),
    ...                                               (1, 1, 0.5), 3)]
    ['#f00', '#0f0', '#00f', '#f00']

    >>> [rgb2hex(hsl2rgb(hsl)) for hsl in color_scale((0, 0, 0), (0, 0, 1), 15)]
    ['#000', '#111', '#222', '#333', '#444', '#555', '#666', '#777', '#888', '#999', '#aaa', '#bbb', '#ccc', '#ddd', '#eee', '#fff']

   

    step = tuple([float(end_hsl[i] - begin_hsl[i])/nb for i in range(0, 3)])

    def mul(step, value):
        return tuple([v * value for v in step])

    def add_v(step, step2):
        return tuple([v + step2[i] for i, v in enumerate(step)])


    return [add_v(begin_hsl, mul(step, r)) for r in range(0, nb + 1)]

##
## All purpose object
##


    """
    raise NotImplementedError

def _denormalise(r,g,b, mode="rgb"):
    check_param_in_list(mode, ["rgb", "hls", "hsv"])
    if mode == "rgb":
        return r*255., g*255., b*255.
    elif mode in ["hls", "hsv"]:
        return r*360., g*100., b*100.

def _normalise(r, g, b, mode="rgb"):
    check_param_in_list(mode, ["rgb", "hls", "hsv"])
    if mode == "rgb":
        return r/255., g/255., b/255.
    elif mode in ["hls", "hsv"]:
        return r/360., g/100., b/100.

def rgb2hex(r, g, b, normalised=False):
    """Convert RGB to hexadecimal color
    
    :param : can be a tuple/list/set of 3 values (R,G,B)
    :return: a hex vesion ofthe RGB 3-tuple

    .. doctest::

        >>> rgb2hex((0,0,255), normalised=False)
        '#0000FF'
        >>> rgb2hex((0,0,1), normalised=True)
        '#0000FF'

    """
    if normalised:
        r,g,b = _denormalise(r,g,b, mode="rgb")
    check_range(r, 0, 255)
    check_range(g, 0, 255)
    check_range(b, 0, 255)
    return '#%02X%02X%02X' % (r, g, b)


def rgb2hls(r, g, b, normalised=True):
    """Convert an RGB value to an HLS value. 

    RGB must be normalised
    LHS are normalised
    """
    # rgb_to_hsv expects normalised values !
    if normalised: upper = 1
    else: upper = 255
    check_range(r, 0, upper)
    check_range(g, 0, upper)
    check_range(b, 0, upper)
    if normalised==False:
        r,g,b = _normalise(r,g,b)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h, l, s


def rgb2hsv(r, g, b, normalised=True):
    """Convert an RGB value to an HSV value.
    
    RGB must be normalised
    HSV are normalised
    """
    # rgb_to_hsv expects normalised values !
    if normalised: upper = 1
    else: upper = 255
    check_range(r, 0, upper)
    check_range(g, 0, upper)
    check_range(b, 0, upper)
    if normalised==False:
        r,g,b = _normalise(r,g,b)
    h,s,v = colorsys.rgb_to_hsv(r, g, b)
    return h,s,v


def hsv2rgb(h, s, v, normalised=True):
    """Convert a hue-saturation-value (HSV) value to a red-green-blue (RGB). 
    
    
    RGB must be normalised
    HSV are normalised
    
    """
    if normalised: upper = 1
    else: upper = 100
    if normalised: uppera = 1
    else: uppera = 360
    check_range(h, 0, uppera)
    check_range(s, 0, upper)
    check_range(v, 0, upper)
    if normalised == False:
        h,s,v = _normalise(h,s,v, mode="hsv")
    return colorsys.hsv_to_rgb(h, s, v)


def hls2rgb(h, s, l, normalised=True):
    """Convert HSL to RGB

    RGB must be normalised
    LHS are normalised
    """
    if normalised: upper = 1
    else: upper = 100
    if normalised: uppera = 1
    else: uppera = 360
    check_range(h, 0, uppera)
    check_range(s, 0, upper)
    check_range(l, 0, upper)
    if normalised == False:
        h,s,l = _normalise(h,s,l, mode="hls")
    return colorsys.hls_to_rgb(h, s, l)


def hex2dec(data):
    """convert integer (data) into hexadecimal."""
    return int(data, 16)/255.


def to_intensity(n):
    """Return intensity

    :param n: value between 0 and 1
    :return: value between 0 and 255
    :returns: round(n*127.5+127.5)
    """
    _check_intensity_range(b, normalise=True)
    return int(round(n * 127.5 + 127.5))
    

XFree86_colors = {
    "Alice Blue" : "#F0F8FF",
    "AliceBlue" : "#F0F8FF",
    "Antique White" : "#FAEBD7",
    "Aqua" : "#00FFFF",
    "Aquamarine" : "#7FFFD4",
    "Azure" : "#F0FFFF",
    "Beige" : "#F5F5DC",
    "Bisque" : "#FFE4C4",
    "Black" : "#000000",
    "Blanched Almond" : "#FFEBCD",
    "Blue" : "#0000FF",
    "Blue Violet" : "#8A2BE2",
    "Brown" : "#A52A2A",
    "Burlywood" : "#DEB887",
    "Cadet Blue" : "#5F9EA0",
    "Chartreuse" : "#7FFF00",
    "Chocolate" : "#D2691E",
    "Coral" : "#FF7F50",
    "Cornflower" : "#6495ED",
    "Cornsilk" : "#FFF8DC",
    "Crimson" : "#DC143C",
    "Cyan" : "#00FFFF",
    "Dark Blue" : "#00008B",
    "Dark Cyan" : "#008B8B",
    "Dark Goldenrod" : "#B8860B",
    "Dark Gray" : "#A9A9A9",
    "Dark Green" : "#006400",
    "Dark Khaki" : "#BDB76B",
    "Dark Magenta" : "#8B008B",
    "Dark Olive Green" : "#556B2F",
    "Dark Orange" : "#FF8C00",
    "Dark Orchid" : "#9932CC",
    "Dark Red" : "#8B0000",
    "Dark Salmon" : "#E9967A",
    "Dark Sea Green" : "#8FBC8F",
    "Dark Slate Blue" : "#483D8B",
    "Dark Slate Gray" : "#2F4F4F",
    "Dark Turquoise" : "#00CED1",
    "Dark Violet" : "#9400D3",
    "Deep Pink" : "#FF1493",
    "Deep Sky Blue" : "#00BFFF",
    "Dim Gray" : "#696969",
    "Dodger Blue" : "#1E90FF",
    "Firebrick" : "#B22222",
    "Floral White" : "#FFFAF0",
    "Forest Green" : "#228B22",
    "Fuchsia" : "#FF00FF",
    "Gainsboro" : "#DCDCDC",
    "Ghost White" : "#F8F8FF",
    "Gold" : "#FFD700",
    "Goldenrod" : "#DAA520",
    "Gray (X11)" : "#BEBEBE",
    "Gray (W3C)" : "#808080",
    "Green (X11)" : "#00FF00",
    "Green (W3C)" : "#008000",
    "Green Yellow" : "#ADFF2F",
    "Honeydew" : "#F0FFF0",
    "Hot Pink" : "#FF69B4",
    "Indian Red" : "#CD5C5C",
    "Indigo" : "#4B0082",
    "Ivory" : "#FFFFF0",
    "Khaki" : "#F0E68C",
    "Lavender" : "#E6E6FA",
    "Lavender Blush" : "#FFF0F5",
    "Lawn Green" : "#7CFC00",
    "Lemon Chiffon" : "#FFFACD",
    "Light Blue" : "#ADD8E6",
    "Light Coral" : "#F08080",
    "Light Cyan" : "#E0FFFF",
    "Light Goldenrod" : "#FAFAD2",
    "Light Gray" : "#D3D3D3",
    "Light Green" : "#90EE90",
    "Light Pink" : "#FFB6C1",
    "Light Salmon" : "#FFA07A",
    "Light Sea Green" : "#20B2AA",
    "Light Sky Blue" : "#87CEFA",
    "Light Slate Gray" : "#778899",
    "Light Steel Blue" : "#B0C4DE",
    "Light Yellow" : "#FFFFE0",
    "Lime (W3C)" : "#00FF00",
    "Lime Green" : "#32CD32",
    "Linen" : "#FAF0E6",
    "Magenta" : "#FF00FF",
    "Maroon (X11)" : "#B03060",
    "Maroon (W3C)" : "#7F0000",
    "Medium Aquamarine" : "#66CDAA",
    "Medium Blue" : "#0000CD",
    "Medium Orchid" : "#BA55D3",
    "Medium Purple" : "#9370DB",
    "Medium Sea Green" : "#3CB371",
    "Medium Slate Blue" : "#7B68EE",
    "Medium Spring Green" : "#00FA9A",
    "Medium Turquoise" : "#48D1CC",
    "Medium Violet Red" : "#C71585",
    "Midnight Blue" : "#191970",
    "Mint Cream" : "#F5FFFA",
    "Misty Rose" : "#FFE4E1",
    "Moccasin" : "#FFE4B5",
    "Navajo White" : "#FFDEAD",
    "Navy" : "#000080",
    "Old Lace" : "#FDF5E6",
    "Olive" : "#808000",
    "Olive Drab" : "#6B8E23",
    "Orange" : "#FFA500",
    "Orange Red" : "#FF4500",
    "Orchid" : "#DA70D6",
    "Pale Goldenrod" : "#EEE8AA",
    "Pale Green" : "#98FB98",
    "Pale Turquoise" : "#AFEEEE",
    "Pale Violet Red" : "#DB7093",
    "Papaya Whip" : "#FFEFD5",
    "Peach Puff" : "#FFDAB9",
    "Peru" : "#CD853F",
    "Pink" : "#FFC0CB",
    "Plum" : "#DDA0DD",
    "Powder Blue" : "#B0E0E6",
    "Purple (X11)" : "#A020F0",
    "Purple (W3C)" : "#7F007F",
    "Red" : "#FF0000",
    "Rosy Brown" : "#BC8F8F",
    "Royal Blue" : "#4169E1",
    "Saddle Brown" : "#8B4513",
    "Salmon" : "#FA8072",
    "Sandy Brown" : "#F4A460",
    "Sea Green" : "#2E8B57",
    "Seashell" : "#FFF5EE",
    "Sienna" : "#A0522D",
    "Silver (W3C)" : "#C0C0C0",
    "Sky Blue" : "#87CEEB",
    "Slate Blue" : "#6A5ACD",
    "Slate Gray" : "#708090",
    "Snow" : "#FFFAFA",
    "Spring Green" : "#00FF7F",
    "Steel Blue" : "#4682B4",
    "Tan" : "#D2B48C",
    "Teal" : "#008080",
    "Thistle" : "#D8BFD8",
    "Tomato" : "#FF6347",
    "Turquoise" : "#40E0D0",
    "Violet" : "#EE82EE",
    "Wheat" : "#F5DEB3",
    "White" : "#FFFFFF",
    "White Smoke" : "#F5F5F5",
    "Yellow" : "#FFFF00",
    "Yellow Green" : "#9ACD32"}


class Color(object):
    """Class to convert name to RBG or Hex


    Valid color names are those from XFree86 http://en.wikipedia.org/wiki/X11_color_names
    plus the same names in lower cases. In addition, names that have a space have also been
    added without the space. So, given those official names "Red", and "Spring Green", the possible
    names are Red, red, Spring Green, spring green, SpringGreen and springgreen.

    You ican set rgb, hsv as long as there are compatible with a color name.

    .. doctest::

        from easydev import Color

        Color("red")           ## human, web compatible representation
        Color("#f00")          ## standard 3 hex digit web compatible representation
        Color("#ff0000")       ## standrad 6 hex digit web compatible representation
        Color(hsv=(0,1,0.5))
        Color(hsl=(0, 1, 0.5)) ## full 3-uple HSL specification
        Color(rgb=(1, 0, 0))   ## full 3-uple RGB specification
        Color(Color("red"))    ## recursion doesn't break object



    .. todo:: CMYK, YUV conversion

    Works with normalised values
    """
    # Get official color names
    colors = XFree86_colors.copy()
    # add color names without spaces
    aliases = dict([(x.replace(" ", ""),x) for x in colors.keys() if " " in x])
    # add color names without spaces in lower cases
    aliases.update([(x.replace(" ", "").lower(),x) for x in colors.keys() if " " in x])
    # add color names in lower case
    aliases.update(dict([(x.lower(),x) for x in colors.keys()]))
    aliases.update(dict([(x,x) for x in colors.keys()]))

    # keep track of all possible names
    color_names = sorted(list(set(colors.keys() + aliases.keys())))

    def __init__(self, name=None, rgb=None, hsl=None, hsv=None):
        self._name = None
        self._mode = None
        self._rgb = None

        # Does the user provided the name argument (first one) as a string ?
        if isinstance(name, str):
            # if so, it can be a valid human name (e.g., red) or an hex
            # assuming that valid hexadecimal starts with # or 0x, 
            # if we can interpret the string as an hexadecimal, we are done
            if is_valid_hex_color(name, verbose=False):
                self.hex = name
            else:
                # if not, then, the user probably provided a valid color name
                # the property will check the validity.
                self.name = name[:]
                #all other input parameters are ignored
        elif name == None:
            if rgb:
                self.rgb = rgb
            elif hsl:
                self.hsl = hsl
            elif hsv:
                self.hsv = hsv
            else:
                raise ValueError("You must set one of the parameter")
        elif isinstance(name, Color):
            self.rgb = name.rgb
        else:
            raise ValueError("name parameter must be a string")
    
    def _get_name(self):
        return self._name
    def _set_name(self, name):
        check_param_in_list(name, self.color_names)
        name = self.aliases[name]
        self._name = name
        # set hex and rgb at the same time based on the name
        self.hex = self.colors[name]

    name = property(_get_name, _set_name)


    def _get_hex(self):
        return self._hex
    def _set_hex(self, value):
        # hex is an approximation made of 255 bits so do not define rgb here
        if is_valid_hex_color(value):
            value = get_standard_hex_color(value)
            self._hex = value
            if self._hex in self.colors.values():
                self._name = swapdict(self.colors, check_ambiguity=False)[self._hex]
            else:
                self._name = "undefined"
            self._rgb = hex2rgb(self._hex, normalise=True)
        else:
            # just to warn the user
            get_standard_hex_color(value)
    hex = property(_get_hex, _set_hex)
    
    def _get_rgb(self):
        return self._rgb
    def _set_rgb(self, value):
        # set name, hex and rgb
        self.hex = rgb2hex(*value , normalised=True)
        # must reset rgb with its real value (set_hex may round the rgb)
        # in _set_hex
        self._rgb = value
    rgb = property(_get_rgb, _set_rgb)

    def _get_hsv(self):
        hsv = rgb2hsv(*self.rgb)
        return hsv
    def _set_hsv(self, value):
        # TODO: value must be normalised
        self.rgb = hsv2rgb(*value)
    hsv = property(_get_hsv, _set_hsv)

    def _get_hls(self):
        hls = rgb2hls(*self.rgb)
        return hls
    def _set_hls(self, value):
        # TODO: value must be normalised
        #hls = _normalise(*value, mode="hls")
        #else:
        hls = value
        self.rgb = hls2rgb(*hls)
    hls = property(_get_hls, _set_hls)

    def _get_lightness(self):
        return self.hls[1]
    def _set_lightness(self, lightness):
        h,l,s = self.hls
        self.hls = (h,lightness,s)
    lightness = property(_get_lightness, _set_lightness)

    def _get_saturation_hls(self):
        return self.hls[2]
    def _set_saturation_hls(self, saturation):
        h,l,s = self.hls
        self.hls = (h,l, saturation)
    saturation_hls = property(_get_saturation_hls, _set_saturation_hls)

    def _get_hue(self):
        return self.hls[0]
    def _set_hue(self, hue):
        h,l,s = self.hls
        self.hls = (hue,l, s)
    hue = property(_get_hue, _set_hue)

    def _get_red(self):
        return self.rgb[0]
    def _set_red(self, red):
        r,g,b = self.rgb
        self.rgb = (red,g,b)
    red = property(_get_red, _set_red)

    def _get_green(self):
        return self.rgb[1]
    def _set_green(self, green):
        r,g,b = self.rgb
        self.rgb = (r,green,b)
    green = property(_get_green, _set_green)

    def _get_blue(self):
        return self.rgb[2]
    def _set_blue(self, blue):
        r,g,b = self.rgb
        self.rgb = (r,g, blue)
    blue = property(_get_blue, _set_blue)

    def _get_value(self):
        return self.hls[0]
    def _set_value(self, value):
        h,s,v = self.hsv
        self.hsv = (h,s,value)
    value = property(_get_value, _set_value)

    def _get_yiq(self):
        return colorsys.rgb_to_yiq(*self.rgb)
    def _set_yiq(self, value):
        raise NotImplementedError
    yiq = property(_get_yiq)

    def __str__(self):
        txt = 'Color {}\n'.format(self.name)
        txt+= '  hexa code: {}\n'.format(self.hex)
        txt+= '  RGB code: {}\n'.format(self.rgb)
        txt+= '  RGB code (un-normalised): {}\n\n'.format([x*255 for x in self.rgb])
        txt+= '  HSV code: {}\n'.format(self.hsv)
        txt+= '  HSV code: (un-normalised) {} {} {}\n\n'.format(self.hsv[0]*360, self.hsv[1]*100, self.hsv[2]*100)
        txt+= '  HLS code: {}\n'.format(self.hls)
        txt+= '  HLS code: (un-normalised) {} {} {}\n\n'.format(self.hls[0]*360, self.hls[1]*100, self.hls[2]*100)
        return txt


def rgb_list_to_colordict(rgb_list):
    colors_by_channel = zip(*rgb_list)
    channels = ('red', 'green', 'blue', 'alpha')
    return dict((color, value)
                for color, value in zip(channels, colors_by_channel))


def get_hexmap(d={'red':[0,255], 'green':[0,255], 'blue':[0,255]}, N=10):
    from numpy import linspace
    rcol = linspace(d['red'][0], d['red'][1], N)
    gcol = linspace(d['green'][0], d['green'][1], N)
    bcol = linspace(d['blue'][0], d['blue'][1], N)
    return [rgb2hex(r,g,b) for r,g,b in zip(rcol, gcol, bcol)]


def green():
    """hard-coded map"""
    return ["#FF0000", "#FF6A6A", "#EEA2AD", "#FFB6C1", "#FFE4E1", "#EEE8AA","#98FB98", "#A2CD5A", "#66CD00", "#228B22"]

def rainbow(N=10):
    return get_hexmap({'red':[255, 255], 'green':[0, 0], 'blue':[0, 255]}, N=N)

def heat(N=10):
    return get_hexmap({'red':[255, 255], 'green':[0, 255], 'blue':[0, 255]}, N=N)
    #return ["#FF0000", "#FF2400","#FF4900", "#FF6D00" ,"#FF9200" ,"#FFB600",
    #"#FFDB00", "#FFFF00", "#FFFF40", "#FFFFBF"]



def get_cmap(colors=None, reverse=True, N=10, index=None):
    """

    colors is a list of hexa colors as returned by rainbow, heat, get_hexmap

    """
    # Keep these dependencies inside the function to allow 
    # installation of easydev without those dependencies
    import numpy as np
    import matplotlib
    # extracted from R, heat.colors(20)
    if colors == "heat":
        colors = heat(N)
    elif colors == "rainbow":
        colors = rainbow(N)
    elif colors=="green":
        colors = green()
    else:
        pass

    #color_data = dict((key, [(x, y, y) for x, y in zip(index, value)])
    #                              for key, value in color_data.iteritems())

    rgb = [hex2rgb(x, normalise=True) for x in colors]
    if reverse:
        rgb.reverse()

    colordict = rgb_list_to_colordict(rgb)
    if index is None:
        # If index not given, RGB colors are evenly-spaced in colormap.
        index = np.linspace(0, 1, len(colordict['red']))

    # Adapt color_data to the form expected by LinearSegmentedColormap.
    color_data = dict((key, [(x, y, y) for x, y in zip(index, value)]) 
            for key, value in colordict.iteritems())
    f = matplotlib.colors.LinearSegmentedColormap
    N = len(colors)
    m = f('my_color_map', color_data, N)
    return m


def is_valid_hex_color(value, verbose=True):
    """Return True is the string can be interpreted as hexadecimal color
    
    """
    try:
        get_standard_hex_color(value)
        return True
    except Exception, e:
        if verbose:print(e)
        return False

def get_standard_hex_color(value):
    """Return standard hexadecimal color
    
    By standard, we mean a string that starts with # sign followed by 6
    character, e.g. #AABBFF
    """
    if isinstance(value, str)==False:
        raise TypeError("value must be a string")
    if len(value) <= 3:
        raise ValueError("input string must be of type 0xFFF, 0xFFFFFF or #FFF or #FFFFFF")

    if value.startswith("0x") or value.startswith("0X"):
        value =  value[2:]
    elif value.startswith("#"):
        value = value[1:]
    else:
        raise ValueError("hexa string must start with a '#' sign or '0x' string")
    value = value.upper()
    # Now, we have either FFFFFF or FFF
    # now check the length
    for x in value:
        if x not in "0123456789ABCDEF":
            raise ValueError("Found invalid hexa character {}".format(x))


    if len(value) == 6 or len(value) == 8:
        value  = "#" + value[0:6]
    elif len(value) == 3:
        value = "#" + value[0]*2 + value[1]*2 + value[2]*2
    else:
        raise ValueError("hexa string should be 3, 6 or 8 digits. if 8 digits, last 2 are ignored")
    return value

