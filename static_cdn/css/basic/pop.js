$(document).ready(function() 
{
	$("#login #cancel").click(function() {
		$(this).parent().parent().hide();
	});
	$("#onclick").click(function() {
		$("#contactdiv").css("display", "block");
	});
	$("#contact #cancel").click(function() {
		$(this).parent().parent().hide();
	});



	$("#send").click(function() 
	{
		var username = $("#username").val();
		var password = $("#password").val();
		if (username == "" || password == ""){
			alert("Please Fill All Fields");
		}
	});

	$("#loginbtn").click(function() 
	{
		var name = $("#username").val();
		var password = $("#password").val();
		if (username == "" || password == "")
		{
			alert("Username or Password was Wrong");
		}
		else
		{	
			$("#logindiv").css("display", "none");
		}
	});	
});