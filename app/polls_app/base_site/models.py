from django.db import models
from django.contrib.sites.models import Site
from config.settings.base import SITE_ID

# Create your models here.


def create_default_site_detail(sender, **kwargs):
    # site = Site.objects.get(pk=settings.SITE_ID)
    site = Site.objects.get(pk=SITE_ID)

    SiteDetail.objects.get_or_create(site=site)


class SiteDetail(models.Model):
    """Siteと1対1で紐づくサイト詳細情報"""
    site = models.OneToOneField(
        Site, verbose_name='Site', on_delete=models.PROTECT
    )

    title = models.CharField('タイトル', max_length=255, default='Webサイトのタイトル')
    description = models.TextField(
        'サイトの説明', max_length=255, default='Webサイトの説明'
    )
    keywords = models.CharField(
        'サイトのキーワード', max_length=255, default='Webサイトのキーワード'
    )
    author = models.CharField('管理者', max_length=255, default='サンプルの管理者')
    email = models.EmailField(
        '管理者アドレス', max_length=255, default='your_mail@gmail.com'
    )

    github = models.CharField('Githubアカウント', max_length=255, blank=True)
    twitter = models.CharField('Twitterアカウント', max_length=255, blank=True)
    facebook = models.CharField('FaceBookアカウント', max_length=255, blank=True)

    google_ad_html = models.TextField('アドセンスHTML', blank=True)
    google_analytics_html = models.TextField('アナリティクスHTML', blank=True)

    def __str__(self):
        return self.author
