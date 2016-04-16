   $(document).ready(function(){
      $('#user-login').show();
	  $('#user-login').fadeOut(10);	
      $('#user-input').addClass('user-input');     	      
      $('#login-b').addClass('login-btn');
      $('#user').addClass('input-line');  
      $('#pass').addClass('input-line');
      $('#login').addClass('input-line');

	  	
	  $('#testbtn').bind('click', function(){
		$('#testModel').css('overflow-y', '50');
		$('#testModel').addClass('test-fade2');
		});

	  $('a').bind('click', function(){
		  $('#home-page').show();
		  $('#user-login').hide();
		});	 
	  $('#user-login').fadeIn(3000);   
	  $('#login-b').hover(function(){
			$(this).toggleClass('button-hover');	
		});     
	  $('#login-b').bind('click', function(){
		alert("id is : " + this.getAttribute('data-target'));
		
	    if($('#username').val() == ''&&$('#password').val() == '')alert('Enter username and pasword');
		else if($('#username').val() == '')alert('Enter username');
		else if($('#password').val() == '')alert('Enter password');
});	      
});
