 $().ready(function() {
                $('#buttonserach').click(function(){$('#searchform').submit()})
                $('#searchInput').focus(function(){$('#searchInput').val(' ').css('color','black')})
            });