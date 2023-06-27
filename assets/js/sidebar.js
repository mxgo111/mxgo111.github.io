// setting the sidebar's height
function sidebarHeight()
{
	// +11 accounts for the padding of the sidebar
	var contentHeight = $('.content')[0].offsetHeight - 11;
	$('.sidebar').height(contentHeight);
}

// rounding the corners
function roundCorners()
{
	var containerHeight = $('.container')[0].offsetHeight;
	var titleHeight = $('.title')[0].offsetHeight;
	var windowHeight = $(window).height();
	var windowWidth = $(window).width();
	// we extend to the bottom of the screen
	if(containerHeight + titleHeight > windowHeight)
	{
		$('.container').css({'border-radius':'0 0 0 0'});
		$('.content').css({'border-radius':'0 0 0 0'});
		$('.sidebar').css({'border-radius':'0 0 0 0'});
	}
	// there's a sidebar
	else if(windowWidth > 800)
	{
		$('.container').css({'border-radius':'0 0 1em 1em'});
		$('.content').css({'border-radius':'0 0 0 1em'});
		$('.sidebar').css({'border-radius':'0 0 1em 0'});
	}
	// there's no sidebar
	else
	{
		$('.container').css({'border-radius':'0 0 1em 1em'});
		$('.content').css({'border-radius':'0 0 1em 1em'});
	}
}

// run the methods
sidebarHeight();
roundCorners();

// update on resize
window.addEventListener('resize', sidebarHeight);
window.addEventListener('resize', roundCorners);

// it's possible that MathJax expands the container, so we have to adjust
window.MathJax.Hub.Queue(function ()
{
	sidebarHeight();
	roundCorners();
});

// the clickable menus
var submenus = document.getElementsByClassName('yearmenu');
for(var i = 0; i < submenus.length; ++i)
{
	// just add a listener for each element
	submenus[i].addEventListener('click', function()
	{
		// hack by looking at the next element directly
		var submenu = this.nextElementSibling;
		if(submenu.style.display === 'block')
			submenu.style.display = 'none';
		else
			submenu.style.display = 'block';
	});
}
