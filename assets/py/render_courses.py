from render_utils import *

def generate_courses_html():
    courses_html = f"""
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

                {generate_header_html("courses")}

                <!-- Main -->
				<div id="main-wrapper">
					<div class="container">
						<div id="content">

							<!-- Content -->
								<article>
									This is a full list of courses Max has taken as an undergraduate at Harvard University.<br/>
									<em>[TA]</em> represents courses for which Max was a Teaching Fellow or Course Assistant for.<br /><br />
									<h3>Spring 2023</h3>
									<p>
										<strong>AM201.</strong> Physical Mathematics.<br/>
										<strong>Econ1011b.</strong> Intermediate Macroeconomics: Advanced.<br/>
										<strong>Econ980KK.</strong> Economic Growth.<br/>
									</p>

									<h3>Fall 2022</h3>
									<p>
										<strong>Stat244.</strong> Generalized Linear Models.<br/>
										<strong>Econ2120.</strong> Principles of Econometrics.<br/>
										<strong>Econ1011a.</strong> Intermediate Microeconomics: Advanced.<br/>
										<strong>Math116.</strong> Real Analysis, Convexity, and Optimization. Some <a href="https://github.com/mxgo111/math116-midterm-prooflist.pdf" target="_blank">midterm proof notes here</a> (in case it's helpful for future students).<br/>
										<strong>CS288.</strong> Artificial Intelligence for Social Impact.<br/>
										<em>[TA]</em> <strong>AC297r.</strong> Applied Computation Capstone.<br/>
										<em>[Head TA]</em> <strong>CS182.</strong> Artificial Intelligence.<br/>
										<!-- <em>[Audited]</em> <strong>Dev309.</strong> Development Policy Strategy.<br/> -->
									</p>
									
									<h3>Spring 2022</h3>
									<p>
										<strong>AM216.</strong> Inverse Problems.<br/>
										<strong>Stat195.</strong> Supervised Learning.<br/>
										<strong>CS238.</strong> Optimized Democracy.<br/>
										<strong>CS91r.</strong> Supervised Research in Computer Science.<br/>
										<em>[TA]</em> <strong>Stat111.</strong> Statistical Inference.<br/>
										<em>[TA]</em> <strong>CS181.</strong> Machine Learning.<br/>
									</p>

									<h3>Fall 2021</h3>
									<p>
										<strong>AM207.</strong> Advanced Scientific Computing: Stochastic Methods for Data Analysis, Inference and Optimization.<br/>
										<strong>CS282br.</strong> Adaptive Methods in Machine Learning.<br/>
										<strong>Stat185.</strong> Introduction to Unsupervised Learning.<br/>
										<strong>Gened1038.</strong> Sleep.<br/>
										<em>[TA]</em> <strong>Stat110.</strong> Introduction to Probability. <em><a href="https://github.com/mxgo111/Stat110-Section-Notes-Fall-2021" target="_blank">[Section Notes]</a></em><br/>
										<em>[TA]</em> <strong>CS182.</strong> Artificial Intelligence.<br/>
										<em>[TA]</em> <strong>CS121.</strong> Introduction to Theoretical Computer Science.<br/>
									</p>

									<h3>Spring 2021</h3>
									<p>
										<strong>CS234r.</strong> Topics on Computation: Markets and Networks.<br/>
										<strong>CS181.</strong> Machine Learning.<br/>
										<strong>CS51.</strong> Abstraction and Design in Computation.<br/>
										<strong>Stat171.</strong> Introduction to Stochastic Processes.<br/>
										<strong>Gened1014.</strong> Ancestry.<br/>
										<em>[TA]</em> <strong>Math101.</strong> Sets, Groups, and Topology. <em><a href="https://github.com/mxgo111/Math-101-Notes" target=_blank>[Lecture Notes]</a></em><br/>
									</p>

									<h3>Fall 2020</h3>
									<p>
										<strong>AM205.</strong> Advanced Scientific Computing: Numerical Methods.<br/>
										<strong>CS182.</strong> Artificial Intelligence.<br/>
										<strong>CS61.</strong> Systems Programming and Machine Organization.<br/>
										<strong>Stat210.</strong> Probability I.<br/>
										<strong>Gened1076.</strong> Equity and Excellence in American Education.<br/>
										<strong>Gened1001.</strong> Stories from the End of the World.<br/>
										<em>[TA]</em> <strong>CS121.</strong> Introduction to Theoretical Computer Science.<br/>
									</p>

									<h3>Spring 2020</h3>
									<p>
										<strong>CS124.</strong> Data Structures and Algorithms.<br/>
										<strong>Stat111.</strong> Introduction to Statistical Inference.<br/>
										<strong>Math55b.</strong> Studies in Real and Complex Analysis.<br/>
										<strong>Expos20.</strong> Expository Writing.<br/>
										<strong>ChnHis113.</strong> Society and Culture of Late Imperial China.<br/>
									</p>

									<h3>Fall 2019</h3>
									<p>
										<strong>CS121.</strong> Introduction to Theoretical Computer Science.<br/>
										<strong>Math55a.</strong> Studies in Algebra and Group Theory.<br/>
										<strong>LS1a.</strong> Introduction to Life Sciences.<br/>
										<strong>Ec10a.</strong> Principles of Economics.<br/>
									</p>

								</article>

						</div>
					</div>
				</div>



                {generate_footer_html()}

                {generate_scripts_html()}

        </body>
    </html>
    """

    return courses_html