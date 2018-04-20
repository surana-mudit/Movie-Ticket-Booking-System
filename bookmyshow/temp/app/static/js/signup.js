
var register=function(){
	console.log("13");
	var v=document.getElementById("form");
	name=v.name.value;
	email=v.email.value;
	username=v.username.value;
	pass=v.password.value;
	retype_pass=v.retype_password.value;
	phone=v.phone.value;
	console.log("hey");
	$.ajax({
		url:'http://127.0.0.1:5000/register',
		method:'POST',
		data:{name:name, email:email, username:username, password:pass, retype_password:retype_pass, phone:phone},
		success:function(response){
			window.location.href="http://127.0.0.1:8080/login";
			console.log('hi');
		},
		error:function(response){
			alert(JSON.parse(response.responseText).message);
		}
	});
};


