
// This is for musiclist
var audio = document.getElementById('audio');
var audioList = document.querySelectorAll(".aTriggers");
var currentlyPlayingAudio = null;

audioList.forEach(function(audioSingle){
    audioSingle.addEventListener('click',function(){
        audioPlayPaused.className= "active";
        var dataAudio = this.getAttribute('data-audio');
        var dataActive = this.getAttribute('data-active');

        // Pause the currently playing audio if there is one
        if (currentlyPlayingAudio && currentlyPlayingAudio !== audio) {
            currentlyPlayingAudio.pause();
            var prevActiveElement = document.querySelector("[data-active='active']");
            if (prevActiveElement) {
                prevActiveElement.setAttribute("data-active", "pause");
                prevActiveElement.querySelector("i").className = "fa fa-play";
            }
        }
        
        currentlyPlayingAudio = audio;

        if(dataActive== "" || dataActive === "pause"){
            audio.src = dataAudio;
            audio.load();
            audio.play();
            this.setAttribute("data-active", "active");
            this.innerHTML="<i class='fa fa-pause'></i>";
        }
        else{
            audio.pause();
            this.setAttribute("data-active", "pause");
            this.innerHTML="<i class='fa fa-play'></i>";
            currentlyPlayingAudio = null;
        }
    })
})