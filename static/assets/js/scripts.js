//MAIN REQUEST ICON HIDE
$(document).on('click', '.abst-link', function () {
  $('.main-request').toggle();
})

//tech btn
$(document).on('click', '.revabst-tech-btn', function () {
  $('#revabst-tech').toggle();
})

//general btn
$(document).on('click', '.revabst-gen-btn', function () {
  $('#revabst-gen').toggle();
})

//SHOW FAV TABLE
$(document).on('click', '.fav-icon', function () {
  $('.maintab').toggle();
  $('.favtab').show();
})


//code for screen control 
function display_controll(){
  if (window.innerWidth <= 800) {
    document.body.innerHTML = '<div class="container text-center mt-5 p-5"><div class="alert alert-danger pb-5"><i class="bi bi-exclamation-circle" style="font-size:80px;"></i><h2 class="mt-4">Desktop-Only Experience</h2>	<p>Please access it on a larger screen for the best experience.</p></div></div>';
  }
}
display_controll();
// end code for screen control
