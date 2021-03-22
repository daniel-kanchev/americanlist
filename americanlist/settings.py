BOT_NAME = 'americanlist'
SPIDER_MODULES = ['americanlist.spiders']
NEWSPIDER_MODULE = 'americanlist.spiders'
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
    'americanlist.pipelines.DatabasePipeline': 300,
}
DOWNLOAD_DELAY = 1
LOG_LEVEL = 'DEBUG'
FEED_EXPORT_ENCODING = 'utf-8'
