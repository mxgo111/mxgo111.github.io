from render_utils import *



def generate_resume_html():
    resume_html = f"""
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

                {generate_header_html("resume")}

                <!-- Main -->
				<div id="main-wrapper">
					<div class="container">
						<div id="content">

							<!-- Content -->
								<article>
									Click <a href="https://mxgo111.github.io/assets/pdfs/resume-05-2023.pdf" target="_blank">here</a> if the page does not load for your browser.
									<div style="position:relative; overflow:hidden; padding-bottom: 94%">
										<iframe src="https://mxgo111.github.io/assets/pdfs/resume-05-2023.pdf" style="width: 100%; height:100%; position: absolute; top: 0; left:0; border-width:0;">
										</iframe>
									</div>
								</article>

						</div>
					</div>
				</div>


                {generate_footer_html()}

                {generate_scripts_html()}

        </body>
    </html>
    """

    return resume_html