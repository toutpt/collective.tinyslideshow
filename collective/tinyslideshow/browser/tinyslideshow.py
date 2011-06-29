# -*- coding: utf-8 -*-
from zope import interface
from zope import schema
from collective.configviews import ConfigurableBaseView

from collective.tinyslideshow import i18n

class ITinySlideshowSettings(interface.Interface):
    """The following are the parameters that can be set on the 
    object more complete documentation will follow soon.
    Default values are displayed as (10) and
    recommended values as [1-20].
    
    Images
    ------
    
    imgSpeed = int; (10)
    navOpacity = int; (25)
    navHover = int; (70)
    letterbox = “string”; (#000) required color for letterbox on portrait images
    link = “string”; class name for link hover state
    
    Auto Slideshow
    --------------
    
    auto = boolean; (false)
    speed = int; (10)
    
    Information Dialog
    ------------------
    
    info = boolean; (true)
    infoID = “string”; required for information dialog
    infoSpeed = int; (10)
    
    Thumbnail Slider
    ----------------
    
    thumbs = “string”; id of thumbnail slider, disabled if not set
    scrollSpeed = int; [1-20] (5)
    thumbOpacity = int; [0-100] (70)
    active = “string”; required for thumbnail active border
    spacing = int; (5) spacing between thumbnails
    left = “string”; id of left navigation link, required for slider
    right = “string”; id of right navigation link, required for slider

    """
    #Image
    imgSpeed   = schema.Int(title=i18n.imgSpeed,
                            default=10)
    navOpacity = schema.Int(title=i18n.navOpacity,
                            default=25)
    navHover   = schema.Int(title=i18n.navHover,
                            default=70)
    #Scroll
    auto  = schema.Bool(title=i18n.auto,
                       default=False)
    speed = schema.Int(title=i18n.speed,
                       default=10)
    #Thumbnail
    info  = schema.Bool(title=i18n.info,
                       default=True)
    infoSpeed   = schema.Int(title=i18n.infoSpeed,
                             default=10)
    scrollSpeed = schema.Int(title=i18n.scrollSpeed,
                             default=5)#TODO: force [1-20]
    thumbOpacity = schema.Int(title=i18n.thumbOpacity,
                              default=70)# TODO force [0-100]

class TinySlideshow(ConfigurableBaseView):
    settings_schema = ITinySlideshowSettings
