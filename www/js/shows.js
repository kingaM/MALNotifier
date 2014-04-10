$(document).ready(function() {
    
    $("#ratingSlider").slider({
        tooltip: 'hide',
        formater: function(value) {
            return 'Current value: ' + value;
        }
    });

    var values = {};
    values['email'] = 'xyz@example.com';
    console.log(window.location.search.substring(1));
    $.post("/shows.php?" + window.location.search.substring(1), values, function(data) {
        console.log(data);
        var json = $.parseJSON(data);
        var i = 0;
        for(var key in json){
            var attrName = key;
            var attrValue = json[key];
            console.log(attrName + " " + attrValue);
            i++;
            displayShow(attrValue, i);
        }
    }); 

    $("#score-form").submit(function (e) {
        e.preventDefault();
        var values = {};
        values['score'] = $("#score").val();
        $.post("/settings.php?" + window.location.search.substring(1), values, function(data) {
            console.log(data);
            var json = $.parseJSON(data);
            $("#score").val("");
                var values = {};
        values['email'] = 'xyz@example.com';
        console.log(window.location.search.substring(1));
        $("#anime-table").empty();
        $.post("/shows.php?" + window.location.search.substring(1), values, function(data) {
            console.log(data);
            var json = $.parseJSON(data);
            var i = 0;
            for(var key in json){
                var attrName = key;
                var attrValue = json[key];
                console.log(attrName + " " + attrValue);
                i++;
                displayShow(attrValue, i);
            }
    }); 
        }); 
    });

});

function displayShow(show, i) {
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