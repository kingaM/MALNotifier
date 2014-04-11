var ovaCheck = false;
var unairedCheck = true;
var ratingCheck = false;
var sliderRating = 5;

$(document).ready(function() {

    setupSlider();

    $("#ovaCheck").prop('checked', false);
    $("#unairedCheck").prop('checked', true);
    $("#ratingCheck").prop('checked', false);

    $(":checkbox").click(function(e){
        var id = e.target.id;
        var checked = $("#" + id).prop('checked');
        window[id] = checked;
    });

    var values = {};
    var MalName = window.location.search.substring(1);
    $.post("/shows.php?" + MalName, displayShows);

    $("#registerForm").submit(function(e) {
        e.preventDefault();

        var email = $("#registerForm :input").val()
        if(email.length == 0)
            return;
        
        var minRating;
        if(ratingCheck)
            minRating = sliderRating;
        else
            minRating = 0;

        $.ajax({
            type: "POST",
            url: "/register.php",
            data: {
                email: email,
                mal: MalName,
                ova: ovaCheck ? 1:0,
                unaired: unairedCheck ? 1:0,
                minRating: minRating
            },
            success: registerSuccess
        });
    });

    // $("#score-form").submit(function (e) {
    //     e.preventDefault();
    //     var values = {};
    //     values['score'] = $("#score").val();
    //     $.post("/settings.php?" + window.location.search.substring(1), values, function(data) {
    //         console.log(data);
    //         var json = $.parseJSON(data);
    //         $("#score").val("");
    //             var values = {};
    //     values['email'] = 'xyz@example.com';
    //     console.log(window.location.search.substring(1));
    //     $("#anime-table").empty();
    //     $.post("/shows.php?" + window.location.search.substring(1), values, displayShows); 
    //     }); 
    // });

});

function registerSuccess(response) {
    console.log("Registered");
}

function displayShows(data) {
    console.log(data);
    var json = $.parseJSON(data);
    for(var key in json){
        var attrName = key;
        var attrValue = json[key];
        displayShow(attrValue);
    }
}

function displayShow(show) {
    var description = show[2]
    if(description.length > 200) {
        description = description.substring(0, 200) + " ..."
    }
    var html = "<tr>" +
                    "<td><a href=\"http://anidb.net/perl-bin/animedb.pl?show=anime&aid=" + show[3] + "\">" + show[1] + "</a></td>" +
                    "<td>" + show[0] + "</td>" +
                    "<td>" + description + "</td>" +
                "</tr>";
    $("#anime-table").append(html);
}

function setupSlider() {

    $("#ratingCheckText").text(sliderRating);
    
    $("#ratingSlider").slider({
        tooltip: 'hide',
        formater: function(value) {
            return 'Current value: ' + value;
        }
    }).on("slide", function() {
        sliderRating = $("#ratingSlider").slider("getValue").val();
        console.log(sliderRating);
        $("#ratingCheckText").text(sliderRating);
    });

    $("#ratingSlider").slider().on("slideStop", function() {
        sliderRating = $("#ratingSlider").slider("getValue").val();
        console.log(sliderRating);
        $("#ratingCheckText").text(sliderRating);

        // Change table info here if ratingCheck is selected
    });
}