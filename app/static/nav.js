function changeBg() {
  const scroller = document.getElementById("nav-base");
  var navlink = document.querySelector(".nav-links");
  var navitems = document.querySelectorAll(".nav-link");
  

  if (window.scrollY > 0) {
    scroller.style.background = "#fff";
    navlink.classList.remove('bg-dark');
    navlink.classList.add('bg-body');
    navitems.forEach(function (item) {
      item.style.color = "#000"; // Black color
    });
    // scroller.style.backdropFilter = "blur(5px) brightness(0.7)";
    scroller.style.boxShadow = "0px 5px 5px rgba(0,0,0,0.1)";

  } else {
    scroller.style.background = "transparent";
    //  scroller.style.backdropFilter = "none";
    scroller.style.boxShadow = "none";
    navlink.classList.remove("bg-body");
    navlink.classList.add("bg-dark");
    
    navitems.forEach(function (item) {
      item.style.color = "#fff"; // Black color
    });




  }
}

window.addEventListener("scroll", changeBg);


changeBg();


