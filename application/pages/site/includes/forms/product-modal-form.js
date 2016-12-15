$("#input-phone").click( function (){
    $(this).mask("375(99)999-99-99");
    });
$("#input-phone").focus( function (){
    $(this).mask("375(99)999-99-99");
});

$(function() {
    $('#ProductForm').ajaxForm(function() {
         $.getJSON($SCRIPT_ROOT, {
    //type : "POST",
    //url : "{{ url_for('mail.send') }}",
    //data: JSON.stringify(data, null, '\t'),
    //contentType: 'application/json;charset=UTF-8',
    success: function(result) {
        alert('fucking fuckers!!!!!!!!')
        console.log(result);
        $('#product-modal').modal('toggle');

    }
        });
    });
});
