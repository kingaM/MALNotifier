$(document).ready(function() {
    console.log("clicked");
    $("#register-from").submit(function(e) {
        e.preventDefault();
        console.log("clicked");
        values= {};
        values['email'] = $("#register-email").val();
        values['mal'] = $("#register-mal").val();
        $.post("/register.php",values, function(data) {
            console.log(data);
            window.location.href = "/shows.html?" + values['mal'];
        });
    });   
});