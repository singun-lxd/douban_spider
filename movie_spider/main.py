# -*- coding: utf-8 -*-

from scrapy import cmdline


if __name__ == '__main__':
    name = 'movie'
    cmd = 'scrapy crawl {0}'.format(name)
    cmdline.execute(cmd.split())
