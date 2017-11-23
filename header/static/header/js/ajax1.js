
$(document).on('submit','#add_to_cart_button',function(e){
	e.preventDefault();
	
	$.ajax({
		type:'POST',
		url:'/addtocart/',
		data:{
			product_id:$('#product_id').val(),
			price:$('#price').val(),
			productname:$('#productname').val(),
			image:$('#image').val(),
			csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
		},
		success:function(){
			alert("Added");
		}	
			
		});
 });


var i = 0;
function buttonClick() {
	document.getElementById('sup1').value = ++i;
}

$(document).on('submit','.delete_from_cart',function(e){
	e.preventDefault();
	
	$.ajax({
		type:'POST',
		url:'/deletefromcart/delete/',
		data:{
			cart_id:$('.cart_value').val(),
			csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
		},
		success:function(){
			
		}	
			
		});
 });

$(document).ready(function (){
   $('tr').on('click',function (){
      $(this).fadeOut(500);
   });
});