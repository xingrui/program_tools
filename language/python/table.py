from prettytable import PrettyTable
x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"], sortby="Area", reversesort=True)
x.align["City name"] = "l"# Left align city names
x.padding_width = 1# One space between column edges and contents (default)
x.add_row(["Adelaide",1295, 1158259, 600.5])
x.add_row(["Brisbane",5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5]) 
x.add_row(["Sydney", 2058, 4336374, 1214.8])
print x
#print x.get_html_string(format=True)
