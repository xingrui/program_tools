ORG_FILE=/data/jackson/svn/adserver/frame/thrift/recommend_types.cpp
TMP_FILE=tmp.cpp
cat $ORG_FILE | 
sed 's/if (!isset_\(.*\))/JUDGE(\1);/'|
sed 's/^        throw TProtocolException(TProtocolException::INVALID_DATA);//g' > $TMP_FILE
cat head.txt $TMP_FILE > $ORG_FILE
rm $TMP_FILE
