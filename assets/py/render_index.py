from render_utils import *

def generate_index_html():
    index_html = f"""
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

                {generate_header_html("index")}

                <!-- Main -->
                    <div id="main-wrapper">
                        <div class="container">
                            <div class="row gtr-200">
                                <div class="col-4 col-12-medium">

                                    <!-- Sidebar -->
                                        <div id="sidebar">
                                            <section class="widget thumbnails">
                                                <a href="#" class="image featured"><img src="images/profile.jpg" alt="" /></a>
                                                <div id=contact-wrapper>
                                                    <a href="mailto:maxguo@stanford.edu" target="_blank"><h5>maxguo@stanford.edu</h5></a>
                                                    <section class="widget contact last">
                                                        <ul>
                                                            <li><a href="mailto:maxguo@stanford.edu" class="icon fa-envelope" target="_blank"><span class="label">Email</span></a></li>
                                                            <li><a href="https://github.com/mxgo111" class="icon brands fa-github" target="_blank"><span class="label">Github</span></a></li>
                                                            <li><a href="https://www.linkedin.com/in/maximillian-guo-261943196/" class="icon brands fa-linkedin" target="_blank"><span class="label">Linkedin</span></a></li>
                                                        </ul>
                                                    </section>
                                                </div>
                                            </section>
                                        </div>

                                </div>
                                <div class="col-8 col-12-medium imp-medium">

                                    <!-- Content -->
                                        <div id="content">
                                            <section class="last">
                                                <h2>About Me</br>
                                                </h2>

                                                <p>
                                                    Max is currently a research fellow and pre-doctoral student at Stanford's Graduate School of Business with the Global Capital Allocation Project (GCAP) group. He recently graduated from Harvard University with a joint bachelor's degree in Computer Science and Statistics and a master's degree in Applied Mathematics. In his future career, he hopes to use economic research to inform policy that alleviates long-term extreme poverty, perhaps through working with multilateral institutions like the World Bank and the IMF. He intends to complete an economics Ph.D. in the near future after his research fellowship. He would love to connect with anyone thinking about similar things!
                                                </p>
                                                <!-- <p>
                                                    Max's various undergraduate experiences include research in machine learning (with the <a href="https://crisp.seas.harvard.edu/" target="_blank">CRISP Group</a> and the <a href="https://dtak.github.io/" target="_blank">DtAK lab</a>), teaching (including as the Head Teaching Fellow of the AI course at Harvard), quantitative finance (internship at Five Rings Capital), and educational programming (with the <a href="https://hauscr.org/" target="_blank">Harvard Association for U.S. China Relations</a>). He also spends time playing the piano, lifting, juggling, and trying to move up the ranks in Duolingo.
                                                </p> -->
                                                <p>
                                                    In his free time, he spends time lifting, playing the piano, juggling, and trying to move up the ranks in Duolingo. <em>[Last Updated June 2023]</em>
                                                </p>
                                            </section>
                                        </div>

                                </div>
                            </div>
                        </div>
                    </div>



                {generate_footer_html()}

                {generate_scripts_html()}

        </body>
    </html>
    """

    return index_html