let links_header = document.querySelectorAll('.header .links_header .nav-item a')
links_header.forEach(function(e){
  e.addEventListener('click',function(){
    links_header.forEach((item)=>{
        item.classList.remove('active')
    })
    e.classList.add('active')
  })
})


