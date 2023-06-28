import os
from pathlib import Path
from render_utils import *

MONTHS = [
    None, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]

py_path = os.getcwd()
til_directory = os.path.join((Path(py_path).parent.parent.absolute()), "til")
til_html_directory = os.path.join((Path(py_path).parent.parent.absolute()), "til-html")

"""
Format of TIL:

Home page: 
    Main: description, list of (Summary of month)s, links to months
    Sidebar
Month page:
    Main: (Summary of month), list of (Summary of day)s, links to days
    Sidebar
Day page:
    Main: (Content of day)
    Sidebar
Sidebar:
    Link back to all Home page
    "Recent Posts"
    List of most recent months
"""

list_of_folder_day_paths = []
list_of_folder_month_paths = []
ALL_YEAR_MONTHS = [] # store as tuples of ints
ALL_YEAR_MONTH_DAYS = []

# iterate through years that exist in directory
for folder_year in os.listdir(til_html_directory):
    folder_year_path = os.path.join(til_html_directory, folder_year)
    if os.path.isfile(folder_year_path):
        continue
    # iterate through months that exist in years directory
    for folder_month in os.listdir(folder_year_path):
        folder_month_path = os.path.join(folder_year_path, folder_month)
        if os.path.isfile(folder_month_path):
            continue
        ALL_YEAR_MONTHS.append((int(folder_year), int(folder_month)))
        # iterate through days that exist in months directory
        for folder_day in os.listdir(folder_month_path):
            folder_day_path = os.path.join(folder_month_path, folder_day)
            if os.path.isfile(folder_day_path):
                continue
            list_of_folder_day_paths.append(folder_day_path)
            ALL_YEAR_MONTH_DAYS.append((int(folder_year), int(folder_month), int(folder_day)))

# read paths
def generate_month_summary_path(year_month):
    year, month = year_month
    return os.path.join(til_html_directory, f"{year}/{month}/summary.html")

def generate_day_summary_path(year_month_day):
    year, month, day = year_month_day
    return os.path.join(til_html_directory, f"{year}/{month}/{day}/summary.html")

def generate_day_content_path(year_month_day):
    year, month, day = year_month_day
    return os.path.join(til_html_directory, f"{year}/{month}/{day}/content.html")

# write paths
def generate_home_index_path():
    return os.path.join(til_directory, f"index.html")

def generate_month_index_path(year_month):
    year, month = year_month
    return os.path.join(til_directory, f"{year}/{month}/index.html")

def generate_day_index_path(year_month_day):
    year, month, day = year_month_day
    return os.path.join(til_directory, f"{year}/{month}/{day}/index.html")

# generate sidebar based on existing folders
def generate_sidebar_list():
    sidebar_list_html = []
    for year_month in ALL_YEAR_MONTHS:
        year, month = year_month
        list_item_html = f"<li><a href=\"https://www.maximillianguo.com/til/{year}/{month}/index.html\">{MONTHS[month]} {year}</a></li>"
        sidebar_list_html.append(list_item_html)
    return "\n".join(sidebar_list_html[-10:])

def generate_sidebar_html():
    return """
<div class="col-4 col-12-medium">
    <div id="sidebar">

        <!-- Sidebar -->
            <section>
                <a href=\"https://www.maximillianguo.com/til/index.html\">All Posts</a>

                <h4>Recent Months</h4>
                <ul class="style2">
"""\
+generate_sidebar_list()\
+"""
                </ul>
            </section>
    </div>
</div>
"""

# RENDER DAY INDEX HTML 
# TODO: add next day and previous day buttons

# paste stuff around the content
def generate_day_html(year_month_day):
    year, month, day = year_month_day
    content_path = generate_day_content_path(year_month_day)
    with open(content_path, "r") as file:
        content = file.read()

    return f"""
    <!DOCTYPE HTML>
    <!--
        Verti by HTML5 UP
        html5up.net | @ajlkn
        Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
    -->
    <html>
        {generate_head_html()}
        <body class="is-preload homepage">
            <div id="page-wrapper">

                {generate_header_html("til")}

                <!-- Main -->
                    <div id="main-wrapper">
                        <div class="container">
                            <div class="row gtr-200">
                                <div class="col-8 col-12-medium">
                                    <div id="content">

                                        <!-- Content -->
                                            <article>

                                                <h3>{MONTHS[month]} {day}, {year}</h3>

                                                {content}

                                            </article>

                                    </div>
                                </div>
                                {generate_sidebar_html()}
                            </div>
                        </div>
                    </div>

                    {generate_footer_html()}

                    {generate_scripts_html()}
        </body>
    </html>
    """

# iterate through existing days and re-write files
# TODO: only re-render things that have been edited? or most recent things?
for year_month_day in ALL_YEAR_MONTH_DAYS:
    day_index_path = generate_day_index_path(year_month_day)
    with open(day_index_path, "w") as file:
        file.write(generate_day_html(year_month_day))

# RENDER MONTH INDEX HTML
def generate_month_html(year_month):
    year, month = year_month
    month_summary_path = generate_month_summary_path(year_month)
    with open(month_summary_path, "r") as file:
        month_summary = file.read()

    list_of_day_summaries_html = []
    for day in range(1, 32):
        if (year, month, day) in ALL_YEAR_MONTH_DAYS:
            day_summary_path = generate_day_summary_path((year, month, day))
            with open(day_summary_path, "r") as file:
                day_summary = file.read()
            list_of_day_summaries_html.append(f"<a href=\"https://www.maximillianguo.com/til/{year}/{month}/{day}/index.html\"><h4>{MONTHS[month]} {day}, {year}</h4></a>\n <p>{day_summary} <em><a href=\"https://www.maximillianguo.com/til/{year}/{month}/{day}/index.html\">(continue reading)</a></em></p>\n")
    
    return f"""
    <!DOCTYPE HTML>
    <!--
        Verti by HTML5 UP
        html5up.net | @ajlkn
        Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
    -->
    <html>
        {generate_head_html()}
        <body class="is-preload homepage">
            <div id="page-wrapper">

                {generate_header_html("til")}

                <!-- Main -->
                    <div id="main-wrapper">
                        <div class="container">
                            <div class="row gtr-200">
                                <div class="col-8 col-12-medium">
                                    <div id="content">

                                        <!-- Content -->
                                            <article>

                                                <h3>{MONTHS[month]} {year}</h3>
                                                <p>{month_summary}</p>

                                                {"".join(list_of_day_summaries_html)}

                                            </article>

                                    </div>
                                </div>
                                {generate_sidebar_html()}
                            </div>
                        </div>
                    </div>

                    {generate_footer_html()}

                {generate_scripts_html()}
        </body>
    </html>
    """

# iterate through existing months and re-write files
# TODO: only re-render things that have been edited? or most recent things?
for year_month in ALL_YEAR_MONTHS:
    month_index_path = generate_month_index_path(year_month)
    with open(month_index_path, "w") as file:
        file.write(generate_month_html(year_month))

# RENDER HOME INDEX HTML
def generate_home_html():
    list_of_month_summaries_html = []
    for (year, month) in ALL_YEAR_MONTHS:
        month_summary_path = generate_month_summary_path((year, month))
        with open(month_summary_path, "r") as file:
            month_summary = file.read()
        list_of_month_summaries_html.append(f"<a href=\"https://www.maximillianguo.com/til/{year}/{month}/index.html\"><h3>{MONTHS[month]} {year}</h3></a>\n <p>{month_summary}</p>")
    
    return f"""
    <!DOCTYPE HTML>
    <!--
        Verti by HTML5 UP
        html5up.net | @ajlkn
        Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
    -->
    <html>
        {generate_head_html()}
        <body class="is-preload homepage">
            <div id="page-wrapper">

                {generate_header_html("til")}

                <!-- Main -->
                    <div id="main-wrapper">
                        <div class="container">
                            <div class="row gtr-200">
                                <div class="col-8 col-12-medium">
                                    <div id="content">

                                        <!-- Content -->
                                            <article>
                                            <p>
                                            TIL (Today I Learned) is my attempt to document, mostly for personal learning reasons, anything economics-adjacent that I learned that day.
                                            </p>

                                            {"".join(list_of_month_summaries_html)}

                                            </article>

                                    </div>
                                </div>
                                {generate_sidebar_html()}
                            </div>
                        </div>
                    </div>

                    {generate_footer_html()}

                    {generate_scripts_html()}
        </body>
    </html>
    """

# re-write home file
# note that this is only done once a new month is created
home_index_path = generate_home_index_path()
with open(home_index_path, "w") as file:
    file.write(generate_home_html())

print("Render TIL Complete")