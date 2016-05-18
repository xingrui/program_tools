import difflib

diff = difflib.HtmlDiff(wrapcolumn=60).make_file('123123123\n123123123\n1', '123123123\n123123123\n2')
print diff
