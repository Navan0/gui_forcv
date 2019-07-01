// White screen found here: http://jsfiddle.net/SfzPc/14/
var canvas = document.getElementById("acanvas");
var w = canvas.width = 200;
var h = canvas.height = 200;
var context = canvas.getContext("2d");
for(i=0;i<w;i++) {
    for(j=0;j<h;j++) {
        var num = Math.floor(Math.random()*255)
        context.fillStyle = "rgb(" + num + "," + num + "," + num + ")";
        context.fillRect(i, j, 1, 1);
    }
}
$("#adiv, no2").css ( {
    "background": "url("+canvas.toDataURL()+")"
});

// getUserMedia
navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia;
      var constraints = {audio: false, video: true};
      var video = document.querySelector("video");
 
      function successCallback(stream) {
        jQuery('#adiv').hide();
        // stream available to console so you could inspect it and see what this object looks like
        window.stream = stream;
        if (window.URL) {
          video.src = window.URL.createObjectURL(stream);
        } else {
          video.src = stream;
        }
        video.play();
      }
 
      function errorCallback(error) {
        console.log("navigator.getUserMedia error: ", error);
      }
 
      navigator.getUserMedia(constraints, successCallback, errorCallback);

if (location.protocol.toLowerCase().indexOf('https')) {
	alert('This pen only works on HTTPS, change URL to use HTTPS and try again')
}