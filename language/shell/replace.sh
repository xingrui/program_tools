#sed '/<Directory .*>/{:n;N;/<\/Directory>/!bn};s/\n.*\n/\n    Options None\n    AllowOverride None\n    Order deny,allow\n    Deny from all\n/' urfile
#sed '/if .*isset.*/:n;N;/        throw TProtocolException(TProtocolException::INVALID_DATA);/&/'
