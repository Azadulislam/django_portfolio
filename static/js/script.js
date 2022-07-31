$(document).ready(function () {
    $(document).on("scroll", function () {
        if ($(document).scrollTop() > 200) {
            $('#fixdNav').addClass('scrll-nav');
        } else {
            $('#fixdNav').removeClass('scrll-nav');

        }
    });
    $(document).on('click', 'a[href="#"]', function (e) {
        // target element id
        var id = $(this).attr('href');

        // target element
        var $id = $(id);
        if ($id.length === 0) {
            return;
        }

        // prevent standard hash navigation (avoid blinking in IE)
        e.preventDefault();

        // top position relative to the document
        var pos = $id.offset().top - 80;

        // animated top scrolling
        $('body, html').animate({ scrollTop: pos });
    });
    $(".gall-img img").click(function () {
        var img = $(this).attr('src');
        $("#show-img").attr('src', img);
        $("#imgmodal").modal('show');
    });

    $(".port-image").click(function () {
        var image = $(this).data('image');
        var title = $(this).data('title');
        var title = $(this).data('title');
        console.log('azad');;
        $(".modal-port-img").attr('src', image);
        $(".modal-title").text(title);
        $(".prot-image-footer").text(title);
        $("#imgmodalTwo").modal('show');
    });

});