var viewPortWidth = 0;
var viewPortHeight = 0;

function sizeReporter() {   // Resize player when window resize
    viewPortWidth = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
    viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
    console.log("[INFO]Window inner size: Height = " + viewPortHeight + "px; Width = " + viewPortWidth + "px");
}

window.addEventListener('resize', function() {
    console.log("[Event]Resize");
    sizeReporter();
});

window.onload = function () {
    console.log("[Event]Onload");
    sizeReporter();
};

