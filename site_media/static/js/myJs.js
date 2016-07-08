/**
 * Created by Luisk on 28/01/2016.
 */
$(document).ready(
    function () {

        /*   $('#id_id_alumno').attr("value", function (indiceArray) {
         //indiceArray tiene el índice de este elemento en el objeto jQuery
         var f = new Date();
         return (f.getFullYear()-'2000');
         });*/
        //terminar para poner foto al subirla
        $("#id_foto").change(function (evento) {
                evento.preventDefault();
                $("#foto").attr('src', '/media/fotos/' + $("#id_foto").val())
                // /$("#foto").attr("src",$())
            }
        )
        var formAjaxSubmit = function (form, modal) {
            $(form).submit(function (e) {
                e.preventDefault();
                $.ajax({
                    type: $(this).attr('method'),
                    url: $(this).attr('action'),
                    data: $(this).serialize(),
                    success: function (xhr, ajaxOptions, thrownError) {
                        if ($(xhr).find('.has-error').length > 0) {
                            $(modal).find('.modal-body').html(xhr);
                            formAjaxSubmit(form, modal);
                        } else {
                            $(modal).modal('toggle');
                        }
                    },
                    error: function (xhr, ajaxOptions, thrownError) {
                        // handle response errors here
                    }
                });
            });
        }

    }
);

$('#enviarform').on('click',Enviar)
function Enviar(){
    console.log('asasassasa')
    var name=$('#id_name').val()
    var phone=$('#id_phone').val()
    var mail=$('#id_mail').val()
    var subject=$('#id_subject').val()
    var message=$('#id_message').val()

    $.ajax({
        data:{'name':name,'phone':phone,'mail':mail,'subject':subject,'message':message},
        url:'/enviarform/',
        type:'post',
        success : function(data){
            var object=JSON.parse(data)
            console.log(object.message)
            html='<p>'+object.message+'</p>'
            $('#message_send').append(html)

        }
    });
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }

    }
});




