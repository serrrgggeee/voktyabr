$(document).ready(function() {

   /* activate the carousel */
   $("#modal-carousel").carousel({interval:false});

   /* change modal title when slide changes */
   $("#modal-carousel").on("slid.bs.carousel", function () {
        var f =$(".modal-title")
        .html($(this)
        .find(".active img")
        .attr("title"));
       console.log(f)
   });

   /* when clicking a thumbnail */
   $(".row .thumbnail").click(function(){
    //var content = $(".carousel-inner");
    var title = $(".modal-title");

    //content.empty();
    title.empty();

  	var id = $(this).attr('id');
     var repo = $("#img-repo .item");
     //var repoCopy = repo.$(this);

     //var active = repoCopy.first();
     console.log(id);
    $('.active').removeClass('active');
    $('#slide-'+id).addClass("active");
    //title.html(active.find("img").attr("title"));
  	//content.append(repoCopy);

    // show the modal
  	$("#modal-gallery").modal("show");
  });

});