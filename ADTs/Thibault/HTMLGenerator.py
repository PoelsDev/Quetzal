def generateHTML(filename):
    output = ""
    newline = "\n"
    with open(filename, "w+") as f:
        output += "<html>"
        output += "<body>"
        output += "<table>" + newline
        output += "<tr>" + newline
        output += "<th> tijdstip </th>"
        output += ""
