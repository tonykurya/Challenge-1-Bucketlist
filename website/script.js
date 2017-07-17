document.addEventListener('DOMContentLoaded', function(){
  var loginButton = document.querySelector('#demo-2');
  var popup = document.querySelector('#popup');
  var popupBg = document.querySelector('#popup-bg');
  var close = document.querySelector('#close');
  
  loginButton.addEventListener('click', function(){
    show(popup);
  });
  
  popupBg.addEventListener('click', function(){
    hide(popup);
	});
  
  close.addEventListener('click', function(){
    hide(popup);
	});
  
});

function show(el){
  el.style.display = 'block';
}

function hide(el){
  el.style.display = 'none';
}




// Check items when complete

$(document).on("click", ".check", function() {

  $(this).toggleClass("selected");

});

// When enter key is pressed append a new item to the list

$(".toDo").keydown(function(event) {

  if (event.which === 13) {

    $(".list").append("<li>" + $(this).val() + "<span class='check'>" + "</span>" + "<svg height='auto' class='remove' version='1.1' viewBox='0 0 19 23' width='15px' xmlns='http://www.w3.org/2000/svg' xmlns:sketch='http://www.bohemiancoding.com/sketch/ns' xmlns:xlink='http://www.w3.org/1999/xlink'><title/><defs><path d='M0.501203573,1.96015511 C0.501203573,1.96015511 7.17230047e-07,1.96015511 0,2.96015511 C-4.1525821e-07,3.96015511 0.501203573,3.96015511 0.501203573,3.96015511 L18.4987964,3.96015511 C18.4987964,3.96015511 19,3.96015511 19,2.96015511 C18.9999995,1.96015511 18.4987964,1.96015511 18.4987964,1.96015511 L0.501203573,1.96015511 L0.501203573,1.96015511 Z M0.973754885,4.96015511 L1.97273588,4.96015511 L3.97375489,21.9601551 L14.9737549,21.9601551 L16.9737549,4.96015511 L17.9737549,4.96015511 L15.9737549,22.9601551 L2.97375489,22.9601551 L0.973754885,4.96015511 Z M7.9737549,0.960155108 C6.9737549,0.960155108 6.9737549,1.96015511 6.9737549,1.96015511 L11.9737549,1.96015511 C11.9737549,1.96015511 11.9737549,0.960155108 10.9737549,0.960155108 L7.9737549,0.960155108 L7.9737549,0.960155108 Z M5.9737549,20.9601551 L6.9737549,20.9601551 L5.9737549,4.92304573 L4.97375489,4.92304573 L5.9737549,20.9601551 Z M12.9737549,4.92304573 L11.9737549,20.9601551 L12.9737549,20.9601551 L13.9737549,4.92304573 L12.9737549,4.92304573 L12.9737549,4.92304573 Z M8.9737549,4.92304573 L8.9737549,20.9601551 L9.9737549,20.9601551 L9.9737549,4.92304573 L8.9737549,4.92304573 L8.9737549,4.92304573 Z' id='path-1'/></defs><g fill='none' fill-rule='evenodd' id='miu' stroke='none' stroke-width='1'><g id='editor_trash_delete_recycle_bin_outline_stroke'><use fill='#FFF' fill-rule='evenodd' xlink:href='#path-1'/><use fill='none' xlink:href='#path-1'/></g></g></svg>" + "</li>");

    $(this).val('');
  }
});

// Delete items off list

$(document).on("click", ".remove", function() {

  $(this).parent().remove();

});



var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "Username" && password == "password"){
alert ("Login successfully");
window.location = "index.html"; // Redirecting to other page.
return false;
}
else{
attempt --;// Decrementing by one.
alert("You have left "+attempt+" attempt;");
// Disabling fields after 3 attempts.
if( attempt == 0){
document.getElementById("username").disabled = true;
document.getElementById("password").disabled = true;
document.getElementById("submit").disabled = true;
return false;
}
}
}






//Push all new elements into this empty //array
var added = [ ];
//add counter for each new element
var counter = 1;
document.getElementById("add").addEventListener("click", function(){
  var newDiv = document.createElement("div");
  var newContent = document.createTextNode("NEW"); 
  var currentDiv = document.getElementById("div1"); 
  //create a constructor function that adds elements to dom
  function addElement(){
    //create new element 
    //give it some content
    newDiv.appendChild(newContent); //add the text node to the newly created div. 
    //add id to current element
    newDiv.id = "new";

    // add the newly created element and its content into the DOM 
    document.body.insertBefore(newDiv, currentDiv); 
    console.log(added.length);
    alert("button was clicked " + (counter++) + " times");
  }
  //initialize function
  addElement();
});

document.getElementById("editor_trash_delete_recycle_bin_outline_stroke").addEventListener("click", function(){ 
  var currentDiv = document.getElementById("new"); 
  function deleteElement(){
    //delete current element 
    //target the currentDiv and if it has a parentNode
    //removeChild of currentDiv
    if (currentDiv.parentNode) {
      currentDiv.parentNode.removeChild(currentDiv);
      alert("button was clicked " + (counter--) + " times");
    }
     
    
  }
  //initialize function
  deleteElement();
});







