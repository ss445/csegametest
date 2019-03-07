function sendUsername(){
        var username = document.getElementById("UsernameInput").value;
        document.getElementById("playername").innerText = username;
        document.getElementById("login").style.display = 'none';
        var toSend = JSON.stringify({"username": username});
        ajaxPostRequest("/sendusername", toSend);
        };



    function sendChat() {
        var messageElement = document.getElementById("chatmessage");
        var toSend = JSON.stringify({"message": message});
        ajaxPostRequest("/sendchat", toSend);
    };


    function renderchat(){
        var response = ajaxGetRequest("/chat");
        // maybe change the format of response
        document.getElementById("chatchannel").innerHTML = response;
    };


    function sendComment() {
        var comment = document.getElementById("comment");
        var toSend = JSON.stringify({"message": comment.value});
        ajaxPostRequest("/sendcomment", toSend);
    };
