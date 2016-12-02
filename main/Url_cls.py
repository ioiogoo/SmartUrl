# *-* coding:utf-8 *-*
from models import Url



class Url_c(object):
    """Convert between Lurl and Surl"""
    baseindex = 'tTcRvia5q7QZhFzoulCK06Xn4DNxMEgGSHIY1k3bLyOsUepV29PfW8wmBgrdAG'
    domain = 'https://0ooo0.cn/'
    def __init__(self, Lurl=None, Surl=None):
        if Lurl:
            self.Lurl = Lurl
        elif Surl:
            self.Surl = Surl

    @classmethod
    def L2S_url(cls, Lurl=None):
        '''Lurl convert to Surl'''
        if not Lurl:raise Exception('Input your Lurl')
        url = Url(Lurl=Lurl)
        try:
            url.save()
            id_ = url.id
            Surl = cls.domain + cls.to62(id_ + 10240)
            # insert Surl
            url.Surl = Surl
            url.save()
            return Surl,url.Views
        except:
            return Url.objects.filter(Lurl=Lurl)[0].Surl, Url.objects.filter(Lurl=Lurl)[0].Views

    @classmethod
    def S2L_url(cls, Surl=None):
        if not Surl:raise Exception('Input your Surl')
        id_ = cls.to10(Surl)
        return Url.objects.filter(id=id_)[0].Lurl


    @classmethod
    def to62(cls, num):
        restr = ''
        while 1:
            if num<62:
                return cls.baseindex[num]+restr
            restr =  cls.baseindex[num%62]+ restr
            num = num / 62

    @classmethod
    def to10(cls, num):
        dec = 0
        for index, i in enumerate(num[::-1]):
            dec += cls.baseindex.find(i) * (62 ** index)
        return dec - 10240




