
$("button").click(function(){  
     $(".roundbutton").toggleClass("searching");  
});  

$('#submit').click(function(){
     setTimeout(function(){
          window.location.href='/switchsettings';
     },3000);
});