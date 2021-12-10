$(document).ready(function() {
   
    $('section:main >  div.container > section:content > section.blockHero > h2.Hero > a.titulo').each(function () {

      var href = $(this).attr("href");
      href = href.replace("superheroes", "superheroesAjax");
      $(this).qtip({

         content: {
            url: href,
            method: 'get'
            
         } 
      });
    });
   
  });

  