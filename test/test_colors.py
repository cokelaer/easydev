from easydev import colors


def assert_almost_equal_tuples(first, second):
    from nose.tools import assert_almost_equal
    for x,y in zip(first, second):
        assert_almost_equal(x,y)

def test_rgb2hsv():
    assert colors.rgb2hsv(0,1,1) == (0.5,1,1)
    assert colors.hsv2rgb(0.5,1,1) == (0,1,1)
    colors.hsv2rgb(180,100,100, normalised=False)

def test_rgb2hls():
    assert_almost_equal_tuples(colors.rgb2hls(0,1,1) , (0.5,0.5,1))
    assert_almost_equal_tuples(colors.hls2rgb(0.5,0.5,1), (0,1,1))

    assert_almost_equal_tuples(colors.rgb2hls(0, 255, 255, normalised=False), (0.5,0.5,1))



def test_rgb2hex():
    colors.rgb2hex(0,0,255)
    colors.rgb2hex(0,0,1)
    colors.rgb2hex(*(0,0,1))
    try:
        colors.rgb2hex([0,0])
        assert False
    except:
        assert True

    try:
        colors.rgb2hex(0,0,1000)
        assert False
    except:
        assert True

    try:
        colors.rgb2hex(0,0,-1000)
        assert False
    except:
        assert True

    try:
        colors.rgb2hex(0,0,10, normalised=True)
        assert False
    except:
        assert True


def testColors():
    c = colors.Color("Blue")
    assert c.rgb == (0, 0 ,1)
    assert c.hex == "#0000FF"
    assert_almost_equal_tuples( c.hsv, (0.66666666666666,1,1))
    assert_almost_equal_tuples(c.hls, (0.666666666666666, .5,1))
    print(c)

    c.normalised = True
    c.name
    c.hsv
    c.hls
    print(c)
    assert c.rgb == (0,0,1)
    c.rgb = (0,0,1)
    c.hsv= (0,0,1)

    c.normalised = False

    # name can be changed and affects RGB/HEX
    c.name = "Magenta"
    assert c.rgb == colors._normalise(255, 0.0, 255)
    
    assert c.hex == "#FF00FF"

    # hex can be changed and affects name/HEX
    c.hex = "#F8F8FF"
    assert c.name == "Ghost White"   # non official name
    #assert c.rgb == 

    # RGB can be changed and affects name/HEX
    c.rgb = colors._normalise(248,248,255)
    assert c.name == "Ghost White"  # official name
    assert c.hex == "#F8F8FF"
    assert c.name == "Ghost White"  # non official but works
    assert c.hex == "#F8F8FF"


def test_normalise():
    colors._normalise(255,255,255, mode='rgb') == (1,1,1)
    colors._normalise(*(255,255,255), mode='rgb') == (1,1,1)
    colors._normalise(*(360,100,100), mode='hls') == (1,1,1)
    colors._denormalise(*(1,1,1), mode='rgb') == (255,255,255)
    colors._denormalise(*(1,1,1), mode='hls') == (360,100,100)


def test_cmap():
    colors.get_cmap("heat")
    colors.get_cmap("green")
    colors.get_cmap("rainbow")
