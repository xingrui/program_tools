list='4792048|2028576|132756|725395|2381111|130823|4136685|501078|1221144|870154|3359916|4491654|134119|3502669|484873|132397|2185330|126083|1348747|791117'
for campaign_id in list.split('|'):
    print '''result = db.campaign.findOne({campaignId:%s})''' % campaign_id
    print '''if(result != null){print(result.packageName)};'''
