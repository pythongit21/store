
$(document).ready(function(){
    $('#department-dropdown').change(function(){
        // Get selected country ID
        var department_id = $(this).val();

        // Send AJAX request to get courses for selected department
        $.ajax({
            url: '/get_courses',
            data: {
                'department_id': department_id
            },
            success: function(data){
                // Remove old options from courses dropdown
                $('#course-dropdown').find('option').remove();
                // Add new options to course dropdown
                console.log(data.courses.length);
                if(data.courses.length != 0){
                    $('#course-dropdown').append('<option value="0">--Select Course--</option>');
                    $.each(data.courses, function(index, course){
                        $('#course-dropdown').append('<option value="'+course.id+'">'+course.name+'</option>');
                    });

                    // Enable course dropdown
                    $('#course-dropdown').prop('disabled', false);
                }else{
                    $('#course-dropdown').append('<option value="0">No courses available</option>');
                }

            }
        });
    });
});
