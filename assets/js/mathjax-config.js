window.MathJax = {
	loader: {
		load: ['[tex]/textmacros']
	},
	tex2jax: {
		// https://tex.stackexchange.com/q/27633
		inlineMath: [ ['$','$'] ],
		processEscapes: true,
		packages: {'[+]': ['textmacros']}
	},
	// macros, copied from pre.tex
	TeX: {
		Macros: {
			AA: "\\mathbb{A}",
			RR: "\\mathbb{R}",
			ZZ: "\\mathbb{Z}",
			NN: "\\mathbb{N}",
			QQ: "\\mathbb{Q}",
			CC: "\\mathbb{C}",
			FF: "\\mathbb{F}",
			PP: "\\mathbb{P}",
			CP: "\\mathbb{CP}",
			e: "\\varepsilon",
			ball: ["(#1-#2,\\,#1+#2)",2],
			floor: ["\\left\\lfloor{#1}\\right\\rfloor",1],
			ceil: ["\\left\\lceil{#1}\\right\\rceil",1],
			norm: ["\\left\\lVert{#1}\\right\\rVert",1],
			diff: "\\operatorname{diff }",
			disc: "\\operatorname{disc }",
			ord: "\\operatorname{ord}",
			lcm: "\\operatorname{lcm}",
			del: "\\partial",
			emp: "\\varnothing",
			divides: "\\,|\\,",
			op: ["\\operatorname{#1}",1],
			mf: ["\\mathfrak{#1}",1],
			mc: ["\\mathcal{#1}",1],
			sgn: "\\operatorname{sgn}",
			refl: "\\operatorname{refl}",
			UU: "\\mathcal{U}",
		}
	},
	SVG: {
		linebreaks: { automatic: true }
	},
};

window.addEventListener('resize', MJrerender);
// https://stackoverflow.com/a/56106854
let t = -1;
let delay = 1000;
function MJrerender() {
	if (t >= 0) {
		// If we are still waiting, user is still resizing
		// postpone the action further!
		window.clearTimeout(t);
	}
	t = window.setTimeout(function() {
		MathJax.Hub.Queue(["Rerender",MathJax.Hub]);
		t = -1; // Reset the handle
	}, delay);
};
