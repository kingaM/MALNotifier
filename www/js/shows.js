$(document).ready(function() {
    console.log("clicked");
    var values = {};
    values['email'] = 'xyz@example.com';
    $.post("/shows.php",values, function(data) {
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

function addShow(show, i) {
    var html = "<tr>" +
                    "<td>" + i + "</td>" +
                    "<td>" + show[1] + "</td>" +
                    "<td>" + show[0] + "</td>" +
                    "<td>" + show[2] + "</td>" +
                "</tr>";
    $("#anime-table").append(html);
}