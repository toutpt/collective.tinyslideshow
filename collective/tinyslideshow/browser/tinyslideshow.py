# -*- coding: utf-8 -*-
from zope import interface
from zope import schema
from collective.configviews import ConfigurableBaseView

from collective.tinyslideshow import i18n

class ITinySlideshowSettings(interface.Interface):
    """The following are the parameters that can be set on the 
    object
    """
    #Image
    imgSpeed   = schema.Int(title=i18n.imgSpeed,
                            default=10)
    navOpacity = schema.Int(title=i18n.navOpacity,
                            default=25)# TODO force [0-100]
    navHover   = schema.Int(title=i18n.navHover,
                            default=70)

    #Scroll
    auto  = schema.Bool(title=i18n.auto,
                       default=True)
    speed = schema.Int(title=i18n.speed,
                       default=10)

    #Thumbnail
    info        = schema.Bool(title=i18n.info,
                              default=True)
    infoSpeed   = schema.Int(title=i18n.infoSpeed,
                             default=10)
    scrollSpeed = schema.Int(title=i18n.scrollSpeed,
                             default=5)#TODO: force [1-20]
    thumbOpacity = schema.Int(title=i18n.thumbOpacity,
                              default=70)# TODO force [0-100]

class TinySlideshow(ConfigurableBaseView):
    settings_schema = ITinySlideshowSettings
    jsvarname = 'slideshowconfig'
    settings_providers = ('context.zope.annotation',)
