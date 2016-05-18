var http = require('http');
var url = require('url');
var url_obj = url.parse('http://app.adjust.com/1gsjtb?campaign=ljf_cop_arb_ios&adgroup=7602_4cee8c87f64aa51d&creative=7602_4cee8c87f64aa51d&tracker_limit=100000&install_callback=mobvista_install%26mobvista_campuuid%3Dljf_cop_arb_ios%26mobvista_clickid%3D5722eef12f7922770638ff06%26mobvista_tag%3Dnew_adjust_postback&idfa=def&idfa_lower_md5=def');
var url_obj = url.parse('http://app.adjust.io/lw0ib0?campaign=App_Generic&deep_link=lazada%3A%2F%2Fth&tracker_limit=100000&install_callback=http%3A%2F%2Fnext.mobvista.com%2Finstall%3Fmobvista_pl%3Dandroid%26mobvista_campuuid%3Dlazada_th_ios%26mobvista_clickid%3D5722eda5d10dc7f41baf5b6f%26mobvista_ip%3D%7Bip_address%7D%26mobvista_devid%3D%7Bidfa%7C%7Candroid_id%7D%26mobvista_type%3Dadjust%26mobvista_device%3D%7Bdevice_name%7D%26mobvista_os%3D%7Bos_version%7D&adgroup=441_9216ab2940fd8b81&clickid=5722eda5d10dc7f41baf5b6f&creative=441_9216ab2940fd8b81&event_callback_2w9wdh=http%3A%2F%2Fstat.mobvista.com%2Fevent%3Fmobvista_ip%3D%7Bip_address%7D%26mobvista_devid%3D%7Bidfa%7C%7Candroid_id%7D%26mobvista_clickid%3D5722eda5d10dc7f41baf5b6f%26mobvista_type%3Dadjust%26mobvista_campuuid%3Dlazada_th_ios%26event_name%3DSale%26event_time%3D%7Bcreated_at%7D%26mobvista_device%3D%7Bdevice_name%7D%26mobvista_os%3D%7Bos_version%7D&event_callback_nzifv4=http%3A%2F%2Fstat.mobvista.com%2Fevent%3Fmobvista_ip%3D%7Bip_address%7D%26mobvista_devid%3D%7Bidfa%7C%7Candroid_id%7D%26mobvista_clickid%3D5722eda5d10dc7f41baf5b6f%26mobvista_type%3Dadjust%26mobvista_campuuid%3Dlazada_th_ios%26event_name%3DGuestSale%26event_time%3D%7Bcreated_at%7D%26mobvista_device%3D%7Bdevice_name%7D%26mobvista_os%3D%7Bos_version%7D&rejected_install_callback=mobvista_event%26mobvista_campuuid%3Dlazada_th_ios%26mobvista_clickid%3D5722eda5d10dc7f41baf5b6f%26event_name%3Drejected_reason%26event_value%3D%7Brejection_reason%7D%26mb_sid%3D441_9216ab2940fd8b81&idfa=def&idfa_lower_md5=def');
url_obj.headers = {
    'User-Agent':'User-Agent: Opera/9.80 (Android; Opera Mini/7.5.32193/36.2592; U; en) Presto/2.12.423 Version/12.16'
    //'User-Agent':'User-Agent: Opera/9.80 (IOS; Opera Mini/7.5.32193/36.2592; U; en) Presto/2.12.423 Version/12.16'
}

var req = http.get(url_obj, function(res) {
    console.log(res.headers.location);
});
