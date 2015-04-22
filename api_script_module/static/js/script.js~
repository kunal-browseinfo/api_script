$(function(){
	$('#first').click(function(){
        $('#first_result').empty();
		$.ajax({
			url: '/getProjectTasks',
			data: $('.form-First').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
                $('#first_result').append(response);
			},
			error: function(error){
				console.log(error);
                $('#first_result').append(error);
			}
		});
	});
    $('#second').click(function(){
        $('#sec_result').empty();
		$.ajax({
			url: '/get_project_details',
			data: $('.form-second').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
                $('#sec_result').append(response);
			},
			error: function(error){
				console.log(error);
                $('#sec_result').append(error);
			}
		});
	});
});
