var files;

$(document).ready(function() {
    console.log("clicked");

    $('input[type=file]').on('change', function (event) {
        files = event.target.files;
    });

    $("#register-from").submit(function(e) {
        e.preventDefault();
        console.log("clicked");
        values= {};
        values['email'] = $("#register-email").val();
        values['mal'] = $("#register-mal").val();
        uploadFiles(e);
    });   
});

function uploadFiles(event) {
    event.stopPropagation();
    event.preventDefault();

    var data = new FormData();
    $.each(files, function(key, value) {
        data.append(key, value);
    });

    data.append("email", $("#register-email").val());
    data.append("mal", $("#register-mal").val());
    
    $.ajax({
        url: '/register.php',
        type: 'POST',
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function(data) {
            console.log(data)
            window.location.href = "/shows.html?" + $("#register-mal").val();
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error("ERROR: " + textStatus);
        }
    });
}