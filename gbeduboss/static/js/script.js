//  Variable collections
var audioPlayPause= document.getElementById('audioPlayPause');
var audioStop = document.getElementById('audioStop');
var audio = document.getElementById('audio');
var currentlyPlayingAudio = null;
var count = 0;



audioPlayPause.addEventListener('click', function(){
    if(count==0){
        count = 1;
        audio.play();
        audioPlayPause.innerHTML= "<i class='fa fa-pause'></i>"
    }else{
        count = 0;
        audio.pause();
        audioPlayPause.innerHTML= "<i class='fa fa-play'></i>"
    }
})
audioStop.addEventListener('click', function(){
    count= 0;
    audio.pause();
    audio.currentTime = 0;
    audioPlayPause.innerHTML= "<i class='fa fa-pause'></i>"
    audioPlayPause.className= "";
    audioStop.className = "";
    document.getElementById('audioTitle').innerHTML = "&nbsp;"
})

var audioList = document.querySelectorAll(".aTrigger");
audioList.forEach(function(audioSingle,index){
    var dataAudioName = audioSingle.getAttribute("data-audio");
    var audioName = dataAudioName.substring(dataAudioName.lastIndexOf("/") + 1, dataAudioName.length);
    audioList[index].nextElementSibling.innerHTML = audioName;
    audioSingle.addEventListener('click', function(index){
        thisisAudioSingle = this;
        audioPlayPause.className= "active";
        audioStop.className= "active";
        var dataAudio = this.getAttribute('data-audio');
        var dataActive = this.getAttribute('data-active');
        
        currentlyPlayingAudio = audio;

        // Pause the currently playing audio if there is one
        if (currentlyPlayingAudio && currentlyPlayingAudio !== audio) {
            currentlyPlayingAudio.pause();
            var prevActiveElement = document.querySelector("[data-active='active']");
            if (prevActiveElement) {
                prevActiveElement.setAttribute("data-active", "pause");
                prevActiveElement.querySelector("i").className = "fa fa-play";
            }
        }


        var audioSource = document.getElementById("audiosource");
        document.getElementById("audioTitle").innerHTML = audioName;
        audio.src = dataAudio;
        for(var i =0 ; i< audioList.length; i++){
            audioList[i].innerHTML= "<i class='fa fa-play'></i>";
            audioList[i].setAttribute("data-active", "");
        }
        if(dataActive== "" || dataActive=="pause"){
            count= 1;
            audio.load();
            audio.play();
            this.setAttribute("data-active", "active");
            this.innerHTML="<i class='fa fa-pause'></i>";
        }
        else{
            count = 0;
            audio.pause();
            this.setAttribute("data-active", "pause");
            this.innerHTML="<i class='fa fa-play'></i>";
            currentlyPlayingAudio = null;
        }
        // audio.addEventListener("timeupdate", function(e){
        //     const currentTime= e.target.currentTime
        // })
        var duration = document.getElementById("duration");
        setTimeout(function(){
            var s = parseInt(audio.duration %60);
            var m = parseInt((audio.duration /60) %60);
            duration.innerHTML= m + ":" + s;
            audio.addEventListener("timeupdate", function(){
                var durationUpdate = document.getElementById("durationUpdate");
                var s = parseInt(audio.currentTime % 60);
                var m = parseInt((audio.currentTime / 60) %60);
                durationUpdate.innerHTML= m + ":" + s;
            },false)
        },200)
    })
})