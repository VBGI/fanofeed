
FEED_URLS = (( 'http://www.ras.ru/RssFeeder.aspx?Name=press', 'RAS News', 'R', 43200, 'ras_parser', 4),
             ('https://minobrnauki.gov.ru/ru/press-center/rss/index.php', 'Minobr News', 'M', 7200, 'minobr_parser', 4))

# structure:  (url_to_be_parsed, name, abbriviation(used in db), renew interval (sec.), view name, # of news)