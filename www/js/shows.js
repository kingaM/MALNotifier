$(document).ready(function() {
    console.log("clicked");
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
            addShow(attrValue, i);
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
                addShow(attrValue, i);
            }
    }); 
        }); 
    });

});

function addShow(show, i) {
    var html = "<tr>" +
                    "<td>" + i + "</td>" +
                    "<td>" + show[1] + "</td>" +
                    "<td>" + show[0] + "</td>" +
                    "<td>" + show[2] + "</td>" +
                    "<td><a href=\"http://anidb.net/perl-bin/animedb.pl?show=anime&aid=" + show[3] + "\">AniDB</a></td>" +
                "</tr>";
    $("#anime-table").append(html);
}