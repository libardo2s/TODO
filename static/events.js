function openModalUpdate(id) {
    console.log(id);
    $.get('/get/'+id+'/', function( data ) {
        $('#id_todo').val(data.id);
        $('#task_update').val(data.task);
        $('#description_update').val(data.description);
        $('#updateModal').modal('show');
    });
}