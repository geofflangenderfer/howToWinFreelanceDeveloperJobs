url="https://api.twitter.com/2/tweets/search/recent?query=from:brennandunn&tweet.fields=created_at,public_metrics"
#curl "https://api.twitter.com/2/tweets/search/recent?query=python&max_results=10&tweet.fields=created_at,lang,conversation_id" -H "Authorization: Bearer $BEARER_TOKEN"

BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAGmCFwEAAAAARLfrP15ktszGc6MruWnleDoUpt4%3DnhEWsoERgWMPmk8fGeerEmjjAW4HpGhKy66t2SuNUnjpC4Dult"

curl --request GET $url --header "Authorization: Bearer $BEARER_TOKEN"
